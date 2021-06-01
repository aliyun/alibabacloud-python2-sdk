# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_snapshot20210315 import models as snapshot_20210315_models
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
        self._endpoint = self.get_endpoint('snapshot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_snapshot_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_info_with_options(request, headers, runtime)

    def get_snapshot_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            snapshot_20210315_models.GetSnapshotInfoResponse(),
            self.do_roarequest('GetSnapshotInfo', '2021-03-15', 'HTTPS', 'GET', 'AK', '/snapshots/info', 'json', req, runtime)
        )

    def get_snapshot_block(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_block_with_options(request, headers, runtime)

    def get_snapshot_block_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.block_index):
            query['BlockIndex'] = request.block_index
        if not UtilClient.is_unset(request.block_token):
            query['BlockToken'] = request.block_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        res = snapshot_20210315_models.GetSnapshotBlockResponse()
        tmp = UtilClient.assert_as_map(self.do_roarequest('GetSnapshotBlock', '2021-03-15', 'HTTPS', 'GET', 'AK', '/snapshots/block', 'binary', req, runtime))
        if not UtilClient.is_unset(tmp.get('body')):
            resp_body = UtilClient.assert_as_readable(tmp.get('body'))
            res.body = resp_body
        if not UtilClient.is_unset(tmp.get('headers')):
            resp_headers = UtilClient.assert_as_map(tmp.get('headers'))
            res.headers = UtilClient.stringify_map_value(resp_headers)
        return res

    def list_snapshot_blocks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshot_blocks_with_options(request, headers, runtime)

    def list_snapshot_blocks_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.starting_block_index):
            query['StartingBlockIndex'] = request.starting_block_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            snapshot_20210315_models.ListSnapshotBlocksResponse(),
            self.do_roarequest('ListSnapshotBlocks', '2021-03-15', 'HTTPS', 'GET', 'AK', '/snapshots/listblocks', 'json', req, runtime)
        )

    def list_changed_blocks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_changed_blocks_with_options(request, headers, runtime)

    def list_changed_blocks_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.first_snapshot_id):
            query['FirstSnapshotId'] = request.first_snapshot_id
        if not UtilClient.is_unset(request.second_snapshot_id):
            query['SecondSnapshotId'] = request.second_snapshot_id
        if not UtilClient.is_unset(request.starting_block_index):
            query['StartingBlockIndex'] = request.starting_block_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            snapshot_20210315_models.ListChangedBlocksResponse(),
            self.do_roarequest('ListChangedBlocks', '2021-03-15', 'HTTPS', 'GET', 'AK', '/snapshots/changedblocks', 'json', req, runtime)
        )
