# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdt20210813 import models as cdt20210813_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_cdt_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtServiceStatusResponse(),
            self.do_rpcrequest('GetCdtServiceStatus', '2021-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cdt_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cdt_service_status_with_options(request, runtime)

    def open_cdt_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtServiceResponse(),
            self.do_rpcrequest('OpenCdtService', '2021-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_cdt_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_cdt_service_with_options(request, runtime)

    def get_cdt_cb_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdt20210813_models.GetCdtCbServiceStatusResponse(),
            self.do_rpcrequest('GetCdtCbServiceStatus', '2021-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cdt_cb_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cdt_cb_service_status_with_options(request, runtime)

    def open_cdt_cb_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdt20210813_models.OpenCdtCbServiceResponse(),
            self.do_rpcrequest('OpenCdtCbService', '2021-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_cdt_cb_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_cdt_cb_service_with_options(request, runtime)
