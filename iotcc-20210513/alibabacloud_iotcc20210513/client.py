# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iotcc20210513 import models as io_tcc20210513_models
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
        self._endpoint = self.get_endpoint('iotcc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cidr_to_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidrs):
            query['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCidrToConnectionPool',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AddCidrToConnectionPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def add_cidr_to_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cidr_to_connection_pool_with_options(request, runtime)

    def add_io_tcloud_connector_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIoTCloudConnectorToGroup',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AddIoTCloudConnectorToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_io_tcloud_connector_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_io_tcloud_connector_to_group_with_options(request, runtime)

    def associate_ip_with_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.ips):
            query['Ips'] = request.ips
        if not UtilClient.is_unset(request.ips_file_path):
            query['IpsFilePath'] = request.ips_file_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateIpWithConnectionPool',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AssociateIpWithConnectionPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_ip_with_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_ip_with_connection_pool_with_options(request, runtime)

    def associate_vswitch_with_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_list):
            query['VSwitchList'] = request.v_switch_list
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateVSwitchWithIoTCloudConnector',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_vswitch_with_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_vswitch_with_io_tcloud_connector_with_options(request, runtime)

    def create_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_description):
            query['AuthorizationRuleDescription'] = request.authorization_rule_description
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_cidrs):
            query['SourceCidrs'] = request.source_cidrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorizationRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_rule_with_options(request, runtime)

    def create_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidrs):
            query['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_description):
            query['ConnectionPoolDescription'] = request.connection_pool_description
        if not UtilClient.is_unset(request.connection_pool_name):
            query['ConnectionPoolName'] = request.connection_pool_name
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConnectionPool',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateConnectionPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def create_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_connection_pool_with_options(request, runtime)

    def create_dnsservice_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_description):
            query['AuthorizationRuleDescription'] = request.authorization_rule_description
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDNSServiceRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateDNSServiceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dnsservice_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dnsservice_rule_with_options(request, runtime)

    def create_group_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_description):
            query['AuthorizationRuleDescription'] = request.authorization_rule_description
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_cidrs):
            query['SourceCidrs'] = request.source_cidrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupAuthorizationRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateGroupAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_authorization_rule_with_options(request, runtime)

    def create_group_dnsservice_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dnsservice_rule_description):
            query['DNSServiceRuleDescription'] = request.dnsservice_rule_description
        if not UtilClient.is_unset(request.dnsservice_rule_name):
            query['DNSServiceRuleName'] = request.dnsservice_rule_name
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupDNSServiceRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateGroupDNSServiceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_dnsservice_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_dnsservice_rule_with_options(request, runtime)

    def create_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apn):
            query['APN'] = request.apn
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.io_tcloud_connector_description):
            query['IoTCloudConnectorDescription'] = request.io_tcloud_connector_description
        if not UtilClient.is_unset(request.io_tcloud_connector_name):
            query['IoTCloudConnectorName'] = request.io_tcloud_connector_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.wildcard_domain_enabled):
            query['WildcardDomainEnabled'] = request.wildcard_domain_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIoTCloudConnector',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateIoTCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_io_tcloud_connector_with_options(request, runtime)

    def create_io_tcloud_connector_group_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIoTCloudConnectorGroup',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateIoTCloudConnectorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_io_tcloud_connector_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_io_tcloud_connector_group_with_options(request, runtime)

    def create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    def create_service_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_entry_description):
            query['ServiceEntryDescription'] = request.service_entry_description
        if not UtilClient.is_unset(request.service_entry_name):
            query['ServiceEntryName'] = request.service_entry_name
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceEntry',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_entry_with_options(request, runtime)

    def delete_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthorizationRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_authorization_rule_with_options(request, runtime)

    def delete_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnectionPool',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteConnectionPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_pool_with_options(request, runtime)

    def delete_dnsservice_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dnsservice_rule_id):
            query['DNSServiceRuleId'] = request.dnsservice_rule_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDNSServiceRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteDNSServiceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dnsservice_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dnsservice_rule_with_options(request, runtime)

    def delete_group_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupAuthorizationRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteGroupAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_authorization_rule_with_options(request, runtime)

    def delete_group_dnsservice_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dnsservice_rule_id):
            query['DNSServiceRuleId'] = request.dnsservice_rule_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupDNSServiceRule',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteGroupDNSServiceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_dnsservice_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_dnsservice_rule_with_options(request, runtime)

    def delete_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIoTCloudConnector',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteIoTCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_io_tcloud_connector_with_options(request, runtime)

    def delete_io_tcloud_connector_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIoTCloudConnectorGroup',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteIoTCloudConnectorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_io_tcloud_connector_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_io_tcloud_connector_group_with_options(request, runtime)

    def delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    def delete_service_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_entry_id):
            query['ServiceEntryId'] = request.service_entry_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceEntry',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_entry_with_options(request, runtime)

    def disable_io_tcloud_connector_access_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableIoTCloudConnectorAccessLog',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_io_tcloud_connector_access_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_io_tcloud_connector_access_log_with_options(request, runtime)

    def dissociate_ip_from_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.ips):
            query['Ips'] = request.ips
        if not UtilClient.is_unset(request.ips_file_path):
            query['IpsFilePath'] = request.ips_file_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateIpFromConnectionPool',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DissociateIpFromConnectionPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_ip_from_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_ip_from_connection_pool_with_options(request, runtime)

    def dissociate_vswitch_from_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateVSwitchFromIoTCloudConnector',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_vswitch_from_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_vswitch_from_io_tcloud_connector_with_options(request, runtime)

    def enable_io_tcloud_connector_access_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_sls_log_store):
            query['AccessLogSlsLogStore'] = request.access_log_sls_log_store
        if not UtilClient.is_unset(request.access_log_sls_project):
            query['AccessLogSlsProject'] = request.access_log_sls_project
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableIoTCloudConnectorAccessLog',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_io_tcloud_connector_access_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_io_tcloud_connector_access_log_with_options(request, runtime)

    def get_connection_pool_ip_operation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.query_request_id):
            query['QueryRequestId'] = request.query_request_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionPoolIpOperationResult',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetConnectionPoolIpOperationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_connection_pool_ip_operation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_pool_ip_operation_result_with_options(request, runtime)

    def get_diagnose_result_for_single_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.diagnose_task_id):
            query['DiagnoseTaskId'] = request.diagnose_task_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagnoseResultForSingleCard',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetDiagnoseResultForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def get_diagnose_result_for_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_diagnose_result_for_single_card_with_options(request, runtime)

    def get_io_tcloud_connector_access_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIoTCloudConnectorAccessLog',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_io_tcloud_connector_access_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_io_tcloud_connector_access_log_with_options(request, runtime)

    def get_sts_info_and_oss_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStsInfoAndOssPath',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetStsInfoAndOssPathResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sts_info_and_oss_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sts_info_and_oss_path_with_options(request, runtime)

    def grant_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.virtual_border_router_id):
            query['VirtualBorderRouterId'] = request.virtual_border_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantVirtualBorderRouter',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GrantVirtualBorderRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_virtual_border_router_with_options(request, runtime)

    def list_apns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apn):
            query['APN'] = request.apn
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAPNs',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListAPNsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apns_with_options(request, runtime)

    def list_authorization_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_ids):
            query['AuthorizationRuleIds'] = request.authorization_rule_ids
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.authorization_rule_status):
            query['AuthorizationRuleStatus'] = request.authorization_rule_status
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizationRules',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authorization_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authorization_rules_with_options(request, runtime)

    def list_connection_pool_all_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectionPoolAllIps',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListConnectionPoolAllIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connection_pool_all_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connection_pool_all_ips_with_options(request, runtime)

    def list_connection_pool_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectionPoolIps',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListConnectionPoolIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connection_pool_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connection_pool_ips_with_options(request, runtime)

    def list_connection_pools_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_pool_ids):
            query['ConnectionPoolIds'] = request.connection_pool_ids
        if not UtilClient.is_unset(request.connection_pool_name):
            query['ConnectionPoolName'] = request.connection_pool_name
        if not UtilClient.is_unset(request.connection_pool_status):
            query['ConnectionPoolStatus'] = request.connection_pool_status
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectionPools',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListConnectionPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connection_pools(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connection_pools_with_options(request, runtime)

    def list_dnsservice_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dnsservice_rule_ids):
            query['DNSServiceRuleIds'] = request.dnsservice_rule_ids
        if not UtilClient.is_unset(request.dnsservice_rule_name):
            query['DNSServiceRuleName'] = request.dnsservice_rule_name
        if not UtilClient.is_unset(request.dnsservice_rule_status):
            query['DNSServiceRuleStatus'] = request.dnsservice_rule_status
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDNSServiceRules',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListDNSServiceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dnsservice_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dnsservice_rules_with_options(request, runtime)

    def list_diagnose_info_for_single_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseInfoForSingleCard',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListDiagnoseInfoForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diagnose_info_for_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_diagnose_info_for_single_card_with_options(request, runtime)

    def list_group_authorization_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_ids):
            query['AuthorizationRuleIds'] = request.authorization_rule_ids
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.authorization_rule_status):
            query['AuthorizationRuleStatus'] = request.authorization_rule_status
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupAuthorizationRules',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListGroupAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_authorization_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_authorization_rules_with_options(request, runtime)

    def list_group_dnsservice_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dnsservice_rule_ids):
            query['DNSServiceRuleIds'] = request.dnsservice_rule_ids
        if not UtilClient.is_unset(request.dnsservice_rule_name):
            query['DNSServiceRuleName'] = request.dnsservice_rule_name
        if not UtilClient.is_unset(request.dnsservice_rule_status):
            query['DNSServiceRuleStatus'] = request.dnsservice_rule_status
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupDNSServiceRules',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListGroupDNSServiceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_dnsservice_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_dnsservice_rules_with_options(request, runtime)

    def list_io_tcloud_connector_available_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectorAvailableZones',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_io_tcloud_connector_available_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_available_zones_with_options(request, runtime)

    def list_io_tcloud_connector_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_group_ids):
            query['IoTCloudConnectorGroupIds'] = request.io_tcloud_connector_group_ids
        if not UtilClient.is_unset(request.io_tcloud_connector_group_name):
            query['IoTCloudConnectorGroupName'] = request.io_tcloud_connector_group_name
        if not UtilClient.is_unset(request.io_tcloud_connector_group_status):
            query['IoTCloudConnectorGroupStatus'] = request.io_tcloud_connector_group_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectorGroups',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_io_tcloud_connector_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_groups_with_options(request, runtime)

    def list_io_tcloud_connectors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apn):
            query['APN'] = request.apn
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.io_tcloud_connector_ids):
            query['IoTCloudConnectorIds'] = request.io_tcloud_connector_ids
        if not UtilClient.is_unset(request.io_tcloud_connector_name):
            query['IoTCloudConnectorName'] = request.io_tcloud_connector_name
        if not UtilClient.is_unset(request.io_tcloud_connector_status):
            query['IoTCloudConnectorStatus'] = request.io_tcloud_connector_status
        if not UtilClient.is_unset(request.is_in_group):
            query['IsInGroup'] = request.is_in_group
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIoTCloudConnectors',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_io_tcloud_connectors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connectors_with_options(request, runtime)

    def list_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    def list_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_statuses):
            query['ResourceStatuses'] = request.resource_statuses
        if not UtilClient.is_unset(request.service_ids):
            query['ServiceIds'] = request.service_ids
        if not UtilClient.is_unset(request.service_names):
            query['ServiceNames'] = request.service_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListService',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_with_options(request, runtime)

    def list_service_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_entry_ids):
            query['ServiceEntryIds'] = request.service_entry_ids
        if not UtilClient.is_unset(request.service_entry_name):
            query['ServiceEntryName'] = request.service_entry_name
        if not UtilClient.is_unset(request.service_entry_status):
            query['ServiceEntryStatus'] = request.service_entry_status
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceEntries',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_entries_with_options(request, runtime)

    def move_authorization_rule_to_dnsservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAuthorizationRuleToDNSService',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.MoveAuthorizationRuleToDNSServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def move_authorization_rule_to_dnsservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_authorization_rule_to_dnsservice_with_options(request, runtime)

    def move_group_authorization_rule_to_dnsservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveGroupAuthorizationRuleToDNSService',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.MoveGroupAuthorizationRuleToDNSServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def move_group_authorization_rule_to_dnsservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_group_authorization_rule_to_dnsservice_with_options(request, runtime)

    def open_io_tcloud_connector_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenIoTCloudConnectorService',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.OpenIoTCloudConnectorServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_io_tcloud_connector_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_io_tcloud_connector_service_with_options(request, runtime)

    def remove_io_tcloud_connector_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIoTCloudConnectorFromGroup',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.RemoveIoTCloudConnectorFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_io_tcloud_connector_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_io_tcloud_connector_from_group_with_options(request, runtime)

    def submit_diagnose_task_for_single_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_uid):
            query['ResourceUid'] = request.resource_uid
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDiagnoseTaskForSingleCard',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.SubmitDiagnoseTaskForSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_diagnose_task_for_single_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_diagnose_task_for_single_card_with_options(request, runtime)

    def update_authorization_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_description):
            query['AuthorizationRuleDescription'] = request.authorization_rule_description
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_cidrs):
            query['SourceCidrs'] = request.source_cidrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationRuleAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_authorization_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_rule_attribute_with_options(request, runtime)

    def update_connection_pool_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidrs):
            query['Cidrs'] = request.cidrs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_pool_description):
            query['ConnectionPoolDescription'] = request.connection_pool_description
        if not UtilClient.is_unset(request.connection_pool_id):
            query['ConnectionPoolId'] = request.connection_pool_id
        if not UtilClient.is_unset(request.connection_pool_name):
            query['ConnectionPoolName'] = request.connection_pool_name
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnectionPoolAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateConnectionPoolAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_connection_pool_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_connection_pool_attribute_with_options(request, runtime)

    def update_dnsservice_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_description):
            query['AuthorizationRuleDescription'] = request.authorization_rule_description
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dnsservice_rule_id):
            query['DNSServiceRuleId'] = request.dnsservice_rule_id
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSServiceRuleAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateDNSServiceRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dnsservice_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dnsservice_rule_attribute_with_options(request, runtime)

    def update_group_authorization_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_rule_description):
            query['AuthorizationRuleDescription'] = request.authorization_rule_description
        if not UtilClient.is_unset(request.authorization_rule_id):
            query['AuthorizationRuleId'] = request.authorization_rule_id
        if not UtilClient.is_unset(request.authorization_rule_name):
            query['AuthorizationRuleName'] = request.authorization_rule_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_cidrs):
            query['SourceCidrs'] = request.source_cidrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupAuthorizationRuleAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateGroupAuthorizationRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_authorization_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_authorization_rule_attribute_with_options(request, runtime)

    def update_group_dnsservice_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dnsservice_rule_description):
            query['DNSServiceRuleDescription'] = request.dnsservice_rule_description
        if not UtilClient.is_unset(request.dnsservice_rule_id):
            query['DNSServiceRuleId'] = request.dnsservice_rule_id
        if not UtilClient.is_unset(request.dnsservice_rule_name):
            query['DNSServiceRuleName'] = request.dnsservice_rule_name
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDNSServiceRuleAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateGroupDNSServiceRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_dnsservice_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_dnsservice_rule_attribute_with_options(request, runtime)

    def update_io_tcloud_connector_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_description):
            query['IoTCloudConnectorDescription'] = request.io_tcloud_connector_description
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.io_tcloud_connector_name):
            query['IoTCloudConnectorName'] = request.io_tcloud_connector_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wildcard_domain_enabled):
            query['WildcardDomainEnabled'] = request.wildcard_domain_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIoTCloudConnectorAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_io_tcloud_connector_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_io_tcloud_connector_attribute_with_options(request, runtime)

    def update_io_tcloud_connector_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_group_id):
            query['IoTCloudConnectorGroupId'] = request.io_tcloud_connector_group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIoTCloudConnectorGroupAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateIoTCloudConnectorGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_io_tcloud_connector_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_io_tcloud_connector_group_attribute_with_options(request, runtime)

    def update_service_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_description):
            query['ServiceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_attribute_with_options(request, runtime)

    def update_service_entry_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.io_tcloud_connector_id):
            query['IoTCloudConnectorId'] = request.io_tcloud_connector_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_entry_description):
            query['ServiceEntryDescription'] = request.service_entry_description
        if not UtilClient.is_unset(request.service_entry_id):
            query['ServiceEntryId'] = request.service_entry_id
        if not UtilClient.is_unset(request.service_entry_name):
            query['ServiceEntryName'] = request.service_entry_name
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceEntryAttribute',
            version='2021-05-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceEntryAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_entry_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_entry_attribute_with_options(request, runtime)
