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
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    def asymmetric_encrypt_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    def asymmetric_sign_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    def asymmetric_verify_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    def cancel_key_deletion_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.cancel_key_deletion_with_options(request, runtime)

    def certificate_private_key_decrypt_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_decrypt_with_options(request, runtime)

    def certificate_private_key_sign_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_sign_with_options(request, runtime)

    def certificate_public_key_encrypt_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_encrypt_with_options(request, runtime)

    def certificate_public_key_verify_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_verify_with_options(request, runtime)

    def create_alias_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_alias_with_options(request, runtime)

    def create_certificate_with_options(self, tmp_req, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    def create_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_key_with_options(request, runtime)

    def create_key_version_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_key_version_with_options(request, runtime)

    def create_secret_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.CreateSecretShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extended_config):
            request.extended_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extended_config, 'ExtendedConfig', 'json')
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_with_options(request, runtime)

    def delete_key_material_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_key_material_with_options(request, runtime)

    def delete_secret_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_with_options(request, runtime)

    def describe_key_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_key_with_options(request, runtime)

    def describe_key_version_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_with_options(request, runtime)

    def disable_key_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    def export_data_key_with_options(self, tmp_req, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.export_data_key_with_options(request, runtime)

    def generate_and_export_data_key_with_options(self, tmp_req, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.generate_and_export_data_key_with_options(request, runtime)

    def generate_data_key_with_options(self, tmp_req, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_with_options(request, runtime)

    def generate_data_key_without_plaintext_with_options(self, tmp_req, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_without_plaintext_with_options(request, runtime)

    def get_certificate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_certificate_with_options(request, runtime)

    def get_parameters_for_import_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    def import_key_material_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    def list_secret_version_ids_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_secret_version_ids_with_options(request, runtime)

    def list_secrets_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    def open_kms_service_with_options(self, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.open_kms_service_with_options(runtime)

    def put_secret_value_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.put_secret_value_with_options(request, runtime)

    def re_encrypt_with_options(self, tmp_req, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.re_encrypt_with_options(request, runtime)

    def restore_secret_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.restore_secret_with_options(request, runtime)

    def rotate_secret_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.rotate_secret_with_options(request, runtime)

    def schedule_key_deletion_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.schedule_key_deletion_with_options(request, runtime)

    def set_deletion_protection_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    def tag_resource_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.tag_resource_with_options(request, runtime)

    def untag_resource_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.untag_resource_with_options(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.update_certificate_status_with_options(request, runtime)

    def update_key_description_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_key_description_with_options(request, runtime)

    def update_rotation_policy_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_rotation_policy_with_options(request, runtime)

    def update_secret_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_secret_with_options(request, runtime)

    def update_secret_rotation_policy_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_secret_rotation_policy_with_options(request, runtime)

    def update_secret_version_stage_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_secret_version_stage_with_options(request, runtime)

    def upload_certificate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.upload_certificate_with_options(request, runtime)
