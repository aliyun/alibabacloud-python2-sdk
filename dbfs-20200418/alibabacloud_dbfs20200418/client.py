# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbfs20200418 import models as dbfs20200418_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'dbfs.aliyuncs.com',
            'cn-beijing-finance-1': 'dbfs.aliyuncs.com',
            'cn-beijing-finance-pop': 'dbfs.aliyuncs.com',
            'cn-beijing-gov-1': 'dbfs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dbfs.aliyuncs.com',
            'cn-edge-1': 'dbfs.aliyuncs.com',
            'cn-fujian': 'dbfs.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dbfs.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dbfs.aliyuncs.com',
            'cn-hangzhou-finance': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dbfs.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dbfs.aliyuncs.com',
            'cn-hangzhou-test-306': 'dbfs.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dbfs.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dbfs.aliyuncs.com',
            'cn-north-2-gov-1': 'dbfs.aliyuncs.com',
            'cn-qingdao-nebula': 'dbfs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dbfs.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dbfs.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbfs.aliyuncs.com',
            'cn-shanghai-inner': 'dbfs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dbfs.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbfs.aliyuncs.com',
            'cn-shenzhen-inner': 'dbfs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dbfs.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dbfs.aliyuncs.com',
            'cn-wuhan': 'dbfs.aliyuncs.com',
            'cn-wulanchabu': 'dbfs.aliyuncs.com',
            'cn-yushanfang': 'dbfs.aliyuncs.com',
            'cn-zhangbei': 'dbfs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dbfs.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dbfs.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dbfs.aliyuncs.com',
            'eu-west-1-oxs': 'dbfs.aliyuncs.com',
            'rus-west-1-pop': 'dbfs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbfs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_tags_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbfs_list):
            query['DbfsList'] = request.dbfs_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_batch_with_options(request, runtime)

    def attach_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not UtilClient.is_unset(request.attach_point):
            query['AttachPoint'] = request.attach_point
        if not UtilClient.is_unset(request.ecsinstance_id):
            query['ECSInstanceId'] = request.ecsinstance_id
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server_url):
            query['ServerUrl'] = request.server_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_dbfs_with_options(request, runtime)

    def create_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_snapshot):
            query['DeleteSnapshot'] = request.delete_snapshot
        if not UtilClient.is_unset(request.enable_raid):
            query['EnableRaid'] = request.enable_raid
        if not UtilClient.is_unset(request.encryption):
            query['Encryption'] = request.encryption
        if not UtilClient.is_unset(request.fs_name):
            query['FsName'] = request.fs_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.raid_stripe_unit_number):
            query['RaidStripeUnitNumber'] = request.raid_stripe_unit_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size_g):
            query['SizeG'] = request.size_g
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.used_scene):
            query['UsedScene'] = request.used_scene
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbfs_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def delete_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbfs_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_tags_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbfs_list):
            query['DbfsList'] = request.dbfs_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagsBatch',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tags_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tags_batch_with_options(request, runtime)

    def describe_dbfs_specifications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.ecs_instance_type):
            query['EcsInstanceType'] = request.ecs_instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDbfsSpecifications',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbfs_specifications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbfs_specifications_with_options(request, runtime)

    def describe_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    def detach_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecsinstance_id):
            query['ECSInstanceId'] = request.ecsinstance_id
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_dbfs_with_options(request, runtime)

    def get_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dbfs_with_options(request, runtime)

    def get_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRole',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_with_options(request, runtime)

    def list_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_with_options(request, runtime)

    def list_dbfs_attachable_ecs_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachableEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachableEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dbfs_attachable_ecs_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_attachable_ecs_instances_with_options(request, runtime)

    def list_dbfs_attached_ecs_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDbfsAttachedEcsInstances',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsAttachedEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dbfs_attached_ecs_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_attached_ecs_instances_with_options(request, runtime)

    def list_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_key):
            query['FilterKey'] = request.filter_key
        if not UtilClient.is_unset(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshot',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def list_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def rename_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.fs_name):
            query['FsName'] = request.fs_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenameDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def rename_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rename_dbfs_with_options(request, runtime)

    def reset_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResetDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_dbfs_with_options(request, runtime)

    def resize_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fs_id):
            query['FsId'] = request.fs_id
        if not UtilClient.is_unset(request.new_size_g):
            query['NewSizeG'] = request.new_size_g
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def resize_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_dbfs_with_options(request, runtime)

    def tag_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbfs_id):
            query['DbfsId'] = request.dbfs_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagDbfs',
            version='2020-04-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_dbfs_with_options(request, runtime)
