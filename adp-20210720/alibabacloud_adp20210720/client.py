# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adp20210720 import models as adp_20210720_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('adp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_environment_nodes(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_environment_nodes_with_options(uid, request, headers, runtime)

    def add_environment_nodes_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.application_disk):
            body['applicationDisk'] = request.application_disk
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.etcd_disk):
            body['etcdDisk'] = request.etcd_disk
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.master_private_ips):
            body['masterPrivateIPs'] = request.master_private_ips
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.os):
            body['os'] = request.os
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.trident_system_disk):
            body['tridentSystemDisk'] = request.trident_system_disk
        if not UtilClient.is_unset(request.trident_system_size_disk):
            body['tridentSystemSizeDisk'] = request.trident_system_size_disk
        if not UtilClient.is_unset(request.worker_private_ips):
            body['workerPrivateIPs'] = request.worker_private_ips
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/nodes' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddEnvironmentNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_product_component_version(self, uid, component_version_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_component_version_with_options(uid, component_version_uid, request, headers, runtime)

    def add_product_component_version_with_options(self, uid, component_version_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        component_version_uid = OpenApiUtilClient.get_encode_param(component_version_uid)
        body = {}
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/product-versions/%s/component-versions/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(component_version_uid)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def add_product_version_config(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_version_config_with_options(uid, request, headers, runtime)

    def add_product_version_config_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/configs' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.AddProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_environment_nodes(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_add_environment_nodes_with_options(uid, request, headers, runtime)

    def batch_add_environment_nodes_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.instance_list):
            body['instanceList'] = request.instance_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/batch/nodes' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.BatchAddEnvironmentNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_product_version_config(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_add_product_version_config_with_options(uid, request, headers, runtime)

    def batch_add_product_version_config_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.product_version_config_list):
            body['productVersionConfigList'] = request.product_version_config_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/batch/configs' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.BatchAddProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_environment(self, request):
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateEnvironmentHeaders()
        return self.create_environment_with_options(request, headers, runtime)

    def create_environment_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vendor_config):
            body['vendorConfig'] = request.vendor_config
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_environment_license(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_license_with_options(uid, request, headers, runtime)

    def create_environment_license_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.company_name):
            body['companyName'] = request.company_name
        if not UtilClient.is_unset(request.contact):
            body['contact'] = request.contact
        if not UtilClient.is_unset(request.machine_fingerprint):
            body['machineFingerprint'] = request.machine_fingerprint
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/licenses' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateEnvironmentLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_foundation_reference(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_foundation_reference_with_options(request, headers, runtime)

    def create_foundation_reference_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_config):
            body['clusterConfig'] = request.cluster_config
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation-references',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateFoundationReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product(self, request):
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateProductHeaders()
        return self.create_product_with_options(request, headers, runtime)

    def create_product_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/products',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_deployment_with_options(request, headers, runtime)

    def create_product_deployment_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_uid):
            body['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProductDeployment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/deployments',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_version(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_product_version_with_options(uid, headers, runtime)

    def create_product_version_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/products/%s/versions' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_version_package(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = adp_20210720_models.CreateProductVersionPackageHeaders()
        return self.create_product_version_package_with_options(uid, request, headers, runtime)

    def create_product_version_package_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        query = {}
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_content_type):
            query['packageContentType'] = request.package_content_type
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = UtilClient.to_jsonstring(headers.client_token)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductVersionPackage',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/hosting/product-versions/%s/packages' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.CreateProductVersionPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_environment(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(uid, headers, runtime)

    def delete_environment_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s' % TeaConverter.to_unicode(uid),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_environment_node(self, uid, node_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_node_with_options(uid, node_uid, headers, runtime)

    def delete_environment_node_with_options(self, uid, node_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        node_uid = OpenApiUtilClient.get_encode_param(node_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/nodes/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(node_uid)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_environment_product_version(self, uid, product_version_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_product_version_with_options(uid, product_version_uid, headers, runtime)

    def delete_environment_product_version_with_options(self, uid, product_version_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        product_version_uid = OpenApiUtilClient.get_encode_param(product_version_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/product-versions/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(product_version_uid)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteEnvironmentProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_with_options(uid, headers, runtime)

    def delete_product_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/products/%s' % TeaConverter.to_unicode(uid),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_component_version(self, uid, relation_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_component_version_with_options(uid, relation_uid, headers, runtime)

    def delete_product_component_version_with_options(self, uid, relation_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        relation_uid = OpenApiUtilClient.get_encode_param(relation_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/relations/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(relation_uid)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_instance_config(self, config_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_instance_config_with_options(config_uid, request, headers, runtime)

    def delete_product_instance_config_with_options(self, config_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        config_uid = OpenApiUtilClient.get_encode_param(config_uid)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProductInstanceConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/configs/%s' % TeaConverter.to_unicode(config_uid),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_version(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_version_with_options(uid, headers, runtime)

    def delete_product_version_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s' % TeaConverter.to_unicode(uid),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_version_config(self, uid, config_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_version_config_with_options(uid, config_uid, headers, runtime)

    def delete_product_version_config_with_options(self, uid, config_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        config_uid = OpenApiUtilClient.get_encode_param(config_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/configs/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(config_uid)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.DeleteProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_product_instance_deployment_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_product_instance_deployment_config_with_options(request, headers, runtime)

    def generate_product_instance_deployment_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProductInstanceDeploymentConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/package-configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GenerateProductInstanceDeploymentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_component(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_with_options(uid, headers, runtime)

    def get_component_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComponent',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/components/%s' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_component_version(self, uid, version_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_version_with_options(uid, version_uid, headers, runtime)

    def get_component_version_with_options(self, uid, version_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        version_uid = OpenApiUtilClient.get_encode_param(version_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/components/%s/versions/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(version_uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_environment(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(uid, headers, runtime)

    def get_environment_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_environment_license(self, uid, license_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_license_with_options(uid, license_uid, headers, runtime)

    def get_environment_license_with_options(self, uid, license_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        license_uid = OpenApiUtilClient.get_encode_param(license_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironmentLicense',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/licenses/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(license_uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_environment_node(self, uid, node_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_node_with_options(uid, node_uid, headers, runtime)

    def get_environment_node_with_options(self, uid, node_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        node_uid = OpenApiUtilClient.get_encode_param(node_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/nodes/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(node_uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetEnvironmentNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_foundation_component_reference(self, component_reference_uid, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_component_reference_with_options(component_reference_uid, uid, headers, runtime)

    def get_foundation_component_reference_with_options(self, component_reference_uid, uid, headers, runtime):
        component_reference_uid = OpenApiUtilClient.get_encode_param(component_reference_uid)
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationComponentReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation-references/%s/components/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(component_reference_uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationComponentReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_foundation_version(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_version_with_options(uid, headers, runtime)

    def get_foundation_version_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFoundationVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation/versions/%s' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetFoundationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_with_options(uid, headers, runtime)

    def get_product_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/products/%s' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_component_version(self, relation_uid, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_component_version_with_options(relation_uid, uid, headers, runtime)

    def get_product_component_version_with_options(self, relation_uid, uid, headers, runtime):
        relation_uid = OpenApiUtilClient.get_encode_param(relation_uid)
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/product-versions/%s/relations/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(relation_uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_deployment(self, deployment_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_deployment_with_options(deployment_uid, request, headers, runtime)

    def get_product_deployment_with_options(self, deployment_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        deployment_uid = OpenApiUtilClient.get_encode_param(deployment_uid)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.with_param_config):
            query['withParamConfig'] = request.with_param_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductDeployment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/deployments/%s' % TeaConverter.to_unicode(deployment_uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_version(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_with_options(uid, headers, runtime)

    def get_product_version_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_version_differences(self, uid, version_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_differences_with_options(uid, version_uid, request, headers, runtime)

    def get_product_version_differences_with_options(self, uid, version_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        version_uid = OpenApiUtilClient.get_encode_param(version_uid)
        query = {}
        if not UtilClient.is_unset(request.pre_version_uid):
            query['preVersionUID'] = request.pre_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersionDifferences',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/integration/api/v2/products/%s/versions/%s/differences' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(version_uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionDifferencesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_version_package(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_package_with_options(uid, request, headers, runtime)

    def get_product_version_package_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        query = {}
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.package_content_type):
            query['packageContentType'] = request.package_content_type
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.package_uid):
            query['packageUID'] = request.package_uid
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        if not UtilClient.is_unset(request.with_url):
            query['withURL'] = request.with_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductVersionPackage',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/hosting/product-versions/%s/packages' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetProductVersionPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workflow_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workflow_status_with_options(request, headers, runtime)

    def get_workflow_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workflow_type):
            query['workflowType'] = request.workflow_type
        if not UtilClient.is_unset(request.xuid):
            query['xuid'] = request.xuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowStatus',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/workflows/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.GetWorkflowStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def init_environment_resource(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_environment_resource_with_options(uid, request, headers, runtime)

    def init_environment_resource_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyID'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_secret):
            body['accessKeySecret'] = request.access_key_secret
        if not UtilClient.is_unset(request.security_token):
            body['securityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitEnvironmentResource',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/resources' % TeaConverter.to_unicode(uid),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.InitEnvironmentResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_component_versions(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_versions_with_options(uid, request, headers, runtime)

    def list_component_versions_with_options(self, uid, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        uid = OpenApiUtilClient.get_encode_param(uid)
        request = adp_20210720_models.ListComponentVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/components/%s/versions' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListComponentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    def list_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environment_licenses(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_licenses_with_options(uid, request, headers, runtime)

    def list_environment_licenses_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentLicenses',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/licenses' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentLicensesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environment_nodes(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_nodes_with_options(uid, request, headers, runtime)

    def list_environment_nodes_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentNodes',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/nodes' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environment_tunnels(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_tunnels_with_options(uid, headers, runtime)

    def list_environment_tunnels_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironmentTunnels',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/tunnels' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentTunnelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    def list_environments_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_uid):
            query['clusterUID'] = request.cluster_uid
        if not UtilClient.is_unset(request.foundation_type):
            query['foundationType'] = request.foundation_type
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.instance_status):
            query['instanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.vendor_type):
            query['vendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_foundation_component_versions(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_component_versions_with_options(uid, headers, runtime)

    def list_foundation_component_versions_with_options(self, uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFoundationComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation/versions/%s/component-versions' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationComponentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_foundation_reference_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_reference_components_with_options(request, headers, runtime)

    def list_foundation_reference_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.foundation_version_uid):
            query['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.only_enabled):
            query['onlyEnabled'] = request.only_enabled
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoundationReferenceComponents',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation-references/component-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationReferenceComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_foundation_versions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_versions_with_options(headers, runtime)

    def list_foundation_versions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFoundationVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListFoundationVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_component_versions(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_component_versions_with_options(uid, request, headers, runtime)

    def list_product_component_versions_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductComponentVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/component-versions' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductComponentVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_deployments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_deployments_with_options(request, headers, runtime)

    def list_product_deployments_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDeployments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/deployments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_environments(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_environments_with_options(uid, request, headers, runtime)

    def list_product_environments_with_options(self, uid, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        uid = OpenApiUtilClient.get_encode_param(uid)
        request = adp_20210720_models.ListProductEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.compatible_product_version_uid):
            query['compatibleProductVersionUID'] = request.compatible_product_version_uid
        if not UtilClient.is_unset(request.env_type):
            query['envType'] = request.env_type
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductEnvironments',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/hosting/products/%s/environments' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_instance_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_instance_configs_with_options(request, headers, runtime)

    def list_product_instance_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_uid):
            query['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.param_type):
            query['paramType'] = request.param_type
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductInstanceConfigs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_instances_with_options(request, headers, runtime)

    def list_product_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_uid):
            query['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_version_uid):
            query['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductInstances',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_version_configs(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_version_configs_with_options(uid, request, headers, runtime)

    def list_product_version_configs_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        query = {}
        if not UtilClient.is_unset(request.config_type):
            query['configType'] = request.config_type
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersionConfigs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/configs' % TeaConverter.to_unicode(uid),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductVersionConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_versions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_versions_with_options(request, headers, runtime)

    def list_product_versions_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = adp_20210720_models.ListProductVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        if not UtilClient.is_unset(tmp_req.supported_foundation_types):
            request.supported_foundation_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.supported_foundation_types, 'supportedFoundationTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        if not UtilClient.is_unset(request.product_name):
            query['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            query['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.released):
            query['released'] = request.released
        if not UtilClient.is_unset(request.supported_foundation_types_shrink):
            query['supportedFoundationTypes'] = request.supported_foundation_types_shrink
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductVersions',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_products(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    def list_products_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workflow_task_logs(self, step_name, task_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflow_task_logs_with_options(step_name, task_name, request, headers, runtime)

    def list_workflow_task_logs_with_options(self, step_name, task_name, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        step_name = OpenApiUtilClient.get_encode_param(step_name)
        task_name = OpenApiUtilClient.get_encode_param(task_name)
        request = adp_20210720_models.ListWorkflowTaskLogsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_values):
            request.filter_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_values, 'filterValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_values_shrink):
            query['filterValues'] = request.filter_values_shrink
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.workflow_type):
            query['workflowType'] = request.workflow_type
        if not UtilClient.is_unset(request.xuid):
            query['xuid'] = request.xuid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowTaskLogs',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/workflows/steps/%s/tasks/%s/logs' % (TeaConverter.to_unicode(step_name), TeaConverter.to_unicode(task_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ListWorkflowTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def put_environment_tunnel(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_environment_tunnel_with_options(uid, request, headers, runtime)

    def put_environment_tunnel_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.tunnel_config):
            body['tunnelConfig'] = request.tunnel_config
        if not UtilClient.is_unset(request.tunnel_type):
            body['tunnelType'] = request.tunnel_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutEnvironmentTunnel',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/tunnels' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.PutEnvironmentTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def put_product_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_product_instance_config_with_options(request, headers, runtime)

    def put_product_instance_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_uid):
            body['componentUID'] = request.component_uid
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.config_uid):
            body['configUID'] = request.config_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_uid):
            body['environmentUID'] = request.environment_uid
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_name):
            body['parentComponentName'] = request.parent_component_name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProductInstanceConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-instances/configs',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.PutProductInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_environment_foundation_reference(self, uid, foundation_reference_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_environment_foundation_reference_with_options(uid, foundation_reference_uid, headers, runtime)

    def set_environment_foundation_reference_with_options(self, uid, foundation_reference_uid, headers, runtime):
        uid = OpenApiUtilClient.get_encode_param(uid)
        foundation_reference_uid = OpenApiUtilClient.get_encode_param(foundation_reference_uid)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SetEnvironmentFoundationReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/foundation-references/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(foundation_reference_uid)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.SetEnvironmentFoundationReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_environment(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(uid, request, headers, runtime)

    def update_environment_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.vendor_config):
            body['vendorConfig'] = request.vendor_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_environment_node(self, uid, node_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_node_with_options(uid, node_uid, request, headers, runtime)

    def update_environment_node_with_options(self, uid, node_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        node_uid = OpenApiUtilClient.get_encode_param(node_uid)
        body = {}
        if not UtilClient.is_unset(request.application_disk):
            body['applicationDisk'] = request.application_disk
        if not UtilClient.is_unset(request.etcd_disk):
            body['etcdDisk'] = request.etcd_disk
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.trident_system_disk):
            body['tridentSystemDisk'] = request.trident_system_disk
        if not UtilClient.is_unset(request.trident_system_size_disk):
            body['tridentSystemSizeDisk'] = request.trident_system_size_disk
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironmentNode',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/nodes/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(node_uid)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_environment_product_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_product_version_with_options(uid, request, headers, runtime)

    def update_environment_product_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvironmentProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/product-versions' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateEnvironmentProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_foundation_component_reference(self, uid, component_reference_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_foundation_component_reference_with_options(uid, component_reference_uid, request, headers, runtime)

    def update_foundation_component_reference_with_options(self, uid, component_reference_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        component_reference_uid = OpenApiUtilClient.get_encode_param(component_reference_uid)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFoundationComponentReference',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/foundation-references/%s/components/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(component_reference_uid)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateFoundationComponentReferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_with_options(uid, request, headers, runtime)

    def update_product_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/products/%s' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_component_version(self, uid, relation_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_component_version_with_options(uid, relation_uid, request, headers, runtime)

    def update_product_component_version_with_options(self, uid, relation_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        relation_uid = OpenApiUtilClient.get_encode_param(relation_uid)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.new_component_version_uid):
            body['newComponentVersionUID'] = request.new_component_version_uid
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductComponentVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/relations/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(relation_uid)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductComponentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_foundation_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_foundation_version_with_options(uid, request, headers, runtime)

    def update_product_foundation_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductFoundationVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/foundation' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductFoundationVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_with_options(uid, request, headers, runtime)

    def update_product_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersion',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_version_config(self, uid, config_uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_config_with_options(uid, config_uid, request, headers, runtime)

    def update_product_version_config_with_options(self, uid, config_uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        config_uid = OpenApiUtilClient.get_encode_param(config_uid)
        body = {}
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent_component_version_uid):
            body['parentComponentVersionUID'] = request.parent_component_version_uid
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.value_type):
            body['valueType'] = request.value_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProductVersionConfig',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/product-versions/%s/configs/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(config_uid)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.UpdateProductVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_environment_tunnel(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_environment_tunnel_with_options(uid, request, headers, runtime)

    def validate_environment_tunnel_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        uid = OpenApiUtilClient.get_encode_param(uid)
        body = {}
        if not UtilClient.is_unset(request.tunnel_config):
            body['tunnelConfig'] = request.tunnel_config
        if not UtilClient.is_unset(request.tunnel_type):
            body['tunnelType'] = request.tunnel_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateEnvironmentTunnel',
            version='2021-07-20',
            protocol='HTTPS',
            pathname='/api/v2/environments/%s/tunnels/validation' % TeaConverter.to_unicode(uid),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            adp_20210720_models.ValidateEnvironmentTunnelResponse(),
            self.call_api(params, req, runtime)
        )
