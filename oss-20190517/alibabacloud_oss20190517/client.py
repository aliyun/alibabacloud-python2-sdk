# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_oss.client import Client as GatewayClientClient
from alibabacloud_oss20190517 import models as oss_20190517_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client = None  # type: SPIClient

    def __init__(self, config):
        super(Client, self).__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._endpoint_rule = ''

    def abort_bucket_worm(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_bucket_worm_with_options(bucket, headers, runtime)

    def abort_bucket_worm_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='AbortBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?worm',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AbortBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    def abort_multipart_upload(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_multipart_upload_with_options(bucket, key, request, headers, runtime)

    def abort_multipart_upload_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AbortMultipartUploadResponse(),
            self.execute(params, req, runtime)
        )

    def append_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.AppendObjectHeaders()
        return self.append_object_with_options(bucket, key, request, headers, runtime)

    def append_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.position):
            query['position'] = request.position
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cache_control):
            real_headers['Cache-Control'] = UtilClient.to_jsonstring(headers.cache_control)
        if not UtilClient.is_unset(headers.content_disposition):
            real_headers['Content-Disposition'] = UtilClient.to_jsonstring(headers.content_disposition)
        if not UtilClient.is_unset(headers.content_encoding):
            real_headers['Content-Encoding'] = UtilClient.to_jsonstring(headers.content_encoding)
        if not UtilClient.is_unset(headers.content_md5):
            real_headers['Content-MD5'] = UtilClient.to_jsonstring(headers.content_md5)
        if not UtilClient.is_unset(headers.expires):
            real_headers['Expires'] = UtilClient.to_jsonstring(headers.expires)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='AppendObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?append' % TeaConverter.to_unicode(key),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.AppendObjectResponse(),
            self.execute(params, req, runtime)
        )

    def complete_bucket_worm(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.complete_bucket_worm_with_options(bucket, request, headers, runtime)

    def complete_bucket_worm_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.worm_id):
            query['wormId'] = request.worm_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CompleteBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    def complete_multipart_upload(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.CompleteMultipartUploadHeaders()
        return self.complete_multipart_upload_with_options(bucket, key, request, headers, runtime)

    def complete_multipart_upload_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        body = {}
        if not UtilClient.is_unset(request.complete_multipart_upload):
            body['completeMultipartUpload'] = request.complete_multipart_upload
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.complete_all):
            real_headers['x-oss-complete-all'] = UtilClient.to_jsonstring(headers.complete_all)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CompleteMultipartUploadResponse(),
            self.execute(params, req, runtime)
        )

    def copy_object(self, bucket, key):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.CopyObjectHeaders()
        return self.copy_object_with_options(bucket, key, headers, runtime)

    def copy_object_with_options(self, bucket, key, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.copy_source):
            real_headers['x-oss-copy-source'] = UtilClient.to_jsonstring(headers.copy_source)
        if not UtilClient.is_unset(headers.copy_source_if_match):
            real_headers['x-oss-copy-source-if-match'] = UtilClient.to_jsonstring(headers.copy_source_if_match)
        if not UtilClient.is_unset(headers.copy_source_if_modified_since):
            real_headers['x-oss-copy-source-if-modified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_modified_since)
        if not UtilClient.is_unset(headers.copy_source_if_none_match):
            real_headers['x-oss-copy-source-if-none-match'] = UtilClient.to_jsonstring(headers.copy_source_if_none_match)
        if not UtilClient.is_unset(headers.copy_source_if_unmodified_since):
            real_headers['x-oss-copy-source-if-unmodified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_unmodified_since)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.metadata_directive):
            real_headers['x-oss-metadata-directive'] = UtilClient.to_jsonstring(headers.metadata_directive)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        if not UtilClient.is_unset(headers.tagging_directive):
            real_headers['x-oss-tagging-directive'] = UtilClient.to_jsonstring(headers.tagging_directive)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='CopyObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.CopyObjectResponse(),
            self.execute(params, req, runtime)
        )

    def create_select_object_meta(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_select_object_meta_with_options(bucket, key, request, headers, runtime)

    def create_select_object_meta_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.select_meta_request))
        )
        params = open_api_models.Params(
            action='CreateSelectObjectMeta',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_20190517_models.CreateSelectObjectMetaResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_with_options(bucket, headers, runtime)

    def delete_bucket_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucket',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_cors(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_cors_with_options(bucket, headers, runtime)

    def delete_bucket_cors_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?cors',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketCorsResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_encryption(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_encryption_with_options(bucket, headers, runtime)

    def delete_bucket_encryption_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?encryption',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_inventory(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_inventory_with_options(bucket, request, headers, runtime)

    def delete_bucket_inventory_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?inventory',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_lifecycle(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_lifecycle_with_options(bucket, headers, runtime)

    def delete_bucket_lifecycle_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?lifecycle',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketLifecycleResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_logging(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_logging_with_options(bucket, headers, runtime)

    def delete_bucket_logging_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_policy(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_policy_with_options(bucket, headers, runtime)

    def delete_bucket_policy_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_replication(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_replication_with_options(bucket, request, headers, runtime)

    def delete_bucket_replication_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='DeleteBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?replication&comp=delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketReplicationResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_tags(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_tags_with_options(bucket, headers, runtime)

    def delete_bucket_tags_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?tagging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketTagsResponse(),
            self.execute(params, req, runtime)
        )

    def delete_bucket_website(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_bucket_website_with_options(bucket, headers, runtime)

    def delete_bucket_website_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?website',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteBucketWebsiteResponse(),
            self.execute(params, req, runtime)
        )

    def delete_live_channel(self, bucket, channel):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_live_channel_with_options(bucket, channel, headers, runtime)

    def delete_live_channel_with_options(self, bucket, channel, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?live' % TeaConverter.to_unicode(channel),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteLiveChannelResponse(),
            self.execute(params, req, runtime)
        )

    def delete_multiple_objects(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_multiple_objects_with_options(bucket, request, headers, runtime)

    def delete_multiple_objects_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.delete))
        )
        params = open_api_models.Params(
            action='DeleteMultipleObjects',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteMultipleObjectsResponse(),
            self.execute(params, req, runtime)
        )

    def delete_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_object_with_options(bucket, key, request, headers, runtime)

    def delete_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteObjectResponse(),
            self.execute(params, req, runtime)
        )

    def delete_object_tagging(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_object_tagging_with_options(bucket, key, request, headers, runtime)

    def delete_object_tagging_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?tagging' % TeaConverter.to_unicode(key),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DeleteObjectTaggingResponse(),
            self.execute(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    def describe_regions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.regions):
            query['regions'] = request.regions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.DescribeRegionsResponse(),
            self.execute(params, req, runtime)
        )

    def extend_bucket_worm(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.extend_bucket_worm_with_options(bucket, request, headers, runtime)

    def extend_bucket_worm_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.worm_id):
            query['wormId'] = request.worm_id
        body = {}
        if not UtilClient.is_unset(request.extend_worm_configuration):
            body['extendWormConfiguration'] = request.extend_worm_configuration
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?wormExtend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ExtendBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_acl(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_acl_with_options(bucket, headers, runtime)

    def get_bucket_acl_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketAclResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_cors(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_cors_with_options(bucket, headers, runtime)

    def get_bucket_cors_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?cors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketCorsResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_encryption(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_encryption_with_options(bucket, headers, runtime)

    def get_bucket_encryption_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?encryption',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_info(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_info_with_options(bucket, headers, runtime)

    def get_bucket_info_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketInfo',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?bucketInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketInfoResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_inventory(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_inventory_with_options(bucket, request, headers, runtime)

    def get_bucket_inventory_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?inventory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_lifecycle(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_lifecycle_with_options(bucket, headers, runtime)

    def get_bucket_lifecycle_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?lifecycle',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLifecycleResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_location(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_location_with_options(bucket, headers, runtime)

    def get_bucket_location_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLocation',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?location',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLocationResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_logging(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_logging_with_options(bucket, headers, runtime)

    def get_bucket_logging_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_policy(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_policy_with_options(bucket, headers, runtime)

    def get_bucket_policy_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_referer(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_referer_with_options(bucket, headers, runtime)

    def get_bucket_referer_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReferer',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?referer',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketRefererResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_replication(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_replication_with_options(bucket, headers, runtime)

    def get_bucket_replication_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?replication',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_replication_location(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_replication_location_with_options(bucket, headers, runtime)

    def get_bucket_replication_location_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketReplicationLocation',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?replicationLocation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationLocationResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_replication_progress(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_replication_progress_with_options(bucket, request, headers, runtime)

    def get_bucket_replication_progress_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['rule-id'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketReplicationProgress',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?replicationProgress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketReplicationProgressResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_request_payment(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_request_payment_with_options(bucket, headers, runtime)

    def get_bucket_request_payment_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketRequestPayment',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?requestPayment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketRequestPaymentResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_tags(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_tags_with_options(bucket, headers, runtime)

    def get_bucket_tags_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?tagging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketTagsResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_transfer_acceleration(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_transfer_acceleration_with_options(bucket, headers, runtime)

    def get_bucket_transfer_acceleration_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketTransferAcceleration',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?transferAcceleration',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_versioning(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_versioning_with_options(bucket, headers, runtime)

    def get_bucket_versioning_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketVersioning',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?versioning',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketVersioningResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_website(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_website_with_options(bucket, headers, runtime)

    def get_bucket_website_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?website',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketWebsiteResponse(),
            self.execute(params, req, runtime)
        )

    def get_bucket_worm(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bucket_worm_with_options(bucket, headers, runtime)

    def get_bucket_worm_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?worm',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    def get_live_channel_history(self, bucket, channel):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_live_channel_history_with_options(bucket, channel, headers, runtime)

    def get_live_channel_history_with_options(self, bucket, channel, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelHistory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?live&comp=history' % TeaConverter.to_unicode(channel),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelHistoryResponse(),
            self.execute(params, req, runtime)
        )

    def get_live_channel_info(self, bucket, channel):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_live_channel_info_with_options(bucket, channel, headers, runtime)

    def get_live_channel_info_with_options(self, bucket, channel, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelInfo',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?live' % TeaConverter.to_unicode(channel),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelInfoResponse(),
            self.execute(params, req, runtime)
        )

    def get_live_channel_stat(self, bucket, channel):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_live_channel_stat_with_options(bucket, channel, headers, runtime)

    def get_live_channel_stat_with_options(self, bucket, channel, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLiveChannelStat',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?live&comp=stat' % TeaConverter.to_unicode(channel),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetLiveChannelStatResponse(),
            self.execute(params, req, runtime)
        )

    def get_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.GetObjectHeaders()
        return self.get_object_with_options(bucket, key, request, headers, runtime)

    def get_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.response_cache_control):
            query['response-cache-control'] = request.response_cache_control
        if not UtilClient.is_unset(request.response_content_disposition):
            query['response-content-disposition'] = request.response_content_disposition
        if not UtilClient.is_unset(request.response_content_encoding):
            query['response-content-encoding'] = request.response_content_encoding
        if not UtilClient.is_unset(request.response_content_language):
            query['response-content-language'] = request.response_content_language
        if not UtilClient.is_unset(request.response_content_type):
            query['response-content-type'] = request.response_content_type
        if not UtilClient.is_unset(request.response_expires):
            query['response-expires'] = request.response_expires
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.if_modified_since):
            real_headers['If-Modified-Since'] = UtilClient.to_jsonstring(headers.if_modified_since)
        if not UtilClient.is_unset(headers.if_none_match):
            real_headers['If-None-Match'] = UtilClient.to_jsonstring(headers.if_none_match)
        if not UtilClient.is_unset(headers.if_unmodified_since):
            real_headers['If-Unmodified-Since'] = UtilClient.to_jsonstring(headers.if_unmodified_since)
        if not UtilClient.is_unset(headers.range):
            real_headers['Range'] = UtilClient.to_jsonstring(headers.range)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectResponse(),
            self.execute(params, req, runtime)
        )

    def get_object_acl(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_object_acl_with_options(bucket, key, request, headers, runtime)

    def get_object_acl_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?acl' % TeaConverter.to_unicode(key),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectAclResponse(),
            self.execute(params, req, runtime)
        )

    def get_object_meta(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_object_meta_with_options(bucket, key, request, headers, runtime)

    def get_object_meta_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectMeta',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?objectMeta' % TeaConverter.to_unicode(key),
            method='HEAD',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectMetaResponse(),
            self.execute(params, req, runtime)
        )

    def get_object_tagging(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_object_tagging_with_options(bucket, key, request, headers, runtime)

    def get_object_tagging_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?tagging' % TeaConverter.to_unicode(key),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetObjectTaggingResponse(),
            self.execute(params, req, runtime)
        )

    def get_symlink(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_symlink_with_options(bucket, key, request, headers, runtime)

    def get_symlink_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSymlink',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?symlink' % TeaConverter.to_unicode(key),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetSymlinkResponse(),
            self.execute(params, req, runtime)
        )

    def get_vod_playlist(self, bucket, channel, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vod_playlist_with_options(bucket, channel, request, headers, runtime)

    def get_vod_playlist_with_options(self, bucket, channel, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVodPlaylist',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?vod' % TeaConverter.to_unicode(channel),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.GetVodPlaylistResponse(),
            self.execute(params, req, runtime)
        )

    def head_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.HeadObjectHeaders()
        return self.head_object_with_options(bucket, key, request, headers, runtime)

    def head_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = UtilClient.to_jsonstring(headers.if_match)
        if not UtilClient.is_unset(headers.if_modified_since):
            real_headers['If-Modified-Since'] = UtilClient.to_jsonstring(headers.if_modified_since)
        if not UtilClient.is_unset(headers.if_none_match):
            real_headers['If-None-Match'] = UtilClient.to_jsonstring(headers.if_none_match)
        if not UtilClient.is_unset(headers.if_unmodified_since):
            real_headers['If-Unmodified-Since'] = UtilClient.to_jsonstring(headers.if_unmodified_since)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HeadObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='HEAD',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.HeadObjectResponse(),
            self.execute(params, req, runtime)
        )

    def initiate_bucket_worm(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initiate_bucket_worm_with_options(bucket, request, headers, runtime)

    def initiate_bucket_worm_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.initiate_worm_configuration))
        )
        params = open_api_models.Params(
            action='InitiateBucketWorm',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?worm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.InitiateBucketWormResponse(),
            self.execute(params, req, runtime)
        )

    def initiate_multipart_upload(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.InitiateMultipartUploadHeaders()
        return self.initiate_multipart_upload_with_options(bucket, key, request, headers, runtime)

    def initiate_multipart_upload_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cache_control):
            real_headers['Cache-Control'] = UtilClient.to_jsonstring(headers.cache_control)
        if not UtilClient.is_unset(headers.content_disposition):
            real_headers['Content-Disposition'] = UtilClient.to_jsonstring(headers.content_disposition)
        if not UtilClient.is_unset(headers.content_encoding):
            real_headers['Content-Encoding'] = UtilClient.to_jsonstring(headers.content_encoding)
        if not UtilClient.is_unset(headers.expires):
            real_headers['Expires'] = UtilClient.to_jsonstring(headers.expires)
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.sse_data_encryption):
            real_headers['x-oss-server-side-data-encryption'] = UtilClient.to_jsonstring(headers.sse_data_encryption)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitiateMultipartUpload',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?uploads' % TeaConverter.to_unicode(key),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.InitiateMultipartUploadResponse(),
            self.execute(params, req, runtime)
        )

    def list_bucket_inventory(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_bucket_inventory_with_options(bucket, request, headers, runtime)

    def list_bucket_inventory_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.continuation_token):
            query['continuation-token'] = request.continuation_token
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?inventory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    def list_buckets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_buckets_with_options(request, headers, runtime)

    def list_buckets_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBuckets',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListBucketsResponse(),
            self.execute(params, req, runtime)
        )

    def list_live_channel(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_live_channel_with_options(bucket, request, headers, runtime)

    def list_live_channel_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?live',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListLiveChannelResponse(),
            self.execute(params, req, runtime)
        )

    def list_multipart_uploads(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_multipart_uploads_with_options(bucket, request, headers, runtime)

    def list_multipart_uploads_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.key_marker):
            query['key-marker'] = request.key_marker
        if not UtilClient.is_unset(request.max_uploads):
            query['max-uploads'] = request.max_uploads
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.upload_id_marker):
            query['upload-id-marker'] = request.upload_id_marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultipartUploads',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?uploads',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListMultipartUploadsResponse(),
            self.execute(params, req, runtime)
        )

    def list_object_versions(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_object_versions_with_options(bucket, request, headers, runtime)

    def list_object_versions_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.key_marker):
            query['key-marker'] = request.key_marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.version_id_marker):
            query['version-id-marker'] = request.version_id_marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectVersions',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectVersionsResponse(),
            self.execute(params, req, runtime)
        )

    def list_objects(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_objects_with_options(bucket, request, headers, runtime)

    def list_objects_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjects',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectsResponse(),
            self.execute(params, req, runtime)
        )

    def list_objects_v2(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_objects_v2with_options(bucket, request, headers, runtime)

    def list_objects_v2with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.continuation_token):
            query['continuation-token'] = request.continuation_token
        if not UtilClient.is_unset(request.delimiter):
            query['delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['encoding-type'] = request.encoding_type
        if not UtilClient.is_unset(request.fetch_owner):
            query['fetch-owner'] = request.fetch_owner
        if not UtilClient.is_unset(request.max_keys):
            query['max-keys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_after):
            query['start-after'] = request.start_after
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectsV2',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?list-type=2',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListObjectsV2Response(),
            self.execute(params, req, runtime)
        )

    def list_parts(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parts_with_options(bucket, key, request, headers, runtime)

    def list_parts_with_options(self, bucket, key, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        host_map = {}
        host_map['bucket'] = bucket
        request = oss_20190517_models.ListPartsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.encoding_type):
            request.encoding_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.encoding_type, 'encoding-type', 'json')
        query = {}
        if not UtilClient.is_unset(request.encoding_type_shrink):
            query['encoding-type'] = request.encoding_type_shrink
        if not UtilClient.is_unset(request.max_parts):
            query['max-parts'] = request.max_parts
        if not UtilClient.is_unset(request.part_number_marker):
            query['part-number-marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParts',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.ListPartsResponse(),
            self.execute(params, req, runtime)
        )

    def option_object(self, bucket, key):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.OptionObjectHeaders()
        return self.option_object_with_options(bucket, key, headers, runtime)

    def option_object_with_options(self, bucket, key, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.access_control_request_headers):
            real_headers['Access-Control-Request-Headers'] = UtilClient.to_jsonstring(headers.access_control_request_headers)
        if not UtilClient.is_unset(headers.access_control_request_method):
            real_headers['Access-Control-Request-Method'] = UtilClient.to_jsonstring(headers.access_control_request_method)
        if not UtilClient.is_unset(headers.origin):
            real_headers['Origin'] = UtilClient.to_jsonstring(headers.origin)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='OptionObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='OPTIONS',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.OptionObjectResponse(),
            self.execute(params, req, runtime)
        )

    def post_object(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_object_with_options(bucket, headers, runtime)

    def post_object_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='PostObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='multiFormData',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PostObjectResponse(),
            self.execute(params, req, runtime)
        )

    def post_vod_playlist(self, bucket, channel, playlist, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_vod_playlist_with_options(bucket, channel, playlist, request, headers, runtime)

    def post_vod_playlist_with_options(self, bucket, channel, playlist, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PostVodPlaylist',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s/%s?vod' % (TeaConverter.to_unicode(channel), TeaConverter.to_unicode(playlist)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PostVodPlaylistResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutBucketHeaders()
        return self.put_bucket_with_options(bucket, request, headers, runtime)

    def put_bucket_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.create_bucket_configuration))
        )
        params = open_api_models.Params(
            action='PutBucket',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_acl(self, bucket):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutBucketAclHeaders()
        return self.put_bucket_acl_with_options(bucket, headers, runtime)

    def put_bucket_acl_with_options(self, bucket, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='PutBucketAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?acl',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketAclResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_cors(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_cors_with_options(bucket, request, headers, runtime)

    def put_bucket_cors_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.c_orsconfiguration))
        )
        params = open_api_models.Params(
            action='PutBucketCors',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?cors',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketCorsResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_encryption(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_encryption_with_options(bucket, request, headers, runtime)

    def put_bucket_encryption_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.server_side_encryption_rule))
        )
        params = open_api_models.Params(
            action='PutBucketEncryption',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?encryption',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketEncryptionResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_inventory(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_inventory_with_options(bucket, request, headers, runtime)

    def put_bucket_inventory_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.inventory_id):
            query['inventoryId'] = request.inventory_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.inventory_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketInventory',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?inventory',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketInventoryResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_lifecycle(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_lifecycle_with_options(bucket, request, headers, runtime)

    def put_bucket_lifecycle_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.lifecycle_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketLifecycle',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?lifecycle',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketLifecycleResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_logging(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_logging_with_options(bucket, request, headers, runtime)

    def put_bucket_logging_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.bucket_logging_status))
        )
        params = open_api_models.Params(
            action='PutBucketLogging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_policy(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_policy_with_options(bucket, request, headers, runtime)

    def put_bucket_policy_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.policy
        )
        params = open_api_models.Params(
            action='PutBucketPolicy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?policy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_referer(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_referer_with_options(bucket, request, headers, runtime)

    def put_bucket_referer_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.referer_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketReferer',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?referer',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketRefererResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_replication(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_replication_with_options(bucket, request, headers, runtime)

    def put_bucket_replication_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.replication_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketReplication',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?replication&comp=add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketReplicationResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_request_payment(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_request_payment_with_options(bucket, request, headers, runtime)

    def put_bucket_request_payment_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.request_payment_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketRequestPayment',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?requestPayment',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketRequestPaymentResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_tags(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_tags_with_options(bucket, request, headers, runtime)

    def put_bucket_tags_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.tagging))
        )
        params = open_api_models.Params(
            action='PutBucketTags',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?tagging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketTagsResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_transfer_acceleration(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_transfer_acceleration_with_options(bucket, request, headers, runtime)

    def put_bucket_transfer_acceleration_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.transfer_acceleration_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketTransferAcceleration',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?transferAcceleration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_versioning(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_versioning_with_options(bucket, request, headers, runtime)

    def put_bucket_versioning_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.versioning_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketVersioning',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?versioning',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketVersioningResponse(),
            self.execute(params, req, runtime)
        )

    def put_bucket_website(self, bucket, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_bucket_website_with_options(bucket, request, headers, runtime)

    def put_bucket_website_with_options(self, bucket, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.website_configuration))
        )
        params = open_api_models.Params(
            action='PutBucketWebsite',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/?website',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutBucketWebsiteResponse(),
            self.execute(params, req, runtime)
        )

    def put_live_channel(self, bucket, channel, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_live_channel_with_options(bucket, channel, request, headers, runtime)

    def put_live_channel_with_options(self, bucket, channel, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.live_channel_configuration))
        )
        params = open_api_models.Params(
            action='PutLiveChannel',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?live' % TeaConverter.to_unicode(channel),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutLiveChannelResponse(),
            self.execute(params, req, runtime)
        )

    def put_live_channel_status(self, bucket, channel, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_live_channel_status_with_options(bucket, channel, request, headers, runtime)

    def put_live_channel_status_with_options(self, bucket, channel, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLiveChannelStatus',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?live' % TeaConverter.to_unicode(channel),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutLiveChannelStatusResponse(),
            self.execute(params, req, runtime)
        )

    def put_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutObjectHeaders()
        return self.put_object_with_options(bucket, key, request, headers, runtime)

    def put_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.meta_data):
            real_headers['x-oss-meta-*'] = UtilClient.to_jsonstring(headers.meta_data)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.sse_data_encryption):
            real_headers['x-oss-server-side-data-encryption'] = UtilClient.to_jsonstring(headers.sse_data_encryption)
        if not UtilClient.is_unset(headers.server_side_encryption):
            real_headers['x-oss-server-side-encryption'] = UtilClient.to_jsonstring(headers.server_side_encryption)
        if not UtilClient.is_unset(headers.sse_key_id):
            real_headers['x-oss-server-side-encryption-key-id'] = UtilClient.to_jsonstring(headers.sse_key_id)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.tagging):
            real_headers['x-oss-tagging'] = UtilClient.to_jsonstring(headers.tagging)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='PutObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='none'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectResponse(),
            self.execute(params, req, runtime)
        )

    def put_object_acl(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutObjectAclHeaders()
        return self.put_object_acl_with_options(bucket, key, request, headers, runtime)

    def put_object_acl_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutObjectAcl',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?acl' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectAclResponse(),
            self.execute(params, req, runtime)
        )

    def put_object_tagging(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_object_tagging_with_options(bucket, key, request, headers, runtime)

    def put_object_tagging_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.tagging))
        )
        params = open_api_models.Params(
            action='PutObjectTagging',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?tagging' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutObjectTaggingResponse(),
            self.execute(params, req, runtime)
        )

    def put_symlink(self, bucket, key):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.PutSymlinkHeaders()
        return self.put_symlink_with_options(bucket, key, headers, runtime)

    def put_symlink_with_options(self, bucket, key, headers, runtime):
        host_map = {}
        host_map['bucket'] = bucket
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.forbid_overwrite):
            real_headers['x-oss-forbid-overwrite'] = UtilClient.to_jsonstring(headers.forbid_overwrite)
        if not UtilClient.is_unset(headers.acl):
            real_headers['x-oss-object-acl'] = UtilClient.to_jsonstring(headers.acl)
        if not UtilClient.is_unset(headers.storage_class):
            real_headers['x-oss-storage-class'] = UtilClient.to_jsonstring(headers.storage_class)
        if not UtilClient.is_unset(headers.symlink_target_key):
            real_headers['x-oss-symlink-target'] = UtilClient.to_jsonstring(headers.symlink_target_key)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers
        )
        params = open_api_models.Params(
            action='PutSymlink',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?symlink' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.PutSymlinkResponse(),
            self.execute(params, req, runtime)
        )

    def restore_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_object_with_options(bucket, key, request, headers, runtime)

    def restore_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.restore_request))
        )
        params = open_api_models.Params(
            action='RestoreObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s?restore' % TeaConverter.to_unicode(key),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.RestoreObjectResponse(),
            self.execute(params, req, runtime)
        )

    def select_object(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.select_object_with_options(bucket, key, request, headers, runtime)

    def select_object_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.select_request))
        )
        params = open_api_models.Params(
            action='SelectObject',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='binary'
        )
        return TeaCore.from_map(
            oss_20190517_models.SelectObjectResponse(),
            self.execute(params, req, runtime)
        )

    def upload_part(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_part_with_options(bucket, key, request, headers, runtime)

    def upload_part_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.part_number):
            query['partNumber'] = request.part_number
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='UploadPart',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='binary',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.UploadPartResponse(),
            self.execute(params, req, runtime)
        )

    def upload_part_copy(self, bucket, key, request):
        runtime = util_models.RuntimeOptions()
        headers = oss_20190517_models.UploadPartCopyHeaders()
        return self.upload_part_copy_with_options(bucket, key, request, headers, runtime)

    def upload_part_copy_with_options(self, bucket, key, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['bucket'] = bucket
        query = {}
        if not UtilClient.is_unset(request.part_number):
            query['partNumber'] = request.part_number
        if not UtilClient.is_unset(request.upload_id):
            query['uploadId'] = request.upload_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.copy_source):
            real_headers['x-oss-copy-source'] = UtilClient.to_jsonstring(headers.copy_source)
        if not UtilClient.is_unset(headers.copy_source_if_match):
            real_headers['x-oss-copy-source-if-match'] = UtilClient.to_jsonstring(headers.copy_source_if_match)
        if not UtilClient.is_unset(headers.copy_source_if_modified_since):
            real_headers['x-oss-copy-source-if-modified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_modified_since)
        if not UtilClient.is_unset(headers.copy_source_if_none_match):
            real_headers['x-oss-copy-source-if-none-match'] = UtilClient.to_jsonstring(headers.copy_source_if_none_match)
        if not UtilClient.is_unset(headers.copy_source_if_unmodified_since):
            real_headers['x-oss-copy-source-if-unmodified-since'] = UtilClient.to_jsonstring(headers.copy_source_if_unmodified_since)
        if not UtilClient.is_unset(headers.copy_source_range):
            real_headers['x-oss-copy-source-range'] = UtilClient.to_jsonstring(headers.copy_source_range)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPartCopy',
            version='2019-05-17',
            protocol='HTTPS',
            pathname='/%s' % TeaConverter.to_unicode(key),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            oss_20190517_models.UploadPartCopyResponse(),
            self.execute(params, req, runtime)
        )
