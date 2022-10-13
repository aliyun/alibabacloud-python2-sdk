# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cc5g20220314 import models as cc5g20220314_models
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
        self._endpoint = self.get_endpoint('cc5g', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_dnsauthorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDNSAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AddDNSAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dnsauthorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dnsauthorization_rule_with_options(request, runtime)

    def attach_vpc_to_net_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switches):
            query['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVpcToNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.AttachVpcToNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_vpc_to_net_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_vpc_to_net_link_with_options(request, runtime)

    def create_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_rule_with_options(request, runtime)

    def create_batch_operate_cards_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.effect_type):
            query['EffectType'] = request.effect_type
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.iccids_oss_file_path):
            query['IccidsOssFilePath'] = request.iccids_oss_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateBatchOperateCardsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_batch_operate_cards_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_batch_operate_cards_task_with_options(request, runtime)

    def create_io_tcloud_connector_backhaul_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateIoTCloudConnectorBackhaulRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_io_tcloud_connector_backhaul_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_io_tcloud_connector_backhaul_route_with_options(request, runtime)

    def create_wireless_cloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_links):
            query['NetLinks'] = request.net_links
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_case):
            query['UseCase'] = request.use_case
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.CreateWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_wireless_cloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_wireless_cloud_connector_with_options(request, runtime)

    def delete_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_authorization_rule_with_options(request, runtime)

    def delete_batch_operate_cards_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_operate_cards_task_id):
            query['BatchOperateCardsTaskId'] = request.batch_operate_cards_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteBatchOperateCardsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_batch_operate_cards_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_batch_operate_cards_task_with_options(request, runtime)

    def delete_io_tcloud_connector_backhaul_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteIoTCloudConnectorBackhaulRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_io_tcloud_connector_backhaul_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_io_tcloud_connector_backhaul_route_with_options(request, runtime)

    def delete_wireless_cloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DeleteWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_wireless_cloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_wireless_cloud_connector_with_options(request, runtime)

    def detach_vpc_from_net_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVpcFromNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.DetachVpcFromNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_vpc_from_net_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_vpc_from_net_link_with_options(request, runtime)

    def fail_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.FailCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def fail_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fail_cards_with_options(request, runtime)

    def get_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCardResponse(),
            self.call_api(params, req, runtime)
        )

    def get_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_card_with_options(request, runtime)

    def get_card_lock_reason_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardLockReason',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCardLockReasonResponse(),
            self.call_api(params, req, runtime)
        )

    def get_card_lock_reason(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_card_lock_reason_with_options(request, runtime)

    def get_create_customer_information_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateCustomerInformation',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetCreateCustomerInformationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_create_customer_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_create_customer_information_with_options(request, runtime)

    def get_diagnose_result_for_single_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_task_id):
            query['DiagnoseTaskId'] = request.diagnose_task_id
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnoseResultForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetDiagnoseResultForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def get_diagnose_result_for_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_diagnose_result_for_single_card_with_options(request, runtime)

    def get_wireless_cloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GetWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def get_wireless_cloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_wireless_cloud_connector_with_options(request, runtime)

    def grant_net_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.grant_ali_uid):
            query['GrantAliUid'] = request.grant_ali_uid
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.GrantNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_net_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_net_link_with_options(request, runtime)

    def list_apns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAPNs',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListAPNsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apns_with_options(request, runtime)

    def list_authorization_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizationRules',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authorization_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authorization_rules_with_options(request, runtime)

    def list_batch_operate_cards_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatchOperateCardsTasks',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListBatchOperateCardsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_batch_operate_cards_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_batch_operate_cards_tasks_with_options(request, runtime)

    def list_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cards_with_options(request, runtime)

    def list_data_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataPackages',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListDataPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_packages_with_options(request, runtime)

    def list_diagnose_info_for_single_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseInfoForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListDiagnoseInfoForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diagnose_info_for_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_diagnose_info_for_single_card_with_options(request, runtime)

    def list_io_tcloud_connector_backhaul_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectorBackhaulRoute',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListIoTCloudConnectorBackhaulRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def list_io_tcloud_connector_backhaul_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_backhaul_route_with_options(request, runtime)

    def list_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrders',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_orders_with_options(request, runtime)

    def list_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    def list_wireless_cloud_connectors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWirelessCloudConnectors',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListWirelessCloudConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_wireless_cloud_connectors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_wireless_cloud_connectors_with_options(request, runtime)

    def list_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_zones_with_options(request, runtime)

    def lock_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.LockCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_cards_with_options(request, runtime)

    def modify_wireless_cloud_connector_feature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_value):
            query['FeatureValue'] = request.feature_value
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWirelessCloudConnectorFeature',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ModifyWirelessCloudConnectorFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_wireless_cloud_connector_feature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_wireless_cloud_connector_feature_with_options(request, runtime)

    def open_cc_5g_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCc5gService',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.OpenCc5gServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_cc_5g_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_cc_5g_service_with_options(request, runtime)

    def resume_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.ResumeCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_cards_with_options(request, runtime)

    def revoke_net_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.net_link_id):
            query['NetLinkId'] = request.net_link_id
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeNetLink',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.RevokeNetLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_net_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_net_link_with_options(request, runtime)

    def stop_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.StopCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cards_with_options(request, runtime)

    def submit_diagnose_task_for_single_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDiagnoseTaskForSingleCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.SubmitDiagnoseTaskForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_diagnose_task_for_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_diagnose_task_for_single_card_with_options(request, runtime)

    def switch_wireless_cloud_connector_to_business_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchWirelessCloudConnectorToBusiness',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.SwitchWirelessCloudConnectorToBusinessResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_wireless_cloud_connector_to_business(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_wireless_cloud_connector_to_business_with_options(request, runtime)

    def unlock_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockCards',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UnlockCardsResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_cards_with_options(request, runtime)

    def update_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_port):
            query['DestinationPort'] = request.destination_port
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCidr'] = request.source_cidr
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_rule_with_options(request, runtime)

    def update_batch_operate_cards_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_operate_cards_task_id):
            query['BatchOperateCardsTaskId'] = request.batch_operate_cards_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.effect_type):
            query['EffectType'] = request.effect_type
        if not UtilClient.is_unset(request.iccids):
            query['Iccids'] = request.iccids
        if not UtilClient.is_unset(request.iccids_oss_file_path):
            query['IccidsOssFilePath'] = request.iccids_oss_file_path
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.wireless_cloud_connector_ids):
            query['WirelessCloudConnectorIds'] = request.wireless_cloud_connector_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBatchOperateCardsTask',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateBatchOperateCardsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_batch_operate_cards_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_batch_operate_cards_task_with_options(request, runtime)

    def update_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCard',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateCardResponse(),
            self.call_api(params, req, runtime)
        )

    def update_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_card_with_options(request, runtime)

    def update_dnsauthorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_ip):
            query['DestinationIp'] = request.destination_ip
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_dnsip):
            query['SourceDNSIp'] = request.source_dnsip
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSAuthorizationRule',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateDNSAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dnsauthorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dnsauthorization_rule_with_options(request, runtime)

    def update_wireless_cloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.wireless_cloud_connector_id):
            query['WirelessCloudConnectorId'] = request.wireless_cloud_connector_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWirelessCloudConnector',
            version='2022-03-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cc5g20220314_models.UpdateWirelessCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_wireless_cloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_wireless_cloud_connector_with_options(request, runtime)
