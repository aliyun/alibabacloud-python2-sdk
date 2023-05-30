# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('kms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def asymmetric_decrypt_with_options(self, request, runtime):
        """
        This operation supports only asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists supported encryption algorithms.
        | KeySpec | Algorithm | Description | Maximum length in bytes |
        | ------- | --------- | ----------- | ----------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 384 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 384 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6144 |
        In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the decryption algorithm `RSAES_OAEP_SHA_1` are used to decrypt the ciphertext `BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1W****==`.
        

        @param request: AsymmetricDecryptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AsymmetricDecryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricDecrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricDecryptResponse(),
            self.call_api(params, req, runtime)
        )

    def asymmetric_decrypt(self, request):
        """
        This operation supports only asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists supported encryption algorithms.
        | KeySpec | Algorithm | Description | Maximum length in bytes |
        | ------- | --------- | ----------- | ----------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 256 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 256 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 384 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 384 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6144 |
        In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the decryption algorithm `RSAES_OAEP_SHA_1` are used to decrypt the ciphertext `BQKP+1zK6+ZEMxTP5qaVzcsgXtWplYBKm0NXdSnB5FzliFxE1bSiu4dnEIlca2JpeH7yz1/S6fed630H+hIH6DoM25fTLNcKj+mFB0Xnh9m2+HN59Mn4qyTfcUeadnfCXSWcGBouhXFwcdd2rJ3n337bzTf4jm659gZu3L0i6PLuxM9p7mqdwO0cKJPfGVfhnfMz+f4alMg79WB/NNyE2lyX7/qxvV49ObNrrJbKSFiz8Djocaf0IESNLMbfYI5bXjWkJlX92DQbKhibtQW8ZOJ//ZC6t0AWcUoKL6QDm/dg5koQalcleRinpB+QadFm894sLbVZ9+N4GVsv1W****==`.
        

        @param request: AsymmetricDecryptRequest

        @return: AsymmetricDecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    def asymmetric_encrypt_with_options(self, request, runtime):
        """
        This operation is supported only for asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists the supported encryption algorithms:
        | KeySpec | Algorithm | Description | Maximum number of bytes that can be encrypted |
        | ------- | --------- | ----------- | --------------------------------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 318 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 342 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6047 |
        You can use the asymmetric CMK whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the algorithm `RSAES_OAEP_SHA_1` to encrypt the plaintext `SGVsbG8gd29ybGQ=` based on the parameter settings provided in this topic.
        

        @param request: AsymmetricEncryptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AsymmetricEncryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    def asymmetric_encrypt(self, request):
        """
        This operation is supported only for asymmetric keys for which the *Usage** parameter is set to **ENCRYPT/DECRYPT**. The following table lists the supported encryption algorithms:
        | KeySpec | Algorithm | Description | Maximum number of bytes that can be encrypted |
        | ------- | --------- | ----------- | --------------------------------------------- |
        | RSA_2048 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 190 |
        | RSA_2048 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 214 |
        | RSA_3072 | RSAES_OAEP_SHA_256 | RSAES-OAEP using SHA-256 and MGF1 with SHA-256 | 318 |
        | RSA_3072 | RSAES_OAEP_SHA_1 | RSAES-OAEP using SHA1 and MGF1 with SHA1 | 342 |
        | EC_SM2 | SM2PKE | SM2 public key encryption algorithm based on elliptic curves | 6047 |
        You can use the asymmetric CMK whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the algorithm `RSAES_OAEP_SHA_1` to encrypt the plaintext `SGVsbG8gd29ybGQ=` based on the parameter settings provided in this topic.
        

        @param request: AsymmetricEncryptRequest

        @return: AsymmetricEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    def asymmetric_sign_with_options(self, request, runtime):
        """
        Generates a signature by using an asymmetric key.
        

        @param request: AsymmetricSignRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AsymmetricSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricSign',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricSignResponse(),
            self.call_api(params, req, runtime)
        )

    def asymmetric_sign(self, request):
        """
        Generates a signature by using an asymmetric key.
        

        @param request: AsymmetricSignRequest

        @return: AsymmetricSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    def asymmetric_verify_with_options(self, request, runtime):
        """
        This operation supports only asymmetric keys for which the *Usage** parameter is set to **SIGN/VERIFY**. The following table describes the supported signature algorithms.
        | KeySpec | Algorithm | Description |
        | ------- | --------- | ----------- |
        | RSA_2048 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_2048 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | RSA_3072 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_3072 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | EC_P256 | ECDSA_SHA_256 | ECDSA on the P-256 Curve(secp256r1) with a SHA-256 digest |
        | EC_P256K | ECDSA_SHA_256 | ECDSA on the P-256K Curve(secp256k1) with a SHA-256 digest |
        | EC_SM2 | SM2DSA | SM2 elliptic curve public key encryption algorithm |
        >  When you calculate the SM2 signature based on GB/T 32918, the **Digest** parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.  In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the signature algorithm RSA_PSS_SHA_256 are used to verify the signature `M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq****==` of the digest `ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw=`.
        

        @param request: AsymmetricVerifyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AsymmetricVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AsymmetricVerify',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.AsymmetricVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def asymmetric_verify(self, request):
        """
        This operation supports only asymmetric keys for which the *Usage** parameter is set to **SIGN/VERIFY**. The following table describes the supported signature algorithms.
        | KeySpec | Algorithm | Description |
        | ------- | --------- | ----------- |
        | RSA_2048 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_2048 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | RSA_3072 | RSA_PSS_SHA_256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |
        | RSA_3072 | RSA_PKCS1_SHA_256 | RSASSA-PKCS1-v1_5 using SHA-256 |
        | EC_P256 | ECDSA_SHA_256 | ECDSA on the P-256 Curve(secp256r1) with a SHA-256 digest |
        | EC_P256K | ECDSA_SHA_256 | ECDSA on the P-256K Curve(secp256k1) with a SHA-256 digest |
        | EC_SM2 | SM2DSA | SM2 elliptic curve public key encryption algorithm |
        >  When you calculate the SM2 signature based on GB/T 32918, the **Digest** parameter is used to calculate the digest value of the combination of Z(A) and M, rather than the SM3 digest value. M indicates the original message to be signed. Z(A) indicates the hash value for User A. The hash value is defined in GB/T 32918.  In this example, the asymmetric key whose ID is `5c438b18-05be-40ad-b6c2-3be6752c****` and version ID is `2ab1a983-7072-4bbc-a582-584b5bd8****` and the signature algorithm RSA_PSS_SHA_256 are used to verify the signature `M2CceNZH00ZgL9ED/ZHFp21YRAvYeZHknJUc207OCZ0N9wNn9As4z2bON3FF3je+1Nu+2+/8Zj50HpMTpzYpMp2R93cYmACCmhaYoKydxylbyGzJR8y9likZRCrkD38lRoS40aBBvv/6iRKzQuo9EGYVcel36cMNg00VmYNBy3pa1rwg3gA4l3cy6kjayZja1WGPkVhrVKsrJMdbpl0ApLjXKuD8rw1n1XLCwCUEL5eLPljTZaAveqdOFQOiZnZEGI27qIiZe7I1fN8tcz6anS/gTM7xRKE++5egEvRWlTQQTJeApnPSiUPA+8ZykNdelQsOQh5SrGoyI4A5pq****==` of the digest `ZOyIygCyaOW6GjVnihtTFtIS9PNmskdyMlNKiuyjfzw=`.
        

        @param request: AsymmetricVerifyRequest

        @return: AsymmetricVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    def cancel_key_deletion_with_options(self, request, runtime):
        """
        If the deletion task of a CMK is canceled, the CMK returns to the Enabled state.
        

        @param request: CancelKeyDeletionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelKeyDeletionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelKeyDeletion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CancelKeyDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_key_deletion(self, request):
        """
        If the deletion task of a CMK is canceled, the CMK returns to the Enabled state.
        

        @param request: CancelKeyDeletionRequest

        @return: CancelKeyDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_key_deletion_with_options(request, runtime)

    def certificate_private_key_decrypt_with_options(self, request, runtime):
        """
        Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to decrypt the data `ZOyIygCyaOW6Gj****MlNKiuyjfzw=`.
        

        @param request: CertificatePrivateKeyDecryptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CertificatePrivateKeyDecryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePrivateKeyDecrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePrivateKeyDecryptResponse(),
            self.call_api(params, req, runtime)
        )

    def certificate_private_key_decrypt(self, request):
        """
        Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to decrypt the data `ZOyIygCyaOW6Gj****MlNKiuyjfzw=`.
        

        @param request: CertificatePrivateKeyDecryptRequest

        @return: CertificatePrivateKeyDecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_decrypt_with_options(request, runtime)

    def certificate_private_key_sign_with_options(self, request, runtime):
        """
        The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the signature algorithm `ECDSA_SHA_256` are used to generate a signature for the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        

        @param request: CertificatePrivateKeySignRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CertificatePrivateKeySignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePrivateKeySign',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePrivateKeySignResponse(),
            self.call_api(params, req, runtime)
        )

    def certificate_private_key_sign(self, request):
        """
        The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the signature algorithm `ECDSA_SHA_256` are used to generate a signature for the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        

        @param request: CertificatePrivateKeySignRequest

        @return: CertificatePrivateKeySignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_sign_with_options(request, runtime)

    def certificate_public_key_encrypt_with_options(self, request, runtime):
        """
        Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to encrypt the data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        

        @param request: CertificatePublicKeyEncryptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CertificatePublicKeyEncryptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePublicKeyEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePublicKeyEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    def certificate_public_key_encrypt(self, request):
        """
        Limit: The encryption algorithm in the request parameters must match the key type.
        The following table describes the mapping between encryption algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSAES_OAEP_SHA_1 | RSA_2048 |
        | RSAES_OAEP_SHA_256 | RSA_2048 |
        | SM2PKE | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the encryption algorithm `RSAES_OAEP_SHA_256` are used to encrypt the data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        

        @param request: CertificatePublicKeyEncryptRequest

        @return: CertificatePublicKeyEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_encrypt_with_options(request, runtime)

    def certificate_public_key_verify_with_options(self, request, runtime):
        """
        The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the signature algorithm `ECDSA_SHA_256` are used to verify the digital signature `ZOyIygCyaOW6Gj****MlNKiuyjfzw=` of the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        

        @param request: CertificatePublicKeyVerifyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CertificatePublicKeyVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signature_value):
            query['SignatureValue'] = request.signature_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CertificatePublicKeyVerify',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CertificatePublicKeyVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def certificate_public_key_verify(self, request):
        """
        The signature algorithm in the request parameters must match the key type. The following table describes the mapping between signature algorithms and key types.
        | Algorithm | Key Spec |
        | --------- | -------- |
        | RSA_PKCS1_SHA_256 | RSA_2048 |
        | RSA_PSS_SHA_256 | RSA_2048 |
        | ECDSA_SHA_256 | EC_P256 |
        | SM2DSA | EC_SM2 |
        In this example, the certificate whose ID is `12345678-1234-1234-1234-12345678****` and the signature algorithm `ECDSA_SHA_256` are used to verify the digital signature `ZOyIygCyaOW6Gj****MlNKiuyjfzw=` of the raw data `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=`.
        

        @param request: CertificatePublicKeyVerifyRequest

        @return: CertificatePublicKeyVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_verify_with_options(request, runtime)

    def create_alias_with_options(self, request, runtime):
        """
        Each alias can be bound to only one CMK at a time.
        *   The aliases of CMKs in the same region must be unique.
        In this topic, an alias named `alias/example` is created for a CMK named `7906979c-8e06-46a2-be2d-68e3ccbc****`.
        

        @param request: CreateAliasRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alias(self, request):
        """
        Each alias can be bound to only one CMK at a time.
        *   The aliases of CMKs in the same region must be unique.
        In this topic, an alias named `alias/example` is created for a CMK named `7906979c-8e06-46a2-be2d-68e3ccbc****`.
        

        @param request: CreateAliasRequest

        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alias_with_options(request, runtime)

    def create_certificate_with_options(self, tmp_req, runtime):
        """
        To create a certificate, you must specify the type of the asymmetric key. Certificates Manager generates a private key and returns a certificate signing request (CSR). Submit the CSR in the Privacy Enhanced Mail (PEM) format to a certificate authority (CA) to obtain the formal certificate and certificate chain. Then, call the [UploadCertificate](~~212136~~) operation to import the certificate into Certificates Manager.
        In this example, a certificate is created and the CSR is obtained.
        

        @param tmp_req: CreateCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCertificateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateCertificateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subject_alternative_names):
            request.subject_alternative_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subject_alternative_names, 'SubjectAlternativeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.exportable_private_key):
            query['ExportablePrivateKey'] = request.exportable_private_key
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.subject_alternative_names_shrink):
            query['SubjectAlternativeNames'] = request.subject_alternative_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_certificate(self, request):
        """
        To create a certificate, you must specify the type of the asymmetric key. Certificates Manager generates a private key and returns a certificate signing request (CSR). Submit the CSR in the Privacy Enhanced Mail (PEM) format to a certificate authority (CA) to obtain the formal certificate and certificate chain. Then, call the [UploadCertificate](~~212136~~) operation to import the certificate into Certificates Manager.
        In this example, a certificate is created and the CSR is obtained.
        

        @param request: CreateCertificateRequest

        @return: CreateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    def create_key_with_options(self, request, runtime):
        """
        Creates a customer master key (CMK).
        

        @param request: CreateKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.key_usage):
            query['KeyUsage'] = request.key_usage
        if not UtilClient.is_unset(request.origin):
            query['Origin'] = request.origin
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_key(self, request):
        """
        Creates a customer master key (CMK).
        

        @param request: CreateKeyRequest

        @return: CreateKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_with_options(request, runtime)

    def create_key_version_with_options(self, request, runtime):
        """
        You can create a version only for an asymmetric CMK that is in the Enabled state. You can call the [CreateKey](~~28947~~) operation to create an asymmetric CMK and the [DescribeKey](~~28952~~) operation to query the status of the CMK. The status is specified by the KeyState parameter.
        *   The minimum interval for creating a version of the same CMK is seven days. You can call the [DescribeKey](~~28952~~) operation to query the time when the last version of a CMK was created. The time is specified by the LastRotationDate parameter.
        *   If a CMK is in a private key store, you cannot create a version for the CMK.
        *   You can create a maximum of 50 versions for a CMK in the same region.
        You can create a version for the CMK whose ID is `0b30658a-ed1a-4922-b8f7-a673ca9c****` by using the parameter settings provided in this topic.
        

        @param request: CreateKeyVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateKeyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyVersion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateKeyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_key_version(self, request):
        """
        You can create a version only for an asymmetric CMK that is in the Enabled state. You can call the [CreateKey](~~28947~~) operation to create an asymmetric CMK and the [DescribeKey](~~28952~~) operation to query the status of the CMK. The status is specified by the KeyState parameter.
        *   The minimum interval for creating a version of the same CMK is seven days. You can call the [DescribeKey](~~28952~~) operation to query the time when the last version of a CMK was created. The time is specified by the LastRotationDate parameter.
        *   If a CMK is in a private key store, you cannot create a version for the CMK.
        *   You can create a maximum of 50 versions for a CMK in the same region.
        You can create a version for the CMK whose ID is `0b30658a-ed1a-4922-b8f7-a673ca9c****` by using the parameter settings provided in this topic.
        

        @param request: CreateKeyVersionRequest

        @return: CreateKeyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_version_with_options(request, runtime)

    def create_secret_with_options(self, tmp_req, runtime):
        """
        The name of the secret.
        The value must be 1 to 64 characters in length and can contain letters, digits, underscores (\\_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        *   If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        *   If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        *   If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        

        @param tmp_req: CreateSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSecretResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extended_config):
            request.extended_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.encryption_key_id):
            query['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.extended_config_shrink):
            query['ExtendedConfig'] = request.extended_config_shrink
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.secret_data):
            query['SecretData'] = request.secret_data
        if not UtilClient.is_unset(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def create_secret(self, request):
        """
        The name of the secret.
        The value must be 1 to 64 characters in length and can contain letters, digits, underscores (\\_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following list describes the name requirements for different types of secrets:
        *   If the SecretType parameter is set to Generic or Rds, the name cannot start with `acs/`.
        *   If the SecretType parameter is set to RAMCredentials, set the SecretName parameter to `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/`. The name includes the display name of RAM user.
        *   If the SecretType parameter is set to ECS, the name must start with `acs/ecs/`.
        

        @param request: CreateSecretRequest

        @return: CreateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    def decrypt_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.DecryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Decrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DecryptResponse(),
            self.call_api(params, req, runtime)
        )

    def decrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    def delete_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alias_with_options(request, runtime)

    def delete_certificate_with_options(self, request, runtime):
        """
        After the certificate and its private key and certificate chain are deleted, they cannot be restored. Proceed with caution.
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4****` and its private key and certificate chain are deleted.
        

        @param request: DeleteCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_certificate(self, request):
        """
        After the certificate and its private key and certificate chain are deleted, they cannot be restored. Proceed with caution.
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4****` and its private key and certificate chain are deleted.
        

        @param request: DeleteCertificateRequest

        @return: DeleteCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_with_options(request, runtime)

    def delete_key_material_with_options(self, request, runtime):
        """
        This operation does not delete the CMK that is created by using the key material.
        If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation.
        After you delete the key material, you can upload only the same key material into the CMK.
        

        @param request: DeleteKeyMaterialRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteKeyMaterialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyMaterial',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteKeyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_key_material(self, request):
        """
        This operation does not delete the CMK that is created by using the key material.
        If the CMK is in the PendingDeletion state, the state of the CMK and the scheduled deletion time do not change after you call this operation. If the CMK is not in the PendingDeletion state, the state of the CMK changes to PendingImport after you call this operation.
        After you delete the key material, you can upload only the same key material into the CMK.
        

        @param request: DeleteKeyMaterialRequest

        @return: DeleteKeyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_key_material_with_options(request, runtime)

    def delete_secret_with_options(self, request, runtime):
        """
        If you call this operation without specifying a recovery period, the deleted secret can be recovered within 30 days.
        If you specify a recovery period, the deleted secret can be recovered within the recovery period. You can also forcibly delete a secret. A forcibly deleted secret cannot be recovered.
        

        @param request: DeleteSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_without_recovery):
            query['ForceDeleteWithoutRecovery'] = request.force_delete_without_recovery
        if not UtilClient.is_unset(request.recovery_window_in_days):
            query['RecoveryWindowInDays'] = request.recovery_window_in_days
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_secret(self, request):
        """
        If you call this operation without specifying a recovery period, the deleted secret can be recovered within 30 days.
        If you specify a recovery period, the deleted secret can be recovered within the recovery period. You can also forcibly delete a secret. A forcibly deleted secret cannot be recovered.
        

        @param request: DeleteSecretRequest

        @return: DeleteSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    def describe_account_kms_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAccountKmsStatus',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeAccountKmsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_account_kms_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_kms_status_with_options(runtime)

    def describe_certificate_with_options(self, request, runtime):
        """
        In this example, the information about the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate information includes the certificate ID, creation time, certificate issuer, validity period, serial number, and signature algorithm.
        

        @param request: DescribeCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_certificate(self, request):
        """
        In this example, the information about the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate information includes the certificate ID, creation time, certificate issuer, validity period, serial number, and signature algorithm.
        

        @param request: DescribeCertificateRequest

        @return: DescribeCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_with_options(request, runtime)

    def describe_key_with_options(self, request, runtime):
        """
        You can query the information about the CMK `05754286-3ba2-4fa6-8d41-4323aca6***` by using parameter settings provided in this topic. The information includes the creator, creation time, status, and deletion protection status of the CMK.
        

        @param request: DescribeKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_key(self, request):
        """
        You can query the information about the CMK `05754286-3ba2-4fa6-8d41-4323aca6***` by using parameter settings provided in this topic. The information includes the creator, creation time, status, and deletion protection status of the CMK.
        

        @param request: DescribeKeyRequest

        @return: DescribeKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_key_with_options(request, runtime)

    def describe_key_version_with_options(self, request, runtime):
        """
        This topic provides an example on how to query the information about a version of the CMK `1234abcd-12ab-34cd-56ef-12345678***`. The ID of the CMK version is `2ab1a983-7072-4bbc-a582-584b5bd8****`. The response shows that the creation time of the CMK version is `2016-03-25T10:42:40Z`.
        

        @param request: DescribeKeyVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeKeyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyVersion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeKeyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_key_version(self, request):
        """
        This topic provides an example on how to query the information about a version of the CMK `1234abcd-12ab-34cd-56ef-12345678***`. The ID of the CMK version is `2ab1a983-7072-4bbc-a582-584b5bd8****`. The response shows that the creation time of the CMK version is `2016-03-25T10:42:40Z`.
        

        @param request: DescribeKeyVersionRequest

        @return: DescribeKeyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_key_version_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def describe_secret_with_options(self, request, runtime):
        """
        This operation returns the metadata of a secret. This operation does not return the secret value.
        In this example, the metadata of the secret named `secret001` is queried.
        

        @param request: DescribeSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DescribeSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_secret(self, request):
        """
        This operation returns the metadata of a secret. This operation does not return the secret value.
        In this example, the metadata of the secret named `secret001` is queried.
        

        @param request: DescribeSecretRequest

        @return: DescribeSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_with_options(request, runtime)

    def disable_key_with_options(self, request, runtime):
        """
        If a customer master key (CMK) is disabled, the ciphertext encrypted by using this CMK cannot be decrypted until you re-enable it. You can call the [EnableKey](~~35150~~) operation to enable the CMK.
        In this example, the CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678****` is disabled.
        

        @param request: DisableKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.DisableKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_key(self, request):
        """
        If a customer master key (CMK) is disabled, the ciphertext encrypted by using this CMK cannot be decrypted until you re-enable it. You can call the [EnableKey](~~35150~~) operation to enable the CMK.
        In this example, the CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678****` is disabled.
        

        @param request: DisableKeyRequest

        @return: DisableKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_key_with_options(request, runtime)

    def enable_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.EnableKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_key_with_options(request, runtime)

    def encrypt_with_options(self, tmp_req, runtime):
        """
        KMS uses the primary version of a specified CMK to encrypt data.
        *   Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database access passwords, or other sensitive information.
        *   When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext of the data key that is used to encrypt the migrated data in the source region. This way, the ciphertext of the data key is generated in the destination region. You can also call the [Decrypt](~~28950~~) operation to decrypt the data key.
        

        @param tmp_req: EncryptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EncryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.EncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Encrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.EncryptResponse(),
            self.call_api(params, req, runtime)
        )

    def encrypt(self, request):
        """
        KMS uses the primary version of a specified CMK to encrypt data.
        *   Only data of 6 KB or less can be encrypted. For example, you can call this operation to encrypt RSA keys, database access passwords, or other sensitive information.
        *   When you migrate encrypted data across regions, you can call this operation in the destination region to encrypt the plaintext of the data key that is used to encrypt the migrated data in the source region. This way, the ciphertext of the data key is generated in the destination region. You can also call the [Decrypt](~~28950~~) operation to decrypt the data key.
        

        @param request: EncryptRequest

        @return: EncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    def export_data_key_with_options(self, tmp_req, runtime):
        """
        You can call the [GenerateDataKeyWithoutPlaintext](~~134043~~) operation to generate a data key, which is encrypted by a CMK. If you want to distribute the data key to other regions or cryptographic modules, you can call the ExportDataKey operation to use a public key to encrypt the data key.
        Then, you can import the ciphertext of the data key to the cryptographic module where the private key is stored. This way, the data key is securely distributed from KMS to the cryptographic module. After the data key is imported to the cryptographic module, you can use it to encrypt or decrypt data.
        

        @param tmp_req: ExportDataKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ExportDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def export_data_key(self, request):
        """
        You can call the [GenerateDataKeyWithoutPlaintext](~~134043~~) operation to generate a data key, which is encrypted by a CMK. If you want to distribute the data key to other regions or cryptographic modules, you can call the ExportDataKey operation to use a public key to encrypt the data key.
        Then, you can import the ciphertext of the data key to the cryptographic module where the private key is stored. This way, the data key is securely distributed from KMS to the cryptographic module. After the data key is imported to the cryptographic module, you can use it to encrypt or decrypt data.
        

        @param request: ExportDataKeyRequest

        @return: ExportDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_data_key_with_options(request, runtime)

    def generate_and_export_data_key_with_options(self, tmp_req, runtime):
        """
        We recommend that you perform the following steps to import your data key to a cryptographic module:
        *   Call the GenerateAndExportDataKey operation to generate a data key and obtain both the ciphertext of the data key encrypted by using the CMK and that encrypted by using the public key.
        *   Store the ciphertext of the data key encrypted by using the CMK in KMS Secrets Manager or in a storage service such as ApsaraDB. This ciphertext is used for backup and restoration.
        *   Import the ciphertext of the data key encrypted by using the public key to the cryptographic module where the private key is stored. Then, you can use the data key to encrypt or decrypt data.
        >  The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the data keys randomly generated by calling this operation. You must take note of the data keys and the returned ciphertext.
        

        @param tmp_req: GenerateAndExportDataKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GenerateAndExportDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateAndExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        if not UtilClient.is_unset(request.public_key_blob):
            query['PublicKeyBlob'] = request.public_key_blob
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAndExportDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateAndExportDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_and_export_data_key(self, request):
        """
        We recommend that you perform the following steps to import your data key to a cryptographic module:
        *   Call the GenerateAndExportDataKey operation to generate a data key and obtain both the ciphertext of the data key encrypted by using the CMK and that encrypted by using the public key.
        *   Store the ciphertext of the data key encrypted by using the CMK in KMS Secrets Manager or in a storage service such as ApsaraDB. This ciphertext is used for backup and restoration.
        *   Import the ciphertext of the data key encrypted by using the public key to the cryptographic module where the private key is stored. Then, you can use the data key to encrypt or decrypt data.
        >  The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the data keys randomly generated by calling this operation. You must take note of the data keys and the returned ciphertext.
        

        @param request: GenerateAndExportDataKeyRequest

        @return: GenerateAndExportDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_and_export_data_key_with_options(request, runtime)

    def generate_data_key_with_options(self, tmp_req, runtime):
        """
        This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext and ciphertext of the data key. You can use the plaintext of the data key to locally encrypt your data without using KMS and store the encrypted data together with the ciphertext of the data key. You can obtain the plaintext of the data key from the Plaintext parameter in the response and the ciphertext of the data key from the CiphertextBlob parameter in the response.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext of the data key in persistent storage.
        We recommend that you locally encrypt data by performing the following steps:
        1\\. Call the GenerateDataKey operation.
        2\\. Use the plaintext of the data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext of the data key from the memory.
        3\\. Store the encrypted data together with the ciphertext of the data key that you obtain.
        We recommend that you locally decrypt data by performing the following steps:
        *   Call the [Decrypt](~~28950~~) operation to decrypt the locally stored ciphertext of the data key. The plaintext of data key is then returned.
        *   Use the plaintext of the data key to locally decrypt data and then delete the plaintext of the data key from the memory.
        In this example, a random data key is generated for the CMK whose ID is `7906979c-8e06-46a2-be2d-68e3ccbc****`.
        

        @param tmp_req: GenerateDataKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GenerateDataKeyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDataKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_data_key(self, request):
        """
        This operation creates a random data key, encrypts the data key by using the specified customer master key (CMK), and returns the plaintext and ciphertext of the data key. You can use the plaintext of the data key to locally encrypt your data without using KMS and store the encrypted data together with the ciphertext of the data key. You can obtain the plaintext of the data key from the Plaintext parameter in the response and the ciphertext of the data key from the CiphertextBlob parameter in the response.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key. Therefore, you need to store the ciphertext of the data key in persistent storage.
        We recommend that you locally encrypt data by performing the following steps:
        1\\. Call the GenerateDataKey operation.
        2\\. Use the plaintext of the data key that you obtain to locally encrypt data without using KMS. Then, delete the plaintext of the data key from the memory.
        3\\. Store the encrypted data together with the ciphertext of the data key that you obtain.
        We recommend that you locally decrypt data by performing the following steps:
        *   Call the [Decrypt](~~28950~~) operation to decrypt the locally stored ciphertext of the data key. The plaintext of data key is then returned.
        *   Use the plaintext of the data key to locally decrypt data and then delete the plaintext of the data key from the memory.
        In this example, a random data key is generated for the CMK whose ID is `7906979c-8e06-46a2-be2d-68e3ccbc****`.
        

        @param request: GenerateDataKeyRequest

        @return: GenerateDataKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_with_options(request, runtime)

    def generate_data_key_without_plaintext_with_options(self, tmp_req, runtime):
        """
        This operation creates a random data key, encrypts the data key by using a specific symmetric CMK, and returns the ciphertext of the data key. This operation serves the same purpose as the [GenerateDataKey](~~28948~~) operation. The only difference is that this operation does not return the plaintext of the data key.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key.
        > * This operation applies to the scenario when you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the [Decrypt](~~28950~~) operation to decrypt the ciphertext of the data key.
        > * This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module creates different partitions and generates different data keys for each partition in advance. This module is not involved in data production and consumption after it completes initialization of the control plane. This module is the key provider. When producing and consuming data, modules on the control plane obtain the ciphertext of the data key for a partition first. After decrypting the ciphertext of the data key, modules on the control plane use the plaintext of the data key to encrypt or decrypt data and then clear the plaintext of the data key from the memory. In such a system, the key provider does not need to obtain the plaintext of the data key. It only needs to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They only need to have the permissions to call the Decrypt operation.
        

        @param tmp_req: GenerateDataKeyWithoutPlaintextRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GenerateDataKeyWithoutPlaintextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.GenerateDataKeyWithoutPlaintextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.encryption_context_shrink):
            query['EncryptionContext'] = request.encryption_context_shrink
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_spec):
            query['KeySpec'] = request.key_spec
        if not UtilClient.is_unset(request.number_of_bytes):
            query['NumberOfBytes'] = request.number_of_bytes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDataKeyWithoutPlaintext',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_data_key_without_plaintext(self, request):
        """
        This operation creates a random data key, encrypts the data key by using a specific symmetric CMK, and returns the ciphertext of the data key. This operation serves the same purpose as the [GenerateDataKey](~~28948~~) operation. The only difference is that this operation does not return the plaintext of the data key.
        The CMK that you specify in the request of this operation is only used to encrypt the data key and is not involved in the generation of the data key. KMS does not record or store the generated data key.
        > * This operation applies to the scenario when you do not need to use the data key to immediately encrypt data. Before you can use the data key to encrypt data, you must call the [Decrypt](~~28950~~) operation to decrypt the ciphertext of the data key.
        > * This operation is also suitable for a distributed system with different trust levels. For example, a system stores data in different partitions based on a preset trust policy. A module creates different partitions and generates different data keys for each partition in advance. This module is not involved in data production and consumption after it completes initialization of the control plane. This module is the key provider. When producing and consuming data, modules on the control plane obtain the ciphertext of the data key for a partition first. After decrypting the ciphertext of the data key, modules on the control plane use the plaintext of the data key to encrypt or decrypt data and then clear the plaintext of the data key from the memory. In such a system, the key provider does not need to obtain the plaintext of the data key. It only needs to have the permissions to call the GenerateDataKeyWithoutPlaintext operation. The data producers or consumers do not need to generate new data keys. They only need to have the permissions to call the Decrypt operation.
        

        @param request: GenerateDataKeyWithoutPlaintextRequest

        @return: GenerateDataKeyWithoutPlaintextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_without_plaintext_with_options(request, runtime)

    def get_certificate_with_options(self, request, runtime):
        """
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate, certificate chain, certificate ID, and certificate signing request (CSR) are returned.
        

        @param request: GetCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_certificate(self, request):
        """
        In this example, the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is queried. The certificate, certificate chain, certificate ID, and certificate signing request (CSR) are returned.
        

        @param request: GetCertificateRequest

        @return: GetCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_certificate_with_options(request, runtime)

    def get_parameters_for_import_with_options(self, request, runtime):
        """
        The returned parameters can be used to call the [ImportKeyMaterial](https://www.alibabacloud.com/help/en/key-management-service/latest/importkeymaterial) operation.
        - You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        - The public key and token that are returned by the GetParametersForImport operation must be used together. The public key and token can be used to import key material only for the CMK that is specified when you call the operation.
        - The public key and token that are returned vary each time you call the GetParametersForImport operation.
        - You must specify the type of the public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and the encryption algorithms allowed for each type.
        | Public key type | Encryption algorithm | Description |
        | --------------- | -------------------- | ----------- |
        | RSA_2048 | RSAES_PKCS1_V1_5
        RSAES_OAEP_SHA_1
        RSAES_OAEP_SHA_256 | CMKs of all regions and all protection levels are supported.
        Dedicated Key Management Service (KMS) does not support RSAES_OAEP_SHA_1. |
        | EC_SM2 | SM2PKE | CMKs whose ProtectionLevel is set to HSM are supported. The SM2 algorithm is developed and approved by the State Cryptography Administration of China. The SM2 algorithm can be used only to import key material for a CMK whose ProtectionLevel is set to HSM. You can use the SM2 algorithm only when you enable the Managed HSM feature for KMS in the Chinese mainland. For more information, see [Overview of Managed HSM](https://www.alibabacloud.com/help/en/key-management-service/latest/managed-hsm-overview). |
        For more information, see [Import key material](https://www.alibabacloud.com/help/en/key-management-service/latest/import-key-material). This topic provides an example on how to query the parameters that are used to import key material for a CMK. The ID of the CMK is `1234abcd-12ab-34cd-56ef-12345678****`, the encryption algorithm is `RSAES_PKCS1_V1_5`, and the public key is of the `RSA_2048` type. The parameters that are returned include the ID of the CMK, the public key that is used to encrypt the key material, the token that is used to import the key material, and the time when the token expires.
        

        @param request: GetParametersForImportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetParametersForImportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.wrapping_algorithm):
            query['WrappingAlgorithm'] = request.wrapping_algorithm
        if not UtilClient.is_unset(request.wrapping_key_spec):
            query['WrappingKeySpec'] = request.wrapping_key_spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParametersForImport',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetParametersForImportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_parameters_for_import(self, request):
        """
        The returned parameters can be used to call the [ImportKeyMaterial](https://www.alibabacloud.com/help/en/key-management-service/latest/importkeymaterial) operation.
        - You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        - The public key and token that are returned by the GetParametersForImport operation must be used together. The public key and token can be used to import key material only for the CMK that is specified when you call the operation.
        - The public key and token that are returned vary each time you call the GetParametersForImport operation.
        - You must specify the type of the public key and the encryption algorithm that are used to encrypt key material. The following table lists the types of public keys and the encryption algorithms allowed for each type.
        | Public key type | Encryption algorithm | Description |
        | --------------- | -------------------- | ----------- |
        | RSA_2048 | RSAES_PKCS1_V1_5
        RSAES_OAEP_SHA_1
        RSAES_OAEP_SHA_256 | CMKs of all regions and all protection levels are supported.
        Dedicated Key Management Service (KMS) does not support RSAES_OAEP_SHA_1. |
        | EC_SM2 | SM2PKE | CMKs whose ProtectionLevel is set to HSM are supported. The SM2 algorithm is developed and approved by the State Cryptography Administration of China. The SM2 algorithm can be used only to import key material for a CMK whose ProtectionLevel is set to HSM. You can use the SM2 algorithm only when you enable the Managed HSM feature for KMS in the Chinese mainland. For more information, see [Overview of Managed HSM](https://www.alibabacloud.com/help/en/key-management-service/latest/managed-hsm-overview). |
        For more information, see [Import key material](https://www.alibabacloud.com/help/en/key-management-service/latest/import-key-material). This topic provides an example on how to query the parameters that are used to import key material for a CMK. The ID of the CMK is `1234abcd-12ab-34cd-56ef-12345678****`, the encryption algorithm is `RSAES_PKCS1_V1_5`, and the public key is of the `RSA_2048` type. The parameters that are returned include the ID of the CMK, the public key that is used to encrypt the key material, the token that is used to import the key material, and the time when the token expires.
        

        @param request: GetParametersForImportRequest

        @return: GetParametersForImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_for_import_with_options(request, runtime)

    def get_public_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_version_id):
            query['KeyVersionId'] = request.key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicKey',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_public_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_public_key_with_options(request, runtime)

    def get_random_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exclude_characters):
            query['ExcludeCharacters'] = request.exclude_characters
        if not UtilClient.is_unset(request.exclude_lowercase):
            query['ExcludeLowercase'] = request.exclude_lowercase
        if not UtilClient.is_unset(request.exclude_numbers):
            query['ExcludeNumbers'] = request.exclude_numbers
        if not UtilClient.is_unset(request.exclude_punctuation):
            query['ExcludePunctuation'] = request.exclude_punctuation
        if not UtilClient.is_unset(request.exclude_uppercase):
            query['ExcludeUppercase'] = request.exclude_uppercase
        if not UtilClient.is_unset(request.password_length):
            query['PasswordLength'] = request.password_length
        if not UtilClient.is_unset(request.require_each_included_type):
            query['RequireEachIncludedType'] = request.require_each_included_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRandomPassword',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetRandomPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_random_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_random_password_with_options(request, runtime)

    def get_secret_value_with_options(self, request, runtime):
        """
        If you do not specify a version number or stage label, Secrets Manager returns the secret value of the version marked with ACSCurrent.
        If a customer master key (CMK) is specified to encrypt the secret value, you must also have the `kms:Decrypt` permission on the CMK to call the GetSecretValue operation.
        In this example, the value of the secret named `secret001` is obtained. The secret value is returned in the `SecretData` parameter. The secret value is `testdata1`.
        

        @param request: GetSecretValueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSecretValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_extended_config):
            query['FetchExtendedConfig'] = request.fetch_extended_config
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecretValue',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.GetSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    def get_secret_value(self, request):
        """
        If you do not specify a version number or stage label, Secrets Manager returns the secret value of the version marked with ACSCurrent.
        If a customer master key (CMK) is specified to encrypt the secret value, you must also have the `kms:Decrypt` permission on the CMK to call the GetSecretValue operation.
        In this example, the value of the secret named `secret001` is obtained. The secret value is returned in the `SecretData` parameter. The secret value is `testdata1`.
        

        @param request: GetSecretValueRequest

        @return: GetSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    def import_key_material_with_options(self, request, runtime):
        """
        Call [CreateKey](~~28947~~) when creating a CMK, you can select its key material source as external. *Origin** set to **EXTERNAL**. This API is used to import the key material into the CMK.
        *   To view the CMK **Origin**, see [DescribeKey](~~28952~~).
        *   Before importing key material, you need to call the [GetParametersForImport](~~68621~~) obtain the parameters required to import the key material, including the public key and import token.
        > *   The key type of the pair is **Aliyun\\_AES\\_256** the key material must be 256 bits. The key type must be **Aliyun\\_SM4** the CMK and key material must be 128 bits.
        > *   You can set the expiration time for the key material, or you can set it to never expire.
        > *   You can reimport the key material and reset the expiration time for the specified CMK at any time, but the same key material must be imported.
        > *   After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material are imported again.
        > *   A Key material can be imported to multiple cmks, but any Data or Data Key encrypted by one CMK cannot be decrypted by another CMK.
        

        @param request: ImportKeyMaterialRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportKeyMaterialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypted_key_material):
            query['EncryptedKeyMaterial'] = request.encrypted_key_material
        if not UtilClient.is_unset(request.import_token):
            query['ImportToken'] = request.import_token
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.key_material_expire_unix):
            query['KeyMaterialExpireUnix'] = request.key_material_expire_unix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyMaterial',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ImportKeyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def import_key_material(self, request):
        """
        Call [CreateKey](~~28947~~) when creating a CMK, you can select its key material source as external. *Origin** set to **EXTERNAL**. This API is used to import the key material into the CMK.
        *   To view the CMK **Origin**, see [DescribeKey](~~28952~~).
        *   Before importing key material, you need to call the [GetParametersForImport](~~68621~~) obtain the parameters required to import the key material, including the public key and import token.
        > *   The key type of the pair is **Aliyun\\_AES\\_256** the key material must be 256 bits. The key type must be **Aliyun\\_SM4** the CMK and key material must be 128 bits.
        > *   You can set the expiration time for the key material, or you can set it to never expire.
        > *   You can reimport the key material and reset the expiration time for the specified CMK at any time, but the same key material must be imported.
        > *   After the imported key material expires or is deleted, the specified CMK is unavailable until the same key material are imported again.
        > *   A Key material can be imported to multiple cmks, but any Data or Data Key encrypted by one CMK cannot be decrypted by another CMK.
        

        @param request: ImportKeyMaterialRequest

        @return: ImportKeyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_key_material_with_options(request, runtime)

    def list_aliases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_aliases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_with_options(request, runtime)

    def list_aliases_by_key_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliasesByKeyId',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListAliasesByKeyIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_aliases_by_key_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_by_key_id_with_options(request, runtime)

    def list_key_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyVersions',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListKeyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_key_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_key_versions_with_options(request, runtime)

    def list_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeys',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_keys_with_options(request, runtime)

    def list_resource_tags_with_options(self, request, runtime):
        """
        Request format: KeyId="string"
        

        @param request: ListResourceTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTags',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_tags(self, request):
        """
        Request format: KeyId="string"
        

        @param request: ListResourceTagsRequest

        @return: ListResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    def list_secret_version_ids_with_options(self, request, runtime):
        """
        The secret value is not included in the returned version information. By default, deprecated secret versions are not returned.
        

        @param request: ListSecretVersionIdsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSecretVersionIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_deprecated):
            query['IncludeDeprecated'] = request.include_deprecated
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecretVersionIds',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListSecretVersionIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_secret_version_ids(self, request):
        """
        The secret value is not included in the returned version information. By default, deprecated secret versions are not returned.
        

        @param request: ListSecretVersionIdsRequest

        @return: ListSecretVersionIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secret_version_ids_with_options(request, runtime)

    def list_secrets_with_options(self, request, runtime):
        """
        Specifies whether to return the resource tags of the secret. Valid values:
        *   true: returns the resource tags.
        *   false: does not return the resource tags. This is the default value.
        

        @param request: ListSecretsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_tags):
            query['FetchTags'] = request.fetch_tags
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_secrets(self, request):
        """
        Specifies whether to return the resource tags of the secret. Valid values:
        *   true: returns the resource tags.
        *   false: does not return the resource tags. This is the default value.
        

        @param request: ListSecretsRequest

        @return: ListSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def open_kms_service_with_options(self, runtime):
        """
        When you call this operation, note that:
        - KMS is a paid service. For more information about the billing method, see [Billing description](https://www.alibabacloud.com/help/en/key-management-service/latest/billing-billing).
        - An Alibaba Cloud account can activate KMS only once.
        - Make sure that your Alibaba Cloud account has passed real-name authentication.
        

        @param request: OpenKmsServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenKmsServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenKmsService',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.OpenKmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_kms_service(self):
        """
        When you call this operation, note that:
        - KMS is a paid service. For more information about the billing method, see [Billing description](https://www.alibabacloud.com/help/en/key-management-service/latest/billing-billing).
        - An Alibaba Cloud account can activate KMS only once.
        - Make sure that your Alibaba Cloud account has passed real-name authentication.
        

        @return: OpenKmsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_kms_service_with_options(runtime)

    def put_secret_value_with_options(self, request, runtime):
        """
        This operation is used to store the secret values of new versions. It cannot be used to modify the secret value of an existing version.
        By default, the newly stored secret value is marked with ACSCurrent, and the mark for the previous version of the secret value is changed from ACSCurrent to ACSPrevious. If you specify the VersionStage parameter, the newly stored secret value is marked with the stage label that you specify.
        You must specify a version number when you call the operation. Secrets Manager performs operations based on the following rules:
        *   If the specified version number does not exist in the secret, Secrets Manager creates the version and stores the secret value.
        *   If the specified version number already exists in the secret and the secret value of the existing version is the same as the secret value that you specify, Secrets Manager ignores the request and returns a success message. The request is idempotent.
        *   If the specified version number already exists in the secret but the secret value of the existing version is different from the secret value that you specify, Secrets Manager rejects the request and returns a failure message.
        Limits: This operation is available only for standard secrets.
        In this example, the secret value of a new version is stored into the `secret001` secret. The `VersionId` parameter is set to `00000000000000000000000000000000203` as the new version, and the `SecretData` parameter is set to `importantdata`.
        

        @param request: PutSecretValueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutSecretValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_data):
            query['SecretData'] = request.secret_data
        if not UtilClient.is_unset(request.secret_data_type):
            query['SecretDataType'] = request.secret_data_type
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        if not UtilClient.is_unset(request.version_stages):
            query['VersionStages'] = request.version_stages
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutSecretValue',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.PutSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    def put_secret_value(self, request):
        """
        This operation is used to store the secret values of new versions. It cannot be used to modify the secret value of an existing version.
        By default, the newly stored secret value is marked with ACSCurrent, and the mark for the previous version of the secret value is changed from ACSCurrent to ACSPrevious. If you specify the VersionStage parameter, the newly stored secret value is marked with the stage label that you specify.
        You must specify a version number when you call the operation. Secrets Manager performs operations based on the following rules:
        *   If the specified version number does not exist in the secret, Secrets Manager creates the version and stores the secret value.
        *   If the specified version number already exists in the secret and the secret value of the existing version is the same as the secret value that you specify, Secrets Manager ignores the request and returns a success message. The request is idempotent.
        *   If the specified version number already exists in the secret but the secret value of the existing version is different from the secret value that you specify, Secrets Manager rejects the request and returns a failure message.
        Limits: This operation is available only for standard secrets.
        In this example, the secret value of a new version is stored into the `secret001` secret. The `VersionId` parameter is set to `00000000000000000000000000000000203` as the new version, and the `SecretData` parameter is set to `importantdata`.
        

        @param request: PutSecretValueRequest

        @return: PutSecretValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_secret_value_with_options(request, runtime)

    def re_encrypt_with_options(self, tmp_req, runtime):
        """
        You can call this operation in the following scenarios:
        *   After the CMK that was used to encrypt your data is rotated, you can call this operation to use the latest CMK version to re-encrypt the data. For more information about automatic key rotation, see [Configure automatic key rotation](~~134270~~).
        *   The CMK that was used to encrypt your data remains unchanged, but EncryptionContext is changed. In this scenario, you can call this operation to re-encrypt the data.
        *   You can call this operation to use a CMK in KMS to re-encrypt data or a data key that was previously encrypted by a different CMK.
        To use the ReEncrypt operation, you must have two permissions:
        *   kms:ReEncryptFrom on the source CMK
        *   kms:ReEncryptTo on the destination CMK
        *   For simplicity, you can specify kms:ReEncrypt\\* to allow both of the preceding permissions.
        

        @param tmp_req: ReEncryptRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReEncryptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ReEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        if not UtilClient.is_unset(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.destination_encryption_context_shrink):
            query['DestinationEncryptionContext'] = request.destination_encryption_context_shrink
        if not UtilClient.is_unset(request.destination_key_id):
            query['DestinationKeyId'] = request.destination_key_id
        if not UtilClient.is_unset(request.source_encryption_algorithm):
            query['SourceEncryptionAlgorithm'] = request.source_encryption_algorithm
        if not UtilClient.is_unset(request.source_encryption_context_shrink):
            query['SourceEncryptionContext'] = request.source_encryption_context_shrink
        if not UtilClient.is_unset(request.source_key_id):
            query['SourceKeyId'] = request.source_key_id
        if not UtilClient.is_unset(request.source_key_version_id):
            query['SourceKeyVersionId'] = request.source_key_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReEncrypt',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ReEncryptResponse(),
            self.call_api(params, req, runtime)
        )

    def re_encrypt(self, request):
        """
        You can call this operation in the following scenarios:
        *   After the CMK that was used to encrypt your data is rotated, you can call this operation to use the latest CMK version to re-encrypt the data. For more information about automatic key rotation, see [Configure automatic key rotation](~~134270~~).
        *   The CMK that was used to encrypt your data remains unchanged, but EncryptionContext is changed. In this scenario, you can call this operation to re-encrypt the data.
        *   You can call this operation to use a CMK in KMS to re-encrypt data or a data key that was previously encrypted by a different CMK.
        To use the ReEncrypt operation, you must have two permissions:
        *   kms:ReEncryptFrom on the source CMK
        *   kms:ReEncryptTo on the destination CMK
        *   For simplicity, you can specify kms:ReEncrypt\\* to allow both of the preceding permissions.
        

        @param request: ReEncryptRequest

        @return: ReEncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.re_encrypt_with_options(request, runtime)

    def restore_secret_with_options(self, request, runtime):
        """
        You can only use this operation to restore a deleted secret that is within its recovery period. If you set *ForceDeleteWithoutRecovery** to **true** when you delete the secret, you cannot restore it.
        

        @param request: RestoreSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestoreSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.RestoreSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_secret(self, request):
        """
        You can only use this operation to restore a deleted secret that is within its recovery period. If you set *ForceDeleteWithoutRecovery** to **true** when you delete the secret, you cannot restore it.
        

        @param request: RestoreSecretRequest

        @return: RestoreSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_secret_with_options(request, runtime)

    def rotate_secret_with_options(self, request, runtime):
        """
        Limits:
        • A secret of each Alibaba Cloud account can be rotated for a maximum of 50 times per hour.
        • The RotateSecret operation is unavailable for standard secrets.
        In this example, the `RdsSecret/Mysql5.4/MyCred` secret is manually rotated, and the version number of the secret is set to `000000123` after the secret is rotated.
        

        @param request: RotateSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RotateSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RotateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.RotateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def rotate_secret(self, request):
        """
        Limits:
        • A secret of each Alibaba Cloud account can be rotated for a maximum of 50 times per hour.
        • The RotateSecret operation is unavailable for standard secrets.
        In this example, the `RdsSecret/Mysql5.4/MyCred` secret is manually rotated, and the version number of the secret is set to `000000123` after the secret is rotated.
        

        @param request: RotateSecretRequest

        @return: RotateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rotate_secret_with_options(request, runtime)

    def schedule_key_deletion_with_options(self, request, runtime):
        """
        During the scheduled period, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys.
        After a CMK is deleted, it cannot be recovered. Data that is encrypted and data keys that are generated by using the CMK cannot be decrypted. To prevent accidental deletion of CMKs, Key Management Service (KMS) allows you to only schedule key deletion tasks. You cannot directly delete CMKs. If you want to delete a CMK, call the [DisableKey](~~35151~~) operation to disable the CMK.
        When you call this operation, you must specify a scheduled period between 7 days to 366 days. The scheduled period starts from the time when you submit the request. You can call the [CancelKeyDeletion](~~44197~~) operation to cancel the key deletion task before the scheduled period ends.
        

        @param request: ScheduleKeyDeletionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ScheduleKeyDeletionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.pending_window_in_days):
            query['PendingWindowInDays'] = request.pending_window_in_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScheduleKeyDeletion',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.ScheduleKeyDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    def schedule_key_deletion(self, request):
        """
        During the scheduled period, the CMK is in the PendingDeletion state and cannot be used to encrypt data, decrypt data, or generate data keys.
        After a CMK is deleted, it cannot be recovered. Data that is encrypted and data keys that are generated by using the CMK cannot be decrypted. To prevent accidental deletion of CMKs, Key Management Service (KMS) allows you to only schedule key deletion tasks. You cannot directly delete CMKs. If you want to delete a CMK, call the [DisableKey](~~35151~~) operation to disable the CMK.
        When you call this operation, you must specify a scheduled period between 7 days to 366 days. The scheduled period starts from the time when you submit the request. You can call the [CancelKeyDeletion](~~44197~~) operation to cancel the key deletion task before the scheduled period ends.
        

        @param request: ScheduleKeyDeletionRequest

        @return: ScheduleKeyDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.schedule_key_deletion_with_options(request, runtime)

    def set_deletion_protection_with_options(self, request, runtime):
        """
        After you enable deletion protection for a CMK, you cannot delete the CMK. If you want to delete the CMK, you must first disable deletion protection for the CMK.
        *   Before you can call the SetDeletionProtection operation, make sure that the required CMK is not in the Pending Deletion state. You can call the [DescribeKey](~~28952~~) operation to query the CMK status, which is specified by the KeyState parameter.
        You can enable deletion protection for the CMK whose Alibaba Cloud Resource Name (ARN) is `acs:kms:cn-hangzhou:123213123****:key/0225f411-b21d-46d1-be5b-93931c82****` by using parameter settings provided in this topic. The CMK ARN is specified by the ProtectedResourceArn parameter.
        

        @param request: SetDeletionProtectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection_description):
            query['DeletionProtectionDescription'] = request.deletion_protection_description
        if not UtilClient.is_unset(request.enable_deletion_protection):
            query['EnableDeletionProtection'] = request.enable_deletion_protection
        if not UtilClient.is_unset(request.protected_resource_arn):
            query['ProtectedResourceArn'] = request.protected_resource_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeletionProtection',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.SetDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_deletion_protection(self, request):
        """
        After you enable deletion protection for a CMK, you cannot delete the CMK. If you want to delete the CMK, you must first disable deletion protection for the CMK.
        *   Before you can call the SetDeletionProtection operation, make sure that the required CMK is not in the Pending Deletion state. You can call the [DescribeKey](~~28952~~) operation to query the CMK status, which is specified by the KeyState parameter.
        You can enable deletion protection for the CMK whose Alibaba Cloud Resource Name (ARN) is `acs:kms:cn-hangzhou:123213123****:key/0225f411-b21d-46d1-be5b-93931c82****` by using parameter settings provided in this topic. The CMK ARN is specified by the ProtectedResourceArn parameter.
        

        @param request: SetDeletionProtectionRequest

        @return: SetDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    def tag_resource_with_options(self, request, runtime):
        """
        You can add up to 10 tags to a CMK, secret, or certificate.
        In this example, the tags `[{"TagKey":"S1key1","TagValue":"S1val1"},{"TagKey":"S1key2","TagValue":"S2val2"}]` are added to the CMK whose ID is `08c33a6f-4e0a-4a1b-a3fa-7ddf****`.
        

        @param request: TagResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.TagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resource(self, request):
        """
        You can add up to 10 tags to a CMK, secret, or certificate.
        In this example, the tags `[{"TagKey":"S1key1","TagValue":"S1val1"},{"TagKey":"S1key2","TagValue":"S2val2"}]` are added to the CMK whose ID is `08c33a6f-4e0a-4a1b-a3fa-7ddf****`.
        

        @param request: TagResourceRequest

        @return: TagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resource_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resource_with_options(self, request, runtime):
        """
        One or more tag keys. Separate multiple tag keys with commas (,).
        You need to specify only the tag keys, not the tag values.
        Each tag key must be 1 to 128 bytes in length.
        

        @param request: UntagResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UntagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resource(self, request):
        """
        One or more tag keys. Separate multiple tag keys with commas (,).
        You need to specify only the tag keys, not the tag values.
        Each tag key must be 1 to 128 bytes in length.
        

        @param request: UntagResourceRequest

        @return: UntagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resource_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_alias_with_options(request, runtime)

    def update_certificate_status_with_options(self, request, runtime):
        """
        In this example, the status of the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is updated to INACTIVE.
        

        @param request: UpdateCertificateStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCertificateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCertificateStatus',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateCertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_certificate_status(self, request):
        """
        In this example, the status of the certificate whose ID is `9a28de48-8d8b-484d-a766-dec4***` is updated to INACTIVE.
        

        @param request: UpdateCertificateStatusRequest

        @return: UpdateCertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_certificate_status_with_options(request, runtime)

    def update_key_description_with_options(self, request, runtime):
        """
        This operation replaces the description of a customer master key (CMK) with the description that you specify. The original description of the CMK is specified by the Description parameter when you call the [DescribeKey](~~28952~~) operation. You can call this operation to add, modify, or delete the description of a CMK.
        

        @param request: UpdateKeyDescriptionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateKeyDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKeyDescription',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateKeyDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_key_description(self, request):
        """
        This operation replaces the description of a customer master key (CMK) with the description that you specify. The original description of the CMK is specified by the Description parameter when you call the [DescribeKey](~~28952~~) operation. You can call this operation to add, modify, or delete the description of a CMK.
        

        @param request: UpdateKeyDescriptionRequest

        @return: UpdateKeyDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_key_description_with_options(request, runtime)

    def update_rotation_policy_with_options(self, request, runtime):
        """
        When automatic key rotation is enabled, KMS automatically creates a key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version.
        An automatic key rotation policy cannot be configured for the following keys:
        *   Asymmetric key
        *   Service-managed key
        *   Bring your own key (BYOK) that is imported into KMS
        *   Key that is not in the **Enabled** state
        In this example, automatic key rotation is enabled for a CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678****`. The automatic rotation period is 30 days.
        

        @param request: UpdateRotationPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRotationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRotationPolicy',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateRotationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rotation_policy(self, request):
        """
        When automatic key rotation is enabled, KMS automatically creates a key version after the preset rotation period arrives. In addition, KMS sets the new key version as the primary key version.
        An automatic key rotation policy cannot be configured for the following keys:
        *   Asymmetric key
        *   Service-managed key
        *   Bring your own key (BYOK) that is imported into KMS
        *   Key that is not in the **Enabled** state
        In this example, automatic key rotation is enabled for a CMK whose ID is `1234abcd-12ab-34cd-56ef-12345678****`. The automatic rotation period is 30 days.
        

        @param request: UpdateRotationPolicyRequest

        @return: UpdateRotationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rotation_policy_with_options(request, runtime)

    def update_secret_with_options(self, request, runtime):
        """
        In this example, the metadata of the `secret001` secret is updated. The `Description` parameter is set to `datainfo`.
        

        @param request: UpdateSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.extended_config):
            query['ExtendedConfig'] = request.extended_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def update_secret(self, request):
        """
        In this example, the metadata of the `secret001` secret is updated. The `Description` parameter is set to `datainfo`.
        

        @param request: UpdateSecretRequest

        @return: UpdateSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_with_options(request, runtime)

    def update_secret_rotation_policy_with_options(self, request, runtime):
        """
        After automatic rotation is enabled, Secrets Manager schedules the first automatic rotation by adding the preset rotation interval to the timestamp of the last rotation.
        Limits: The UpdateSecretRotationPolicy operation cannot be used to update the rotation policy of generic secrets.
        In this example, the rotation policy of the `RdsSecret/Mysql5.4/MyCred` secret is updated. The following settings are modified:
        *   The `EnableAutomaticRotation` parameter is set to `true`, which indicates that automatic rotation is enabled.
        *   The `RotationInterval` parameter is set to `30d`, which indicates that the interval for automatic rotation is 30 days.
        

        @param request: UpdateSecretRotationPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSecretRotationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_automatic_rotation):
            query['EnableAutomaticRotation'] = request.enable_automatic_rotation
        if not UtilClient.is_unset(request.rotation_interval):
            query['RotationInterval'] = request.rotation_interval
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretRotationPolicy',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretRotationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_secret_rotation_policy(self, request):
        """
        After automatic rotation is enabled, Secrets Manager schedules the first automatic rotation by adding the preset rotation interval to the timestamp of the last rotation.
        Limits: The UpdateSecretRotationPolicy operation cannot be used to update the rotation policy of generic secrets.
        In this example, the rotation policy of the `RdsSecret/Mysql5.4/MyCred` secret is updated. The following settings are modified:
        *   The `EnableAutomaticRotation` parameter is set to `true`, which indicates that automatic rotation is enabled.
        *   The `RotationInterval` parameter is set to `30d`, which indicates that the interval for automatic rotation is 30 days.
        

        @param request: UpdateSecretRotationPolicyRequest

        @return: UpdateSecretRotationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_rotation_policy_with_options(request, runtime)

    def update_secret_version_stage_with_options(self, request, runtime):
        """
        Updates the stage label that marks a secret version.
        

        @param request: UpdateSecretVersionStageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSecretVersionStageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.move_to_version):
            query['MoveToVersion'] = request.move_to_version
        if not UtilClient.is_unset(request.remove_from_version):
            query['RemoveFromVersion'] = request.remove_from_version
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.version_stage):
            query['VersionStage'] = request.version_stage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecretVersionStage',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UpdateSecretVersionStageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_secret_version_stage(self, request):
        """
        Updates the stage label that marks a secret version.
        

        @param request: UpdateSecretVersionStageRequest

        @return: UpdateSecretVersionStageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_secret_version_stage_with_options(request, runtime)

    def upload_certificate_with_options(self, request, runtime):
        """
        In this example, a certificate issued by a CA is imported into Certificates Manager. The ID of the certificate in Certificates Manager is `12345678-1234-1234-1234-12345678***`.
        

        @param request: UploadCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.certificate_chain):
            query['CertificateChain'] = request.certificate_chain
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCertificate',
            version='2016-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            kms_20160120_models.UploadCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_certificate(self, request):
        """
        In this example, a certificate issued by a CA is imported into Certificates Manager. The ID of the certificate in Certificates Manager is `12345678-1234-1234-1234-12345678***`.
        

        @param request: UploadCertificateRequest

        @return: UploadCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_certificate_with_options(request, runtime)
