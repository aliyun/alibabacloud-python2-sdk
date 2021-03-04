# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricDecryptResponse().from_map(
            self.do_rpcrequest('AsymmetricDecrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def asymmetric_decrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_decrypt_with_options(request, runtime)

    def asymmetric_encrypt_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricEncryptResponse().from_map(
            self.do_rpcrequest('AsymmetricEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def asymmetric_encrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_encrypt_with_options(request, runtime)

    def asymmetric_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricSignResponse().from_map(
            self.do_rpcrequest('AsymmetricSign', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def asymmetric_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_sign_with_options(request, runtime)

    def asymmetric_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.AsymmetricVerifyResponse().from_map(
            self.do_rpcrequest('AsymmetricVerify', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def asymmetric_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.asymmetric_verify_with_options(request, runtime)

    def cancel_key_deletion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CancelKeyDeletionResponse().from_map(
            self.do_rpcrequest('CancelKeyDeletion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_key_deletion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_key_deletion_with_options(request, runtime)

    def certificate_private_key_decrypt_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePrivateKeyDecryptResponse().from_map(
            self.do_rpcrequest('CertificatePrivateKeyDecrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def certificate_private_key_decrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_decrypt_with_options(request, runtime)

    def certificate_private_key_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePrivateKeySignResponse().from_map(
            self.do_rpcrequest('CertificatePrivateKeySign', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def certificate_private_key_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.certificate_private_key_sign_with_options(request, runtime)

    def certificate_public_key_encrypt_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePublicKeyEncryptResponse().from_map(
            self.do_rpcrequest('CertificatePublicKeyEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def certificate_public_key_encrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_encrypt_with_options(request, runtime)

    def certificate_public_key_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CertificatePublicKeyVerifyResponse().from_map(
            self.do_rpcrequest('CertificatePublicKeyVerify', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def certificate_public_key_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.certificate_public_key_verify_with_options(request, runtime)

    def create_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateAliasResponse().from_map(
            self.do_rpcrequest('CreateAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateCertificateResponse().from_map(
            self.do_rpcrequest('CreateCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    def create_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateKeyResponse().from_map(
            self.do_rpcrequest('CreateKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_key_with_options(request, runtime)

    def create_key_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateKeyVersionResponse().from_map(
            self.do_rpcrequest('CreateKeyVersion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.CreateSecretResponse().from_map(
            self.do_rpcrequest('CreateSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DecryptResponse().from_map(
            self.do_rpcrequest('Decrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def decrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    def delete_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteAliasResponse().from_map(
            self.do_rpcrequest('DeleteAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alias_with_options(request, runtime)

    def delete_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteCertificateResponse().from_map(
            self.do_rpcrequest('DeleteCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_with_options(request, runtime)

    def delete_key_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteKeyMaterialResponse().from_map(
            self.do_rpcrequest('DeleteKeyMaterial', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_key_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_key_material_with_options(request, runtime)

    def delete_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DeleteSecretResponse().from_map(
            self.do_rpcrequest('DeleteSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    def describe_account_kms_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeAccountKmsStatusResponse().from_map(
            self.do_rpcrequest('DescribeAccountKmsStatus', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_kms_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_kms_status_with_options(runtime)

    def describe_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeCertificateResponse().from_map(
            self.do_rpcrequest('DescribeCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_with_options(request, runtime)

    def describe_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeKeyResponse().from_map(
            self.do_rpcrequest('DescribeKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_key_with_options(request, runtime)

    def describe_key_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeKeyVersionResponse().from_map(
            self.do_rpcrequest('DescribeKeyVersion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_key_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_key_version_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def describe_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DescribeSecretResponse().from_map(
            self.do_rpcrequest('DescribeSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_with_options(request, runtime)

    def describe_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.DescribeServiceResponse().from_map(
            self.do_rpcrequest('DescribeService', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_with_options(runtime)

    def disable_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.DisableKeyResponse().from_map(
            self.do_rpcrequest('DisableKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_key_with_options(request, runtime)

    def enable_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.EnableKeyResponse().from_map(
            self.do_rpcrequest('EnableKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.EncryptResponse().from_map(
            self.do_rpcrequest('Encrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def encrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    def export_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ExportCertificateResponse().from_map(
            self.do_rpcrequest('ExportCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_certificate_with_options(request, runtime)

    def export_data_key_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ExportDataKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encryption_context):
            request.encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encryption_context, 'EncryptionContext', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ExportDataKeyResponse().from_map(
            self.do_rpcrequest('ExportDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateAndExportDataKeyResponse().from_map(
            self.do_rpcrequest('GenerateAndExportDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateDataKeyResponse().from_map(
            self.do_rpcrequest('GenerateDataKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GenerateDataKeyWithoutPlaintextResponse().from_map(
            self.do_rpcrequest('GenerateDataKeyWithoutPlaintext', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_data_key_without_plaintext(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_data_key_without_plaintext_with_options(request, runtime)

    def get_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetCertificateResponse().from_map(
            self.do_rpcrequest('GetCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_certificate_with_options(request, runtime)

    def get_parameters_for_import_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetParametersForImportResponse().from_map(
            self.do_rpcrequest('GetParametersForImport', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_parameters_for_import(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_for_import_with_options(request, runtime)

    def get_public_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetPublicKeyResponse().from_map(
            self.do_rpcrequest('GetPublicKey', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_public_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_public_key_with_options(request, runtime)

    def get_random_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetRandomPasswordResponse().from_map(
            self.do_rpcrequest('GetRandomPassword', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_random_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_random_password_with_options(request, runtime)

    def get_secret_value_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.GetSecretValueResponse().from_map(
            self.do_rpcrequest('GetSecretValue', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_secret_value(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_secret_value_with_options(request, runtime)

    def import_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportCertificateResponse().from_map(
            self.do_rpcrequest('ImportCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_certificate_with_options(request, runtime)

    def import_encryption_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportEncryptionCertificateResponse().from_map(
            self.do_rpcrequest('ImportEncryptionCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_encryption_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_encryption_certificate_with_options(request, runtime)

    def import_key_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ImportKeyMaterialResponse().from_map(
            self.do_rpcrequest('ImportKeyMaterial', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_key_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_key_material_with_options(request, runtime)

    def list_aliases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListAliasesResponse().from_map(
            self.do_rpcrequest('ListAliases', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aliases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_with_options(request, runtime)

    def list_aliases_by_key_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListAliasesByKeyIdResponse().from_map(
            self.do_rpcrequest('ListAliasesByKeyId', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aliases_by_key_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_aliases_by_key_id_with_options(request, runtime)

    def list_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListCertificatesResponse().from_map(
            self.do_rpcrequest('ListCertificates', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_certificates_with_options(request, runtime)

    def list_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListKeysResponse().from_map(
            self.do_rpcrequest('ListKeys', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_keys_with_options(request, runtime)

    def list_key_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListKeyVersionsResponse().from_map(
            self.do_rpcrequest('ListKeyVersions', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_key_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_key_versions_with_options(request, runtime)

    def list_resource_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListResourceTagsResponse().from_map(
            self.do_rpcrequest('ListResourceTags', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_tags_with_options(request, runtime)

    def list_secrets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListSecretsResponse().from_map(
            self.do_rpcrequest('ListSecrets', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_secrets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_secrets_with_options(request, runtime)

    def list_secret_version_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ListSecretVersionIdsResponse().from_map(
            self.do_rpcrequest('ListSecretVersionIds', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_secret_version_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_secret_version_ids_with_options(request, runtime)

    def open_kms_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return kms_20160120_models.OpenKmsServiceResponse().from_map(
            self.do_rpcrequest('OpenKmsService', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_kms_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_kms_service_with_options(runtime)

    def put_secret_value_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.PutSecretValueResponse().from_map(
            self.do_rpcrequest('PutSecretValue', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_secret_value(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_secret_value_with_options(request, runtime)

    def re_encrypt_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = kms_20160120_models.ReEncryptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_encryption_context):
            request.source_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_encryption_context, 'SourceEncryptionContext', 'json')
        if not UtilClient.is_unset(tmp_req.destination_encryption_context):
            request.destination_encryption_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_encryption_context, 'DestinationEncryptionContext', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ReEncryptResponse().from_map(
            self.do_rpcrequest('ReEncrypt', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_encrypt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_encrypt_with_options(request, runtime)

    def restore_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.RestoreSecretResponse().from_map(
            self.do_rpcrequest('RestoreSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_secret_with_options(request, runtime)

    def rotate_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.RotateSecretResponse().from_map(
            self.do_rpcrequest('RotateSecret', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rotate_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rotate_secret_with_options(request, runtime)

    def schedule_key_deletion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.ScheduleKeyDeletionResponse().from_map(
            self.do_rpcrequest('ScheduleKeyDeletion', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def schedule_key_deletion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.schedule_key_deletion_with_options(request, runtime)

    def tag_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.TagResourceResponse().from_map(
            self.do_rpcrequest('TagResource', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resource_with_options(request, runtime)

    def untag_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UntagResourceResponse().from_map(
            self.do_rpcrequest('UntagResource', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resource_with_options(request, runtime)

    def update_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateAliasResponse().from_map(
            self.do_rpcrequest('UpdateAlias', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_alias_with_options(request, runtime)

    def update_certificate_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateCertificateStatusResponse().from_map(
            self.do_rpcrequest('UpdateCertificateStatus', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_certificate_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_certificate_status_with_options(request, runtime)

    def update_key_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateKeyDescriptionResponse().from_map(
            self.do_rpcrequest('UpdateKeyDescription', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_key_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_key_description_with_options(request, runtime)

    def update_rotation_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateRotationPolicyResponse().from_map(
            self.do_rpcrequest('UpdateRotationPolicy', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_rotation_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rotation_policy_with_options(request, runtime)

    def update_secret_rotation_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateSecretRotationPolicyResponse().from_map(
            self.do_rpcrequest('UpdateSecretRotationPolicy', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_secret_rotation_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_secret_rotation_policy_with_options(request, runtime)

    def update_secret_version_stage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UpdateSecretVersionStageResponse().from_map(
            self.do_rpcrequest('UpdateSecretVersionStage', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_secret_version_stage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_secret_version_stage_with_options(request, runtime)

    def upload_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return kms_20160120_models.UploadCertificateResponse().from_map(
            self.do_rpcrequest('UploadCertificate', '2016-01-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_certificate_with_options(request, runtime)
