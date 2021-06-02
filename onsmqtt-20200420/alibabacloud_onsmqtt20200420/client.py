# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_onsmqtt20200420 import models as ons_mqtt_20200420_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ApplyTokenResponse(),
            self.do_rpcrequest('ApplyToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_token_with_options(request, runtime)

    def batch_query_session_by_client_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse(),
            self.do_rpcrequest('BatchQuerySessionByClientIds', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_query_session_by_client_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_query_session_by_client_ids_with_options(request, runtime)

    def create_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.CreateGroupIdResponse(),
            self.do_rpcrequest('CreateGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_id_with_options(request, runtime)

    def delete_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.DeleteGroupIdResponse(),
            self.do_rpcrequest('DeleteGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_id_with_options(request, runtime)

    def get_device_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.GetDeviceCredentialResponse(),
            self.do_rpcrequest('GetDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_credential_with_options(request, runtime)

    def list_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.ListGroupIdResponse(),
            self.do_rpcrequest('ListGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_id_with_options(request, runtime)

    def query_mqtt_trace_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceDeviceResponse(),
            self.do_rpcrequest('QueryMqttTraceDevice', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mqtt_trace_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_device_with_options(request, runtime)

    def query_mqtt_trace_message_of_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessageOfClientResponse(),
            self.do_rpcrequest('QueryMqttTraceMessageOfClient', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mqtt_trace_message_of_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_message_of_client_with_options(request, runtime)

    def query_mqtt_trace_message_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessagePublishResponse(),
            self.do_rpcrequest('QueryMqttTraceMessagePublish', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mqtt_trace_message_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_message_publish_with_options(request, runtime)

    def query_mqtt_trace_message_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryMqttTraceMessageSubscribeResponse(),
            self.do_rpcrequest('QueryMqttTraceMessageSubscribe', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mqtt_trace_message_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mqtt_trace_message_subscribe_with_options(request, runtime)

    def query_session_by_client_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QuerySessionByClientIdResponse(),
            self.do_rpcrequest('QuerySessionByClientId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_session_by_client_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_session_by_client_id_with_options(request, runtime)

    def query_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.QueryTokenResponse(),
            self.do_rpcrequest('QueryToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_token_with_options(request, runtime)

    def refresh_device_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RefreshDeviceCredentialResponse(),
            self.do_rpcrequest('RefreshDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_device_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_device_credential_with_options(request, runtime)

    def register_device_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RegisterDeviceCredentialResponse(),
            self.do_rpcrequest('RegisterDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_device_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_credential_with_options(request, runtime)

    def revoke_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.RevokeTokenResponse(),
            self.do_rpcrequest('RevokeToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_token_with_options(request, runtime)

    def send_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.SendMessageResponse(),
            self.do_rpcrequest('SendMessage', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    def un_register_device_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse(),
            self.do_rpcrequest('UnRegisterDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_register_device_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_register_device_credential_with_options(request, runtime)
