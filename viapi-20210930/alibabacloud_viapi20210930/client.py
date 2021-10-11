# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_viapi20210930 import models as viapi_20210930_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('viapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_ai_store_user_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskResponse(),
            self.do_rpcrequest('GetAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ai_store_user_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ai_store_user_task_with_options(request, runtime)

    def query_ai_store_user_task_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreUserTaskPageResponse(),
            self.do_rpcrequest('QueryAiStoreUserTaskPage', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ai_store_user_task_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_user_task_page_with_options(request, runtime)

    def query_ai_store_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreRegionsResponse(),
            self.do_rpcrequest('QueryAiStoreRegions', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ai_store_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_regions_with_options(runtime)

    def list_ai_store_buckets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.ListAiStoreBucketsResponse(),
            self.do_rpcrequest('ListAiStoreBuckets', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ai_store_buckets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ai_store_buckets_with_options(request, runtime)

    def get_ai_store_user_task_by_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreUserTaskByNameResponse(),
            self.do_rpcrequest('GetAiStoreUserTaskByName', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ai_store_user_task_by_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ai_store_user_task_by_name_with_options(request, runtime)

    def update_ai_store_user_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.UpdateAiStoreUserTaskResponse(),
            self.do_rpcrequest('UpdateAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ai_store_user_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ai_store_user_task_with_options(request, runtime)

    def disable_ai_store_user_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.DisableAiStoreUserTaskResponse(),
            self.do_rpcrequest('DisableAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_ai_store_user_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_ai_store_user_task_with_options(request, runtime)

    def query_ai_store_api_tree_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            viapi_20210930_models.QueryAiStoreApiTreeResponse(),
            self.do_rpcrequest('QueryAiStoreApiTree', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_ai_store_api_tree(self):
        runtime = util_models.RuntimeOptions()
        return self.query_ai_store_api_tree_with_options(runtime)

    def delete_ai_store_user_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.DeleteAiStoreUserTaskResponse(),
            self.do_rpcrequest('DeleteAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ai_store_user_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ai_store_user_task_with_options(request, runtime)

    def create_ai_store_user_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreUserTaskResponse(),
            self.do_rpcrequest('CreateAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ai_store_user_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ai_store_user_task_with_options(request, runtime)

    def create_ai_store_receive_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreReceiveConfigResponse(),
            self.do_rpcrequest('CreateAiStoreReceiveConfig', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ai_store_receive_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ai_store_receive_config_with_options(request, runtime)

    def get_ai_store_receive_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.GetAiStoreReceiveConfigResponse(),
            self.do_rpcrequest('GetAiStoreReceiveConfig', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ai_store_receive_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ai_store_receive_config_with_options(request, runtime)

    def enable_ai_store_user_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.EnableAiStoreUserTaskResponse(),
            self.do_rpcrequest('EnableAiStoreUserTask', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_ai_store_user_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_ai_store_user_task_with_options(request, runtime)

    def create_ai_store_bucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CreateAiStoreBucketResponse(),
            self.do_rpcrequest('CreateAiStoreBucket', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ai_store_bucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ai_store_bucket_with_options(request, runtime)

    def check_service_linked_role_for_deleting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            viapi_20210930_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.do_rpcrequest('CheckServiceLinkedRoleForDeleting', '2021-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role_for_deleting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)
