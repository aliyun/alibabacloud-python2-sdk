# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eipanycast20200309 import models as eipanycast_20200309_models
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
        self._endpoint = self.get_endpoint('eipanycast', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_anycast_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Bandwidth'] = request.bandwidth
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['InstanceChargeType'] = request.instance_charge_type
        query['InternetChargeType'] = request.internet_charge_type
        query['Name'] = request.name
        query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.AllocateAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_anycast_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_anycast_eip_address_with_options(request, runtime)

    def associate_anycast_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['AssociationMode'] = request.association_mode
        query['BindInstanceId'] = request.bind_instance_id
        query['BindInstanceRegionId'] = request.bind_instance_region_id
        query['BindInstanceType'] = request.bind_instance_type
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['PopLocations'] = request.pop_locations
        query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.AssociateAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_anycast_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_anycast_eip_address_with_options(request, runtime)

    def describe_anycast_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['BindInstanceId'] = request.bind_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_anycast_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_eip_address_with_options(request, runtime)

    def describe_anycast_pop_locations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAnycastPopLocations',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastPopLocationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_anycast_pop_locations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_pop_locations_with_options(request, runtime)

    def describe_anycast_server_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ServiceLocation'] = request.service_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAnycastServerRegions',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.DescribeAnycastServerRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_anycast_server_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_anycast_server_regions_with_options(request, runtime)

    def list_anycast_eip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastEipAddress'] = request.anycast_eip_address
        query['AnycastId'] = request.anycast_id
        query['BindInstanceIds'] = request.bind_instance_ids
        query['BusinessStatus'] = request.business_status
        query['InstanceChargeType'] = request.instance_charge_type
        query['InternetChargeType'] = request.internet_charge_type
        query['MaxResults'] = request.max_results
        query['Name'] = request.name
        query['NextToken'] = request.next_token
        query['ServiceLocation'] = request.service_location
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAnycastEipAddresses',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ListAnycastEipAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_anycast_eip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_anycast_eip_addresses_with_options(request, runtime)

    def modify_anycast_eip_address_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['Description'] = request.description
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAnycastEipAddressAttribute',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ModifyAnycastEipAddressAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_anycast_eip_address_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_anycast_eip_address_attribute_with_options(request, runtime)

    def modify_anycast_eip_address_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['Bandwidth'] = request.bandwidth
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAnycastEipAddressSpec',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ModifyAnycastEipAddressSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_anycast_eip_address_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_anycast_eip_address_spec_with_options(request, runtime)

    def release_anycast_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.ReleaseAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def release_anycast_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_anycast_eip_address_with_options(request, runtime)

    def unassociate_anycast_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['BindInstanceId'] = request.bind_instance_id
        query['BindInstanceRegionId'] = request.bind_instance_region_id
        query['BindInstanceType'] = request.bind_instance_type
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnassociateAnycastEipAddress',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UnassociateAnycastEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def unassociate_anycast_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_anycast_eip_address_with_options(request, runtime)

    def update_anycast_eip_address_associations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AnycastId'] = request.anycast_id
        query['AssociationMode'] = request.association_mode
        query['BindInstanceId'] = request.bind_instance_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['PopLocationAddList'] = request.pop_location_add_list
        query['PopLocationDeleteList'] = request.pop_location_delete_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAnycastEipAddressAssociations',
            version='2020-03-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eipanycast_20200309_models.UpdateAnycastEipAddressAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_anycast_eip_address_associations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_anycast_eip_address_associations_with_options(request, runtime)
