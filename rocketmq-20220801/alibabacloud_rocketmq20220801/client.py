# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rocketmq20220801 import models as rocket_mq20220801_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('rocketmq', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_resource_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    def create_consumer_group_with_options(self, instance_id, consumer_group_id, request, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: CreateConsumerGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not UtilClient.is_unset(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(consumer_group_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_consumer_group(self, instance_id, consumer_group_id, request):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: CreateConsumerGroupRequest

        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(instance_id, consumer_group_id, request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: CreateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_info):
            body['networkInfo'] = request.network_info
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['periodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.product_info):
            body['productInfo'] = request.product_info
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series_code):
            body['seriesCode'] = request.series_code
        if not UtilClient.is_unset(request.service_code):
            body['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.sub_series_code):
            body['subSeriesCode'] = request.sub_series_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: CreateInstanceRequest

        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def create_topic_with_options(self, instance_id, topic_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.message_type):
            body['messageType'] = request.message_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/topics/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(topic_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def create_topic(self, instance_id, topic_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_topic_with_options(instance_id, topic_name, request, headers, runtime)

    def delete_consumer_group_with_options(self, instance_id, consumer_group_id, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After you delete a consumer group, the consumer client associated with the consumer group cannot consume messages. Exercise caution when you call this operation.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConsumerGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(consumer_group_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_consumer_group(self, instance_id, consumer_group_id):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        After you delete a consumer group, the consumer client associated with the consumer group cannot consume messages. Exercise caution when you call this operation.
        

        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(instance_id, consumer_group_id, headers, runtime)

    def delete_instance_with_options(self, instance_id, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After an instance is deleted, the instance cannot be restored. Exercise caution when you call this operation.
        *   This operation is used to delete a pay-as-you-go instance. A subscription instance is automatically released after it expires. You do not need to manually delete a subscription instance.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, instance_id):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        *   After an instance is deleted, the instance cannot be restored. Exercise caution when you call this operation.
        *   This operation is used to delete a pay-as-you-go instance. A subscription instance is automatically released after it expires. You do not need to manually delete a subscription instance.
        

        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    def delete_topic_with_options(self, instance_id, topic_name, headers, runtime):
        """
        If you delete the topic, the publishing and subscription relationships that are established based on the topic are cleared. Exercise caution when you call this operation.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTopicResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/topics/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(topic_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_topic(self, instance_id, topic_name):
        """
        If you delete the topic, the publishing and subscription relationships that are established based on the topic are cleared. Exercise caution when you call this operation.
        

        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_topic_with_options(instance_id, topic_name, headers, runtime)

    def get_consumer_group_with_options(self, instance_id, consumer_group_id, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetConsumerGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(consumer_group_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_consumer_group(self, instance_id, consumer_group_id):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @return: GetConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_consumer_group_with_options(instance_id, consumer_group_id, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def get_topic_with_options(self, instance_id, topic_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/topics/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(topic_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.GetTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def get_topic(self, instance_id, topic_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_topic_with_options(instance_id, topic_name, headers, runtime)

    def list_consumer_group_subscriptions_with_options(self, instance_id, consumer_group_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroupSubscriptions',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups/%s/subscriptions' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(consumer_group_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerGroupSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_consumer_group_subscriptions(self, instance_id, consumer_group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_subscriptions_with_options(instance_id, consumer_group_id, headers, runtime)

    def list_consumer_groups_with_options(self, instance_id, request, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: ListConsumerGroupsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConsumerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumerGroups',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListConsumerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_consumer_groups(self, instance_id, request):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: ListConsumerGroupsRequest

        @return: ListConsumerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_groups_with_options(instance_id, request, headers, runtime)

    def list_instances_with_options(self, request, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: ListInstancesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: ListInstancesRequest

        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def list_topics_with_options(self, instance_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = rocket_mq20220801_models.ListTopicsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.message_types):
            request.message_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.message_types, 'messageTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.message_types_shrink):
            query['messageTypes'] = request.message_types_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopics',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/topics' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ListTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_topics(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_topics_with_options(instance_id, request, headers, runtime)

    def reset_consume_offset_with_options(self, instance_id, consumer_group_id, topic_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.reset_time):
            body['resetTime'] = request.reset_time
        if not UtilClient.is_unset(request.reset_type):
            body['resetType'] = request.reset_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetConsumeOffset',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups/%s/consumeOffsets/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(consumer_group_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(topic_name))),
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.ResetConsumeOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_consume_offset(self, instance_id, consumer_group_id, topic_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_consume_offset_with_options(instance_id, consumer_group_id, topic_name, request, headers, runtime)

    def update_consumer_group_with_options(self, instance_id, consumer_group_id, request, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: UpdateConsumerGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not UtilClient.is_unset(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/consumerGroups/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(consumer_group_id))),
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_consumer_group(self, instance_id, consumer_group_id, request):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: UpdateConsumerGroupRequest

        @return: UpdateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(instance_id, consumer_group_id, request, headers, runtime)

    def update_instance_with_options(self, instance_id, request, headers, runtime):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: UpdateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_info):
            body['networkInfo'] = request.network_info
        if not UtilClient.is_unset(request.product_info):
            body['productInfo'] = request.product_info
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, instance_id, request):
        """
        > API operations provided by Alibaba Cloud are used to manage and query resources of Alibaba Cloud services. We recommend that you integrate these API operations only in management systems. Do not use these API operations in the core system of messaging services. Otherwise, system risks may occur.
        

        @param request: UpdateInstanceRequest

        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    def update_topic_with_options(self, instance_id, topic_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTopic',
            version='2022-08-01',
            protocol='HTTPS',
            pathname='/instances/%s/topics/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(topic_name))),
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rocket_mq20220801_models.UpdateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def update_topic(self, instance_id, topic_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_topic_with_options(instance_id, topic_name, request, headers, runtime)
