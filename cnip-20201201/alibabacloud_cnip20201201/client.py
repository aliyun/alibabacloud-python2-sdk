# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cnip20201201 import models as cnip_20201201_models
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
        self._endpoint = self.get_endpoint('cnip', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_environment(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(uid, headers, runtime)

    def get_environment_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentResponse(),
            self.do_roarequest('GetEnvironment', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_product_version_related_component_versions(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_version_related_component_versions_with_options(uid, headers, runtime)

    def list_product_version_related_component_versions_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionRelatedComponentVersionsResponse(),
            self.do_roarequest('ListProductVersionRelatedComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_versions/%s/component_versions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_component_version_children(self, uid, version_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_version_children_with_options(uid, version_uid, headers, runtime)

    def get_component_version_children_with_options(self, uid, version_uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetComponentVersionChildrenResponse(),
            self.do_roarequest('GetComponentVersionChildren', '2020-12-01', 'HTTPS', 'GET', 'AK', '/integration/api/v1/components/%s/versions/%s/children' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(version_uid)), 'json', req, runtime)
        )

    def get_product_environment(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_environment_with_options(uid, headers, runtime)

    def get_product_environment_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductEnvironmentResponse(),
            self.do_roarequest('GetProductEnvironment', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_envs/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_product_version_package(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_package_with_options(uid, request, headers, runtime)

    def get_product_version_package_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.platform):
            query['platform'] = request.platform
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        if not UtilClient.is_unset(request.old_product_version_uid):
            query['oldProductVersionUID'] = request.old_product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionPackageResponse(),
            self.do_roarequest('GetProductVersionPackage', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/hosting/product_versions/%s/packages' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_alicloud_region(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alicloud_region_with_options(headers, runtime)

    def list_alicloud_region_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListAlicloudRegionResponse(),
            self.do_roarequest('ListAlicloudRegion', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/alicloud/regions', 'json', req, runtime)
        )

    def list_component_versions(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_versions_with_options(uid, request, headers, runtime)

    def list_component_versions_with_options(self, uid, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.ListComponentVersionsShrinkRequest()
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
        return TeaCore.from_map(
            cnip_20201201_models.ListComponentVersionsResponse(),
            self.do_roarequest('ListComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/components/%s/versions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_snapshot_instance_join_option_with_batch(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_instance_join_option_with_batch_with_options(uid, request, headers, runtime)

    def update_snapshot_instance_join_option_with_batch_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_uids):
            query['instanceUIDs'] = request.instance_uids
        body = {}
        if not UtilClient.is_unset(request.join_snapshot):
            body['joinSnapshot'] = request.join_snapshot
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotInstanceJoinOptionWithBatchResponse(),
            self.do_roarequest('UpdateSnapshotInstanceJoinOptionWithBatch', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/snapshots/%s/instances' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def generate_vendor_config_template(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_vendor_config_template_with_options(uid, headers, runtime)

    def generate_vendor_config_template_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GenerateVendorConfigTemplateResponse(),
            self.do_roarequest('GenerateVendorConfigTemplate', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s/vendorConfigTmpl' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_product_component(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_component_with_options(uid, request, headers, runtime)

    def update_product_component_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_orchestration_values):
            body['componentOrchestrationValues'] = request.component_orchestration_values
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductComponentResponse(),
            self.do_roarequest('UpdateProductComponent', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/productComponentVersions/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_environment_nodes(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_nodes_with_options(uid, request, headers, runtime)

    def update_environment_nodes_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.data_disk_2):
            body['dataDisk2'] = request.data_disk_2
        if not UtilClient.is_unset(request.env_uid):
            body['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.node_ip):
            body['nodeIP'] = request.node_ip
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.system_disk_2):
            body['systemDisk2'] = request.system_disk_2
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentNodesResponse(),
            self.do_roarequest('UpdateEnvironmentNodes', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/environmentnodes/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_environment_packages(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_packages_with_options(uid, request, headers, runtime)

    def list_environment_packages_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentPackagesResponse(),
            self.do_roarequest('ListEnvironmentPackages', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s/packages' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def create_environment(self, request):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateEnvironmentHeaders()
        return self.create_environment_with_options(request, headers, runtime)

    def create_environment_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.location):
            body['location'] = request.location
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentResponse(),
            self.do_roarequest('CreateEnvironment', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments', 'json', req, runtime)
        )

    def get_environment_log(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_log_with_options(uid, headers, runtime)

    def get_environment_log_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentLogResponse(),
            self.do_roarequest('GetEnvironmentLog', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/envLogs/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_environment_node(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_node_with_options(uid, request, headers, runtime)

    def list_environment_node_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.node_ip):
            query['nodeIp'] = request.node_ip
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentNodeResponse(),
            self.do_roarequest('ListEnvironmentNode', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s/nodes' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_product_version_related_foundation_component_versions(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_version_related_foundation_component_versions_with_options(uid, headers, runtime)

    def list_product_version_related_foundation_component_versions_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionRelatedFoundationComponentVersionsResponse(),
            self.do_roarequest('ListProductVersionRelatedFoundationComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_versions/%s/foundation/component_versions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def sync_component(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_component_with_options(request, headers, runtime)

    def sync_component_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.SyncComponentResponse(),
            self.do_roarequest('SyncComponent', '2020-12-01', 'HTTPS', 'GET', 'AK', '/integration/api/v1/oss/sync/apps', 'json', req, runtime)
        )

    def update_component_to_product(self, id, version_id, product_component_version_relation_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_component_to_product_with_options(id, version_id, product_component_version_relation_id, request, headers, runtime)

    def update_component_to_product_with_options(self, id, version_id, product_component_version_relation_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.component_version_id):
            query['componentVersionID'] = request.component_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateComponentToProductResponse(),
            self.do_roarequest('UpdateComponentToProduct', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/integration/api/v1/products/%s/versions/%s/componentVersionRelations/%s' % (TeaConverter.to_unicode(id), TeaConverter.to_unicode(version_id), TeaConverter.to_unicode(product_component_version_relation_id)), 'json', req, runtime)
        )

    def create_environment_node(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_node_with_options(uid, request, headers, runtime)

    def create_environment_node_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['cpu'] = request.cpu
        if not UtilClient.is_unset(request.data_disk):
            body['dataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.identifier):
            body['identifier'] = request.identifier
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.memory):
            body['memory'] = request.memory
        if not UtilClient.is_unset(request.os):
            body['os'] = request.os
        if not UtilClient.is_unset(request.private_ip):
            body['privateIP'] = request.private_ip
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        if not UtilClient.is_unset(request.system_disk):
            body['systemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentNodeResponse(),
            self.do_roarequest('CreateEnvironmentNode', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/nodes' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_component(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_component_with_options(uid, headers, runtime)

    def get_component_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetComponentResponse(),
            self.do_roarequest('GetComponent', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/components/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_foundation_version_related_component_versions(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_version_related_component_versions_with_options(uid, headers, runtime)

    def list_foundation_version_related_component_versions_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListFoundationVersionRelatedComponentVersionsResponse(),
            self.do_roarequest('ListFoundationVersionRelatedComponentVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/foundation/versions/%s/component_versions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_snapshot(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_with_options(uid, headers, runtime)

    def get_snapshot_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetSnapshotResponse(),
            self.do_roarequest('GetSnapshot', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/snapshots/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_license(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_license_with_options(uid, headers, runtime)

    def get_license_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetLicenseResponse(),
            self.do_roarequest('GetLicense', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s/licenses' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def create_latest_product_version(self, uid, version_uid):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateLatestProductVersionHeaders()
        return self.create_latest_product_version_with_options(uid, version_uid, headers, runtime)

    def create_latest_product_version_with_options(self, uid, version_uid, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateLatestProductVersionResponse(),
            self.do_roarequest('CreateLatestProductVersion', '2020-12-01', 'HTTPS', 'POST', 'AK', '/integration/api/v1/products/%s/versions/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(version_uid)), 'json', req, runtime)
        )

    def list_alicloud_vpc(self, regionid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alicloud_vpcwith_options(regionid, headers, runtime)

    def list_alicloud_vpcwith_options(self, regionid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListAlicloudVPCResponse(),
            self.do_roarequest('ListAlicloudVPC', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/alicloud/regions/%s/vpcs' % TeaConverter.to_unicode(regionid), 'json', req, runtime)
        )

    def create_product(self, request):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateProductHeaders()
        return self.create_product_with_options(request, headers, runtime)

    def create_product_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.foundation_version_uid):
            body['foundationVersionUID'] = request.foundation_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.prometheus_uid):
            body['prometheusUID'] = request.prometheus_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateProductResponse(),
            self.do_roarequest('CreateProduct', '2020-12-01', 'HTTPS', 'POST', 'AK', '/integration/api/v1/products', 'json', req, runtime)
        )

    def get_product_environments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_environments_with_options(request, headers, runtime)

    def get_product_environments_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.GetProductEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.product_uid):
            query['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.env_type):
            query['envType'] = request.env_type
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductEnvironmentsResponse(),
            self.do_roarequest('GetProductEnvironments', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_envs', 'json', req, runtime)
        )

    def delete_component(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_component_with_options(uid, headers, runtime)

    def delete_component_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteComponentResponse(),
            self.do_roarequest('DeleteComponent', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/integration/api/v1/components/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def delete_product_component(self, id, version_id, product_component_version_relation_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_component_with_options(id, version_id, product_component_version_relation_id, headers, runtime)

    def delete_product_component_with_options(self, id, version_id, product_component_version_relation_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteProductComponentResponse(),
            self.do_roarequest('DeleteProductComponent', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/integration/api/v1/products/%s/versions/%s/componentVersionRelations/%s' % (TeaConverter.to_unicode(id), TeaConverter.to_unicode(version_id), TeaConverter.to_unicode(product_component_version_relation_id)), 'json', req, runtime)
        )

    def create_environment_with_snapshot(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_with_snapshot_with_options(uid, request, headers, runtime)

    def create_environment_with_snapshot_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.environment_desc):
            body['environmentDesc'] = request.environment_desc
        if not UtilClient.is_unset(request.environment_name):
            body['environmentName'] = request.environment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentWithSnapshotResponse(),
            self.do_roarequest('CreateEnvironmentWithSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/snapshots/%s/environments' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def delete_environment(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(uid, headers, runtime)

    def delete_environment_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentResponse(),
            self.do_roarequest('DeleteEnvironment', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/api/v1/environments/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_product_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_with_options(uid, request, headers, runtime)

    def update_product_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compatible_versions):
            body['compatibleVersions'] = request.compatible_versions
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductVersionResponse(),
            self.do_roarequest('UpdateProductVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/product_versions/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_children_component_version_parameters_list(self, id, version_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_children_component_version_parameters_list_with_options(id, version_id, request, headers, runtime)

    def get_children_component_version_parameters_list_with_options(self, id, version_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_id):
            query['relation_id'] = request.relation_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetChildrenComponentVersionParametersListResponse(),
            self.do_roarequest('GetChildrenComponentVersionParametersList', '2020-12-01', 'HTTPS', 'GET', 'AK', '/integration/api/v1/components/%s/versions/%s/parameters' % (TeaConverter.to_unicode(id), TeaConverter.to_unicode(version_id)), 'json', req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(request, headers, runtime)

    def create_snapshot_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_desc):
            body['productVersionDesc'] = request.product_version_desc
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateSnapshotResponse(),
            self.do_roarequest('CreateSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/snapshots', 'json', req, runtime)
        )

    def get_latest_version_differences(self, id, version_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_latest_version_differences_with_options(id, version_id, request, headers, runtime)

    def get_latest_version_differences_with_options(self, id, version_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_version_id):
            query['preVersionID'] = request.pre_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetLatestVersionDifferencesResponse(),
            self.do_roarequest('GetLatestVersionDifferences', '2020-12-01', 'HTTPS', 'GET', 'AK', '/integration/api/v1/products/%s/versions/%s/differences' % (TeaConverter.to_unicode(id), TeaConverter.to_unicode(version_id)), 'json', req, runtime)
        )

    def delete_environment_node(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_node_with_options(uid, request, headers, runtime)

    def delete_environment_node_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_uid):
            query['envUID'] = request.env_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentNodeResponse(),
            self.do_roarequest('DeleteEnvironmentNode', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/api/v1/environmentnodes/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def apply_component(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_component_with_options(request, headers, runtime)

    def apply_component_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.annotations):
            body['annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_version):
            body['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.component_class):
            body['componentClass'] = request.component_class
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.documents):
            body['documents'] = request.documents
        if not UtilClient.is_unset(request.images_mapping):
            body['imagesMapping'] = request.images_mapping
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['namespace'] = request.namespace
        if not UtilClient.is_unset(request.orchestration_type):
            body['orchestrationType'] = request.orchestration_type
        if not UtilClient.is_unset(request.orchestration_values):
            body['orchestrationValues'] = request.orchestration_values
        if not UtilClient.is_unset(request.package_url):
            body['packageURL'] = request.package_url
        if not UtilClient.is_unset(request.parent_component):
            body['parentComponent'] = request.parent_component
        if not UtilClient.is_unset(request.platforms):
            body['platforms'] = request.platforms
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.public):
            body['public'] = request.public
        if not UtilClient.is_unset(request.readme):
            body['readme'] = request.readme
        if not UtilClient.is_unset(request.resources):
            body['resources'] = request.resources
        if not UtilClient.is_unset(request.singleton):
            body['singleton'] = request.singleton
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ApplyComponentResponse(),
            self.do_roarequest('ApplyComponent', '2020-12-01', 'HTTPS', 'POST', 'AK', '/integration/api/v1/apps', 'json', req, runtime)
        )

    def get_snapshot_instances(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_instances_with_options(uid, request, headers, runtime)

    def get_snapshot_instances_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.sort_key):
            query['sortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_direct):
            query['sortDirect'] = request.sort_direct
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetSnapshotInstancesResponse(),
            self.do_roarequest('GetSnapshotInstances', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/snapshots/%s/instances' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_environments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    def list_environments_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.instance_status):
            query['instanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.vendor_type):
            query['vendorType'] = request.vendor_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentsResponse(),
            self.do_roarequest('ListEnvironments', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments', 'json', req, runtime)
        )

    def check_slr(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_slrwith_options(request, headers, runtime)

    def check_slrwith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CheckSLRResponse(),
            self.do_roarequest('CheckSLR', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/slr', 'json', req, runtime)
        )

    def update_product(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_with_options(uid, request, headers, runtime)

    def update_product_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.description
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductResponse(),
            self.do_roarequest('UpdateProduct', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/products/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def apply_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_components_with_options(request, headers, runtime)

    def apply_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.children_list):
            body['childrenList'] = request.children_list
        if not UtilClient.is_unset(request.component):
            body['component'] = request.component
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ApplyComponentsResponse(),
            self.do_roarequest('ApplyComponents', '2020-12-01', 'HTTPS', 'POST', 'AK', '/integration/api/v1/components', 'json', req, runtime)
        )

    def create_package_config(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_package_config_with_options(uid, headers, runtime)

    def create_package_config_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreatePackageConfigResponse(),
            self.do_roarequest('CreatePackageConfig', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/package_config' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def add_product_component(self, id, version_id, component_version_id, client_token, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_component_with_options(id, version_id, component_version_id, client_token, request, headers, runtime)

    def add_product_component_with_options(self, id, version_id, component_version_id, client_token, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.release_name
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddProductComponentResponse(),
            self.do_roarequest('AddProductComponent', '2020-12-01', 'HTTPS', 'POST', 'AK', '/integration/api/v1/products/%s/versions/%s/componentVersions/%s' % (TeaConverter.to_unicode(id), TeaConverter.to_unicode(version_id), TeaConverter.to_unicode(component_version_id)), 'json', req, runtime)
        )

    def delete_snapshot(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_with_options(uid, headers, runtime)

    def delete_snapshot_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteSnapshotResponse(),
            self.do_roarequest('DeleteSnapshot', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/api/v1/snapshots/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_environments_with_snapshot(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_snapshot_with_options(uid, headers, runtime)

    def list_environments_with_snapshot_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentsWithSnapshotResponse(),
            self.do_roarequest('ListEnvironmentsWithSnapshot', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/snapshots/%s/environments' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_environment_node(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_node_with_options(uid, headers, runtime)

    def get_environment_node_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentNodeResponse(),
            self.do_roarequest('GetEnvironmentNode', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environmentnodes/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_snapshot(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_with_options(uid, request, headers, runtime)

    def update_snapshot_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_desc):
            body['productVersionDesc'] = request.product_version_desc
        if not UtilClient.is_unset(request.update_key):
            body['updateKey'] = request.update_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotResponse(),
            self.do_roarequest('UpdateSnapshot', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/snapshots/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def create_environment_and_generate_vendor_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigHeaders()
        return self.create_environment_and_generate_vendor_config_with_options(request, headers, runtime)

    def create_environment_and_generate_vendor_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env_uid):
            body['envUID'] = request.env_uid
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        if not UtilClient.is_unset(request.vendor_type):
            body['vendorType'] = request.vendor_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentAndGenerateVendorConfigResponse(),
            self.do_roarequest('CreateEnvironmentAndGenerateVendorConfig', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/product_envs/vendor_config', 'json', req, runtime)
        )

    def create_environment_snapshot(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_environment_snapshot_with_options(uid, request, headers, runtime)

    def create_environment_snapshot_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateEnvironmentSnapshotResponse(),
            self.do_roarequest('CreateEnvironmentSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/snapshots' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def init_snapshot_instance(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_snapshot_instance_with_options(uid, headers, runtime)

    def init_snapshot_instance_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.InitSnapshotInstanceResponse(),
            self.do_roarequest('InitSnapshotInstance', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/snapshots/%s/instances' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_product_version_related_foundation_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_product_version_related_foundation_version_with_options(uid, request, headers, runtime)

    def update_product_version_related_foundation_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.foundation_version_uid
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateProductVersionRelatedFoundationVersionResponse(),
            self.do_roarequest('UpdateProductVersionRelatedFoundationVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/product_versions/%s/foundation' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_environment_params(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_params_with_options(uid, request, headers, runtime)

    def list_environment_params_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentParamsResponse(),
            self.do_roarequest('ListEnvironmentParams', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s/params' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_foundation_version(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_foundation_version_with_options(uid, headers, runtime)

    def get_foundation_version_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetFoundationVersionResponse(),
            self.do_roarequest('GetFoundationVersion', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/foundation/versions/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def delete_product(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_with_options(uid, headers, runtime)

    def delete_product_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteProductResponse(),
            self.do_roarequest('DeleteProduct', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/integration/api/v1/products/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_environment(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(uid, request, headers, runtime)

    def update_environment_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
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
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentResponse(),
            self.do_roarequest('UpdateEnvironment', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/environments/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_environment_package(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_package_with_options(uid, headers, runtime)

    def get_environment_package_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetEnvironmentPackageResponse(),
            self.do_roarequest('GetEnvironmentPackage', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/envPackages/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_product_component_detail(self, uid, version_uid, product_component_version_relation_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_component_detail_with_options(uid, version_uid, product_component_version_relation_uid, headers, runtime)

    def get_product_component_detail_with_options(self, uid, version_uid, product_component_version_relation_uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductComponentDetailResponse(),
            self.do_roarequest('GetProductComponentDetail', '2020-12-01', 'HTTPS', 'GET', 'AK', '/integration/api/v1/products/%s/versions/%s/productComponentVersionRelations/%s/detail' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(version_uid), TeaConverter.to_unicode(product_component_version_relation_uid)), 'json', req, runtime)
        )

    def import_environment_nodes(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_environment_nodes_with_options(uid, request, headers, runtime)

    def import_environment_nodes_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.node_list_yaml
        )
        return TeaCore.from_map(
            cnip_20201201_models.ImportEnvironmentNodesResponse(),
            self.do_roarequest('ImportEnvironmentNodes', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/importnodes' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    def list_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.fuzzy):
            query['fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListComponentsResponse(),
            self.do_roarequest('ListComponents', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/components', 'json', req, runtime)
        )

    def add_environment_product_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.AddEnvironmentProductVersionHeaders()
        return self.add_environment_product_version_with_options(uid, request, headers, runtime)

    def add_environment_product_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddEnvironmentProductVersionResponse(),
            self.do_roarequest('AddEnvironmentProductVersion', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/productVersions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_product_versions(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_product_versions_with_options(uid, request, headers, runtime)

    def list_product_versions_with_options(self, uid, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cnip_20201201_models.ListProductVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.platforms):
            request.platforms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.platforms, 'platforms', 'json')
        query = {}
        if not UtilClient.is_unset(request.released):
            query['released'] = request.released
        if not UtilClient.is_unset(request.platforms_shrink):
            query['platforms'] = request.platforms_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListProductVersionsResponse(),
            self.do_roarequest('ListProductVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/products/%s/versions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_children_component_version_list(self, id, version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_children_component_version_list_with_options(id, version_id, headers, runtime)

    def get_children_component_version_list_with_options(self, id, version_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetChildrenComponentVersionListResponse(),
            self.do_roarequest('GetChildrenComponentVersionList', '2020-12-01', 'HTTPS', 'GET', 'AK', '/integration/api/v1/products/%s/versions/%s/children' % (TeaConverter.to_unicode(id), TeaConverter.to_unicode(version_id)), 'json', req, runtime)
        )

    def create_slr(self):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.CreateSLRHeaders()
        return self.create_slrwith_options(headers, runtime)

    def create_slrwith_options(self, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateSLRResponse(),
            self.do_roarequest('CreateSLR', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/slr', 'json', req, runtime)
        )

    def get_product_version_related_component_version_detail(self, uid, relation_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_related_component_version_detail_with_options(uid, relation_uid, headers, runtime)

    def get_product_version_related_component_version_detail_with_options(self, uid, relation_uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionRelatedComponentVersionDetailResponse(),
            self.do_roarequest('GetProductVersionRelatedComponentVersionDetail', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_versions/%s/relations/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(relation_uid)), 'json', req, runtime)
        )

    def add_environment_package(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = cnip_20201201_models.AddEnvironmentPackageHeaders()
        return self.add_environment_package_with_options(uid, request, headers, runtime)

    def add_environment_package_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.package_type):
            query['packageType'] = request.package_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.client_token):
            real_headers['ClientToken'] = headers.client_token
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.AddEnvironmentPackageResponse(),
            self.do_roarequest('AddEnvironmentPackage', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/package' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_environment_product_version(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_environment_product_version_with_options(uid, request, headers, runtime)

    def update_environment_product_version_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.compatible_versions):
            body['compatibleVersions'] = request.compatible_versions
        if not UtilClient.is_unset(request.old_product_version):
            body['oldProductVersion'] = request.old_product_version
        if not UtilClient.is_unset(request.old_product_version_uid):
            body['oldProductVersionUID'] = request.old_product_version_uid
        if not UtilClient.is_unset(request.product_name):
            body['productName'] = request.product_name
        if not UtilClient.is_unset(request.product_uid):
            body['productUID'] = request.product_uid
        if not UtilClient.is_unset(request.product_version):
            body['productVersion'] = request.product_version
        if not UtilClient.is_unset(request.product_version_uid):
            body['productVersionUID'] = request.product_version_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateEnvironmentProductVersionResponse(),
            self.do_roarequest('UpdateEnvironmentProductVersion', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/environments/%s/product_versions' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_product_version_platforms(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_platforms_with_options(uid, headers, runtime)

    def get_product_version_platforms_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionPlatformsResponse(),
            self.do_roarequest('GetProductVersionPlatforms', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_versions/%s/platforms' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def save_environment_param(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_environment_param_with_options(uid, request, headers, runtime)

    def save_environment_param_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_uid):
            body['componentUID'] = request.component_uid
        if not UtilClient.is_unset(request.component_version_uid):
            body['componentVersionUID'] = request.component_version_uid
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.param_uid):
            body['paramUID'] = request.param_uid
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.release_name):
            body['releaseName'] = request.release_name
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.SaveEnvironmentParamResponse(),
            self.do_roarequest('SaveEnvironmentParam', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/environments/%s/params' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def update_snapshot_instance_join_option(self, instanceuid, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_instance_join_option_with_options(instanceuid, uid, request, headers, runtime)

    def update_snapshot_instance_join_option_with_options(self, instanceuid, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_snapshot):
            body['joinSnapshot'] = request.join_snapshot
        if not UtilClient.is_unset(request.root_password):
            body['rootPassword'] = request.root_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.UpdateSnapshotInstanceJoinOptionResponse(),
            self.do_roarequest('UpdateSnapshotInstanceJoinOption', '2020-12-01', 'HTTPS', 'PUT', 'AK', '/api/v1/snapshots/%s/instances/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(instanceuid)), 'json', req, runtime)
        )

    def get_product_version_resource(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_version_resource_with_options(uid, headers, runtime)

    def get_product_version_resource_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductVersionResourceResponse(),
            self.do_roarequest('GetProductVersionResource', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/product_versions/%s/resources' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def create_license(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_license_with_options(uid, request, headers, runtime)

    def create_license_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_year):
            query['effectiveYear'] = request.effective_year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.CreateLicenseResponse(),
            self.do_roarequest('CreateLicense', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/licenses' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def share_snapshot(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.share_snapshot_with_options(uid, request, headers, runtime)

    def share_snapshot_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.target_provider):
            body['targetProvider'] = request.target_provider
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ShareSnapshotResponse(),
            self.do_roarequest('ShareSnapshot', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/snapshots/%s/snapshots' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def delete_environment_param(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_param_with_options(uid, headers, runtime)

    def delete_environment_param_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteEnvironmentParamResponse(),
            self.do_roarequest('DeleteEnvironmentParam', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/api/v1/environmentparams/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def get_product(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_product_with_options(uid, headers, runtime)

    def get_product_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.GetProductResponse(),
            self.do_roarequest('GetProduct', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/products/%s' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def delete_component_version(self, uid, version_uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_component_version_with_options(uid, version_uid, headers, runtime)

    def delete_component_version_with_options(self, uid, version_uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeleteComponentVersionResponse(),
            self.do_roarequest('DeleteComponentVersion', '2020-12-01', 'HTTPS', 'DELETE', 'AK', '/integration/api/v1/components/%s/versions/%s' % (TeaConverter.to_unicode(uid), TeaConverter.to_unicode(version_uid)), 'json', req, runtime)
        )

    def deploy_environment_product(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_environment_product_with_options(uid, headers, runtime)

    def deploy_environment_product_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.DeployEnvironmentProductResponse(),
            self.do_roarequest('DeployEnvironmentProduct', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/deployment' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def init_environment_resource(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.init_environment_resource_with_options(uid, request, headers, runtime)

    def init_environment_resource_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
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
        return TeaCore.from_map(
            cnip_20201201_models.InitEnvironmentResourceResponse(),
            self.do_roarequest('InitEnvironmentResource', '2020-12-01', 'HTTPS', 'POST', 'AK', '/api/v1/environments/%s/resources' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )

    def list_foundation_versions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_foundation_versions_with_options(headers, runtime)

    def list_foundation_versions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListFoundationVersionsResponse(),
            self.do_roarequest('ListFoundationVersions', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/foundation/versions', 'json', req, runtime)
        )

    def list_environment_deploy_record(self, uid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_deploy_record_with_options(uid, request, headers, runtime)

    def list_environment_deploy_record_with_options(self, uid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            cnip_20201201_models.ListEnvironmentDeployRecordResponse(),
            self.do_roarequest('ListEnvironmentDeployRecord', '2020-12-01', 'HTTPS', 'GET', 'AK', '/api/v1/environments/%s/deployments' % TeaConverter.to_unicode(uid), 'json', req, runtime)
        )
