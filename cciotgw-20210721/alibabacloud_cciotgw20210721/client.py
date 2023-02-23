# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cciotgw20210721 import models as ccio_tgw20210721_models
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
        self._endpoint = self.get_endpoint('cciotgw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cloud_connector_gateway_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_gateway_id):
            query['IoTCloudConnectorGatewayId'] = request.io_tcloud_connector_gateway_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCloudConnectorGatewayPrivilege',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.AddCloudConnectorGatewayPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_cloud_connector_gateway_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cloud_connector_gateway_privilege_with_options(request, runtime)

    def add_ip_to_connection_pool_from_excel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpToConnectionPoolFromExcel',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.AddIpToConnectionPoolFromExcelResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ip_to_connection_pool_from_excel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ip_to_connection_pool_from_excel_with_options(request, runtime)

    def allocate_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apn):
            query['Apn'] = request.apn
        if not UtilClient.is_unset(request.cciot_gw_id):
            query['CciotGwId'] = request.cciot_gw_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ip_count):
            query['IpCount'] = request.ip_count
        if not UtilClient.is_unset(request.ips):
            query['Ips'] = request.ips
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateIps',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.AllocateIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_ips_with_options(request, runtime)

    def associate_iccid_to_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateIccidToIp',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.AssociateIccidToIpResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_iccid_to_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_iccid_to_ip_with_options(request, runtime)

    def associate_iccid_to_ip_excel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateIccidToIpExcel',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.AssociateIccidToIpExcelResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_iccid_to_ip_excel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_iccid_to_ip_excel_with_options(request, runtime)

    def delete_cloud_connector_gateway_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_gateway_id):
            query['IoTCloudConnectorGatewayId'] = request.io_tcloud_connector_gateway_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudConnectorGatewayPrivilege',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.DeleteCloudConnectorGatewayPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cloud_connector_gateway_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_connector_gateway_privilege_with_options(request, runtime)

    def get_free_ip_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFreeIpCount',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.GetFreeIpCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_free_ip_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_free_ip_count_with_options(request, runtime)

    def get_iccid_and_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIccidAndIp',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.GetIccidAndIpResponse(),
            self.call_api(params, req, runtime)
        )

    def get_iccid_and_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_iccid_and_ip_with_options(request, runtime)

    def get_io_tcloud_connector_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIoTCloudConnectorGateway',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.GetIoTCloudConnectorGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def get_io_tcloud_connector_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_io_tcloud_connector_gateway_with_options(request, runtime)

    def get_ip_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIpStatus',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.GetIpStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ip_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ip_status_with_options(request, runtime)

    def list_cloud_connector_gateway_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudConnectorGatewayPrivilege',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ListCloudConnectorGatewayPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cloud_connector_gateway_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_connector_gateway_privilege_with_options(request, runtime)

    def list_connection_pool_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectionPoolIp',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ListConnectionPoolIpResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connection_pool_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connection_pool_ip_with_options(request, runtime)

    def list_gre_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGreInterfaces',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ListGreInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_gre_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_gre_interfaces_with_options(request, runtime)

    def list_io_tcloud_connector_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectorGateways',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ListIoTCloudConnectorGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_io_tcloud_connector_gateways(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_gateways_with_options(request, runtime)

    def list_ips_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apn):
            query['Apn'] = request.apn
        if not UtilClient.is_unset(request.cciot_gw_id):
            query['CciotGwId'] = request.cciot_gw_id
        if not UtilClient.is_unset(request.ips):
            query['Ips'] = request.ips
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpsStatus',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ListIpsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ips_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ips_status_with_options(request, runtime)

    def list_result_token_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResultTokenUrl',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ListResultTokenUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def list_result_token_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_result_token_url_with_options(request, runtime)

    def modify_ip_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpStatus',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.ModifyIpStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_status_with_options(request, runtime)

    def query_asyn_token_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAsynTokenResult',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.QueryAsynTokenResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_asyn_token_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_asyn_token_result_with_options(request, runtime)

    def switch_vpc_route_to_back_up_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cciot_gw_id):
            query['CciotGwId'] = request.cciot_gw_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gre_gw_id):
            query['GreGwId'] = request.gre_gw_id
        if not UtilClient.is_unset(request.gre_interface_id):
            query['GreInterfaceId'] = request.gre_interface_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchVpcRouteToBackUpZone',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.SwitchVpcRouteToBackUpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_vpc_route_to_back_up_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_vpc_route_to_back_up_zone_with_options(request, runtime)

    def un_associate_iccid_to_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAssociateIccidToIp',
            version='2021-07-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ccio_tgw20210721_models.UnAssociateIccidToIpResponse(),
            self.call_api(params, req, runtime)
        )

    def un_associate_iccid_to_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_associate_iccid_to_ip_with_options(request, runtime)
