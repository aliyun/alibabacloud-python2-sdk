# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sae20190506 import models as sae_20190506_models
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
        self._endpoint = self.get_endpoint('sae', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_and_rollback_change_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_and_rollback_change_order_with_options(request, headers, runtime)

    def abort_and_rollback_change_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortAndRollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def abort_change_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_change_order_with_options(request, headers, runtime)

    def abort_change_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/AbortChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_applications(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_start_applications_with_options(request, headers, runtime)

    def batch_start_applications_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/batchStartApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStartApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_applications(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_stop_applications_with_options(request, headers, runtime)

    def batch_stop_applications_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/batchStopApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStopApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_slb(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_slb_with_options(request, headers, runtime)

    def bind_slb_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_pipeline_batch(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_pipeline_batch_with_options(request, headers, runtime)

    def confirm_pipeline_batch_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmPipelineBatch',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ConfirmPipelineBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    def create_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.kafka_endpoint):
            query['KafkaEndpoint'] = request.kafka_endpoint
        if not UtilClient.is_unset(request.kafka_instance_id):
            query['KafkaInstanceId'] = request.kafka_instance_id
        if not UtilClient.is_unset(request.kafka_logfile_config):
            query['KafkaLogfileConfig'] = request.kafka_logfile_config
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.open_collect_to_kafka):
            query['OpenCollectToKafka'] = request.open_collect_to_kafka
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.mse_feature_config):
            query['mseFeatureConfig'] = request.mse_feature_config
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/createApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_scaling_rule_with_options(request, headers, runtime)

    def create_application_scaling_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/applicationScalingRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_config_map(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_map_with_options(request, headers, runtime)

    def create_config_map_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/configmap/configMap',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    def create_grey_tag_route(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_grey_tag_route_with_options(request, headers, runtime)

    def create_grey_tag_route_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/tagroute/greyTagRoute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ingress(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ingress_with_options(request, headers, runtime)

    def create_ingress_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/ingress/Ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(request, headers, runtime)

    def create_namespace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    def delete_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/deleteApplication',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_scaling_rule_with_options(request, headers, runtime)

    def delete_application_scaling_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/applicationScalingRule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_config_map(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_map_with_options(request, headers, runtime)

    def delete_config_map_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/configmap/configMap',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_grey_tag_route(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_grey_tag_route_with_options(request, headers, runtime)

    def delete_grey_tag_route_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/tagroute/greyTagRoute',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ingress(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ingress_with_options(request, headers, runtime)

    def delete_ingress_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/ingress/Ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteIngressResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(request, headers, runtime)

    def delete_namespace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_application_with_options(request, headers, runtime)

    def deploy_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.kafka_endpoint):
            query['KafkaEndpoint'] = request.kafka_endpoint
        if not UtilClient.is_unset(request.kafka_instance_id):
            query['KafkaInstanceId'] = request.kafka_instance_id
        if not UtilClient.is_unset(request.kafka_logfile_config):
            query['KafkaLogfileConfig'] = request.kafka_logfile_config
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.mse_feature_config):
            query['MseFeatureConfig'] = request.mse_feature_config
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.open_collect_to_kafka):
            query['OpenCollectToKafka'] = request.open_collect_to_kafka
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/deployApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_service_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_service_detail_with_options(request, headers, runtime)

    def describe_app_service_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppServiceDetail',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/service/describeAppServiceDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeAppServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_config_with_options(request, headers, runtime)

    def describe_application_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/describeApplicationConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_groups_with_options(request, headers, runtime)

    def describe_application_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroups',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/describeApplicationGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_image(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_image_with_options(request, headers, runtime)

    def describe_application_image_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationImage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/container/describeApplicationImage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationImageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_instances_with_options(request, headers, runtime)

    def describe_application_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/describeApplicationInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rule_with_options(request, headers, runtime)

    def describe_application_scaling_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/applicationScalingRule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_scaling_rules(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rules_with_options(request, headers, runtime)

    def describe_application_scaling_rules_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/applicationScalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_slbs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_slbs_with_options(request, headers, runtime)

    def describe_application_slbs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationSlbs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/slb',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationSlbsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_status_with_options(request, headers, runtime)

    def describe_application_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/describeApplicationStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_change_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_change_order_with_options(request, headers, runtime)

    def describe_change_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/DescribeChangeOrder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_components_with_options(request, headers, runtime)

    def describe_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_config_map(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_map_with_options(request, headers, runtime)

    def describe_config_map_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/configmap/configMap',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_configuration_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_configuration_price_with_options(request, headers, runtime)

    def describe_configuration_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigurationPrice',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/configurationPrice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigurationPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_edas_containers(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edas_containers_with_options(headers, runtime)

    def describe_edas_containers_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdasContainers',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/resource/edasContainers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeEdasContainersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grey_tag_route(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_grey_tag_route_with_options(request, headers, runtime)

    def describe_grey_tag_route_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/tagroute/greyTagRoute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ingress(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ingress_with_options(request, headers, runtime)

    def describe_ingress_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/ingress/Ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeIngressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_log(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_log_with_options(request, headers, runtime)

    def describe_instance_log_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLog',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/instance/describeInstanceLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_specifications(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_specifications_with_options(headers, runtime)

    def describe_instance_specifications_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecifications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/quota/instanceSpecifications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_status_with_options(request, headers, runtime)

    def describe_job_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/job/describeJobStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_with_options(request, headers, runtime)

    def describe_namespace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_namespace_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_list_with_options(request, headers, runtime)

    def describe_namespace_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not UtilClient.is_unset(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceList',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/namespace/describeNamespaceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_namespace_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_resources_with_options(request, headers, runtime)

    def describe_namespace_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/namespace/describeNamespaceResources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_namespaces(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_options(request, headers, runtime)

    def describe_namespaces_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(request, headers, runtime)

    def describe_pipeline_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/DescribePipeline',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    def describe_regions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/regionConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_application_scaling_rule_with_options(request, headers, runtime)

    def disable_application_scaling_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/disableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DisableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_application_scaling_rule_with_options(request, headers, runtime)

    def enable_application_scaling_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/enableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.EnableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def exec_job(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.exec_job_with_options(request, headers, runtime)

    def exec_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/job/execJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ExecJobResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_events_with_options(request, headers, runtime)

    def list_app_events_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEvents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/listAppEvents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_services_page(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_services_page_with_options(request, headers, runtime)

    def list_app_services_page_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServicesPage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/service/listAppServicesPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesPageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_versions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_versions_with_options(request, headers, runtime)

    def list_app_versions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppVersions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/listAppVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_applications_with_options(request, headers, runtime)

    def list_applications_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/listApplications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_change_orders(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_change_orders_with_options(request, headers, runtime)

    def list_change_orders_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/ListChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_consumed_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumed_services_with_options(request, headers, runtime)

    def list_consumed_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListConsumedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_grey_tag_route(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_grey_tag_route_with_options(request, headers, runtime)

    def list_grey_tag_route_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/tagroute/greyTagRouteList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ingresses(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ingresses_with_options(request, headers, runtime)

    def list_ingresses_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIngresses',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/ingress/IngressList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListIngressesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_log_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_configs_with_options(request, headers, runtime)

    def list_log_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogConfigs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/log/listLogConfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListLogConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_namespace_change_orders(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespace_change_orders_with_options(request, headers, runtime)

    def list_namespace_change_orders_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaceChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespaceChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_namespaced_config_maps(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespaced_config_maps_with_options(request, headers, runtime)

    def list_namespaced_config_maps_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespacedConfigMaps',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespacedConfigMapsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_published_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_published_services_with_options(request, headers, runtime)

    def list_published_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListPublishedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def list_tag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def open_sae_service(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_sae_service_with_options(headers, runtime)

    def open_sae_service_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenSaeService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.OpenSaeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_resource_statics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_resource_statics_with_options(request, headers, runtime)

    def query_resource_statics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/quota/queryResourceStatics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.QueryResourceStaticsResponse(),
            self.call_api(params, req, runtime)
        )

    def reduce_application_capacity_by_instance_ids(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reduce_application_capacity_by_instance_ids_with_options(request, headers, runtime)

    def reduce_application_capacity_by_instance_ids_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReduceApplicationCapacityByInstanceIds',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def rescale_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rescale_application_with_options(request, headers, runtime)

    def rescale_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/rescaleApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def rescale_application_vertically(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rescale_application_vertically_with_options(request, headers, runtime)

    def rescale_application_vertically_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplicationVertically',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/rescaleApplicationVertically',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationVerticallyResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_application_with_options(request, headers, runtime)

    def restart_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/restartApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instances_with_options(request, headers, runtime)

    def restart_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/restartInstances',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollback_application_with_options(request, headers, runtime)

    def rollback_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/rollbackApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def start_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_application_with_options(request, headers, runtime)

    def start_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/startApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_application_with_options(request, headers, runtime)

    def stop_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/stopApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_slb(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_slb_with_options(request, headers, runtime)

    def unbind_slb_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/slb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def untag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_security_group_with_options(request, headers, runtime)

    def update_app_security_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppSecurityGroup',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/updateAppSecurityGroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateAppSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_description(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_description_with_options(request, headers, runtime)

    def update_application_description_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/updateAppDescription',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_scaling_rule_with_options(request, headers, runtime)

    def update_application_scaling_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/scale/applicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_vswitches_with_options(request, headers, runtime)

    def update_application_vswitches_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationVswitches',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/app/updateAppVswitches',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_config_map(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_map_with_options(request, headers, runtime)

    def update_config_map_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/configmap/configMap',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    def update_grey_tag_route(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_grey_tag_route_with_options(request, headers, runtime)

    def update_grey_tag_route_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/tagroute/greyTagRoute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ingress(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ingress_with_options(request, headers, runtime)

    def update_ingress_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/ingress/Ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    def update_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(request, headers, runtime)

    def update_namespace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/paas/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_namespace_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_vpc_with_options(request, headers, runtime)

    def update_namespace_vpc_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceVpc',
            version='2019-05-06',
            protocol='HTTPS',
            pathname='/pop/v1/sam/namespace/updateNamespaceVpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceVpcResponse(),
            self.call_api(params, req, runtime)
        )
