# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_carbonfootprint20230711 import models as carbon_footprint_20230711_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('carbonfootprint', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allow_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Allow',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.AllowResponse(),
            self.call_api(params, req, runtime)
        )

    def allow(self):
        runtime = util_models.RuntimeOptions()
        return self.allow_with_options(runtime)

    def get_summary_data_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = carbon_footprint_20230711_models.GetSummaryDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uids):
            request.uids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uids, 'Uids', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uids_shrink):
            query['Uids'] = request.uids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSummaryData',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.GetSummaryDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_summary_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_summary_data_with_options(request, runtime)

    def query_carbon_track_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = carbon_footprint_20230711_models.QueryCarbonTrackShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uids):
            request.uids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uids, 'Uids', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_rdaccount):
            query['FilterRDAccount'] = request.filter_rdaccount
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        if not UtilClient.is_unset(request.uids_shrink):
            query['Uids'] = request.uids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCarbonTrack',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.QueryCarbonTrackResponse(),
            self.call_api(params, req, runtime)
        )

    def query_carbon_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_carbon_track_with_options(request, runtime)

    def query_multi_account_carbon_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMultiAccountCarbonTrack',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.QueryMultiAccountCarbonTrackResponse(),
            self.call_api(params, req, runtime)
        )

    def query_multi_account_carbon_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_multi_account_carbon_track_with_options(request, runtime)

    def verify_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Verify',
            version='2023-07-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            carbon_footprint_20230711_models.VerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def verify(self):
        runtime = util_models.RuntimeOptions()
        return self.verify_with_options(runtime)
