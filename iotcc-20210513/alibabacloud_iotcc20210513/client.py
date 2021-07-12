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

    def delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceResponse(),
            self.do_rpcrequest('DeleteService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    def delete_service_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceEntryResponse(),
            self.do_rpcrequest('DeleteServiceEntry', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_entry_with_options(request, runtime)

    def update_service_entry_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceEntryAttributeResponse(),
            self.do_rpcrequest('UpdateServiceEntryAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service_entry_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_entry_attribute_with_options(request, runtime)

    def update_service_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceAttributeResponse(),
            self.do_rpcrequest('UpdateServiceAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_attribute_with_options(request, runtime)

    def list_authorization_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListAuthorizationRulesResponse(),
            self.do_rpcrequest('ListAuthorizationRules', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authorization_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authorization_rules_with_options(request, runtime)

    def list_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceResponse(),
            self.do_rpcrequest('ListService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_with_options(request, runtime)

    def associate_vswitch_with_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse(),
            self.do_rpcrequest('AssociateVSwitchWithIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_vswitch_with_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_vswitch_with_io_tcloud_connector_with_options(request, runtime)

    def list_connection_pools_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListConnectionPoolsResponse(),
            self.do_rpcrequest('ListConnectionPools', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connection_pools(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connection_pools_with_options(request, runtime)

    def update_connection_pool_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateConnectionPoolAttributeResponse(),
            self.do_rpcrequest('UpdateConnectionPoolAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_connection_pool_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_connection_pool_attribute_with_options(request, runtime)

    def disable_io_tcloud_connector_access_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse(),
            self.do_rpcrequest('DisableIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_io_tcloud_connector_access_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_io_tcloud_connector_access_log_with_options(request, runtime)

    def create_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateConnectionPoolResponse(),
            self.do_rpcrequest('CreateConnectionPool', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_connection_pool_with_options(request, runtime)

    def create_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateAuthorizationRuleResponse(),
            self.do_rpcrequest('CreateAuthorizationRule', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_rule_with_options(request, runtime)

    def update_io_tcloud_connector_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse(),
            self.do_rpcrequest('UpdateIoTCloudConnectorAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_io_tcloud_connector_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_io_tcloud_connector_attribute_with_options(request, runtime)

    def delete_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteIoTCloudConnectorResponse(),
            self.do_rpcrequest('DeleteIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_io_tcloud_connector_with_options(request, runtime)

    def list_io_tcloud_connector_available_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse(),
            self.do_rpcrequest('ListIoTCloudConnectorAvailableZones', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_io_tcloud_connector_available_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_available_zones_with_options(request, runtime)

    def get_io_tcloud_connector_access_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse(),
            self.do_rpcrequest('GetIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_io_tcloud_connector_access_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_io_tcloud_connector_access_log_with_options(request, runtime)

    def delete_authorization_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteAuthorizationRuleResponse(),
            self.do_rpcrequest('DeleteAuthorizationRule', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_authorization_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_authorization_rule_with_options(request, runtime)

    def delete_connection_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteConnectionPoolResponse(),
            self.do_rpcrequest('DeleteConnectionPool', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_connection_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_pool_with_options(request, runtime)

    def dissociate_vswitch_from_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse(),
            self.do_rpcrequest('DissociateVSwitchFromIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_vswitch_from_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_vswitch_from_io_tcloud_connector_with_options(request, runtime)

    def enable_io_tcloud_connector_access_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse(),
            self.do_rpcrequest('EnableIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_io_tcloud_connector_access_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_io_tcloud_connector_access_log_with_options(request, runtime)

    def list_service_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceEntriesResponse(),
            self.do_rpcrequest('ListServiceEntries', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_entries_with_options(request, runtime)

    def create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceResponse(),
            self.do_rpcrequest('CreateService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    def list_io_tcloud_connectors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorsResponse(),
            self.do_rpcrequest('ListIoTCloudConnectors', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_io_tcloud_connectors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connectors_with_options(request, runtime)

    def create_io_tcloud_connector_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateIoTCloudConnectorResponse(),
            self.do_rpcrequest('CreateIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_io_tcloud_connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_io_tcloud_connector_with_options(request, runtime)

    def update_authorization_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse(),
            self.do_rpcrequest('UpdateAuthorizationRuleAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_authorization_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_rule_attribute_with_options(request, runtime)

    def create_service_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceEntryResponse(),
            self.do_rpcrequest('CreateServiceEntry', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_entry_with_options(request, runtime)
