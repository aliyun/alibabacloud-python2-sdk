# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cas20200630 import models as cas_20200630_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'cas.aliyuncs.com',
            'ap-northeast-2-pop': 'cas.aliyuncs.com',
            'ap-southeast-1': 'cas.aliyuncs.com',
            'ap-southeast-3': 'cas.aliyuncs.com',
            'ap-southeast-5': 'cas.aliyuncs.com',
            'cn-beijing': 'cas.aliyuncs.com',
            'cn-beijing-finance-1': 'cas.aliyuncs.com',
            'cn-beijing-finance-pop': 'cas.aliyuncs.com',
            'cn-beijing-gov-1': 'cas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cas.aliyuncs.com',
            'cn-chengdu': 'cas.aliyuncs.com',
            'cn-edge-1': 'cas.aliyuncs.com',
            'cn-fujian': 'cas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cas.aliyuncs.com',
            'cn-hangzhou-finance': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cas.aliyuncs.com',
            'cn-hangzhou-test-306': 'cas.aliyuncs.com',
            'cn-hongkong': 'cas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cas.aliyuncs.com',
            'cn-huhehaote': 'cas.aliyuncs.com',
            'cn-north-2-gov-1': 'cas.aliyuncs.com',
            'cn-qingdao': 'cas.aliyuncs.com',
            'cn-qingdao-nebula': 'cas.aliyuncs.com',
            'cn-shanghai': 'cas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cas.aliyuncs.com',
            'cn-shanghai-finance-1': 'cas.aliyuncs.com',
            'cn-shanghai-inner': 'cas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cas.aliyuncs.com',
            'cn-shenzhen': 'cas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cas.aliyuncs.com',
            'cn-shenzhen-inner': 'cas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cas.aliyuncs.com',
            'cn-wuhan': 'cas.aliyuncs.com',
            'cn-yushanfang': 'cas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cas.aliyuncs.com',
            'cn-zhangjiakou': 'cas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cas.aliyuncs.com',
            'eu-west-1': 'cas.aliyuncs.com',
            'eu-west-1-oxs': 'cas.aliyuncs.com',
            'rus-west-1-pop': 'cas.aliyuncs.com',
            'us-east-1': 'cas.aliyuncs.com',
            'us-west-1': 'cas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_certificate_with_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['AlgorithmKeySize'] = request.algorithm_key_size
        query['AliasName'] = request.alias_name
        query['AppendCrl'] = request.append_crl
        query['BasicConstraintsCritical'] = request.basic_constraints_critical
        query['BeforeTime'] = request.before_time
        query['CertType'] = request.cert_type
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['CsrPemString'] = request.csr_pem_string
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['ParentIdentifier'] = request.parent_identifier
        query['Sans'] = request.sans
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateWithExtension',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateCertificateWithExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_certificate_with_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_extension_with_options(request, runtime)

    def create_client_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['Algorithm'] = request.algorithm
        query['BeforeTime'] = request.before_time
        query['CommonName'] = request.common_name
        query['Days'] = request.days
        query['ParentIdentifier'] = request.parent_identifier
        query['SanType'] = request.san_type
        query['SanValue'] = request.san_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_client_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_client_certificate_with_options(request, runtime)

    def create_client_certificate_with_csr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['BeforeTime'] = request.before_time
        query['Csr'] = request.csr
        query['Days'] = request.days
        query['ParentIdentifier'] = request.parent_identifier
        query['SanType'] = request.san_type
        query['SanValue'] = request.san_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClientCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateClientCertificateWithCsrResponse(),
            self.call_api(params, req, runtime)
        )

    def create_client_certificate_with_csr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_client_certificate_with_csr_with_options(request, runtime)

    def create_revoke_client_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRevokeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateRevokeClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_revoke_client_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_revoke_client_certificate_with_options(request, runtime)

    def create_root_cacertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Algorithm'] = request.algorithm
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['State'] = request.state
        query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRootCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateRootCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_root_cacertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_root_cacertificate_with_options(request, runtime)

    def create_server_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['Algorithm'] = request.algorithm
        query['BeforeTime'] = request.before_time
        query['CommonName'] = request.common_name
        query['Days'] = request.days
        query['Domain'] = request.domain
        query['ParentIdentifier'] = request.parent_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_server_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_server_certificate_with_options(request, runtime)

    def create_server_certificate_with_csr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['BeforeTime'] = request.before_time
        query['Csr'] = request.csr
        query['Days'] = request.days
        query['Domain'] = request.domain
        query['ParentIdentifier'] = request.parent_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateServerCertificateWithCsrResponse(),
            self.call_api(params, req, runtime)
        )

    def create_server_certificate_with_csr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_server_certificate_with_csr_with_options(request, runtime)

    def create_sub_cacertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Algorithm'] = request.algorithm
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['ParentIdentifier'] = request.parent_identifier
        query['State'] = request.state
        query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateSubCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sub_cacertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sub_cacertificate_with_options(request, runtime)

    def delete_client_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DeleteClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_client_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_client_certificate_with_options(request, runtime)

    def describe_cacertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cacertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_with_options(request, runtime)

    def describe_cacertificate_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCACertificateCount',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cacertificate_count(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_count_with_options(runtime)

    def describe_cacertificate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificateList',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cacertificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_list_with_options(request, runtime)

    def describe_certificate_private_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EncryptedCode'] = request.encrypted_code
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificatePrivateKey',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCertificatePrivateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_certificate_private_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_private_key_with_options(request, runtime)

    def describe_client_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_with_options(request, runtime)

    def describe_client_certificate_for_serial_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateForSerialNumber',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateForSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_certificate_for_serial_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_for_serial_number_with_options(request, runtime)

    def describe_client_certificate_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_certificate_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_status_with_options(request, runtime)

    def describe_client_certificate_status_for_serial_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatusForSerialNumber',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_certificate_status_for_serial_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_status_for_serial_number_with_options(request, runtime)

    def get_cainstance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCAInstanceStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.GetCAInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cainstance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cainstance_status_with_options(request, runtime)

    def list_cacertificate_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCACertificateLog',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListCACertificateLogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cacertificate_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cacertificate_log_with_options(request, runtime)

    def list_client_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_client_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_client_certificate_with_options(request, runtime)

    def list_revoke_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRevokeCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListRevokeCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_revoke_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_revoke_certificate_with_options(request, runtime)

    def update_cacertificate_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCACertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.UpdateCACertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cacertificate_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cacertificate_status_with_options(request, runtime)
