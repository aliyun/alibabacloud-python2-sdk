# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_amqp_open20191212 import models as amqp_open_20191212_models
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
        self._endpoint = self.get_endpoint('amqp-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_account_with_options(self, request, runtime):
        """
        

        @param request: CreateAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_access_key):
            query['accountAccessKey'] = request.account_access_key
        if not UtilClient.is_unset(request.create_timestamp):
            query['createTimestamp'] = request.create_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_sign):
            query['secretSign'] = request.secret_sign
        if not UtilClient.is_unset(request.signature):
            query['signature'] = request.signature
        if not UtilClient.is_unset(request.user_name):
            query['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account(self, request):
        """
        

        @param request: CreateAccountRequest

        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.argument):
            body['Argument'] = request.argument
        if not UtilClient.is_unset(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            body['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    def create_exchange_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alternate_exchange):
            body['AlternateExchange'] = request.alternate_exchange
        if not UtilClient.is_unset(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not UtilClient.is_unset(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['ExchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.internal):
            body['Internal'] = request.internal
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExchange',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_exchange(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_exchange_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_connections):
            query['MaxConnections'] = request.max_connections
        if not UtilClient.is_unset(request.max_eip_tps):
            query['MaxEipTps'] = request.max_eip_tps
        if not UtilClient.is_unset(request.max_private_tps):
            query['MaxPrivateTps'] = request.max_private_tps
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_cycle):
            query['PeriodCycle'] = request.period_cycle
        if not UtilClient.is_unset(request.queue_capacity):
            query['QueueCapacity'] = request.queue_capacity
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.renewal_duration_unit):
            query['RenewalDurationUnit'] = request.renewal_duration_unit
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.support_eip):
            query['SupportEip'] = request.support_eip
        if not UtilClient.is_unset(request.support_tracing):
            query['SupportTracing'] = request.support_tracing
        if not UtilClient.is_unset(request.tracing_storage_time):
            query['TracingStorageTime'] = request.tracing_storage_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_delete_state):
            body['AutoDeleteState'] = request.auto_delete_state
        if not UtilClient.is_unset(request.auto_expire_state):
            body['AutoExpireState'] = request.auto_expire_state
        if not UtilClient.is_unset(request.dead_letter_exchange):
            body['DeadLetterExchange'] = request.dead_letter_exchange
        if not UtilClient.is_unset(request.dead_letter_routing_key):
            body['DeadLetterRoutingKey'] = request.dead_letter_routing_key
        if not UtilClient.is_unset(request.exclusive_state):
            body['ExclusiveState'] = request.exclusive_state
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_length):
            body['MaxLength'] = request.max_length
        if not UtilClient.is_unset(request.maximum_priority):
            body['MaximumPriority'] = request.maximum_priority
        if not UtilClient.is_unset(request.message_ttl):
            body['MessageTTL'] = request.message_ttl
        if not UtilClient.is_unset(request.queue_name):
            body['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def create_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    def create_virtual_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualHost',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.CreateVirtualHostResponse(),
            self.call_api(params, req, runtime)
        )

    def create_virtual_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_host_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_timestamp):
            query['CreateTimestamp'] = request.create_timestamp
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.binding_key):
            body['BindingKey'] = request.binding_key
        if not UtilClient.is_unset(request.binding_type):
            body['BindingType'] = request.binding_type
        if not UtilClient.is_unset(request.destination_name):
            body['DestinationName'] = request.destination_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.source_exchange):
            body['SourceExchange'] = request.source_exchange
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    def delete_exchange_with_options(self, request, runtime):
        """
        ## [](#)Usage notes
        *   You cannot delete exchanges of the **headers** and **x-jms-topic** types.
        *   You cannot delete built-in exchanges in a vhost. These exchanges are amq.direct, amq.topic, and amq.fanout.
        

        @param request: DeleteExchangeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteExchangeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exchange_name):
            body['ExchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExchange',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteExchangeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_exchange(self, request):
        """
        ## [](#)Usage notes
        *   You cannot delete exchanges of the **headers** and **x-jms-topic** types.
        *   You cannot delete built-in exchanges in a vhost. These exchanges are amq.direct, amq.topic, and amq.fanout.
        

        @param request: DeleteExchangeRequest

        @return: DeleteExchangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_exchange_with_options(request, runtime)

    def delete_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.queue_name):
            body['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    def delete_virtual_host_with_options(self, request, runtime):
        """
        Before you delete a vhost, make sure that all exchanges and queues in the vhost are deleted.
        

        @param request: DeleteVirtualHostRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVirtualHostResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.virtual_host):
            body['VirtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualHost',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.DeleteVirtualHostResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_virtual_host(self, request):
        """
        Before you delete a vhost, make sure that all exchanges and queues in the vhost are deleted.
        

        @param request: DeleteVirtualHostRequest

        @return: DeleteVirtualHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_host_with_options(request, runtime)

    def get_metadata_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetadataAmount',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.GetMetadataAmountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_metadata_amount(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_metadata_amount_with_options(request, runtime)

    def list_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    def list_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    def list_down_stream_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListDownStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_down_stream_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_down_stream_bindings_with_options(request, runtime)

    def list_exchange_up_stream_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchangeUpStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListExchangeUpStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_exchange_up_stream_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_exchange_up_stream_bindings_with_options(request, runtime)

    def list_exchanges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExchanges',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListExchangesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_exchanges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_exchanges_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_queue_consumers_with_options(self, request, runtime):
        """
        ApsaraMQ for RabbitMQ allows you to query only online consumers.
        

        @param request: ListQueueConsumersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListQueueConsumersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueConsumers',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueueConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_queue_consumers(self, request):
        """
        ApsaraMQ for RabbitMQ allows you to query only online consumers.
        

        @param request: ListQueueConsumersRequest

        @return: ListQueueConsumersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queue_consumers_with_options(request, runtime)

    def list_queue_up_stream_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueueUpStreamBindings',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueueUpStreamBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_queue_up_stream_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_queue_up_stream_bindings_with_options(request, runtime)

    def list_queues_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_queues(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    def list_virtual_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualHosts',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.ListVirtualHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_virtual_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_hosts_with_options(request, runtime)

    def update_instance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2019-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amqp_open_20191212_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_name_with_options(request, runtime)
