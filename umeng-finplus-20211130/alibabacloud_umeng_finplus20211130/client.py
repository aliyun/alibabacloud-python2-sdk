# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_finplus20211130 import models as umeng_finplus_20211130_models
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
        self._endpoint = self.get_endpoint('umeng-finplus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_compute_task_by_bc_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bc_id):
            query['bcId'] = request.bc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelComputeTaskByBcId',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/cancelComputeTaskByBcId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.CancelComputeTaskByBcIdResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_compute_task_by_bc_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_compute_task_by_bc_id_with_options(request, headers, runtime)

    def create_compute_task_by_data_set_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_info_form):
            body['BatchInfoForm'] = request.batch_info_form
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeTaskByDataSetId',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/createComputeTaskByDataSetId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.CreateComputeTaskByDataSetIdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_compute_task_by_data_set_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_compute_task_by_data_set_id_with_options(request, headers, runtime)

    def create_compute_task_by_multi_data_set_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.data_set_ids):
            body['dataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeTaskByMultiDataSetId',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/createComputeTaskByMultiDataSetId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.CreateComputeTaskByMultiDataSetIdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_compute_task_by_multi_data_set_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_compute_task_by_multi_data_set_id_with_options(request, headers, runtime)

    def get_available_data_set_list_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAvailableDataSetList',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/getAvailableDataSetList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.GetAvailableDataSetListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_available_data_set_list(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_available_data_set_list_with_options(headers, runtime)

    def get_compute_result_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bc_id):
            query['bcId'] = request.bc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetComputeResult',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/getComputeTaskResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.GetComputeResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_compute_result(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_compute_result_with_options(request, headers, runtime)

    def get_data_set_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_set_id):
            query['dataSetId'] = request.data_set_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSetStatus',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/getDataSetStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.GetDataSetStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_set_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_set_status_with_options(request, headers, runtime)

    def get_data_set_sts_akwith_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSetStsAK',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/getDataSetStsAk',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.GetDataSetStsAKResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_set_sts_ak(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_set_sts_akwith_options(headers, runtime)

    def submit_data_set_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_set_type):
            body['dataSetType'] = request.data_set_type
        if not UtilClient.is_unset(request.id_type):
            body['idType'] = request.id_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.oss_file_name):
            body['ossFileName'] = request.oss_file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitDataSetTask',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/submitDataSetTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.SubmitDataSetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_data_set_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_data_set_task_with_options(request, headers, runtime)

    def cancel_yyd_task_by_bc_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bc_id):
            query['bcId'] = request.bc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='cancelYydTaskByBcId',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/yyd/task/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.CancelYydTaskByBcIdResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_yyd_task_by_bc_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_yyd_task_by_bc_id_with_options(request, headers, runtime)

    def create_yyd_compute_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='createYydComputeTask',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/yyd/task/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.CreateYydComputeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_yyd_compute_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_yyd_compute_task_with_options(request, headers, runtime)

    def create_yyd_data_set_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.oss_file_name):
            body['ossFileName'] = request.oss_file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='createYydDataSet',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/yyd/dataset/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.CreateYydDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_yyd_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_yyd_data_set_with_options(request, headers, runtime)

    def list_yyd_compute_task_list_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='listYydComputeTaskList',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/yyd/task/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.ListYydComputeTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def list_yyd_compute_task_list(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_yyd_compute_task_list_with_options(headers, runtime)

    def list_yyd_data_set_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='listYydDataSet',
            version='2021-11-30',
            protocol='HTTPS',
            pathname='/batch_compute/yyd/dataset/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_finplus_20211130_models.ListYydDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    def list_yyd_data_set(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_yyd_data_set_with_options(headers, runtime)
