# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_sls20201230 import models as sls_20201230_models
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
        self._endpoint_rule = 'central'

    def apply_config_to_machine_group_with_options(self, project, machine_group, config_name, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApplyConfigToMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ApplyConfigToMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/configs/%s' % (TeaConverter.to_unicode(machine_group), TeaConverter.to_unicode(config_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ApplyConfigToMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def apply_config_to_machine_group(self, project, machine_group, config_name):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: ApplyConfigToMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_config_to_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    def change_resource_group_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/resourcegroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ChangeResourceGroupResponse(),
            self.execute(params, req, runtime)
        )

    def change_resource_group(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(project, request, headers, runtime)

    def consumer_group_heart_beat_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        """
        ### Usage notes
        *   Connections between consumers and servers are established by sending heartbeats at regular intervals. If a server does not receive heartbeats from a consumer on schedule, the server deletes the consumer.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ConsumerGroupHeartBeatRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConsumerGroupHeartBeatResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.consumer):
            query['consumer'] = request.consumer
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ConsumerGroupHeartBeat',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s?type=heartbeat' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ConsumerGroupHeartBeatResponse(),
            self.execute(params, req, runtime)
        )

    def consumer_group_heart_beat(self, project, logstore, consumer_group, request):
        """
        ### Usage notes
        *   Connections between consumers and servers are established by sending heartbeats at regular intervals. If a server does not receive heartbeats from a consumer on schedule, the server deletes the consumer.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ConsumerGroupHeartBeatRequest

        @return: ConsumerGroupHeartBeatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.consumer_group_heart_beat_with_options(project, logstore, consumer_group, request, headers, runtime)

    def create_alert_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlert',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAlertResponse(),
            self.execute(params, req, runtime)
        )

    def create_alert(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_alert_with_options(project, request, headers, runtime)

    def create_annotation_data_set_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['datasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def create_annotation_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annotation_data_set_with_options(request, headers, runtime)

    def create_annotation_label_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def create_annotation_label(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annotation_label_with_options(request, headers, runtime)

    def create_config_with_options(self, project, request, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong, the region of the project, and the name of the Logstore to which the logs belong. For more information, see [Manage a project](~~48984~~).
        *   You can create up to 100 Logtail configurations in a project.
        *   The Logtail configuration is planned out. For more information, see [Logtail configurations](~~29058~~).
        

        @param request: CreateConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateConfigResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConfigResponse(),
            self.execute(params, req, runtime)
        )

    def create_config(self, project, request):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong, the region of the project, and the name of the Logstore to which the logs belong. For more information, see [Manage a project](~~48984~~).
        *   You can create up to 100 Logtail configurations in a project.
        *   The Logtail configuration is planned out. For more information, see [Logtail configurations](~~29058~~).
        

        @param request: CreateConfigRequest

        @return: CreateConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_with_options(project, request, headers, runtime)

    def create_consumer_group_with_options(self, project, logstore, request, headers, runtime):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   You can create up to 30 consumer groups for a Logstore.
        *   Simple Log Service provides examples of both regular log consumption and consumer group-based log consumption by using Simple Log Service SDKs for Java. For more information, see [Consume log data](~~120035~~) and [Use consumer groups to consume data](~~28998~~).
        

        @param request: CreateConsumerGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def create_consumer_group(self, project, logstore, request):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   You can create up to 30 consumer groups for a Logstore.
        *   Simple Log Service provides examples of both regular log consumption and consumer group-based log consumption by using Simple Log Service SDKs for Java. For more information, see [Consume log data](~~120035~~) and [Use consumer groups to consume data](~~28998~~).
        

        @param request: CreateConsumerGroupRequest

        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

    def create_dashboard_with_options(self, project, request, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @param request: CreateDashboardRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDashboardResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def create_dashboard(self, project, request):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @param request: CreateDashboardRequest

        @return: CreateDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dashboard_with_options(project, request, headers, runtime)

    def create_domain_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateDomainRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDomainResponse(),
            self.execute(params, req, runtime)
        )

    def create_domain(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateDomainRequest

        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(project, request, headers, runtime)

    def create_etlwith_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateETL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateETLResponse(),
            self.execute(params, req, runtime)
        )

    def create_etl(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_etlwith_options(project, request, headers, runtime)

    def create_index_with_options(self, project, logstore, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateIndexResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateIndexResponse(),
            self.execute(params, req, runtime)
        )

    def create_index(self, project, logstore, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateIndexRequest

        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(project, logstore, request, headers, runtime)

    def create_log_store_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateLogStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLogStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_log_store(self, project, request):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateLogStoreRequest

        @return: CreateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

    def create_logging_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateLoggingRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLoggingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def create_logging(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateLoggingRequest

        @return: CreateLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logging_with_options(project, request, headers, runtime)

    def create_logtail_pipeline_config_with_options(self, project, request, headers, runtime):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @param request: CreateLogtailPipelineConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLogtailPipelineConfigResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def create_logtail_pipeline_config(self, project, request):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @param request: CreateLogtailPipelineConfigRequest

        @return: CreateLogtailPipelineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logtail_pipeline_config_with_options(project, request, headers, runtime)

    def create_machine_group_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateMachineGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def create_machine_group(self, project, request):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateMachineGroupRequest

        @return: CreateMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_machine_group_with_options(project, request, headers, runtime)

    def create_ossexport_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOSSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    def create_ossexport(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ossexport_with_options(project, request, headers, runtime)

    def create_osshdfsexport_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOSSHDFSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    def create_osshdfsexport(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_osshdfsexport_with_options(project, request, headers, runtime)

    def create_ossingestion_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOSSIngestion',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    def create_ossingestion(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ossingestion_with_options(project, request, headers, runtime)

    def create_oss_external_store_with_options(self, project, request, headers, runtime):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateOssExternalStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateOssExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOssExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_oss_external_store(self, project, request):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateOssExternalStoreRequest

        @return: CreateOssExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_external_store_with_options(project, request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_redundancy_type):
            body['dataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            self.execute(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_rds_external_store_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateRdsExternalStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRdsExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateRdsExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_rds_external_store(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateRdsExternalStoreRequest

        @return: CreateRdsExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rds_external_store_with_options(project, request, headers, runtime)

    def create_saved_search_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateSavedSearchRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSavedSearchResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def create_saved_search(self, project, request):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: CreateSavedSearchRequest

        @return: CreateSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(project, request, headers, runtime)

    def create_scheduled_sqlwith_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduledSQL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/scheduledsqls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    def create_scheduled_sql(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scheduled_sqlwith_options(project, request, headers, runtime)

    def create_ticket_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/tickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateTicketResponse(),
            self.execute(params, req, runtime)
        )

    def create_ticket(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ticket_with_options(headers, runtime)

    def delete_alert_with_options(self, project, alert_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlert',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts/%s' % TeaConverter.to_unicode(alert_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAlertResponse(),
            self.execute(params, req, runtime)
        )

    def delete_alert(self, project, alert_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_with_options(project, alert_name, headers, runtime)

    def delete_annotation_data_with_options(self, dataset_id, annotationdata_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata/%s' % (TeaConverter.to_unicode(dataset_id), TeaConverter.to_unicode(annotationdata_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def delete_annotation_data(self, dataset_id, annotationdata_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    def delete_annotation_data_set_with_options(self, dataset_id, headers, runtime):
        """
        You can delete a dataset only if no data exists in the dataset.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAnnotationDataSetResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s' % TeaConverter.to_unicode(dataset_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def delete_annotation_data_set(self, dataset_id):
        """
        You can delete a dataset only if no data exists in the dataset.
        

        @return: DeleteAnnotationDataSetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_set_with_options(dataset_id, headers, runtime)

    def delete_annotation_label_with_options(self, label_id, headers, runtime):
        """
        Only non-built-in tags can be deleted.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAnnotationLabelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel/%s' % TeaConverter.to_unicode(label_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def delete_annotation_label(self, label_id):
        """
        Only non-built-in tags can be deleted.
        

        @return: DeleteAnnotationLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_label_with_options(label_id, headers, runtime)

    def delete_collection_policy_with_options(self, policy_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/collectionpolicy/%s' % TeaConverter.to_unicode(policy_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def delete_collection_policy(self, policy_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_collection_policy_with_options(policy_name, request, headers, runtime)

    def delete_config_with_options(self, project, config_name, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If a Logtail configuration is applied to a machine group, you cannot collect data from the machine group after you delete the Logtail configuration.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        *   The name of the required Logtail configuration is obtained. For more information, see [ListConfig](~~29043~~).
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConfigResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s' % TeaConverter.to_unicode(config_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConfigResponse(),
            self.execute(params, req, runtime)
        )

    def delete_config(self, project, config_name):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If a Logtail configuration is applied to a machine group, you cannot collect data from the machine group after you delete the Logtail configuration.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        *   The name of the required Logtail configuration is obtained. For more information, see [ListConfig](~~29043~~).
        

        @return: DeleteConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(project, config_name, headers, runtime)

    def delete_consumer_group_with_options(self, project, logstore, consumer_group, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConsumerGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def delete_consumer_group(self, project, logstore, consumer_group):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

    def delete_dashboard_with_options(self, project, dashboard_name, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDashboardResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards/%s' % TeaConverter.to_unicode(dashboard_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def delete_dashboard(self, project, dashboard_name):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @return: DeleteDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dashboard_with_options(project, dashboard_name, headers, runtime)

    def delete_domain_with_options(self, project, domain_name, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDomainResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/domains/%s' % TeaConverter.to_unicode(domain_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDomainResponse(),
            self.execute(params, req, runtime)
        )

    def delete_domain(self, project, domain_name):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(project, domain_name, headers, runtime)

    def delete_etlwith_options(self, project, etl_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteETL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls/%s' % TeaConverter.to_unicode(etl_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteETLResponse(),
            self.execute(params, req, runtime)
        )

    def delete_etl(self, project, etl_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_etlwith_options(project, etl_name, headers, runtime)

    def delete_external_store_with_options(self, project, external_store_name, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteExternalStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def delete_external_store(self, project, external_store_name):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_external_store_with_options(project, external_store_name, headers, runtime)

    def delete_index_with_options(self, project, logstore, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIndexResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteIndexResponse(),
            self.execute(params, req, runtime)
        )

    def delete_index(self, project, logstore):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(project, logstore, headers, runtime)

    def delete_log_store_with_options(self, project, logstore, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLogStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def delete_log_store(self, project, logstore):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_log_store_with_options(project, logstore, headers, runtime)

    def delete_logging_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def delete_logging(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logging_with_options(project, headers, runtime)

    def delete_logtail_pipeline_config_with_options(self, project, config_name, headers, runtime):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLogtailPipelineConfigResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs/%s' % TeaConverter.to_unicode(config_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def delete_logtail_pipeline_config(self, project, config_name):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @return: DeleteLogtailPipelineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    def delete_machine_group_with_options(self, project, machine_group, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s' % TeaConverter.to_unicode(machine_group),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def delete_machine_group(self, project, machine_group):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(project, machine_group, headers, runtime)

    def delete_ossexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteOSSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports/%s' % TeaConverter.to_unicode(oss_export_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    def delete_ossexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ossexport_with_options(project, oss_export_name, headers, runtime)

    def delete_osshdfsexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteOSSHDFSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports/%s' % TeaConverter.to_unicode(oss_export_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    def delete_osshdfsexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    def delete_ossingestion_with_options(self, project, oss_ingestion_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteOSSIngestion',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions/%s' % TeaConverter.to_unicode(oss_ingestion_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    def delete_ossingestion(self, project, oss_ingestion_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    def delete_project_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            self.execute(params, req, runtime)
        )

    def delete_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, headers, runtime)

    def delete_project_policy_with_options(self, project, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteProjectPolicyResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def delete_project_policy(self, project):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_policy_with_options(project, headers, runtime)

    def delete_saved_search_with_options(self, project, savedsearch_name, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSavedSearchResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def delete_saved_search(self, project, savedsearch_name):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_saved_search_with_options(project, savedsearch_name, headers, runtime)

    def delete_scheduled_sqlwith_options(self, project, scheduled_sqlname, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteScheduledSQL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/scheduledsqls/%s' % TeaConverter.to_unicode(scheduled_sqlname),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    def delete_scheduled_sql(self, project, scheduled_sqlname):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_scheduled_sqlwith_options(project, scheduled_sqlname, headers, runtime)

    def delete_shipper_with_options(self, project, logstore, shipper_name, headers, runtime):
        """
        @deprecated
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteShipperResponse
        Deprecated
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteShipperResponse(),
            self.execute(params, req, runtime)
        )

    def delete_shipper(self, project, logstore, shipper_name):
        """
        @deprecated
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: DeleteShipperResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_shipper_with_options(project, logstore, shipper_name, headers, runtime)

    def disable_alert_with_options(self, project, alert_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DisableAlert',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts/%s?action=disable' % TeaConverter.to_unicode(alert_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DisableAlertResponse(),
            self.execute(params, req, runtime)
        )

    def disable_alert(self, project, alert_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_alert_with_options(project, alert_name, headers, runtime)

    def enable_alert_with_options(self, project, alert_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableAlert',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts/%s?action=enable' % TeaConverter.to_unicode(alert_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.EnableAlertResponse(),
            self.execute(params, req, runtime)
        )

    def enable_alert(self, project, alert_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_alert_with_options(project, alert_name, headers, runtime)

    def get_alert_with_options(self, project, alert_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlert',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts/%s' % TeaConverter.to_unicode(alert_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAlertResponse(),
            self.execute(params, req, runtime)
        )

    def get_alert(self, project, alert_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alert_with_options(project, alert_name, headers, runtime)

    def get_annotation_data_with_options(self, dataset_id, annotationdata_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata/%s' % (TeaConverter.to_unicode(dataset_id), TeaConverter.to_unicode(annotationdata_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def get_annotation_data(self, dataset_id, annotationdata_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    def get_annotation_data_set_with_options(self, dataset_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s' % TeaConverter.to_unicode(dataset_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def get_annotation_data_set(self, dataset_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_data_set_with_options(dataset_id, headers, runtime)

    def get_annotation_label_with_options(self, label_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel/%s' % TeaConverter.to_unicode(label_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def get_annotation_label(self, label_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_label_with_options(label_id, headers, runtime)

    def get_applied_configs_with_options(self, project, machine_group, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAppliedConfigsResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedConfigs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/configs' % TeaConverter.to_unicode(machine_group),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedConfigsResponse(),
            self.execute(params, req, runtime)
        )

    def get_applied_configs(self, project, machine_group):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetAppliedConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_configs_with_options(project, machine_group, headers, runtime)

    def get_applied_machine_groups_with_options(self, project, config_name, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAppliedMachineGroupsResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedMachineGroups',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s/machinegroups' % TeaConverter.to_unicode(config_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedMachineGroupsResponse(),
            self.execute(params, req, runtime)
        )

    def get_applied_machine_groups(self, project, config_name):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetAppliedMachineGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_machine_groups_with_options(project, config_name, headers, runtime)

    def get_check_point_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetCheckPointRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCheckPointResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.shard):
            query['shard'] = request.shard
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckPoint',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCheckPointResponse(),
            self.execute(params, req, runtime)
        )

    def get_check_point(self, project, logstore, consumer_group, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetCheckPointRequest

        @return: GetCheckPointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

    def get_collection_policy_with_options(self, policy_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/collectionpolicy/%s' % TeaConverter.to_unicode(policy_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def get_collection_policy(self, policy_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_collection_policy_with_options(policy_name, request, headers, runtime)

    def get_config_with_options(self, project, config_name, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        *   The name of the required Logtail configuration is obtained. For more information, see [ListConfig](~~29043~~).
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetConfigResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s' % TeaConverter.to_unicode(config_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetConfigResponse(),
            self.execute(params, req, runtime)
        )

    def get_config(self, project, config_name):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        *   The name of the required Logtail configuration is obtained. For more information, see [ListConfig](~~29043~~).
        

        @return: GetConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_config_with_options(project, config_name, headers, runtime)

    def get_context_logs_with_options(self, project, logstore, request, headers, runtime):
        """
        You can specify a log as the start log. The time range of a contextual query is one day before and one day after the generation time of the start log.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetContextLogsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetContextLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.back_lines):
            query['back_lines'] = request.back_lines
        if not UtilClient.is_unset(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not UtilClient.is_unset(request.pack_id):
            query['pack_id'] = request.pack_id
        if not UtilClient.is_unset(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContextLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetContextLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_context_logs(self, project, logstore, request):
        """
        You can specify a log as the start log. The time range of a contextual query is one day before and one day after the generation time of the start log.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetContextLogsRequest

        @return: GetContextLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_context_logs_with_options(project, logstore, request, headers, runtime)

    def get_cursor_with_options(self, project, logstore, shard_id, request, headers, runtime):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The following content describes the relationships among a cursor, project, Logstore, and shard:
        *   A project can have multiple Logstores.
        *   A Logstore can have multiple shards.
        *   You can use a cursor to obtain a log in a shard.
        

        @param request: GetCursorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCursorResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursor',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?type=cursor' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorResponse(),
            self.execute(params, req, runtime)
        )

    def get_cursor(self, project, logstore, shard_id, request):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The following content describes the relationships among a cursor, project, Logstore, and shard:
        *   A project can have multiple Logstores.
        *   A Logstore can have multiple shards.
        *   You can use a cursor to obtain a log in a shard.
        

        @param request: GetCursorRequest

        @return: GetCursorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_time_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursorTime',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?type=cursor_time' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorTimeResponse(),
            self.execute(params, req, runtime)
        )

    def get_cursor_time(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_time_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_dashboard_with_options(self, project, dashboard_name, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDashboardResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards/%s' % TeaConverter.to_unicode(dashboard_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def get_dashboard(self, project, dashboard_name):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @return: GetDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(project, dashboard_name, headers, runtime)

    def get_etlwith_options(self, project, etl_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetETL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls/%s' % TeaConverter.to_unicode(etl_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetETLResponse(),
            self.execute(params, req, runtime)
        )

    def get_etl(self, project, etl_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_etlwith_options(project, etl_name, headers, runtime)

    def get_external_store_with_options(self, project, external_store_name, headers, runtime):
        """
        The supported data sources of external stores include Object Storage Service (OSS) buckets and ApsaraDB RDS for MySQL databases in a virtual private cloud (VPC).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetExternalStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def get_external_store(self, project, external_store_name):
        """
        The supported data sources of external stores include Object Storage Service (OSS) buckets and ApsaraDB RDS for MySQL databases in a virtual private cloud (VPC).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_external_store_with_options(project, external_store_name, headers, runtime)

    def get_histograms_with_options(self, project, logstore, request, headers, runtime):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The time range is evenly divided into subintervals in the responses. If the time range that is specified in the request remains unchanged, the subintervals in the responses also remain unchanged.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        *   Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:\\__receive_time\\_\\_ field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetHistograms operation by using Simple Log Service SDK for Java. For more information, see [Use GetHistograms to query the distribution of logs](~~462234~~).
        

        @param request: GetHistogramsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetHistogramsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index?type=histogram' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetHistogramsResponse(),
            self.execute(params, req, runtime)
        )

    def get_histograms(self, project, logstore, request):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The time range is evenly divided into subintervals in the responses. If the time range that is specified in the request remains unchanged, the subintervals in the responses also remain unchanged.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        *   Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:\\__receive_time\\_\\_ field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetHistograms operation by using Simple Log Service SDK for Java. For more information, see [Use GetHistograms to query the distribution of logs](~~462234~~).
        

        @param request: GetHistogramsRequest

        @return: GetHistogramsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_histograms_with_options(project, logstore, request, headers, runtime)

    def get_index_with_options(self, project, logstore, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetIndexResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetIndexResponse(),
            self.execute(params, req, runtime)
        )

    def get_index(self, project, logstore):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(project, logstore, headers, runtime)

    def get_log_store_with_options(self, project, logstore, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLogStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def get_log_store(self, project, logstore):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

    def get_log_store_metering_mode_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStoreMeteringMode',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/meteringmode' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    def get_log_store_metering_mode(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_metering_mode_with_options(project, logstore, headers, runtime)

    def get_logging_with_options(self, project, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLoggingResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def get_logging(self, project):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logging_with_options(project, headers, runtime)

    def get_logs_with_options(self, project, logstore, request, headers, runtime):
        """
        ### Usage notes
        > Simple Log Service allows you to create a Scheduled SQL job. For more information, see [Create a Scheduled SQL job](~~286457~~).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot forecast the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the x-log-progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. This type of log is usually generated in common scenarios.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:**receive_time** field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetLogs operation by using Simple Log Service SDK for Java and Simple Log Service SDK for Python. For more information, see [Examples of calling the GetLogs operation by using Simple Log Service SDK for Java](~~407683~~) and [Examples of calling the GetLogs operation by using Simple Log Service SDK for Python](~~407684~~).
        

        @param request: GetLogsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            query['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            query['reverse'] = request.reverse
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s?type=log' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_logs(self, project, logstore, request):
        """
        ### Usage notes
        > Simple Log Service allows you to create a Scheduled SQL job. For more information, see [Create a Scheduled SQL job](~~286457~~).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot forecast the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the x-log-progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. This type of log is usually generated in common scenarios.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:**receive_time** field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetLogs operation by using Simple Log Service SDK for Java and Simple Log Service SDK for Python. For more information, see [Examples of calling the GetLogs operation by using Simple Log Service SDK for Java](~~407683~~) and [Examples of calling the GetLogs operation by using Simple Log Service SDK for Python](~~407684~~).
        

        @param request: GetLogsRequest

        @return: GetLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logs_with_options(project, logstore, request, headers, runtime)

    def get_logs_v2with_options(self, project, logstore, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times you must call this API operation to obtain a complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation again to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log. The latency of the query varies based on the type of the log. Simple Log Service classifies logs into the following types based on log timestamps:
        1.  1.  Real-time data: The difference between the time record in the log and the current server time is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as real-time data. This type of log is usually generated in common scenarios.
        2.  2.  Historical data: The difference between the time record in the log and the current server time is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as historical data. This type of log is usually generated in data backfill scenarios. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        

        @param request: GetLogsV2Request

        @param headers: GetLogsV2Headers

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLogsV2Response
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.forward):
            body['forward'] = request.forward
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.highlight):
            body['highlight'] = request.highlight
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            body['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            body['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            body['reverse'] = request.reverse
        if not UtilClient.is_unset(request.session):
            body['session'] = request.session
        if not UtilClient.is_unset(request.shard):
            body['shard'] = request.shard
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogsV2',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/logs' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsV2Response(),
            self.execute(params, req, runtime)
        )

    def get_logs_v2(self, project, logstore, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times you must call this API operation to obtain a complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation again to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log. The latency of the query varies based on the type of the log. Simple Log Service classifies logs into the following types based on log timestamps:
        1.  1.  Real-time data: The difference between the time record in the log and the current server time is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as real-time data. This type of log is usually generated in common scenarios.
        2.  2.  Historical data: The difference between the time record in the log and the current server time is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as historical data. This type of log is usually generated in data backfill scenarios. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        

        @param request: GetLogsV2Request

        @return: GetLogsV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = sls_20201230_models.GetLogsV2Headers()
        return self.get_logs_v2with_options(project, logstore, request, headers, runtime)

    def get_logtail_pipeline_config_with_options(self, project, config_name, headers, runtime):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLogtailPipelineConfigResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs/%s' % TeaConverter.to_unicode(config_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def get_logtail_pipeline_config(self, project, config_name):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @return: GetLogtailPipelineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    def get_mlservice_results_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GetMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/service/%s/analysis' % TeaConverter.to_unicode(service_name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMLServiceResultsResponse(),
            self.execute(params, req, runtime)
        )

    def get_mlservice_results(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mlservice_results_with_options(service_name, request, headers, runtime)

    def get_machine_group_with_options(self, project, machine_group, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s' % TeaConverter.to_unicode(machine_group),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def get_machine_group(self, project, machine_group):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(project, machine_group, headers, runtime)

    def get_ossexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOSSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports/%s' % TeaConverter.to_unicode(oss_export_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    def get_ossexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ossexport_with_options(project, oss_export_name, headers, runtime)

    def get_osshdfsexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOSSHDFSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports/%s' % TeaConverter.to_unicode(oss_export_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    def get_osshdfsexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    def get_ossingestion_with_options(self, project, oss_ingestion_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOSSIngestion',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions/%s' % TeaConverter.to_unicode(oss_ingestion_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    def get_ossingestion(self, project, oss_ingestion_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    def get_project_with_options(self, project, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProjectResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            self.execute(params, req, runtime)
        )

    def get_project(self, project):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

    def get_project_logs_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        *   You can use the query parameter to specify a standard SQL statement.
        *   You must specify a project in the domain name of the request.
        *   You must specify a Logstore in the FROM clause of the SQL statement. A Logstore can be used as an SQL table.
        *   You must specify a time range in the SQL statement by using the \\__date\\_\\_ parameter or \\__time\\_\\_ parameter. The value of the \\__date\\_\\_ parameter is a timestamp, and the value of the \\__time\\_\\_ parameter is an integer. The unit of the \\__time\\_\\_ parameter is seconds.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetProjectLogsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProjectLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_project_logs(self, project, request):
        """
        ### Usage notes
        *   You can use the query parameter to specify a standard SQL statement.
        *   You must specify a project in the domain name of the request.
        *   You must specify a Logstore in the FROM clause of the SQL statement. A Logstore can be used as an SQL table.
        *   You must specify a time range in the SQL statement by using the \\__date\\_\\_ parameter or \\__time\\_\\_ parameter. The value of the \\__date\\_\\_ parameter is a timestamp, and the value of the \\__time\\_\\_ parameter is an integer. The unit of the \\__time\\_\\_ parameter is seconds.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetProjectLogsRequest

        @return: GetProjectLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_logs_with_options(project, request, headers, runtime)

    def get_project_policy_with_options(self, project, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProjectPolicyResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def get_project_policy(self, project):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_policy_with_options(project, headers, runtime)

    def get_saved_search_with_options(self, project, savedsearch_name, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSavedSearchResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def get_saved_search(self, project, savedsearch_name):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: GetSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_saved_search_with_options(project, savedsearch_name, headers, runtime)

    def get_scheduled_sqlwith_options(self, project, scheduled_sqlname, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetScheduledSQL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/scheduledsqls/%s' % TeaConverter.to_unicode(scheduled_sqlname),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    def get_scheduled_sql(self, project, scheduled_sqlname):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scheduled_sqlwith_options(project, scheduled_sqlname, headers, runtime)

    def get_shipper_status_with_options(self, project, logstore, shipper_name, request, headers, runtime):
        """
        @deprecated
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetShipperStatusRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetShipperStatusResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetShipperStatus',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s/tasks' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetShipperStatusResponse(),
            self.execute(params, req, runtime)
        )

    def get_shipper_status(self, project, logstore, shipper_name, request):
        """
        @deprecated
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: GetShipperStatusRequest

        @return: GetShipperStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shipper_status_with_options(project, logstore, shipper_name, request, headers, runtime)

    def list_alerts_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore):
            query['logstore'] = request.logstore
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAlertsResponse(),
            self.execute(params, req, runtime)
        )

    def list_alerts(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alerts_with_options(project, request, headers, runtime)

    def list_annotation_data_with_options(self, dataset_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata' % TeaConverter.to_unicode(dataset_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def list_annotation_data(self, dataset_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_data_with_options(dataset_id, request, headers, runtime)

    def list_annotation_data_sets_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationDataSets',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataSetsResponse(),
            self.execute(params, req, runtime)
        )

    def list_annotation_data_sets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_data_sets_with_options(request, headers, runtime)

    def list_annotation_labels_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationLabels',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationLabelsResponse(),
            self.execute(params, req, runtime)
        )

    def list_annotation_labels(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_labels_with_options(request, headers, runtime)

    def list_collection_policies_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListCollectionPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute):
            request.attribute_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute, 'attribute', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_shrink):
            query['attribute'] = request.attribute_shrink
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollectionPolicies',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/collectionpolicy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListCollectionPoliciesResponse(),
            self.execute(params, req, runtime)
        )

    def list_collection_policies(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_collection_policies_with_options(request, headers, runtime)

    def list_config_with_options(self, project, request, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @param request: ListConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConfigResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConfigResponse(),
            self.execute(params, req, runtime)
        )

    def list_config(self, project, request):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @param request: ListConfigRequest

        @return: ListConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_config_with_options(project, request, headers, runtime)

    def list_consumer_group_with_options(self, project, logstore, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConsumerGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def list_consumer_group(self, project, logstore):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: ListConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

    def list_dashboard_with_options(self, project, request, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @param request: ListDashboardRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDashboardResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def list_dashboard(self, project, request):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        

        @param request: ListDashboardRequest

        @return: ListDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_with_options(project, request, headers, runtime)

    def list_domains_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Only one custom domain name can be bound to each project.
        

        @param request: ListDomainsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDomainsResponse(),
            self.execute(params, req, runtime)
        )

    def list_domains(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Only one custom domain name can be bound to each project.
        

        @param request: ListDomainsRequest

        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(project, request, headers, runtime)

    def list_etls_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListETLs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListETLsResponse(),
            self.execute(params, req, runtime)
        )

    def list_etls(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_etls_with_options(project, request, headers, runtime)

    def list_external_store_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListExternalStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.external_store_name):
            query['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.sizs):
            query['sizs'] = request.sizs
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def list_external_store(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListExternalStoreRequest

        @return: ListExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_external_store_with_options(project, request, headers, runtime)

    def list_log_stores_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        * Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        * An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O&#x26;M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        * The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        ### Authentication resources
        The following table describes the authorization information that is required for this operation. You can add the information to the Action element of a RAM policy statement to grant a RAM user or a RAM role the permissions to call this operation.
        |Action|Resource|
        |:---|:---|
        |`log:ListLogStores`|`acs:log:{#regionId}:{#accountId}:project/{#ProjectName}/logstore/*`|
        

        @param request: ListLogStoresRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLogStoresResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            self.execute(params, req, runtime)
        )

    def list_log_stores(self, project, request):
        """
        ### Usage notes
        * Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        * An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O&#x26;M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        * The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        ### Authentication resources
        The following table describes the authorization information that is required for this operation. You can add the information to the Action element of a RAM policy statement to grant a RAM user or a RAM role the permissions to call this operation.
        |Action|Resource|
        |:---|:---|
        |`log:ListLogStores`|`acs:log:{#regionId}:{#accountId}:project/{#ProjectName}/logstore/*`|
        

        @param request: ListLogStoresRequest

        @return: ListLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

    def list_logtail_pipeline_config_with_options(self, project, request, headers, runtime):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @param request: ListLogtailPipelineConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLogtailPipelineConfigResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def list_logtail_pipeline_config(self, project, request):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @param request: ListLogtailPipelineConfigRequest

        @return: ListLogtailPipelineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logtail_pipeline_config_with_options(project, request, headers, runtime)

    def list_machine_group_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListMachineGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['groupName'] = request.group_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def list_machine_group(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListMachineGroupRequest

        @return: ListMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machine_group_with_options(project, request, headers, runtime)

    def list_machines_with_options(self, project, machine_group, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListMachinesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListMachinesResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachines',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/machines' % TeaConverter.to_unicode(machine_group),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachinesResponse(),
            self.execute(params, req, runtime)
        )

    def list_machines(self, project, machine_group, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListMachinesRequest

        @return: ListMachinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machines_with_options(project, machine_group, request, headers, runtime)

    def list_ossexports_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOSSExports',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListOSSExportsResponse(),
            self.execute(params, req, runtime)
        )

    def list_ossexports(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ossexports_with_options(project, request, headers, runtime)

    def list_osshdfsexports_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOSSHDFSExports',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListOSSHDFSExportsResponse(),
            self.execute(params, req, runtime)
        )

    def list_osshdfsexports(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_osshdfsexports_with_options(project, request, headers, runtime)

    def list_ossingestions_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOSSIngestions',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListOSSIngestionsResponse(),
            self.execute(params, req, runtime)
        )

    def list_ossingestions(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ossingestions_with_options(project, request, headers, runtime)

    def list_project_with_options(self, request, headers, runtime):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListProjectRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            self.execute(params, req, runtime)
        )

    def list_project(self, request):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListProjectRequest

        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    def list_saved_search_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListSavedSearchRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSavedSearchResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def list_saved_search(self, project, request):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListSavedSearchRequest

        @return: ListSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

    def list_scheduled_sqls_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledSQLs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/scheduledsqls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListScheduledSQLsResponse(),
            self.execute(params, req, runtime)
        )

    def list_scheduled_sqls(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scheduled_sqls_with_options(project, request, headers, runtime)

    def list_shards_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShardsResponse(),
            self.execute(params, req, runtime)
        )

    def list_shards(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shards_with_options(project, logstore, headers, runtime)

    def list_shipper_with_options(self, project, logstore, headers, runtime):
        """
        @deprecated
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListShipperResponse
        Deprecated
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShipperResponse(),
            self.execute(params, req, runtime)
        )

    def list_shipper(self, project, logstore):
        """
        @deprecated
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: ListShipperResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shipper_with_options(project, logstore, headers, runtime)

    def list_tag_resources_with_options(self, tmp_req, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param tmp_req: ListTagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListTagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def merge_shard_with_options(self, project, logstore, shard, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='MergeShard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?action=merge' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.MergeShardResponse(),
            self.execute(params, req, runtime)
        )

    def merge_shard(self, project, logstore, shard):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.merge_shard_with_options(project, logstore, shard, headers, runtime)

    def put_annotation_data_with_options(self, dataset_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotationdata_id):
            query['annotationdataId'] = request.annotationdata_id
        body = {}
        if not UtilClient.is_unset(request.ml_data_param):
            body['mlDataParam'] = request.ml_data_param
        if not UtilClient.is_unset(request.raw_log):
            body['rawLog'] = request.raw_log
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata' % TeaConverter.to_unicode(dataset_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def put_annotation_data(self, dataset_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_annotation_data_with_options(dataset_id, request, headers, runtime)

    def put_project_policy_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Alibaba Cloud Simple Log Service allows you to configure a project policy to authorize other users to access the specified Log Service resources.
        *   You must configure a project policy based on policy syntax. Before you configure a project policy, you must be familiar with the Action, Resource, and Condition parameters. For more information, see [RAM](~~128139~~).
        *   If you set the Principal element to an asterisk (\\*) and do not configure the Condition element when you configure a project policy, the policy applies to all users except for the project owner. If you set the Principal element to an asterisk (\\*) and configure the Condition element when you configure a project policy, the policy applies to all users including the project owner.
        *   You can configure multiple project policies for a project. The total size of the policies cannot exceed 16 KB.
        

        @param request: PutProjectPolicyRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutProjectPolicyResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PutProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/policy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def put_project_policy(self, project, request):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Alibaba Cloud Simple Log Service allows you to configure a project policy to authorize other users to access the specified Log Service resources.
        *   You must configure a project policy based on policy syntax. Before you configure a project policy, you must be familiar with the Action, Resource, and Condition parameters. For more information, see [RAM](~~128139~~).
        *   If you set the Principal element to an asterisk (\\*) and do not configure the Condition element when you configure a project policy, the policy applies to all users except for the project owner. If you set the Principal element to an asterisk (\\*) and configure the Condition element when you configure a project policy, the policy applies to all users including the project owner.
        *   You can configure multiple project policies for a project. The total size of the policies cannot exceed 16 KB.
        

        @param request: PutProjectPolicyRequest

        @return: PutProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_project_policy_with_options(project, request, headers, runtime)

    def put_project_transfer_acceleration_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProjectTransferAcceleration',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/transferacceleration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    def put_project_transfer_acceleration(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_project_transfer_acceleration_with_options(project, request, headers, runtime)

    def put_webtracking_with_options(self, project, logstore_name, request, headers, runtime):
        """
        ### [](#)Usage notes
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong, the region of the project, and the name of the Logstore to which the logs belong. For more information, see [Manage a project](~~48984~~) and [Manage a Logstore](~~48990~~).
        *   You can call this operation to collect logs from web pages or clients.
        *   If you use web tracking to collect logs and you do not call this operation, you can send only one log to Simple Log Service in a request. For more information, see [Use web tracking to collect logs](~~31752~~).
        *   If you want to collect a large amount of log data, you can call this operation to send multiple logs to Simple Log Service in one request.
        *   Before you can call this operation to send logs to a Logstore, you must enable web tracking for the Logstore. For more information, see [Use web tracking to collect logs](~~31752~~).
        *   You cannot call this operation to send the logs of multiple topics to Simple Log Service at a time.
        *   If you call this operation, anonymous users from the Internet are granted the write permissions on the Logstore. This may generate dirty data because AccessKey pair-based authentication is not performed.
        

        @param request: PutWebtrackingRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutWebtrackingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logs):
            body['__logs__'] = request.logs
        if not UtilClient.is_unset(request.source):
            body['__source__'] = request.source
        if not UtilClient.is_unset(request.tags):
            body['__tags__'] = request.tags
        if not UtilClient.is_unset(request.topic):
            body['__topic__'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWebtracking',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/track' % TeaConverter.to_unicode(logstore_name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutWebtrackingResponse(),
            self.execute(params, req, runtime)
        )

    def put_webtracking(self, project, logstore_name, request):
        """
        ### [](#)Usage notes
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong, the region of the project, and the name of the Logstore to which the logs belong. For more information, see [Manage a project](~~48984~~) and [Manage a Logstore](~~48990~~).
        *   You can call this operation to collect logs from web pages or clients.
        *   If you use web tracking to collect logs and you do not call this operation, you can send only one log to Simple Log Service in a request. For more information, see [Use web tracking to collect logs](~~31752~~).
        *   If you want to collect a large amount of log data, you can call this operation to send multiple logs to Simple Log Service in one request.
        *   Before you can call this operation to send logs to a Logstore, you must enable web tracking for the Logstore. For more information, see [Use web tracking to collect logs](~~31752~~).
        *   You cannot call this operation to send the logs of multiple topics to Simple Log Service at a time.
        *   If you call this operation, anonymous users from the Internet are granted the write permissions on the Logstore. This may generate dirty data because AccessKey pair-based authentication is not performed.
        

        @param request: PutWebtrackingRequest

        @return: PutWebtrackingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_webtracking_with_options(project, logstore_name, request, headers, runtime)

    def query_mlservice_results_with_options(self, service_name, request, headers, runtime):
        """
        @deprecated
        

        @param request: QueryMLServiceResultsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryMLServiceResultsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/service/%s/analysis' % TeaConverter.to_unicode(service_name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.QueryMLServiceResultsResponse(),
            self.execute(params, req, runtime)
        )

    def query_mlservice_results(self, service_name, request):
        """
        @deprecated
        

        @param request: QueryMLServiceResultsRequest

        @return: QueryMLServiceResultsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_mlservice_results_with_options(service_name, request, headers, runtime)

    def remove_config_from_machine_group_with_options(self, project, machine_group, config_name, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveConfigFromMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveConfigFromMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/configs/%s' % (TeaConverter.to_unicode(machine_group), TeaConverter.to_unicode(config_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.RemoveConfigFromMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def remove_config_from_machine_group(self, project, machine_group, config_name):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @return: RemoveConfigFromMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_config_from_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    def split_shard_with_options(self, project, logstore, shard, request, headers, runtime):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Each shard has an MD5 hash range, and each range is a left-closed, right-open interval. The interval is in the `[BeginKey,EndKey)` format. A shard can be in the readwrite or readonly state. You can split a shard and merge shards. For more information, see [Shard](~~28976~~).
        

        @param request: SplitShardRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: SplitShardResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SplitShard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?action=split' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.SplitShardResponse(),
            self.execute(params, req, runtime)
        )

    def split_shard(self, project, logstore, shard, request):
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Each shard has an MD5 hash range, and each range is a left-closed, right-open interval. The interval is in the `[BeginKey,EndKey)` format. A shard can be in the readwrite or readonly state. You can split a shard and merge shards. For more information, see [Shard](~~28976~~).
        

        @param request: SplitShardRequest

        @return: SplitShardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_shard_with_options(project, logstore, shard, request, headers, runtime)

    def start_etlwith_options(self, project, etl_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StartETL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls/%s?action=START' % TeaConverter.to_unicode(etl_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StartETLResponse(),
            self.execute(params, req, runtime)
        )

    def start_etl(self, project, etl_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_etlwith_options(project, etl_name, headers, runtime)

    def start_ossexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StartOSSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports/%s?action=START' % TeaConverter.to_unicode(oss_export_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StartOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    def start_ossexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_ossexport_with_options(project, oss_export_name, headers, runtime)

    def start_osshdfsexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StartOSSHDFSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports/%s?action=START' % TeaConverter.to_unicode(oss_export_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StartOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    def start_osshdfsexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    def start_ossingestion_with_options(self, project, oss_ingestion_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StartOSSIngestion',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions/%s?action=START' % TeaConverter.to_unicode(oss_ingestion_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StartOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    def start_ossingestion(self, project, oss_ingestion_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    def stop_etlwith_options(self, project, etl_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StopETL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls/%s?action=STOP' % TeaConverter.to_unicode(etl_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StopETLResponse(),
            self.execute(params, req, runtime)
        )

    def stop_etl(self, project, etl_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_etlwith_options(project, etl_name, headers, runtime)

    def stop_ossexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StopOSSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports/%s?action=STOP' % TeaConverter.to_unicode(oss_export_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StopOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    def stop_ossexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_ossexport_with_options(project, oss_export_name, headers, runtime)

    def stop_osshdfsexport_with_options(self, project, oss_export_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StopOSSHDFSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports/%s?action=STOP' % TeaConverter.to_unicode(oss_export_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StopOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    def stop_osshdfsexport(self, project, oss_export_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_osshdfsexport_with_options(project, oss_export_name, headers, runtime)

    def stop_ossingestion_with_options(self, project, oss_ingestion_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='StopOSSIngestion',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions/%s?action=STOP' % TeaConverter.to_unicode(oss_ingestion_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.StopOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    def stop_ossingestion(self, project, oss_ingestion_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_ossingestion_with_options(project, oss_ingestion_name, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: TagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.TagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def untag_resources_with_options(self, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UntagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/untag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UntagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def update_alert_with_options(self, project, alert_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAlert',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/alerts/%s' % TeaConverter.to_unicode(alert_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAlertResponse(),
            self.execute(params, req, runtime)
        )

    def update_alert(self, project, alert_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_alert_with_options(project, alert_name, request, headers, runtime)

    def update_annotation_data_set_with_options(self, dataset_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s' % TeaConverter.to_unicode(dataset_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def update_annotation_data_set(self, dataset_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_annotation_data_set_with_options(dataset_id, request, headers, runtime)

    def update_annotation_label_with_options(self, request, headers, runtime):
        """
        You can update only the names of the tags in a tag set.
        

        @param request: UpdateAnnotationLabelRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAnnotationLabelResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def update_annotation_label(self, request):
        """
        You can update only the names of the tags in a tag set.
        

        @param request: UpdateAnnotationLabelRequest

        @return: UpdateAnnotationLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_annotation_label_with_options(request, headers, runtime)

    def update_config_with_options(self, project, config_name, request, headers, runtime):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   After you update a Logtail configuration that is applied to a machine group, the new configuration immediately takes effect.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        *   The Logtail configuration is planned out. For more information, see [Logtail configurations](~~29058~~).
        

        @param request: UpdateConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateConfigResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s' % TeaConverter.to_unicode(config_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConfigResponse(),
            self.execute(params, req, runtime)
        )

    def update_config(self, project, config_name, request):
        """
        ### [](#)Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   After you update a Logtail configuration that is applied to a machine group, the new configuration immediately takes effect.
        *   An AccessKey pair is created and obtained. For more information, see [AccessKey pair](~~29009~~).
        The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. Using these credentials to perform operations in Simple Log Service is a high-risk operation. We recommend that you use a RAM user to call API operations or perform routine O\\&M. To create a RAM user, log on to the RAM console. Make sure that the RAM user has the management permissions on Simple Log Service resources. For more information, see [Create a RAM user and authorize the RAM user to access Simple Log Service](~~47664~~).
        *   The information that is required to query logs is obtained. The information includes the name of the project to which the logs belong and the region of the project. For more information, see [Manage a project](~~48984~~).
        *   The Logtail configuration is planned out. For more information, see [Logtail configurations](~~29058~~).
        

        @param request: UpdateConfigRequest

        @return: UpdateConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_with_options(project, config_name, request, headers, runtime)

    def update_consumer_group_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateConsumerGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_consumer_group(self, project, logstore, consumer_group, request):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateConsumerGroupRequest

        @return: UpdateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

    def update_dashboard_with_options(self, project, dashboard_name, request, headers, runtime):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateDashboardRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDashboardResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.charts):
            body['charts'] = request.charts
        if not UtilClient.is_unset(request.dashboard_name):
            body['dashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards/%s' % TeaConverter.to_unicode(dashboard_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def update_dashboard(self, project, dashboard_name, request):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateDashboardRequest

        @return: UpdateDashboardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dashboard_with_options(project, dashboard_name, request, headers, runtime)

    def update_etlwith_options(self, project, etl_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateETL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etls/%s' % TeaConverter.to_unicode(etl_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateETLResponse(),
            self.execute(params, req, runtime)
        )

    def update_etl(self, project, etl_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_etlwith_options(project, etl_name, request, headers, runtime)

    def update_index_with_options(self, project, logstore, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateIndexResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateIndexResponse(),
            self.execute(params, req, runtime)
        )

    def update_index(self, project, logstore, request):
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateIndexRequest

        @return: UpdateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_with_options(project, logstore, request, headers, runtime)

    def update_log_store_with_options(self, project, logstore, request, headers, runtime):
        """
        ### Usage notes
        *   Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        *   You can call the UpdateLogStore operation to change only the time-to-live (TTL) attribute.
        

        @param request: UpdateLogStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLogStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_log_store(self, project, logstore, request):
        """
        ### Usage notes
        *   Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        *   You can call the UpdateLogStore operation to change only the time-to-live (TTL) attribute.
        

        @param request: UpdateLogStoreRequest

        @return: UpdateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

    def update_log_store_metering_mode_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStoreMeteringMode',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/meteringmode' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    def update_log_store_metering_mode(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_metering_mode_with_options(project, logstore, request, headers, runtime)

    def update_logging_with_options(self, project, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateLoggingRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLoggingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def update_logging(self, project, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateLoggingRequest

        @return: UpdateLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logging_with_options(project, request, headers, runtime)

    def update_logtail_pipeline_config_with_options(self, project, config_name, request, headers, runtime):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @param request: UpdateLogtailPipelineConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLogtailPipelineConfigResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs/%s' % TeaConverter.to_unicode(config_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def update_logtail_pipeline_config(self, project, config_name, request):
        """
        The UK (London) region is supported. Supported regions are constantly updated.
        

        @param request: UpdateLogtailPipelineConfigRequest

        @return: UpdateLogtailPipelineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logtail_pipeline_config_with_options(project, config_name, request, headers, runtime)

    def update_machine_group_with_options(self, project, group_name, request, headers, runtime):
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateMachineGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s' % TeaConverter.to_unicode(group_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_machine_group(self, project, group_name, request):
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateMachineGroupRequest

        @return: UpdateMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_with_options(project, group_name, request, headers, runtime)

    def update_machine_group_machine_with_options(self, project, machine_group, request, headers, runtime):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateMachineGroupMachineRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMachineGroupMachineResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateMachineGroupMachine',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/machines' % TeaConverter.to_unicode(machine_group),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupMachineResponse(),
            self.execute(params, req, runtime)
        )

    def update_machine_group_machine(self, project, machine_group, request):
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateMachineGroupMachineRequest

        @return: UpdateMachineGroupMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_machine_with_options(project, machine_group, request, headers, runtime)

    def update_ossexport_with_options(self, project, oss_export_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOSSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossexports/%s' % TeaConverter.to_unicode(oss_export_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOSSExportResponse(),
            self.execute(params, req, runtime)
        )

    def update_ossexport(self, project, oss_export_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ossexport_with_options(project, oss_export_name, request, headers, runtime)

    def update_osshdfsexport_with_options(self, project, oss_export_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOSSHDFSExport',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/osshdfsexports/%s' % TeaConverter.to_unicode(oss_export_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOSSHDFSExportResponse(),
            self.execute(params, req, runtime)
        )

    def update_osshdfsexport(self, project, oss_export_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_osshdfsexport_with_options(project, oss_export_name, request, headers, runtime)

    def update_ossingestion_with_options(self, project, oss_ingestion_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOSSIngestion',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ossingestions/%s' % TeaConverter.to_unicode(oss_ingestion_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOSSIngestionResponse(),
            self.execute(params, req, runtime)
        )

    def update_ossingestion(self, project, oss_ingestion_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ossingestion_with_options(project, oss_ingestion_name, request, headers, runtime)

    def update_oss_external_store_with_options(self, project, external_store_name, request, headers, runtime):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateOssExternalStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateOssExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOssExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_oss_external_store(self, project, external_store_name, request):
        """
        ### [](#)Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateOssExternalStoreRequest

        @return: UpdateOssExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_oss_external_store_with_options(project, external_store_name, request, headers, runtime)

    def update_project_with_options(self, project, request, headers, runtime):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateProjectRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            self.execute(params, req, runtime)
        )

    def update_project(self, project, request):
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateProjectRequest

        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

    def update_rds_external_store_with_options(self, project, external_store_name, request, headers, runtime):
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateRdsExternalStoreRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRdsExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateRdsExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_rds_external_store(self, project, external_store_name, request):
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        

        @param request: UpdateRdsExternalStoreRequest

        @return: UpdateRdsExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rds_external_store_with_options(project, external_store_name, request, headers, runtime)

    def update_saved_search_with_options(self, project, savedsearch_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def update_saved_search(self, project, savedsearch_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_saved_search_with_options(project, savedsearch_name, request, headers, runtime)

    def update_scheduled_sqlwith_options(self, project, scheduled_sqlname, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.schedule):
            body['schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScheduledSQL',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/scheduledsqls/%s' % TeaConverter.to_unicode(scheduled_sqlname),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateScheduledSQLResponse(),
            self.execute(params, req, runtime)
        )

    def update_scheduled_sql(self, project, scheduled_sqlname, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_scheduled_sqlwith_options(project, scheduled_sqlname, request, headers, runtime)

    def upsert_collection_policy_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.centralize_config):
            body['centralizeConfig'] = request.centralize_config
        if not UtilClient.is_unset(request.centralize_enabled):
            body['centralizeEnabled'] = request.centralize_enabled
        if not UtilClient.is_unset(request.data_code):
            body['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.enabled):
            body['enabled'] = request.enabled
        if not UtilClient.is_unset(request.policy_config):
            body['policyConfig'] = request.policy_config
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.product_code):
            body['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/collectionpolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpsertCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def upsert_collection_policy(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upsert_collection_policy_with_options(request, headers, runtime)
