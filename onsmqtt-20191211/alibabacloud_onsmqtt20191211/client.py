# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_onsmqtt20191211 import models as ons_mqtt_20191211_models
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
        self._endpoint = self.get_endpoint('onsmqtt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actions):
            query['Actions'] = request.actions
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyToken',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.ApplyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_token_with_options(request, runtime)

    def batch_query_session_by_client_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQuerySessionByClientIds',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.BatchQuerySessionByClientIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_query_session_by_client_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_query_session_by_client_ids_with_options(request, runtime)

    def batch_send_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.messages):
            query['Messages'] = request.messages
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSendMessages',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.BatchSendMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_send_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_send_messages_with_options(request, runtime)

    def create_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupId',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.CreateGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_id_with_options(request, runtime)

    def delete_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupId',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.DeleteGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_id_with_options(request, runtime)

    def list_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupId',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.ListGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_id_with_options(request, runtime)

    def query_session_by_client_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySessionByClientId',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.QuerySessionByClientIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_session_by_client_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_session_by_client_id_with_options(request, runtime)

    def query_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryToken',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.QueryTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def query_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_token_with_options(request, runtime)

    def revoke_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeToken',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.RevokeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_token_with_options(request, runtime)

    def send_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mqtt_topic):
            query['MqttTopic'] = request.mqtt_topic
        if not UtilClient.is_unset(request.payload):
            query['Payload'] = request.payload
        if not UtilClient.is_unset(request.receipt_id):
            query['ReceiptId'] = request.receipt_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2019-12-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ons_mqtt_20191211_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)
