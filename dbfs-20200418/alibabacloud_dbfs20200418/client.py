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

    def create_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateConstantsResponse(),
            self.do_rpcrequest('CreateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_constants_with_options(request, runtime)

    def delete_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteDbfsResponse(),
            self.do_rpcrequest('DeleteDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbfs_with_options(request, runtime)

    def delete_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteConstantsResponse(),
            self.do_rpcrequest('DeleteConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_constants_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def resize_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResizeDbfsResponse(),
            self.do_rpcrequest('ResizeDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_dbfs_with_options(request, runtime)

    def publish_upgrade_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.PublishUpgradeTaskResponse(),
            self.do_rpcrequest('PublishUpgradeTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_upgrade_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_upgrade_task_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def detach_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DetachDbfsResponse(),
            self.do_rpcrequest('DetachDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_dbfs_with_options(request, runtime)

    def generate_upgrade_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GenerateUpgradeRecordResponse(),
            self.do_rpcrequest('GenerateUpgradeRecord', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_upgrade_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_upgrade_record_with_options(request, runtime)

    def reset_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ResetDbfsResponse(),
            self.do_rpcrequest('ResetDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_dbfs_with_options(request, runtime)

    def get_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetDbfsResponse(),
            self.do_rpcrequest('GetDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dbfs_with_options(request, runtime)

    def dbfs_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DbfsRecordResponse(),
            self.do_rpcrequest('DbfsRecord', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dbfs_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dbfs_record_with_options(request, runtime)

    def stop_upgrade_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.StopUpgradeTaskResponse(),
            self.do_rpcrequest('StopUpgradeTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_upgrade_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_upgrade_task_with_options(request, runtime)

    def create_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateDbfsResponse(),
            self.do_rpcrequest('CreateDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbfs_with_options(request, runtime)

    def update_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateTaskResponse(),
            self.do_rpcrequest('UpdateTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_task_with_options(request, runtime)

    def delete_tags_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DeleteTagsBatchResponse(),
            self.do_rpcrequest('DeleteTagsBatch', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tags_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tags_batch_with_options(request, runtime)

    def get_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetServiceLinkedRoleResponse(),
            self.do_rpcrequest('GetServiceLinkedRole', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_with_options(request, runtime)

    def update_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.UpdateConstantsResponse(),
            self.do_rpcrequest('UpdateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_constants_with_options(request, runtime)

    def insert_synchroniz_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.InsertSynchronizConstantsResponse(),
            self.do_rpcrequest('InsertSynchronizConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_synchroniz_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_synchroniz_constants_with_options(request, runtime)

    def attach_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.AttachDbfsResponse(),
            self.do_rpcrequest('AttachDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_dbfs_with_options(request, runtime)

    def list_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTaskResponse(),
            self.do_rpcrequest('ListTask', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    def list_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListDbfsResponse(),
            self.do_rpcrequest('ListDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dbfs_with_options(request, runtime)

    def add_tags_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.AddTagsBatchResponse(),
            self.do_rpcrequest('AddTagsBatch', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_batch_with_options(request, runtime)

    def tag_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.TagDbfsResponse(),
            self.do_rpcrequest('TagDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_dbfs_with_options(request, runtime)

    def get_synchroniz_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.GetSynchronizConstantsResponse(),
            self.do_rpcrequest('GetSynchronizConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_synchroniz_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_synchroniz_constants_with_options(request, runtime)

    def opreate_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.OpreateConstantsResponse(),
            self.do_rpcrequest('OpreateConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def opreate_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.opreate_constants_with_options(request, runtime)

    def rename_dbfs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.RenameDbfsResponse(),
            self.do_rpcrequest('RenameDbfs', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rename_dbfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rename_dbfs_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_constants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListConstantsResponse(),
            self.do_rpcrequest('ListConstants', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_constants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_constants_with_options(request, runtime)

    def list_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.ListSnapshotResponse(),
            self.do_rpcrequest('ListSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_with_options(request, runtime)

    def describe_dbfs_specifications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.DescribeDbfsSpecificationsResponse(),
            self.do_rpcrequest('DescribeDbfsSpecifications', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbfs_specifications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbfs_specifications_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dbfs20200418_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2020-04-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)
