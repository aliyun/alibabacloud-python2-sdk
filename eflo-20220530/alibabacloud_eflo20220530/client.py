# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eflo20220530 import models as eflo_20220530_models
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
        self._endpoint = self.get_endpoint('eflo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def assign_private_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def assign_private_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_address_with_options(request, runtime)

    def create_er_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErResponse(),
            self.call_api(params, req, runtime)
        )

    def create_er(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_er_with_options(request, runtime)

    def create_er_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_er_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_er_attachment_with_options(request, runtime)

    def create_er_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def create_er_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_er_route_map_with_options(request, runtime)

    def create_subnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subnet_with_options(request, runtime)

    def create_vcc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vcc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_with_options(request, runtime)

    def create_vcc_grant_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vcc_grant_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_grant_rule_with_options(request, runtime)

    def create_vcc_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vcc_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_route_entry_with_options(request, runtime)

    def create_vpd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vpd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vpd_with_options(request, runtime)

    def create_vpd_grant_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vpd_grant_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vpd_grant_rule_with_options(request, runtime)

    def delete_er_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_er(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_er_with_options(request, runtime)

    def delete_er_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_er_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_er_attachment_with_options(request, runtime)

    def delete_er_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_er_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_er_route_map_with_options(request, runtime)

    def delete_subnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_subnet_with_options(request, runtime)

    def delete_vcc_grant_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vcc_grant_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vcc_grant_rule_with_options(request, runtime)

    def delete_vcc_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vcc_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vcc_route_entry_with_options(request, runtime)

    def delete_vpd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vpd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vpd_with_options(request, runtime)

    def delete_vpd_grant_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vpd_grant_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vpd_grant_rule_with_options(request, runtime)

    def describe_slr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DescribeSlrResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slr_with_options(request, runtime)

    def get_er_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErResponse(),
            self.call_api(params, req, runtime)
        )

    def get_er(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_er_with_options(request, runtime)

    def get_er_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_er_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_er_attachment_with_options(request, runtime)

    def get_er_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_er_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_er_route_entry_with_options(request, runtime)

    def get_er_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def get_er_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_er_route_map_with_options(request, runtime)

    def get_lni_private_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def get_lni_private_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_lni_private_ip_address_with_options(request, runtime)

    def get_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_network_interface_with_options(request, runtime)

    def get_subnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_subnet_with_options(request, runtime)

    def get_vcc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vcc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_with_options(request, runtime)

    def get_vcc_grant_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vcc_grant_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_grant_rule_with_options(request, runtime)

    def get_vcc_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vcc_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_route_entry_with_options(request, runtime)

    def get_vpd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vpd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_with_options(request, runtime)

    def get_vpd_grant_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vpd_grant_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_grant_rule_with_options(request, runtime)

    def get_vpd_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vpd_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_route_entry_with_options(request, runtime)

    def initialize_vcc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.InitializeVccResponse(),
            self.call_api(params, req, runtime)
        )

    def initialize_vcc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.initialize_vcc_with_options(request, runtime)

    def list_er_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErAttachments',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_er_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_er_attachments_with_options(request, runtime)

    def list_er_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_er_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_er_route_entries_with_options(request, runtime)

    def list_er_route_maps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteMaps',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_er_route_maps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_er_route_maps_with_options(request, runtime)

    def list_ers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ers_with_options(request, runtime)

    def list_lni_private_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def list_lni_private_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_lni_private_ip_address_with_options(request, runtime)

    def list_network_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_network_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_network_interfaces_with_options(request, runtime)

    def list_subnets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubnets',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListSubnetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subnets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_subnets_with_options(request, runtime)

    def list_vcc_grant_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vcc_grant_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_grant_rules_with_options(request, runtime)

    def list_vcc_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vcc_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_route_entries_with_options(request, runtime)

    def list_vccs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vccs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vccs_with_options(request, runtime)

    def list_vpd_grant_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpd_grant_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vpd_grant_rules_with_options(request, runtime)

    def list_vpd_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpd_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vpd_route_entries_with_options(request, runtime)

    def list_vpds_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not UtilClient.is_unset(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not UtilClient.is_unset(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpds',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpds(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vpds_with_options(request, runtime)

    def un_assign_private_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def un_assign_private_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_assign_private_ip_address_with_options(request, runtime)

    def update_er_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErResponse(),
            self.call_api(params, req, runtime)
        )

    def update_er(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_er_with_options(request, runtime)

    def update_er_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_er_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_er_attachment_with_options(request, runtime)

    def update_er_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def update_er_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_er_route_map_with_options(request, runtime)

    def update_subnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    def update_subnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_subnet_with_options(request, runtime)

    def update_vcc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVccResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vcc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vcc_with_options(request, runtime)

    def update_vpd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vpd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vpd_with_options(request, runtime)
