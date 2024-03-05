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

    def add_image_mosaic_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddImageMosaicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImageMosaic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddImageMosaicResponse(),
            self.call_api(params, req, runtime)
        )

    def add_image_mosaic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_image_mosaic_with_options(request, runtime)

    def add_story_files_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_story_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_story_files_with_options(request, runtime)

    def attach_ossbucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AttachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_ossbucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_ossbucket_with_options(request, runtime)

    def batch_delete_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchDeleteFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_file_meta_with_options(request, runtime)

    def batch_get_figure_cluster_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_figure_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_figure_cluster_with_options(request, runtime)

    def batch_get_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_file_meta_with_options(request, runtime)

    def compare_image_faces_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CompareImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CompareImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    def compare_image_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.compare_image_faces_with_options(request, runtime)

    def create_archive_file_inspection_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateArchiveFileInspectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArchiveFileInspectionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateArchiveFileInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_archive_file_inspection_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_archive_file_inspection_task_with_options(request, runtime)

    def create_batch_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_batch_with_options(request, runtime)

    def create_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    def create_compress_point_cloud_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCompressPointCloudTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.kdtree_option):
            request.kdtree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.octree_option):
            request.octree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not UtilClient.is_unset(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not UtilClient.is_unset(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCompressPointCloudTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCompressPointCloudTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_compress_point_cloud_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_compress_point_cloud_task_with_options(request, runtime)

    def create_customized_story_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCustomizedStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCustomizedStoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_customized_story(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_customized_story_with_options(request, runtime)

    def create_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    def create_faces_searching_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFacesSearchingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFacesSearchingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFacesSearchingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_faces_searching_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_faces_searching_task_with_options(request, runtime)

    def create_figure_clustering_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_figure_clustering_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clustering_task_with_options(request, runtime)

    def create_figure_clusters_merging_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.froms):
            request.froms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClustersMergingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClustersMergingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_figure_clusters_merging_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clusters_merging_task_with_options(request, runtime)

    def create_file_compression_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileCompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileCompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileCompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file_compression_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_file_compression_task_with_options(request, runtime)

    def create_file_uncompression_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileUncompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.selected_files):
            request.selected_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileUncompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileUncompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file_uncompression_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_file_uncompression_task_with_options(request, runtime)

    def create_image_moderation_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_moderation_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_moderation_task_with_options(request, runtime)

    def create_image_splicing_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.align):
            query['Align'] = request.align
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.margin):
            query['Margin'] = request.margin
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.padding):
            query['Padding'] = request.padding
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageSplicingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageSplicingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_splicing_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_splicing_task_with_options(request, runtime)

    def create_image_to_pdftask_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageToPDFTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageToPDFTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageToPDFTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_to_pdftask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_to_pdftask_with_options(request, runtime)

    def create_location_date_clustering_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateLocationDateClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.date_options):
            request.date_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.location_options):
            request.location_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not UtilClient.is_unset(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocationDateClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateLocationDateClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_location_date_clustering_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_location_date_clustering_task_with_options(request, runtime)

    def create_media_convert_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMediaConvertTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateMediaConvertTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_media_convert_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_media_convert_task_with_options(request, runtime)

    def create_office_conversion_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.first_page):
            query['FirstPage'] = request.first_page
        if not UtilClient.is_unset(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not UtilClient.is_unset(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not UtilClient.is_unset(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not UtilClient.is_unset(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not UtilClient.is_unset(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not UtilClient.is_unset(request.long_text):
            query['LongText'] = request.long_text
        if not UtilClient.is_unset(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not UtilClient.is_unset(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not UtilClient.is_unset(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not UtilClient.is_unset(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not UtilClient.is_unset(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not UtilClient.is_unset(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_office_conversion_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def create_similar_image_clustering_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateSimilarImageClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateSimilarImageClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_similar_image_clustering_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_similar_image_clustering_task_with_options(request, runtime)

    def create_story_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.address_shrink):
            body['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not UtilClient.is_unset(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not UtilClient.is_unset(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_story(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_story_with_options(request, runtime)

    def create_trigger_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    def create_video_label_classification_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoLabelClassificationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoLabelClassificationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoLabelClassificationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_video_label_classification_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_label_classification_task_with_options(request, runtime)

    def create_video_moderation_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_video_moderation_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_moderation_task_with_options(request, runtime)

    def delete_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_batch_with_options(request, runtime)

    def delete_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    def delete_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    def delete_file_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_meta_with_options(request, runtime)

    def delete_location_date_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_location_date_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_location_date_cluster_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def delete_story_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteStoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_story(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_story_with_options(request, runtime)

    def delete_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    def detach_ossbucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_ossbucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_ossbucket_with_options(request, runtime)

    def detect_image_bodies_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageBodiesResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_bodies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    def detect_image_cars_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCars',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCarsResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_cars(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cars_with_options(request, runtime)

    def detect_image_codes_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCodes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCodesResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_codes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_codes_with_options(request, runtime)

    def detect_image_cropping_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCropping',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCroppingResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_cropping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cropping_with_options(request, runtime)

    def detect_image_faces_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_faces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    def detect_image_labels_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_labels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_labels_with_options(request, runtime)

    def detect_image_score_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageScore',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageScoreResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_score(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_score_with_options(request, runtime)

    def detect_image_texts_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageTextsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTexts',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageTextsResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_image_texts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_image_texts_with_options(request, runtime)

    def detect_media_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMediaMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectMediaMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_media_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_media_meta_with_options(request, runtime)

    def detect_text_anomaly_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectTextAnomaly',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectTextAnomalyResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_text_anomaly(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_text_anomaly_with_options(request, runtime)

    def extract_document_text_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ExtractDocumentTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractDocumentText',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ExtractDocumentTextResponse(),
            self.call_api(params, req, runtime)
        )

    def extract_document_text(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_document_text_with_options(request, runtime)

    def fuzzy_query_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.FuzzyQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def fuzzy_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_query_with_options(request, runtime)

    def generate_video_playlist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateVideoPlaylistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.source_subtitles):
            request.source_subtitles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not UtilClient.is_unset(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not UtilClient.is_unset(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateVideoPlaylist',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateVideoPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_video_playlist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_video_playlist_with_options(request, runtime)

    def generate_weboffice_token_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not UtilClient.is_unset(request.filename):
            query['Filename'] = request.filename
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not UtilClient.is_unset(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_weboffice_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_weboffice_token_with_options(request, runtime)

    def get_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_batch_with_options(request, runtime)

    def get_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_binding_with_options(request, runtime)

    def get_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    def get_figure_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_figure_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_figure_cluster_with_options(request, runtime)

    def get_file_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_meta_with_options(request, runtime)

    def get_image_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_moderation_result_with_options(request, runtime)

    def get_ossbucket_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSBucketAttachment',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOSSBucketAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ossbucket_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ossbucket_attachment_with_options(request, runtime)

    def get_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    def get_story_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetStoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_story(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_story_with_options(request, runtime)

    def get_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    def get_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trigger_with_options(request, runtime)

    def get_video_label_classification_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoLabelClassificationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoLabelClassificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_label_classification_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_label_classification_result_with_options(request, runtime)

    def get_video_moderation_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_moderation_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_moderation_result_with_options(request, runtime)

    def index_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def index_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.index_file_meta_with_options(request, runtime)

    def list_batches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatches',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBatchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_batches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_batches_with_options(request, runtime)

    def list_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    def list_datasets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_datasets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    def list_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    def list_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    def list_tasks_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.task_types):
            request.task_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not UtilClient.is_unset(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    def list_triggers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_triggers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_triggers_with_options(request, runtime)

    def query_figure_clusters_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryFigureClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not UtilClient.is_unset(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFigureClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryFigureClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_figure_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_figure_clusters_with_options(request, runtime)

    def query_location_date_clusters_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryLocationDateClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not UtilClient.is_unset(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not UtilClient.is_unset(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocationDateClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryLocationDateClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_location_date_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_location_date_clusters_with_options(request, runtime)

    def query_similar_image_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimilarImageClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QuerySimilarImageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_similar_image_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_similar_image_clusters_with_options(request, runtime)

    def query_stories_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not UtilClient.is_unset(request.story_name):
            query['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not UtilClient.is_unset(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            query['StoryType'] = request.story_type
        if not UtilClient.is_unset(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryStoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_stories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_stories_with_options(request, runtime)

    def refresh_weboffice_token_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RefreshWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_weboffice_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    def remove_story_files_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RemoveStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RemoveStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_story_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_story_files_with_options(request, runtime)

    def resume_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_batch_with_options(request, runtime)

    def resume_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_trigger_with_options(request, runtime)

    def search_image_figure_cluster_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SearchImageFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SearchImageFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def search_image_figure_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_image_figure_cluster_with_options(request, runtime)

    def semantic_query_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SemanticQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.media_types):
            request.media_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SemanticQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SemanticQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def semantic_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.semantic_query_with_options(request, runtime)

    def simple_query_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not UtilClient.is_unset(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def simple_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.simple_query_with_options(request, runtime)

    def suspend_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_batch_with_options(request, runtime)

    def suspend_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_trigger_with_options(request, runtime)

    def update_batch_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def update_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_batch_with_options(request, runtime)

    def update_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    def update_figure_cluster_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_figure_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_figure_cluster_with_options(request, runtime)

    def update_file_meta_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def update_file_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_file_meta_with_options(request, runtime)

    def update_location_date_cluster_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateLocationDateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_id):
            query['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_location_date_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_location_date_cluster_with_options(request, runtime)

    def update_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def update_story_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_story(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_story_with_options(request, runtime)

    def update_trigger_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_trigger_with_options(request, runtime)
