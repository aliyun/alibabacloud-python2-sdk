# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AsymmetricDecryptRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, key_version_id=None, algorithm=None):
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        return self


class AsymmetricDecryptResponseBody(TeaModel):
    def __init__(self, request_id=None, plaintext=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricDecryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AsymmetricDecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AsymmetricDecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricEncryptRequest(TeaModel):
    def __init__(self, plaintext=None, key_id=None, key_version_id=None, algorithm=None):
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        return self


class AsymmetricEncryptResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricEncryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AsymmetricEncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AsymmetricEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricSignRequest(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, algorithm=None, digest=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode
        self.digest = TeaConverter.to_unicode(digest)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        return self


class AsymmetricSignResponseBody(TeaModel):
    def __init__(self, request_id=None, value=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricSignResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AsymmetricSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AsymmetricSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AsymmetricVerifyRequest(TeaModel):
    def __init__(self, key_id=None, key_version_id=None, algorithm=None, digest=None, value=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode
        self.digest = TeaConverter.to_unicode(digest)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AsymmetricVerifyResponseBody(TeaModel):
    def __init__(self, request_id=None, value=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.value = value  # type: bool
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class AsymmetricVerifyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AsymmetricVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AsymmetricVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelKeyDeletionRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CancelKeyDeletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CancelKeyDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePrivateKeyDecryptRequest(TeaModel):
    def __init__(self, certificate_id=None, algorithm=None, ciphertext_blob=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        return self


class CertificatePrivateKeyDecryptResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_id=None, plaintext=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class CertificatePrivateKeyDecryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CertificatePrivateKeyDecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CertificatePrivateKeyDecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePrivateKeySignRequest(TeaModel):
    def __init__(self, certificate_id=None, algorithm=None, message_type=None, message=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode
        self.message_type = TeaConverter.to_unicode(message_type)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CertificatePrivateKeySignResponseBody(TeaModel):
    def __init__(self, signature_value=None, request_id=None, certificate_id=None):
        self.signature_value = TeaConverter.to_unicode(signature_value)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class CertificatePrivateKeySignResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CertificatePrivateKeySignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CertificatePrivateKeySignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePublicKeyEncryptRequest(TeaModel):
    def __init__(self, certificate_id=None, algorithm=None, plaintext=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        return self


class CertificatePublicKeyEncryptResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, certificate_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class CertificatePublicKeyEncryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CertificatePublicKeyEncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CertificatePublicKeyEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificatePublicKeyVerifyRequest(TeaModel):
    def __init__(self, certificate_id=None, algorithm=None, message=None, message_type=None, signature_value=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.algorithm = TeaConverter.to_unicode(algorithm)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.message_type = TeaConverter.to_unicode(message_type)  # type: unicode
        self.signature_value = TeaConverter.to_unicode(signature_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.message is not None:
            result['Message'] = self.message
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        return self


class CertificatePublicKeyVerifyResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_id=None, signature_valid=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.signature_valid = signature_valid  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.signature_valid is not None:
            result['SignatureValid'] = self.signature_valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('SignatureValid') is not None:
            self.signature_valid = m.get('SignatureValid')
        return self


class CertificatePublicKeyVerifyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CertificatePublicKeyVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CertificatePublicKeyVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasRequest(TeaModel):
    def __init__(self, key_id=None, alias_name=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.alias_name = TeaConverter.to_unicode(alias_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateRequest(TeaModel):
    def __init__(self, subject=None, subject_alternative_names=None, key_spec=None, protection_level=None):
        self.subject = TeaConverter.to_unicode(subject)  # type: unicode
        self.subject_alternative_names = subject_alternative_names  # type: dict[unicode, any]
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        return self


class CreateCertificateShrinkRequest(TeaModel):
    def __init__(self, subject=None, subject_alternative_names_shrink=None, key_spec=None, protection_level=None):
        self.subject = TeaConverter.to_unicode(subject)  # type: unicode
        self.subject_alternative_names_shrink = TeaConverter.to_unicode(subject_alternative_names_shrink)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.subject_alternative_names_shrink is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names_shrink
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names_shrink = m.get('SubjectAlternativeNames')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        return self


class CreateCertificateResponseBody(TeaModel):
    def __init__(self, csr=None, request_id=None, certificate_id=None, arn=None):
        self.csr = TeaConverter.to_unicode(csr)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class CreateCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyRequest(TeaModel):
    def __init__(self, description=None, key_usage=None, origin=None, protection_level=None,
                 enable_automatic_rotation=None, rotation_interval=None, key_spec=None):
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.key_usage = TeaConverter.to_unicode(key_usage)  # type: unicode
        self.origin = TeaConverter.to_unicode(origin)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        return self


class CreateKeyResponseBodyKeyMetadata(TeaModel):
    def __init__(self, key_id=None, next_rotation_date=None, key_state=None, rotation_interval=None, arn=None,
                 creator=None, delete_date=None, last_rotation_date=None, description=None, primary_key_version=None,
                 origin=None, key_spec=None, material_expire_time=None, automatic_rotation=None, protection_level=None,
                 key_usage=None, creation_date=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.next_rotation_date = TeaConverter.to_unicode(next_rotation_date)  # type: unicode
        self.key_state = TeaConverter.to_unicode(key_state)  # type: unicode
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode
        self.creator = TeaConverter.to_unicode(creator)  # type: unicode
        self.delete_date = TeaConverter.to_unicode(delete_date)  # type: unicode
        self.last_rotation_date = TeaConverter.to_unicode(last_rotation_date)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.primary_key_version = TeaConverter.to_unicode(primary_key_version)  # type: unicode
        self.origin = TeaConverter.to_unicode(origin)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.material_expire_time = TeaConverter.to_unicode(material_expire_time)  # type: unicode
        self.automatic_rotation = TeaConverter.to_unicode(automatic_rotation)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode
        self.key_usage = TeaConverter.to_unicode(key_usage)  # type: unicode
        self.creation_date = TeaConverter.to_unicode(creation_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.key_state is not None:
            result['KeyState'] = self.key_state
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.description is not None:
            result['Description'] = self.description
        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        return self


class CreateKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, key_metadata=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.key_metadata = key_metadata  # type: CreateKeyResponseBodyKeyMetadata

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeyMetadata') is not None:
            temp_model = CreateKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m['KeyMetadata'])
        return self


class CreateKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyVersionRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, key_version_id=None, key_id=None, creation_date=None):
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.creation_date = TeaConverter.to_unicode(creation_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        return self


class CreateKeyVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, key_version=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.key_version = key_version  # type: CreateKeyVersionResponseBodyKeyVersion

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeyVersion') is not None:
            temp_model = CreateKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m['KeyVersion'])
        return self


class CreateKeyVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateKeyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateKeyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretRequest(TeaModel):
    def __init__(self, secret_name=None, version_id=None, encryption_key_id=None, secret_data=None,
                 secret_data_type=None, description=None, tags=None, secret_type=None, extended_config=None,
                 enable_automatic_rotation=None, rotation_interval=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.encryption_key_id = TeaConverter.to_unicode(encryption_key_id)  # type: unicode
        self.secret_data = TeaConverter.to_unicode(secret_data)  # type: unicode
        self.secret_data_type = TeaConverter.to_unicode(secret_data_type)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.secret_type = TeaConverter.to_unicode(secret_type)  # type: unicode
        self.extended_config = extended_config  # type: dict[unicode, any]
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class CreateSecretShrinkRequest(TeaModel):
    def __init__(self, secret_name=None, version_id=None, encryption_key_id=None, secret_data=None,
                 secret_data_type=None, description=None, tags=None, secret_type=None, extended_config_shrink=None,
                 enable_automatic_rotation=None, rotation_interval=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.encryption_key_id = TeaConverter.to_unicode(encryption_key_id)  # type: unicode
        self.secret_data = TeaConverter.to_unicode(secret_data)  # type: unicode
        self.secret_data_type = TeaConverter.to_unicode(secret_data_type)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.secret_type = TeaConverter.to_unicode(secret_type)  # type: unicode
        self.extended_config_shrink = TeaConverter.to_unicode(extended_config_shrink)  # type: unicode
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.extended_config_shrink is not None:
            result['ExtendedConfig'] = self.extended_config_shrink
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('ExtendedConfig') is not None:
            self.extended_config_shrink = m.get('ExtendedConfig')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class CreateSecretResponseBody(TeaModel):
    def __init__(self, secret_name=None, version_id=None, next_rotation_date=None, request_id=None,
                 secret_type=None, rotation_interval=None, extended_config=None, arn=None, automatic_rotation=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.next_rotation_date = TeaConverter.to_unicode(next_rotation_date)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.secret_type = TeaConverter.to_unicode(secret_type)  # type: unicode
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode
        self.extended_config = TeaConverter.to_unicode(extended_config)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode
        self.automatic_rotation = TeaConverter.to_unicode(automatic_rotation)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        return self


class CreateSecretResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecryptRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context=None):
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.encryption_context = encryption_context  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
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
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.encryption_context_shrink = TeaConverter.to_unicode(encryption_context_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, plaintext=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class DecryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DecryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DecryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAliasRequest(TeaModel):
    def __init__(self, alias_name=None):
        self.alias_name = TeaConverter.to_unicode(alias_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyMaterialRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteKeyMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteKeyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretRequest(TeaModel):
    def __init__(self, secret_name=None, force_delete_without_recovery=None, recovery_window_in_days=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.force_delete_without_recovery = TeaConverter.to_unicode(force_delete_without_recovery)  # type: unicode
        self.recovery_window_in_days = TeaConverter.to_unicode(recovery_window_in_days)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.force_delete_without_recovery is not None:
            result['ForceDeleteWithoutRecovery'] = self.force_delete_without_recovery
        if self.recovery_window_in_days is not None:
            result['RecoveryWindowInDays'] = self.recovery_window_in_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('ForceDeleteWithoutRecovery') is not None:
            self.force_delete_without_recovery = m.get('ForceDeleteWithoutRecovery')
        if m.get('RecoveryWindowInDays') is not None:
            self.recovery_window_in_days = m.get('RecoveryWindowInDays')
        return self


class DeleteSecretResponseBody(TeaModel):
    def __init__(self, secret_name=None, request_id=None, planned_delete_time=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.planned_delete_time = TeaConverter.to_unicode(planned_delete_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        return self


class DeleteSecretResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountKmsStatusResponseBody(TeaModel):
    def __init__(self, account_status=None, request_id=None):
        self.account_status = TeaConverter.to_unicode(account_status)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAccountKmsStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAccountKmsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, status=None, protection_level=None, request_id=None, issuer=None, certificate_id=None,
                 created_at=None, key_spec=None, subject_alternative_names=None, signature_algorithm=None,
                 subject_key_identifier=None, not_after=None, updated_at=None, subject=None, serial=None, subject_public_key=None, arn=None,
                 not_before=None, tags=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.issuer = TeaConverter.to_unicode(issuer)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.created_at = TeaConverter.to_unicode(created_at)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.subject_alternative_names = subject_alternative_names  # type: list[unicode]
        self.signature_algorithm = TeaConverter.to_unicode(signature_algorithm)  # type: unicode
        self.subject_key_identifier = TeaConverter.to_unicode(subject_key_identifier)  # type: unicode
        self.not_after = TeaConverter.to_unicode(not_after)  # type: unicode
        self.updated_at = TeaConverter.to_unicode(updated_at)  # type: unicode
        self.subject = TeaConverter.to_unicode(subject)  # type: unicode
        self.serial = TeaConverter.to_unicode(serial)  # type: unicode
        self.subject_public_key = TeaConverter.to_unicode(subject_public_key)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode
        self.not_before = TeaConverter.to_unicode(not_before)  # type: unicode
        self.tags = tags  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.subject_alternative_names is not None:
            result['SubjectAlternativeNames'] = self.subject_alternative_names
        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm
        if self.subject_key_identifier is not None:
            result['SubjectKeyIdentifier'] = self.subject_key_identifier
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.serial is not None:
            result['Serial'] = self.serial
        if self.subject_public_key is not None:
            result['SubjectPublicKey'] = self.subject_public_key
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('SubjectAlternativeNames') is not None:
            self.subject_alternative_names = m.get('SubjectAlternativeNames')
        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')
        if m.get('SubjectKeyIdentifier') is not None:
            self.subject_key_identifier = m.get('SubjectKeyIdentifier')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        if m.get('SubjectPublicKey') is not None:
            self.subject_public_key = m.get('SubjectPublicKey')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, key_id=None, next_rotation_date=None, key_state=None, rotation_interval=None, arn=None,
                 creator=None, delete_date=None, last_rotation_date=None, description=None, primary_key_version=None,
                 origin=None, key_spec=None, material_expire_time=None, automatic_rotation=None, protection_level=None,
                 key_usage=None, creation_date=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.next_rotation_date = TeaConverter.to_unicode(next_rotation_date)  # type: unicode
        self.key_state = TeaConverter.to_unicode(key_state)  # type: unicode
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode
        self.creator = TeaConverter.to_unicode(creator)  # type: unicode
        self.delete_date = TeaConverter.to_unicode(delete_date)  # type: unicode
        self.last_rotation_date = TeaConverter.to_unicode(last_rotation_date)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.primary_key_version = TeaConverter.to_unicode(primary_key_version)  # type: unicode
        self.origin = TeaConverter.to_unicode(origin)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.material_expire_time = TeaConverter.to_unicode(material_expire_time)  # type: unicode
        self.automatic_rotation = TeaConverter.to_unicode(automatic_rotation)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode
        self.key_usage = TeaConverter.to_unicode(key_usage)  # type: unicode
        self.creation_date = TeaConverter.to_unicode(creation_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.key_state is not None:
            result['KeyState'] = self.key_state
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.description is not None:
            result['Description'] = self.description
        if self.primary_key_version is not None:
            result['PrimaryKeyVersion'] = self.primary_key_version
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('KeyState') is not None:
            self.key_state = m.get('KeyState')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PrimaryKeyVersion') is not None:
            self.primary_key_version = m.get('PrimaryKeyVersion')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        return self


class DescribeKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, key_metadata=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.key_metadata = key_metadata  # type: DescribeKeyResponseBodyKeyMetadata

    def validate(self):
        if self.key_metadata:
            self.key_metadata.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_metadata is not None:
            result['KeyMetadata'] = self.key_metadata.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeyMetadata') is not None:
            temp_model = DescribeKeyResponseBodyKeyMetadata()
            self.key_metadata = temp_model.from_map(m['KeyMetadata'])
        return self


class DescribeKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyVersionRequest(TeaModel):
    def __init__(self, key_id=None, key_version_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, key_version_id=None, key_id=None, creation_date=None):
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.creation_date = TeaConverter.to_unicode(creation_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
        return self


class DescribeKeyVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, key_version=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.key_version = key_version  # type: DescribeKeyVersionResponseBodyKeyVersion

    def validate(self):
        if self.key_version:
            self.key_version.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_version is not None:
            result['KeyVersion'] = self.key_version.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeyVersion') is not None:
            temp_model = DescribeKeyVersionResponseBodyKeyVersion()
            self.key_version = temp_model.from_map(m['KeyVersion'])
        return self


class DescribeKeyVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeKeyVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeKeyVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, regions=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecretRequest(TeaModel):
    def __init__(self, secret_name=None, fetch_tags=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.fetch_tags = TeaConverter.to_unicode(fetch_tags)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')
        return self


class DescribeSecretResponseBodyTagsTag(TeaModel):
    def __init__(self, tag_value=None, tag_key=None):
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
    def __init__(self, description=None, rotation_interval=None, last_rotation_date=None, request_id=None,
                 secret_type=None, create_time=None, automatic_rotation=None, secret_name=None, next_rotation_date=None,
                 update_time=None, extended_config=None, planned_delete_time=None, arn=None, tags=None, encryption_key_id=None):
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode
        self.last_rotation_date = TeaConverter.to_unicode(last_rotation_date)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.secret_type = TeaConverter.to_unicode(secret_type)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.automatic_rotation = TeaConverter.to_unicode(automatic_rotation)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.next_rotation_date = TeaConverter.to_unicode(next_rotation_date)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.extended_config = TeaConverter.to_unicode(extended_config)  # type: unicode
        self.planned_delete_time = TeaConverter.to_unicode(planned_delete_time)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode
        self.tags = tags  # type: DescribeSecretResponseBodyTags
        self.encryption_key_id = TeaConverter.to_unicode(encryption_key_id)  # type: unicode

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('Tags') is not None:
            temp_model = DescribeSecretResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')
        return self


class DescribeSecretResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceResponseBodyProtectionLevelsProtectionLevel(TeaModel):
    def __init__(self, type=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeServiceResponseBodyProtectionLevels(TeaModel):
    def __init__(self, protection_level=None):
        self.protection_level = protection_level  # type: list[DescribeServiceResponseBodyProtectionLevelsProtectionLevel]

    def validate(self):
        if self.protection_level:
            for k in self.protection_level:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ProtectionLevel'] = []
        if self.protection_level is not None:
            for k in self.protection_level:
                result['ProtectionLevel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.protection_level = []
        if m.get('ProtectionLevel') is not None:
            for k in m.get('ProtectionLevel'):
                temp_model = DescribeServiceResponseBodyProtectionLevelsProtectionLevel()
                self.protection_level.append(temp_model.from_map(k))
        return self


class DescribeServiceResponseBodyKeySpecsKeySpecSupportedProtectionLevels(TeaModel):
    def __init__(self, supported_protection_level=None):
        self.supported_protection_level = supported_protection_level  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.supported_protection_level is not None:
            result['SupportedProtectionLevel'] = self.supported_protection_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedProtectionLevel') is not None:
            self.supported_protection_level = m.get('SupportedProtectionLevel')
        return self


class DescribeServiceResponseBodyKeySpecsKeySpecUsages(TeaModel):
    def __init__(self, usage=None):
        self.usage = usage  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class DescribeServiceResponseBodyKeySpecsKeySpec(TeaModel):
    def __init__(self, supported_protection_levels=None, name=None, usages=None):
        self.supported_protection_levels = supported_protection_levels  # type: DescribeServiceResponseBodyKeySpecsKeySpecSupportedProtectionLevels
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.usages = usages  # type: DescribeServiceResponseBodyKeySpecsKeySpecUsages

    def validate(self):
        if self.supported_protection_levels:
            self.supported_protection_levels.validate()
        if self.usages:
            self.usages.validate()

    def to_map(self):
        result = dict()
        if self.supported_protection_levels is not None:
            result['SupportedProtectionLevels'] = self.supported_protection_levels.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.usages is not None:
            result['Usages'] = self.usages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedProtectionLevels') is not None:
            temp_model = DescribeServiceResponseBodyKeySpecsKeySpecSupportedProtectionLevels()
            self.supported_protection_levels = temp_model.from_map(m['SupportedProtectionLevels'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Usages') is not None:
            temp_model = DescribeServiceResponseBodyKeySpecsKeySpecUsages()
            self.usages = temp_model.from_map(m['Usages'])
        return self


class DescribeServiceResponseBodyKeySpecs(TeaModel):
    def __init__(self, key_spec=None):
        self.key_spec = key_spec  # type: list[DescribeServiceResponseBodyKeySpecsKeySpec]

    def validate(self):
        if self.key_spec:
            for k in self.key_spec:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['KeySpec'] = []
        if self.key_spec is not None:
            for k in self.key_spec:
                result['KeySpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_spec = []
        if m.get('KeySpec') is not None:
            for k in m.get('KeySpec'):
                temp_model = DescribeServiceResponseBodyKeySpecsKeySpec()
                self.key_spec.append(temp_model.from_map(k))
        return self


class DescribeServiceResponseBody(TeaModel):
    def __init__(self, protection_levels=None, request_id=None, key_specs=None):
        self.protection_levels = protection_levels  # type: DescribeServiceResponseBodyProtectionLevels
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.key_specs = key_specs  # type: DescribeServiceResponseBodyKeySpecs

    def validate(self):
        if self.protection_levels:
            self.protection_levels.validate()
        if self.key_specs:
            self.key_specs.validate()

    def to_map(self):
        result = dict()
        if self.protection_levels is not None:
            result['ProtectionLevels'] = self.protection_levels.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_specs is not None:
            result['KeySpecs'] = self.key_specs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProtectionLevels') is not None:
            temp_model = DescribeServiceResponseBodyProtectionLevels()
            self.protection_levels = temp_model.from_map(m['ProtectionLevels'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeySpecs') is not None:
            temp_model = DescribeServiceResponseBodyKeySpecs()
            self.key_specs = temp_model.from_map(m['KeySpecs'])
        return self


class DescribeServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableKeyRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DisableKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableKeyRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EnableKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptRequest(TeaModel):
    def __init__(self, key_id=None, plaintext=None, encryption_context=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode
        self.encryption_context = encryption_context  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        return self


class EncryptShrinkRequest(TeaModel):
    def __init__(self, key_id=None, plaintext=None, encryption_context_shrink=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode
        self.encryption_context_shrink = TeaConverter.to_unicode(encryption_context_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        return self


class EncryptResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class EncryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None, passphrase=None, export_format=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.passphrase = TeaConverter.to_unicode(passphrase)  # type: unicode
        self.export_format = TeaConverter.to_unicode(export_format)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.passphrase is not None:
            result['Passphrase'] = self.passphrase
        if self.export_format is not None:
            result['ExportFormat'] = self.export_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Passphrase') is not None:
            self.passphrase = m.get('Passphrase')
        if m.get('ExportFormat') is not None:
            self.export_format = m.get('ExportFormat')
        return self


class ExportCertificateResponseBody(TeaModel):
    def __init__(self, private_key=None, request_id=None, certificate_id=None, certificate_chain=None,
                 pkcs12blob=None, certificate=None):
        self.private_key = TeaConverter.to_unicode(private_key)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.certificate_chain = TeaConverter.to_unicode(certificate_chain)  # type: unicode
        self.pkcs12blob = TeaConverter.to_unicode(pkcs12blob)  # type: unicode
        self.certificate = TeaConverter.to_unicode(certificate)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.pkcs12blob is not None:
            result['PKCS12Blob'] = self.pkcs12blob
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('PKCS12Blob') is not None:
            self.pkcs12blob = m.get('PKCS12Blob')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        return self


class ExportCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ExportCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExportCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportDataKeyRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context=None, public_key_blob=None, wrapping_key_spec=None,
                 wrapping_algorithm=None):
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.encryption_context = encryption_context  # type: dict[unicode, any]
        self.public_key_blob = TeaConverter.to_unicode(public_key_blob)  # type: unicode
        self.wrapping_key_spec = TeaConverter.to_unicode(wrapping_key_spec)  # type: unicode
        self.wrapping_algorithm = TeaConverter.to_unicode(wrapping_algorithm)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        return self


class ExportDataKeyShrinkRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, encryption_context_shrink=None, public_key_blob=None,
                 wrapping_key_spec=None, wrapping_algorithm=None):
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.encryption_context_shrink = TeaConverter.to_unicode(encryption_context_shrink)  # type: unicode
        self.public_key_blob = TeaConverter.to_unicode(public_key_blob)  # type: unicode
        self.wrapping_key_spec = TeaConverter.to_unicode(wrapping_key_spec)  # type: unicode
        self.wrapping_algorithm = TeaConverter.to_unicode(wrapping_algorithm)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        return self


class ExportDataKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, exported_data_key=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.exported_data_key = TeaConverter.to_unicode(exported_data_key)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exported_data_key is not None:
            result['ExportedDataKey'] = self.exported_data_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExportedDataKey') is not None:
            self.exported_data_key = m.get('ExportedDataKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class ExportDataKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ExportDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExportDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAndExportDataKeyRequest(TeaModel):
    def __init__(self, key_id=None, key_spec=None, number_of_bytes=None, encryption_context=None,
                 public_key_blob=None, wrapping_key_spec=None, wrapping_algorithm=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.number_of_bytes = number_of_bytes  # type: int
        self.encryption_context = encryption_context  # type: dict[unicode, any]
        self.public_key_blob = TeaConverter.to_unicode(public_key_blob)  # type: unicode
        self.wrapping_key_spec = TeaConverter.to_unicode(wrapping_key_spec)  # type: unicode
        self.wrapping_algorithm = TeaConverter.to_unicode(wrapping_algorithm)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        return self


class GenerateAndExportDataKeyShrinkRequest(TeaModel):
    def __init__(self, key_id=None, key_spec=None, number_of_bytes=None, encryption_context_shrink=None,
                 public_key_blob=None, wrapping_key_spec=None, wrapping_algorithm=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.number_of_bytes = number_of_bytes  # type: int
        self.encryption_context_shrink = TeaConverter.to_unicode(encryption_context_shrink)  # type: unicode
        self.public_key_blob = TeaConverter.to_unicode(public_key_blob)  # type: unicode
        self.wrapping_key_spec = TeaConverter.to_unicode(wrapping_key_spec)  # type: unicode
        self.wrapping_algorithm = TeaConverter.to_unicode(wrapping_algorithm)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        if self.public_key_blob is not None:
            result['PublicKeyBlob'] = self.public_key_blob
        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec
        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        if m.get('PublicKeyBlob') is not None:
            self.public_key_blob = m.get('PublicKeyBlob')
        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')
        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')
        return self


class GenerateAndExportDataKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, exported_data_key=None, key_id=None,
                 key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.exported_data_key = TeaConverter.to_unicode(exported_data_key)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.exported_data_key is not None:
            result['ExportedDataKey'] = self.exported_data_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('ExportedDataKey') is not None:
            self.exported_data_key = m.get('ExportedDataKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class GenerateAndExportDataKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GenerateAndExportDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GenerateAndExportDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDataKeyRequest(TeaModel):
    def __init__(self, key_id=None, key_spec=None, number_of_bytes=None, encryption_context=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.number_of_bytes = number_of_bytes  # type: int
        self.encryption_context = encryption_context  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        return self


class GenerateDataKeyShrinkRequest(TeaModel):
    def __init__(self, key_id=None, key_spec=None, number_of_bytes=None, encryption_context_shrink=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.number_of_bytes = number_of_bytes  # type: int
        self.encryption_context_shrink = TeaConverter.to_unicode(encryption_context_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        return self


class GenerateDataKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, plaintext=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.plaintext = TeaConverter.to_unicode(plaintext)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class GenerateDataKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GenerateDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GenerateDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDataKeyWithoutPlaintextRequest(TeaModel):
    def __init__(self, key_id=None, key_spec=None, number_of_bytes=None, encryption_context=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.number_of_bytes = number_of_bytes  # type: int
        self.encryption_context = encryption_context  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.encryption_context is not None:
            result['EncryptionContext'] = self.encryption_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('EncryptionContext') is not None:
            self.encryption_context = m.get('EncryptionContext')
        return self


class GenerateDataKeyWithoutPlaintextShrinkRequest(TeaModel):
    def __init__(self, key_id=None, key_spec=None, number_of_bytes=None, encryption_context_shrink=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.number_of_bytes = number_of_bytes  # type: int
        self.encryption_context_shrink = TeaConverter.to_unicode(encryption_context_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.number_of_bytes is not None:
            result['NumberOfBytes'] = self.number_of_bytes
        if self.encryption_context_shrink is not None:
            result['EncryptionContext'] = self.encryption_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('NumberOfBytes') is not None:
            self.number_of_bytes = m.get('NumberOfBytes')
        if m.get('EncryptionContext') is not None:
            self.encryption_context_shrink = m.get('EncryptionContext')
        return self


class GenerateDataKeyWithoutPlaintextResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class GenerateDataKeyWithoutPlaintextResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GenerateDataKeyWithoutPlaintextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GenerateDataKeyWithoutPlaintextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, csr=None, request_id=None, certificate_id=None, certificate_chain=None, certificate=None):
        self.csr = TeaConverter.to_unicode(csr)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.certificate_chain = TeaConverter.to_unicode(certificate_chain)  # type: unicode
        self.certificate = TeaConverter.to_unicode(certificate)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.csr is not None:
            result['Csr'] = self.csr
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        return self


class GetCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersForImportRequest(TeaModel):
    def __init__(self, key_id=None, wrapping_algorithm=None, wrapping_key_spec=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.wrapping_algorithm = TeaConverter.to_unicode(wrapping_algorithm)  # type: unicode
        self.wrapping_key_spec = TeaConverter.to_unicode(wrapping_key_spec)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, public_key=None, key_id=None, token_expire_time=None, import_token=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.public_key = TeaConverter.to_unicode(public_key)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.token_expire_time = TeaConverter.to_unicode(token_expire_time)  # type: unicode
        self.import_token = TeaConverter.to_unicode(import_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time
        if self.import_token is not None:
            result['ImportToken'] = self.import_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')
        return self


class GetParametersForImportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetParametersForImportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetParametersForImportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicKeyRequest(TeaModel):
    def __init__(self, key_id=None, key_version_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, public_key=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.public_key = TeaConverter.to_unicode(public_key)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class GetPublicKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetPublicKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRandomPasswordRequest(TeaModel):
    def __init__(self, password_length=None, exclude_characters=None, exclude_lowercase=None,
                 exclude_uppercase=None, exclude_numbers=None, exclude_punctuation=None, require_each_included_type=None):
        self.password_length = TeaConverter.to_unicode(password_length)  # type: unicode
        self.exclude_characters = TeaConverter.to_unicode(exclude_characters)  # type: unicode
        self.exclude_lowercase = TeaConverter.to_unicode(exclude_lowercase)  # type: unicode
        self.exclude_uppercase = TeaConverter.to_unicode(exclude_uppercase)  # type: unicode
        self.exclude_numbers = TeaConverter.to_unicode(exclude_numbers)  # type: unicode
        self.exclude_punctuation = TeaConverter.to_unicode(exclude_punctuation)  # type: unicode
        self.require_each_included_type = TeaConverter.to_unicode(require_each_included_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.password_length is not None:
            result['PasswordLength'] = self.password_length
        if self.exclude_characters is not None:
            result['ExcludeCharacters'] = self.exclude_characters
        if self.exclude_lowercase is not None:
            result['ExcludeLowercase'] = self.exclude_lowercase
        if self.exclude_uppercase is not None:
            result['ExcludeUppercase'] = self.exclude_uppercase
        if self.exclude_numbers is not None:
            result['ExcludeNumbers'] = self.exclude_numbers
        if self.exclude_punctuation is not None:
            result['ExcludePunctuation'] = self.exclude_punctuation
        if self.require_each_included_type is not None:
            result['RequireEachIncludedType'] = self.require_each_included_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PasswordLength') is not None:
            self.password_length = m.get('PasswordLength')
        if m.get('ExcludeCharacters') is not None:
            self.exclude_characters = m.get('ExcludeCharacters')
        if m.get('ExcludeLowercase') is not None:
            self.exclude_lowercase = m.get('ExcludeLowercase')
        if m.get('ExcludeUppercase') is not None:
            self.exclude_uppercase = m.get('ExcludeUppercase')
        if m.get('ExcludeNumbers') is not None:
            self.exclude_numbers = m.get('ExcludeNumbers')
        if m.get('ExcludePunctuation') is not None:
            self.exclude_punctuation = m.get('ExcludePunctuation')
        if m.get('RequireEachIncludedType') is not None:
            self.require_each_included_type = m.get('RequireEachIncludedType')
        return self


class GetRandomPasswordResponseBody(TeaModel):
    def __init__(self, random_password=None, request_id=None):
        self.random_password = TeaConverter.to_unicode(random_password)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetRandomPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetRandomPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretValueRequest(TeaModel):
    def __init__(self, secret_name=None, version_stage=None, version_id=None, fetch_extended_config=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_stage = TeaConverter.to_unicode(version_stage)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.fetch_extended_config = fetch_extended_config  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.fetch_extended_config is not None:
            result['FetchExtendedConfig'] = self.fetch_extended_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('FetchExtendedConfig') is not None:
            self.fetch_extended_config = m.get('FetchExtendedConfig')
        return self


class GetSecretValueResponseBodyVersionStages(TeaModel):
    def __init__(self, version_stage=None):
        self.version_stage = version_stage  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, version_id=None, rotation_interval=None, last_rotation_date=None, request_id=None,
                 secret_type=None, create_time=None, secret_data_type=None, version_stages=None, automatic_rotation=None,
                 secret_name=None, next_rotation_date=None, extended_config=None, secret_data=None):
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode
        self.last_rotation_date = TeaConverter.to_unicode(last_rotation_date)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.secret_type = TeaConverter.to_unicode(secret_type)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.secret_data_type = TeaConverter.to_unicode(secret_data_type)  # type: unicode
        self.version_stages = version_stages  # type: GetSecretValueResponseBodyVersionStages
        self.automatic_rotation = TeaConverter.to_unicode(automatic_rotation)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.next_rotation_date = TeaConverter.to_unicode(next_rotation_date)  # type: unicode
        self.extended_config = TeaConverter.to_unicode(extended_config)  # type: unicode
        self.secret_data = TeaConverter.to_unicode(secret_data)  # type: unicode

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('VersionStages') is not None:
            temp_model = GetSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        return self


class GetSecretValueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetSecretValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetSecretValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportCertificateRequest(TeaModel):
    def __init__(self, pkcs12blob=None, passphrase=None):
        self.pkcs12blob = TeaConverter.to_unicode(pkcs12blob)  # type: unicode
        self.passphrase = TeaConverter.to_unicode(passphrase)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pkcs12blob is not None:
            result['PKCS12Blob'] = self.pkcs12blob
        if self.passphrase is not None:
            result['Passphrase'] = self.passphrase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PKCS12Blob') is not None:
            self.pkcs12blob = m.get('PKCS12Blob')
        if m.get('Passphrase') is not None:
            self.passphrase = m.get('Passphrase')
        return self


class ImportCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_id=None, arn=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ImportCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ImportCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ImportCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportEncryptionCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None, encrypted_symmetric_key=None, encrypted_private_key=None,
                 symmetric_algorithm=None, asymmetric_algorithm=None, certificate=None, certificate_chain=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.encrypted_symmetric_key = TeaConverter.to_unicode(encrypted_symmetric_key)  # type: unicode
        self.encrypted_private_key = TeaConverter.to_unicode(encrypted_private_key)  # type: unicode
        self.symmetric_algorithm = TeaConverter.to_unicode(symmetric_algorithm)  # type: unicode
        self.asymmetric_algorithm = TeaConverter.to_unicode(asymmetric_algorithm)  # type: unicode
        self.certificate = TeaConverter.to_unicode(certificate)  # type: unicode
        self.certificate_chain = TeaConverter.to_unicode(certificate_chain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.encrypted_symmetric_key is not None:
            result['EncryptedSymmetricKey'] = self.encrypted_symmetric_key
        if self.encrypted_private_key is not None:
            result['EncryptedPrivateKey'] = self.encrypted_private_key
        if self.symmetric_algorithm is not None:
            result['SymmetricAlgorithm'] = self.symmetric_algorithm
        if self.asymmetric_algorithm is not None:
            result['AsymmetricAlgorithm'] = self.asymmetric_algorithm
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('EncryptedSymmetricKey') is not None:
            self.encrypted_symmetric_key = m.get('EncryptedSymmetricKey')
        if m.get('EncryptedPrivateKey') is not None:
            self.encrypted_private_key = m.get('EncryptedPrivateKey')
        if m.get('SymmetricAlgorithm') is not None:
            self.symmetric_algorithm = m.get('SymmetricAlgorithm')
        if m.get('AsymmetricAlgorithm') is not None:
            self.asymmetric_algorithm = m.get('AsymmetricAlgorithm')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        return self


class ImportEncryptionCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_id=None, arn=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class ImportEncryptionCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ImportEncryptionCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ImportEncryptionCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyMaterialRequest(TeaModel):
    def __init__(self, key_id=None, encrypted_key_material=None, import_token=None, key_material_expire_unix=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.encrypted_key_material = TeaConverter.to_unicode(encrypted_key_material)  # type: unicode
        self.import_token = TeaConverter.to_unicode(import_token)  # type: unicode
        self.key_material_expire_unix = key_material_expire_unix  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.encrypted_key_material is not None:
            result['EncryptedKeyMaterial'] = self.encrypted_key_material
        if self.import_token is not None:
            result['ImportToken'] = self.import_token
        if self.key_material_expire_unix is not None:
            result['KeyMaterialExpireUnix'] = self.key_material_expire_unix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('EncryptedKeyMaterial') is not None:
            self.encrypted_key_material = m.get('EncryptedKeyMaterial')
        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')
        if m.get('KeyMaterialExpireUnix') is not None:
            self.key_material_expire_unix = m.get('KeyMaterialExpireUnix')
        return self


class ImportKeyMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ImportKeyMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ImportKeyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, alias_arn=None, key_id=None, alias_name=None):
        self.alias_arn = TeaConverter.to_unicode(alias_arn)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.alias_name = TeaConverter.to_unicode(alias_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
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
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, aliases=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.aliases = aliases  # type: ListAliasesResponseBodyAliases

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Aliases') is not None:
            temp_model = ListAliasesResponseBodyAliases()
            self.aliases = temp_model.from_map(m['Aliases'])
        return self


class ListAliasesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAliasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAliasesByKeyIdRequest(TeaModel):
    def __init__(self, key_id=None, page_number=None, page_size=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, alias_arn=None, key_id=None, alias_name=None):
        self.alias_arn = TeaConverter.to_unicode(alias_arn)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.alias_name = TeaConverter.to_unicode(alias_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias_arn is not None:
            result['AliasArn'] = self.alias_arn
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasArn') is not None:
            self.alias_arn = m.get('AliasArn')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
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
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, aliases=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.aliases = aliases  # type: ListAliasesByKeyIdResponseBodyAliases

    def validate(self):
        if self.aliases:
            self.aliases.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.aliases is not None:
            result['Aliases'] = self.aliases.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Aliases') is not None:
            temp_model = ListAliasesByKeyIdResponseBodyAliases()
            self.aliases = temp_model.from_map(m['Aliases'])
        return self


class ListAliasesByKeyIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAliasesByKeyIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListAliasesByKeyIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCertificatesRequest(TeaModel):
    def __init__(self, subject=None, issuer=None, status=None, page_number=None, page_size=None):
        self.subject = TeaConverter.to_unicode(subject)  # type: unicode
        self.issuer = TeaConverter.to_unicode(issuer)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.status is not None:
            result['Status'] = self.status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCertificatesResponseBodyCertificateSummaryListCertificateSummary(TeaModel):
    def __init__(self, status=None, key_spec=None, subject=None, protection_level=None, issuer=None, not_before=None,
                 not_after=None, certificate_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.key_spec = TeaConverter.to_unicode(key_spec)  # type: unicode
        self.subject = TeaConverter.to_unicode(subject)  # type: unicode
        self.protection_level = TeaConverter.to_unicode(protection_level)  # type: unicode
        self.issuer = TeaConverter.to_unicode(issuer)  # type: unicode
        self.not_before = TeaConverter.to_unicode(not_before)  # type: unicode
        self.not_after = TeaConverter.to_unicode(not_after)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.key_spec is not None:
            result['KeySpec'] = self.key_spec
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('KeySpec') is not None:
            self.key_spec = m.get('KeySpec')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class ListCertificatesResponseBodyCertificateSummaryList(TeaModel):
    def __init__(self, certificate_summary=None):
        self.certificate_summary = certificate_summary  # type: list[ListCertificatesResponseBodyCertificateSummaryListCertificateSummary]

    def validate(self):
        if self.certificate_summary:
            for k in self.certificate_summary:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CertificateSummary'] = []
        if self.certificate_summary is not None:
            for k in self.certificate_summary:
                result['CertificateSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificate_summary = []
        if m.get('CertificateSummary') is not None:
            for k in m.get('CertificateSummary'):
                temp_model = ListCertificatesResponseBodyCertificateSummaryListCertificateSummary()
                self.certificate_summary.append(temp_model.from_map(k))
        return self


class ListCertificatesResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, certificate_summary_list=None,
                 total_size=None):
        self.page_size = page_size  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.certificate_summary_list = certificate_summary_list  # type: ListCertificatesResponseBodyCertificateSummaryList
        self.total_size = total_size  # type: int

    def validate(self):
        if self.certificate_summary_list:
            self.certificate_summary_list.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.certificate_summary_list is not None:
            result['CertificateSummaryList'] = self.certificate_summary_list.to_map()
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('CertificateSummaryList') is not None:
            temp_model = ListCertificatesResponseBodyCertificateSummaryList()
            self.certificate_summary_list = temp_model.from_map(m['CertificateSummaryList'])
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListCertificatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListCertificatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeysRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, filters=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.filters = TeaConverter.to_unicode(filters)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.filters is not None:
            result['Filters'] = self.filters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        return self


class ListKeysResponseBodyKeysKey(TeaModel):
    def __init__(self, key_arn=None, key_id=None):
        self.key_arn = TeaConverter.to_unicode(key_arn)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, keys=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.keys = keys  # type: ListKeysResponseBodyKeys

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Keys') is not None:
            temp_model = ListKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        return self


class ListKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKeyVersionsRequest(TeaModel):
    def __init__(self, key_id=None, page_number=None, page_size=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, key_version_id=None, key_id=None, creation_date=None):
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.creation_date = TeaConverter.to_unicode(creation_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')
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
    def __init__(self, key_versions=None, total_count=None, page_size=None, request_id=None, page_number=None):
        self.key_versions = key_versions  # type: ListKeyVersionsResponseBodyKeyVersions
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int

    def validate(self):
        if self.key_versions:
            self.key_versions.validate()

    def to_map(self):
        result = dict()
        if self.key_versions is not None:
            result['KeyVersions'] = self.key_versions.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyVersions') is not None:
            temp_model = ListKeyVersionsResponseBodyKeyVersions()
            self.key_versions = temp_model.from_map(m['KeyVersions'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListKeyVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListKeyVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListKeyVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTagsRequest(TeaModel):
    def __init__(self, key_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, key_id=None, tag_value=None, tag_key=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tags = tags  # type: ListResourceTagsResponseBodyTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListResourceTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListResourceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretsRequest(TeaModel):
    def __init__(self, fetch_tags=None, page_number=None, page_size=None, filters=None):
        self.fetch_tags = TeaConverter.to_unicode(fetch_tags)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.filters = TeaConverter.to_unicode(filters)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.filters is not None:
            result['Filters'] = self.filters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        return self


class ListSecretsResponseBodySecretListSecretTagsTag(TeaModel):
    def __init__(self, tag_value=None, tag_key=None):
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
    def __init__(self, update_time=None, create_time=None, secret_name=None, tags=None, secret_type=None,
                 planned_delete_time=None):
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.tags = tags  # type: ListSecretsResponseBodySecretListSecretTags
        self.secret_type = TeaConverter.to_unicode(secret_type)  # type: unicode
        self.planned_delete_time = TeaConverter.to_unicode(planned_delete_time)  # type: unicode

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.secret_type is not None:
            result['SecretType'] = self.secret_type
        if self.planned_delete_time is not None:
            result['PlannedDeleteTime'] = self.planned_delete_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('Tags') is not None:
            temp_model = ListSecretsResponseBodySecretListSecretTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')
        if m.get('PlannedDeleteTime') is not None:
            self.planned_delete_time = m.get('PlannedDeleteTime')
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
    def __init__(self, total_count=None, page_size=None, request_id=None, secret_list=None, page_number=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.secret_list = secret_list  # type: ListSecretsResponseBodySecretList
        self.page_number = page_number  # type: int

    def validate(self):
        if self.secret_list:
            self.secret_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_list is not None:
            result['SecretList'] = self.secret_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretList') is not None:
            temp_model = ListSecretsResponseBodySecretList()
            self.secret_list = temp_model.from_map(m['SecretList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListSecretsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListSecretsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListSecretsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretVersionIdsRequest(TeaModel):
    def __init__(self, secret_name=None, include_deprecated=None, page_number=None, page_size=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.include_deprecated = TeaConverter.to_unicode(include_deprecated)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.include_deprecated is not None:
            result['IncludeDeprecated'] = self.include_deprecated
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('IncludeDeprecated') is not None:
            self.include_deprecated = m.get('IncludeDeprecated')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages(TeaModel):
    def __init__(self, version_stage=None):
        self.version_stage = version_stage  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.version_stages = version_stages  # type: ListSecretVersionIdsResponseBodyVersionIdsVersionIdVersionStages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
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
    def __init__(self, secret_name=None, total_count=None, request_id=None, page_size=None, page_number=None,
                 version_ids=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.version_ids = version_ids  # type: ListSecretVersionIdsResponseBodyVersionIds

    def validate(self):
        if self.version_ids:
            self.version_ids.validate()

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.version_ids is not None:
            result['VersionIds'] = self.version_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('VersionIds') is not None:
            temp_model = ListSecretVersionIdsResponseBodyVersionIds()
            self.version_ids = temp_model.from_map(m['VersionIds'])
        return self


class ListSecretVersionIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListSecretVersionIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListSecretVersionIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenKmsServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: OpenKmsServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = OpenKmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutSecretValueRequest(TeaModel):
    def __init__(self, version_id=None, secret_name=None, secret_data=None, secret_data_type=None,
                 version_stages=None):
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.secret_data = TeaConverter.to_unicode(secret_data)  # type: unicode
        self.secret_data_type = TeaConverter.to_unicode(secret_data_type)  # type: unicode
        self.version_stages = TeaConverter.to_unicode(version_stages)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.secret_data is not None:
            result['SecretData'] = self.secret_data
        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')
        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')
        if m.get('VersionStages') is not None:
            self.version_stages = m.get('VersionStages')
        return self


class PutSecretValueResponseBodyVersionStages(TeaModel):
    def __init__(self, version_stage=None):
        self.version_stage = version_stage  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, secret_name=None, version_id=None, request_id=None, version_stages=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.version_stages = version_stages  # type: PutSecretValueResponseBodyVersionStages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionStages') is not None:
            temp_model = PutSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m['VersionStages'])
        return self


class PutSecretValueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: PutSecretValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = PutSecretValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReEncryptRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, source_key_id=None, source_key_version_id=None,
                 source_encryption_algorithm=None, source_encryption_context=None, destination_key_id=None,
                 destination_encryption_context=None):
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.source_key_id = TeaConverter.to_unicode(source_key_id)  # type: unicode
        self.source_key_version_id = TeaConverter.to_unicode(source_key_version_id)  # type: unicode
        self.source_encryption_algorithm = TeaConverter.to_unicode(source_encryption_algorithm)  # type: unicode
        self.source_encryption_context = source_encryption_context  # type: dict[unicode, any]
        self.destination_key_id = TeaConverter.to_unicode(destination_key_id)  # type: unicode
        self.destination_encryption_context = destination_encryption_context  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id
        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id
        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm
        if self.source_encryption_context is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context
        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id
        if self.destination_encryption_context is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')
        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')
        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')
        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context = m.get('SourceEncryptionContext')
        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')
        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context = m.get('DestinationEncryptionContext')
        return self


class ReEncryptShrinkRequest(TeaModel):
    def __init__(self, ciphertext_blob=None, source_key_id=None, source_key_version_id=None,
                 source_encryption_algorithm=None, source_encryption_context_shrink=None, destination_key_id=None,
                 destination_encryption_context_shrink=None):
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.source_key_id = TeaConverter.to_unicode(source_key_id)  # type: unicode
        self.source_key_version_id = TeaConverter.to_unicode(source_key_version_id)  # type: unicode
        self.source_encryption_algorithm = TeaConverter.to_unicode(source_encryption_algorithm)  # type: unicode
        self.source_encryption_context_shrink = TeaConverter.to_unicode(source_encryption_context_shrink)  # type: unicode
        self.destination_key_id = TeaConverter.to_unicode(destination_key_id)  # type: unicode
        self.destination_encryption_context_shrink = TeaConverter.to_unicode(destination_encryption_context_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.source_key_id is not None:
            result['SourceKeyId'] = self.source_key_id
        if self.source_key_version_id is not None:
            result['SourceKeyVersionId'] = self.source_key_version_id
        if self.source_encryption_algorithm is not None:
            result['SourceEncryptionAlgorithm'] = self.source_encryption_algorithm
        if self.source_encryption_context_shrink is not None:
            result['SourceEncryptionContext'] = self.source_encryption_context_shrink
        if self.destination_key_id is not None:
            result['DestinationKeyId'] = self.destination_key_id
        if self.destination_encryption_context_shrink is not None:
            result['DestinationEncryptionContext'] = self.destination_encryption_context_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('SourceKeyId') is not None:
            self.source_key_id = m.get('SourceKeyId')
        if m.get('SourceKeyVersionId') is not None:
            self.source_key_version_id = m.get('SourceKeyVersionId')
        if m.get('SourceEncryptionAlgorithm') is not None:
            self.source_encryption_algorithm = m.get('SourceEncryptionAlgorithm')
        if m.get('SourceEncryptionContext') is not None:
            self.source_encryption_context_shrink = m.get('SourceEncryptionContext')
        if m.get('DestinationKeyId') is not None:
            self.destination_key_id = m.get('DestinationKeyId')
        if m.get('DestinationEncryptionContext') is not None:
            self.destination_encryption_context_shrink = m.get('DestinationEncryptionContext')
        return self


class ReEncryptResponseBody(TeaModel):
    def __init__(self, request_id=None, ciphertext_blob=None, key_id=None, key_version_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ciphertext_blob = TeaConverter.to_unicode(ciphertext_blob)  # type: unicode
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.key_version_id = TeaConverter.to_unicode(key_version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')
        return self


class ReEncryptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ReEncryptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ReEncryptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreSecretRequest(TeaModel):
    def __init__(self, secret_name=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, secret_name=None, request_id=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestoreSecretResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RestoreSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RestoreSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RotateSecretRequest(TeaModel):
    def __init__(self, secret_name=None, version_id=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, version_id=None, secret_name=None, request_id=None, arn=None):
        self.version_id = TeaConverter.to_unicode(version_id)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.arn = TeaConverter.to_unicode(arn)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class RotateSecretResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RotateSecretResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RotateSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScheduleKeyDeletionRequest(TeaModel):
    def __init__(self, key_id=None, pending_window_in_days=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.pending_window_in_days = pending_window_in_days  # type: int

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ScheduleKeyDeletionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ScheduleKeyDeletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourceRequest(TeaModel):
    def __init__(self, key_id=None, tags=None, secret_name=None, certificate_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class TagResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TagResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TagResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourceRequest(TeaModel):
    def __init__(self, key_id=None, tag_keys=None, secret_name=None, certificate_id=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.tag_keys = TeaConverter.to_unicode(tag_keys)  # type: unicode
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class UntagResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UntagResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UntagResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(self, key_id=None, alias_name=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.alias_name = TeaConverter.to_unicode(alias_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCertificateStatusRequest(TeaModel):
    def __init__(self, certificate_id=None, status=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateCertificateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateCertificateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKeyDescriptionRequest(TeaModel):
    def __init__(self, key_id=None, description=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateKeyDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateKeyDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateKeyDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRotationPolicyRequest(TeaModel):
    def __init__(self, key_id=None, enable_automatic_rotation=None, rotation_interval=None):
        self.key_id = TeaConverter.to_unicode(key_id)  # type: unicode
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class UpdateRotationPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateRotationPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateRotationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretRotationPolicyRequest(TeaModel):
    def __init__(self, secret_name=None, enable_automatic_rotation=None, rotation_interval=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.enable_automatic_rotation = enable_automatic_rotation  # type: bool
        self.rotation_interval = TeaConverter.to_unicode(rotation_interval)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation
        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')
        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')
        return self


class UpdateSecretRotationPolicyResponseBody(TeaModel):
    def __init__(self, secret_name=None, request_id=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSecretRotationPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateSecretRotationPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateSecretRotationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretVersionStageRequest(TeaModel):
    def __init__(self, secret_name=None, version_stage=None, remove_from_version=None, move_to_version=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.version_stage = TeaConverter.to_unicode(version_stage)  # type: unicode
        self.remove_from_version = TeaConverter.to_unicode(remove_from_version)  # type: unicode
        self.move_to_version = TeaConverter.to_unicode(move_to_version)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage
        if self.remove_from_version is not None:
            result['RemoveFromVersion'] = self.remove_from_version
        if self.move_to_version is not None:
            result['MoveToVersion'] = self.move_to_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')
        if m.get('RemoveFromVersion') is not None:
            self.remove_from_version = m.get('RemoveFromVersion')
        if m.get('MoveToVersion') is not None:
            self.move_to_version = m.get('MoveToVersion')
        return self


class UpdateSecretVersionStageResponseBody(TeaModel):
    def __init__(self, secret_name=None, request_id=None):
        self.secret_name = TeaConverter.to_unicode(secret_name)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSecretVersionStageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateSecretVersionStageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateSecretVersionStageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadCertificateRequest(TeaModel):
    def __init__(self, certificate_id=None, certificate=None, certificate_chain=None):
        self.certificate_id = TeaConverter.to_unicode(certificate_id)  # type: unicode
        self.certificate = TeaConverter.to_unicode(certificate)  # type: unicode
        self.certificate_chain = TeaConverter.to_unicode(certificate_chain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')
        return self


class UploadCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UploadCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UploadCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


