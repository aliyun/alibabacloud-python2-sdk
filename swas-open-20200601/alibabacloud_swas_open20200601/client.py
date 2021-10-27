# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_swas_open20200601 import models as swas__open20200601_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('swas-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_custom_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            self.do_rpcrequest('CreateCustomImage', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_image_with_options(request, runtime)

    def create_firewall_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            self.do_rpcrequest('CreateFirewallRule', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_firewall_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_rule_with_options(request, runtime)

    def create_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            self.do_rpcrequest('CreateInstances', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def delete_custom_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            self.do_rpcrequest('DeleteCustomImage', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_custom_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_image_with_options(request, runtime)

    def delete_firewall_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            self.do_rpcrequest('DeleteFirewallRule', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_firewall_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_rule_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def list_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            self.do_rpcrequest('ListDisks', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_disks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_disks_with_options(request, runtime)

    def list_firewall_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            self.do_rpcrequest('ListFirewallRules', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_firewall_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_firewall_rules_with_options(request, runtime)

    def list_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            self.do_rpcrequest('ListImages', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    def list_instance_plans_modification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            self.do_rpcrequest('ListInstancePlansModification', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instance_plans_modification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_plans_modification_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_instances_traffic_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            self.do_rpcrequest('ListInstancesTrafficPackages', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances_traffic_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_traffic_packages_with_options(request, runtime)

    def list_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            self.do_rpcrequest('ListPlans', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_plans_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def list_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            self.do_rpcrequest('ListSnapshots', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    def modify_image_share_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            self.do_rpcrequest('ModifyImageShareStatus', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_status_with_options(request, runtime)

    def reboot_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            self.do_rpcrequest('RebootInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def reset_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            self.do_rpcrequest('ResetDisk', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    def reset_system_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            self.do_rpcrequest('ResetSystem', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_system(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_system_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            self.do_rpcrequest('StopInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def update_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            self.do_rpcrequest('UpdateInstanceAttribute', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_attribute_with_options(request, runtime)

    def upgrade_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            self.do_rpcrequest('UpgradeInstance', '2020-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_with_options(request, runtime)
