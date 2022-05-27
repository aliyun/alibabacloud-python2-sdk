# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ebs20210730 import models as ebs_20210730_models
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
        self._endpoint = self.get_endpoint('ebs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.AddDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def add_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_disk_replica_pair_with_options(request, runtime)

    def create_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_group_with_options(request, runtime)

    def create_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def create_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_pair_with_options(request, runtime)

    def delete_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_group_with_options(request, runtime)

    def delete_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_pair_with_options(request, runtime)

    def describe_disk_replica_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaGroups',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_disk_replica_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_groups_with_options(request, runtime)

    def describe_disk_replica_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_disk_replica_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pairs_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def failover_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def failover_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.failover_disk_replica_group_with_options(request, runtime)

    def failover_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def failover_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.failover_disk_replica_pair_with_options(request, runtime)

    def modify_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_replica_group_with_options(request, runtime)

    def modify_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_replica_pair_with_options(request, runtime)

    def remove_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.RemoveDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_disk_replica_pair_with_options(request, runtime)

    def reprotect_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def reprotect_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reprotect_disk_replica_group_with_options(request, runtime)

    def reprotect_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def reprotect_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reprotect_disk_replica_pair_with_options(request, runtime)

    def start_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def start_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_group_with_options(request, runtime)

    def start_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def start_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_pair_with_options(request, runtime)

    def stop_disk_replica_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_disk_replica_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_group_with_options(request, runtime)

    def stop_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_pair_with_options(request, runtime)
