# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mns_open20220119 import models as mns_open_20220119_models
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
        self._endpoint = self.get_endpoint('mns-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not UtilClient.is_unset(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not UtilClient.is_unset(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def create_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    def create_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_logging):
            body['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.max_message_size):
            body['MaxMessageSize'] = request.max_message_size
        if not UtilClient.is_unset(request.topic_name):
            body['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def create_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    def delete_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    def delete_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    def get_queue_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.GetQueueAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_queue_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_queue_attributes_with_options(request, runtime)

    def get_subscription_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.GetSubscriptionAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subscription_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_attributes_with_options(request, runtime)

    def get_topic_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.GetTopicAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_topic_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_attributes_with_options(request, runtime)

    def list_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.ListQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def list_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_queue_with_options(request, runtime)

    def list_subscription_by_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionByTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.ListSubscriptionByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subscription_by_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_subscription_by_topic_with_options(request, runtime)

    def list_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.ListTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def list_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_topic_with_options(request, runtime)

    def set_queue_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not UtilClient.is_unset(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not UtilClient.is_unset(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQueueAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.SetQueueAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_queue_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_queue_attributes_with_options(request, runtime)

    def set_subscription_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSubscriptionAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.SetSubscriptionAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_subscription_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_subscription_attributes_with_options(request, runtime)

    def set_topic_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.max_message_size):
            query['MaxMessageSize'] = request.max_message_size
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTopicAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.SetTopicAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_topic_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_topic_attributes_with_options(request, runtime)

    def subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.message_tag):
            query['MessageTag'] = request.message_tag
        if not UtilClient.is_unset(request.notify_content_format):
            query['NotifyContentFormat'] = request.notify_content_format
        if not UtilClient.is_unset(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Subscribe',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.SubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.subscribe_with_options(request, runtime)

    def unsubscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Unsubscribe',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mns_open_20220119_models.UnsubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def unsubscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_with_options(request, runtime)
