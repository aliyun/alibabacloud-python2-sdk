# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imm20200930 import models as imm_20200930_models
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
            'cn-beijing-gov-1': 'imm-vpc.cn-beijing-gov-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('imm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_delete_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchDeleteFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            self.do_rpcrequest('BatchDeleteFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_file_meta_with_options(request, runtime)

    def batch_get_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            self.do_rpcrequest('BatchGetFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_get_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_file_meta_with_options(request, runtime)

    def batch_index_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            self.do_rpcrequest('BatchIndexFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_index_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_index_file_meta_with_options(request, runtime)

    def batch_update_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchUpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            self.do_rpcrequest('BatchUpdateFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_update_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_file_meta_with_options(request, runtime)

    def create_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            self.do_rpcrequest('CreateBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    def create_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            self.do_rpcrequest('CreateDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def delete_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            self.do_rpcrequest('DeleteBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    def delete_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            self.do_rpcrequest('DeleteDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    def delete_file_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            self.do_rpcrequest('DeleteFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_meta_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            self.do_rpcrequest('DeleteProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def fuzzy_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            self.do_rpcrequest('FuzzyQuery', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fuzzy_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_query_with_options(request, runtime)

    def get_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            self.do_rpcrequest('GetBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_binding_with_options(request, runtime)

    def get_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            self.do_rpcrequest('GetDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    def get_file_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            self.do_rpcrequest('GetFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_meta_with_options(request, runtime)

    def get_file_signed_uriwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileSignedURIResponse(),
            self.do_rpcrequest('GetFileSignedURI', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file_signed_uri(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_signed_uriwith_options(request, runtime)

    def get_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            self.do_rpcrequest('GetProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    def index_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            self.do_rpcrequest('IndexFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def index_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.index_file_meta_with_options(request, runtime)

    def list_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            self.do_rpcrequest('ListBindings', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    def list_datasets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            self.do_rpcrequest('ListDatasets', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_datasets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    def list_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def resume_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBindingResponse(),
            self.do_rpcrequest('ResumeBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_binding_with_options(request, runtime)

    def simple_query_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query), 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            self.do_rpcrequest('SimpleQuery', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def simple_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.simple_query_with_options(request, runtime)

    def stop_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.StopBindingResponse(),
            self.do_rpcrequest('StopBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_binding_with_options(request, runtime)

    def update_dataset_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reset_items):
            request.reset_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reset_items, 'ResetItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            self.do_rpcrequest('UpdateDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    def update_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            self.do_rpcrequest('UpdateFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_file_meta_with_options(request, runtime)

    def update_project_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reset_items):
            request.reset_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reset_items, 'ResetItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)
