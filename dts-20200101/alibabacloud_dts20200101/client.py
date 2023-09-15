# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dts20200101 import models as dts_20200101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'dts.aliyuncs.com',
            'cn-beijing': 'dts.aliyuncs.com',
            'cn-zhangjiakou': 'dts.aliyuncs.com',
            'cn-huhehaote': 'dts.aliyuncs.com',
            'cn-hangzhou': 'dts.aliyuncs.com',
            'cn-shanghai': 'dts.aliyuncs.com',
            'cn-shenzhen': 'dts.aliyuncs.com',
            'cn-hongkong': 'dts.aliyuncs.com',
            'ap-southeast-1': 'dts.aliyuncs.com',
            'ap-southeast-2': 'dts.aliyuncs.com',
            'ap-southeast-3': 'dts.aliyuncs.com',
            'ap-southeast-5': 'dts.aliyuncs.com',
            'eu-west-1': 'dts.aliyuncs.com',
            'us-west-1': 'dts.aliyuncs.com',
            'us-east-1': 'dts.aliyuncs.com',
            'eu-central-1': 'dts.aliyuncs.com',
            'me-east-1': 'dts.aliyuncs.com',
            'ap-south-1': 'dts.aliyuncs.com',
            'cn-hangzhou-finance': 'dts.aliyuncs.com',
            'cn-shanghai-finance-1': 'dts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dts.aliyuncs.com',
            'cn-north-2-gov-1': 'dts.aliyuncs.com',
            'ap-northeast-2-pop': 'dts.aliyuncs.com',
            'cn-beijing-finance-1': 'dts.aliyuncs.com',
            'cn-beijing-finance-pop': 'dts.aliyuncs.com',
            'cn-beijing-gov-1': 'dts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dts.aliyuncs.com',
            'cn-chengdu': 'dts.aliyuncs.com',
            'cn-edge-1': 'dts.aliyuncs.com',
            'cn-fujian': 'dts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dts.aliyuncs.com',
            'cn-hangzhou-test-306': 'dts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dts.aliyuncs.com',
            'cn-qingdao-nebula': 'dts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dts.aliyuncs.com',
            'cn-shanghai-inner': 'dts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dts.aliyuncs.com',
            'cn-shenzhen-inner': 'dts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dts.aliyuncs.com',
            'cn-wuhan': 'dts.aliyuncs.com',
            'cn-wulanchabu': 'dts.aliyuncs.com',
            'cn-yushanfang': 'dts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dts.aliyuncs.com',
            'eu-west-1-oxs': 'dts.aliyuncs.com',
            'rus-west-1-pop': 'dts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def configure_dts_job_with_options(self, request, runtime):
        """
        The name of the DTS instance.
        

        @param request: ConfigureDtsJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigureDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_check_configure):
            query['DataCheckConfigure'] = request.data_check_configure
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_owner_id):
            query['DestinationEndpointOwnerID'] = request.destination_endpoint_owner_id
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_role):
            query['DestinationEndpointRole'] = request.destination_endpoint_role
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.disaster_recovery_job):
            query['DisasterRecoveryJob'] = request.disaster_recovery_job
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.source_endpoint_vswitch_id):
            query['SourceEndpointVSwitchID'] = request.source_endpoint_vswitch_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list):
            body['DbList'] = request.db_list
        if not UtilClient.is_unset(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_dts_job(self, request):
        """
        The name of the DTS instance.
        

        @param request: ConfigureDtsJobRequest

        @return: ConfigureDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_dts_job_with_options(request, runtime)

    def configure_dts_job_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Dts',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        configure_dts_job_req = dts_20200101_models.ConfigureDtsJobRequest()
        OpenApiUtilClient.convert(request, configure_dts_job_req)
        if not UtilClient.is_unset(request.file_oss_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            configure_dts_job_req.file_oss_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        configure_dts_job_resp = self.configure_dts_job_with_options(configure_dts_job_req, runtime)
        return configure_dts_job_resp

    def configure_migration_job_with_options(self, request, runtime):
        """
        After you call this operation to configure a data migration task, the task will be automatically started. You do not need to call the [StartMigrationJob](~~49429~~) operation to start the task.
        A data migration task may fail to be started due to precheck failures. You can call the [DescribeMigrationJobStatus](~~49433~~) operation to query the error messages about precheck failures. Then, you can fix the issue based on the error messages. After you fix the issue, you must call the [StartMigrationJob](~~49429~~) operation to restart the data migration task.
        

        @param request: ConfigureMigrationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigureMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_migration_job(self, request):
        """
        After you call this operation to configure a data migration task, the task will be automatically started. You do not need to call the [StartMigrationJob](~~49429~~) operation to start the task.
        A data migration task may fail to be started due to precheck failures. You can call the [DescribeMigrationJobStatus](~~49433~~) operation to query the error messages about precheck failures. Then, you can fix the issue based on the error messages. After you fix the issue, you must call the [StartMigrationJob](~~49429~~) operation to restart the data migration task.
        

        @param request: ConfigureMigrationJobRequest

        @return: ConfigureMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    def configure_migration_job_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureMigrationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_migration_job_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_alert_with_options(request, runtime)

    def configure_subscription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserve):
            query['Reserve'] = request.reserve
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not UtilClient.is_unset(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_with_options(request, runtime)

    def configure_subscription_instance_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *ConfigureSubscriptionInstance**.
        

        @param request: ConfigureSubscriptionInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigureSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not UtilClient.is_unset(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not UtilClient.is_unset(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_subscription_instance(self, request):
        """
        The operation that you want to perform. Set the value to *ConfigureSubscriptionInstance**.
        

        @param request: ConfigureSubscriptionInstanceRequest

        @return: ConfigureSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_with_options(request, runtime)

    def configure_subscription_instance_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_subscription_instance_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_alert_with_options(request, runtime)

    def configure_synchronization_job_with_options(self, request, runtime):
        """
        Before you call this operation, you must call the [CreateSynchronizationJob](~~49446~~) operation to create a data synchronization instance.
        >
        *   After you call this operation to configure a data synchronization task, the task will be automatically started and prechecked. You do not need to call the [StartSynchronizationJob](~~49448~~) operation to start the task.
        *   A data synchronization task may fail to be started due to precheck failures. You can call the [DescribeSynchronizationJobStatus](~~49453~~) operation to query the status of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the [StartSynchronizationJob](~~49448~~) operation to restart the data synchronization task.
        

        @param request: ConfigureSynchronizationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigureSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_synchronization_job(self, request):
        """
        Before you call this operation, you must call the [CreateSynchronizationJob](~~49446~~) operation to create a data synchronization instance.
        >
        *   After you call this operation to configure a data synchronization task, the task will be automatically started and prechecked. You do not need to call the [StartSynchronizationJob](~~49448~~) operation to start the task.
        *   A data synchronization task may fail to be started due to precheck failures. You can call the [DescribeSynchronizationJobStatus](~~49453~~) operation to query the status of the task. Then, you can change parameter settings based on the error messages about the precheck failures. After you fix the issue, you must call the [StartSynchronizationJob](~~49448~~) operation to restart the data synchronization task.
        

        @param request: ConfigureSynchronizationJobRequest

        @return: ConfigureSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    def configure_synchronization_job_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_synchronization_job_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_alert_with_options(request, runtime)

    def configure_synchronization_job_replicator_compare_with_options(self, request, runtime):
        """
        When you use Data Transmission Service (DTS) to synchronize data, other data sources may write data to the destination instance. In this case, data may become inconsistent between the source and destination instances. To ensure data consistency, you can enable image matching.
        After you call this operation, you can call the [DescribeSynchronizationJobReplicatorCompare](~~199183~~) operation to verify whether image matching is enabled for the data synchronization instance.
        

        @param request: ConfigureSynchronizationJobReplicatorCompareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigureSynchronizationJobReplicatorCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_synchronization_job_replicator_compare(self, request):
        """
        When you use Data Transmission Service (DTS) to synchronize data, other data sources may write data to the destination instance. In this case, data may become inconsistent between the source and destination instances. To ensure data consistency, you can enable image matching.
        After you call this operation, you can call the [DescribeSynchronizationJobReplicatorCompare](~~199183~~) operation to verify whether image matching is enabled for the data synchronization instance.
        

        @param request: ConfigureSynchronizationJobReplicatorCompareRequest

        @return: ConfigureSynchronizationJobReplicatorCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_replicator_compare_with_options(request, runtime)

    def count_job_by_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountJobByCondition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CountJobByConditionResponse(),
            self.call_api(params, req, runtime)
        )

    def count_job_by_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_job_by_condition_with_options(request, runtime)

    def create_consumer_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_consumer_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_channel_with_options(request, runtime)

    def create_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    def create_dedicated_cluster_monitor_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_alarm_threshold):
            query['CpuAlarmThreshold'] = request.cpu_alarm_threshold
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.disk_alarm_threshold):
            query['DiskAlarmThreshold'] = request.disk_alarm_threshold
        if not UtilClient.is_unset(request.du_alarm_threshold):
            query['DuAlarmThreshold'] = request.du_alarm_threshold
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mem_alarm_threshold):
            query['MemAlarmThreshold'] = request.mem_alarm_threshold
        if not UtilClient.is_unset(request.notice_switch):
            query['NoticeSwitch'] = request.notice_switch
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phones):
            query['Phones'] = request.phones
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedClusterMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateDedicatedClusterMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_cluster_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_cluster_monitor_rule_with_options(request, runtime)

    def create_dts_instance_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of DTS.
        *   If you want to run a DTS task on a DTS dedicated cluster, you must configure the task before you purchase a DTS instance. You can call the [ConfigureDtsJob](~~208399~~) operation to configure a DTS task.
        

        @param request: CreateDtsInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDtsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not UtilClient.is_unset(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.du):
            query['Du'] = request.du
        if not UtilClient.is_unset(request.fee_type):
            query['FeeType'] = request.fee_type
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDtsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateDtsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dts_instance(self, request):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/apsaradb-for-mongodb/pricing) of DTS.
        *   If you want to run a DTS task on a DTS dedicated cluster, you must configure the task before you purchase a DTS instance. You can call the [ConfigureDtsJob](~~208399~~) operation to configure a DTS task.
        

        @param request: CreateDtsInstanceRequest

        @return: CreateDtsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dts_instance_with_options(request, runtime)

    def create_job_monitor_rule_with_options(self, request, runtime):
        """
        DTS provides the following metrics for DTS tasks:***********\
        *   **Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. Unit: seconds.
        *   **Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
        *   **Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. Unit: hours.
        

        @param request: CreateJobMonitorRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateJobMonitorRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.notice_value):
            query['NoticeValue'] = request.notice_value
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.times):
            query['Times'] = request.times
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateJobMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job_monitor_rule(self, request):
        """
        DTS provides the following metrics for DTS tasks:***********\
        *   **Latency**: DTS monitors the latency of a DTS task. If the latency of the task exceeds the specified threshold, an alert is triggered. Unit: seconds.
        *   **Status**: DTS monitors the status of a DTS task. If the state of the task changes to **Error** or **Restore**, an alert is triggered.
        *   **Full Timeout**: DTS monitors the duration of a DTS task. If the duration of the task exceeds the specified threshold, an alert is triggered. Unit: hours.
        

        @param request: CreateJobMonitorRuleRequest

        @return: CreateJobMonitorRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_monitor_rule_with_options(request, runtime)

    def create_migration_job_with_options(self, request, runtime):
        """
        >  This API operation is outdated. We recommend that you use the new version. For more information, see [CreateDtsInstance](~~208270~~).
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS).
        After you purchase a data migration instance, you must call the [ConfigureMigrationJob](~~324260~~) operation to configure a data migration task.
        

        @param request: CreateMigrationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_migration_job(self, request):
        """
        >  This API operation is outdated. We recommend that you use the new version. For more information, see [CreateDtsInstance](~~208270~~).
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS).
        After you purchase a data migration instance, you must call the [ConfigureMigrationJob](~~324260~~) operation to configure a data migration task.
        

        @param request: CreateMigrationJobRequest

        @return: CreateMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    def create_subscription_instance_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS).
        

        @param request: CreateSubscriptionInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subscription_instance(self, request):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS).
        

        @param request: CreateSubscriptionInstanceRequest

        @return: CreateSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_instance_with_options(request, runtime)

    def create_synchronization_job_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS).
        After you purchase a data synchronization instance, you must call the [ConfigureSynchronizationJob](~~49447~~) operation to configure a data synchronization task. Then, the task is automatically started.
        

        @param request: CreateSynchronizationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.network_type):
            query['networkType'] = request.network_type
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_synchronization_job(self, request):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS).
        After you purchase a data synchronization instance, you must call the [ConfigureSynchronizationJob](~~49447~~) operation to configure a data synchronization task. Then, the task is automatically started.
        

        @param request: CreateSynchronizationJobRequest

        @return: CreateSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

    def delete_consumer_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_consumer_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_channel_with_options(request, runtime)

    def delete_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    def delete_dts_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dts_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dts_job_with_options(request, runtime)

    def delete_dts_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dts_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dts_jobs_with_options(request, runtime)

    def delete_migration_job_with_options(self, request, runtime):
        """
        >  After a data migration instance is released, it cannot be recovered.
        

        @param request: DeleteMigrationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_migration_job(self, request):
        """
        >  After a data migration instance is released, it cannot be recovered.
        

        @param request: DeleteMigrationJobRequest

        @return: DeleteMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    def delete_subscription_instance_with_options(self, request, runtime):
        """
        >  After a change tracking instance is released, it cannot be recovered.
        

        @param request: DeleteSubscriptionInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subscription_instance(self, request):
        """
        >  After a change tracking instance is released, it cannot be recovered.
        

        @param request: DeleteSubscriptionInstanceRequest

        @return: DeleteSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_subscription_instance_with_options(request, runtime)

    def delete_synchronization_job_with_options(self, request, runtime):
        """
        >  After a data synchronization instance is released, it cannot be recovered.
        

        @param request: DeleteSynchronizationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_synchronization_job(self, request):
        """
        >  After a data synchronization instance is released, it cannot be recovered.
        

        @param request: DeleteSynchronizationJobRequest

        @return: DeleteSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    def describe_channel_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAccount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeChannelAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_account_with_options(request, runtime)

    def describe_check_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeCheckJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_jobs_with_options(request, runtime)

    def describe_cluster_operate_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterOperateLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeClusterOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_operate_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_operate_logs_with_options(request, runtime)

    def describe_cluster_used_utilization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            body['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterUsedUtilization',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeClusterUsedUtilizationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_used_utilization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_used_utilization_with_options(request, runtime)

    def describe_connection_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConnectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_connection_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_connection_status_with_options(request, runtime)

    def describe_consumer_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_consumer_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_channel_with_options(request, runtime)

    def describe_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_group_with_options(request, runtime)

    def describe_dtsipwith_options(self, request, runtime):
        """
        If the *source or destination instance** is an **on-premises database**, you need to call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the security settings of the source or destination instance, for example, the firewall of your database. For more information, see [Add the CIDR blocks of DTS servers to the security settings of on-premises databases](~~176627~~).
        >  If the **source or destination database** is an **ApsaraDB database instance** (such as RDS instance and ApsaraDB for MongoDB instance) or a **self-managed database hosted on ECS**, you do not need to add the CIDR blocks. When you click **Set Whitelist and Next** in the DTS console, DTS automatically add the CIDR blocks of DTS servers to the security settings of the source or destination instance.
        

        @param request: DescribeDTSIPRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDTSIPResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDTSIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDTSIPResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dtsip(self, request):
        """
        If the *source or destination instance** is an **on-premises database**, you need to call this operation to query the CIDR blocks of DTS servers. Then, you need to add the CIDR blocks of DTS servers to the security settings of the source or destination instance, for example, the firewall of your database. For more information, see [Add the CIDR blocks of DTS servers to the security settings of on-premises databases](~~176627~~).
        >  If the **source or destination database** is an **ApsaraDB database instance** (such as RDS instance and ApsaraDB for MongoDB instance) or a **self-managed database hosted on ECS**, you do not need to add the CIDR blocks. When you click **Set Whitelist and Next** in the DTS console, DTS automatically add the CIDR blocks of DTS servers to the security settings of the source or destination instance.
        

        @param request: DescribeDTSIPRequest

        @return: DescribeDTSIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dtsipwith_options(request, runtime)

    def describe_data_check_report_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckReportUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDataCheckReportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_check_report_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_check_report_url_with_options(request, runtime)

    def describe_data_check_table_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckTableDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDataCheckTableDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_check_table_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_check_table_details_with_options(request, runtime)

    def describe_data_check_table_diff_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tb_name):
            query['TbName'] = request.tb_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCheckTableDiffDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDataCheckTableDiffDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_check_table_diff_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_check_table_diff_details_with_options(request, runtime)

    def describe_dedicated_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_with_options(request, runtime)

    def describe_dedicated_cluster_monitor_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedClusterMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDedicatedClusterMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_cluster_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_cluster_monitor_rule_with_options(request, runtime)

    def describe_dts_etl_job_version_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsEtlJobVersionInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dts_etl_job_version_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_etl_job_version_info_with_options(request, runtime)

    def describe_dts_job_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dts_job_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_job_detail_with_options(request, runtime)

    def describe_dts_jobs_with_options(self, request, runtime):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Dts\\&api=DescribeDtsJobs\\&type=RPC\\&version=2020-01-01)
        

        @param request: DescribeDtsJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDtsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_bis_label):
            query['DtsBisLabel'] = request.dts_bis_label
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.without_db_list):
            query['WithoutDbList'] = request.without_db_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dts_jobs(self, request):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Dts\\&api=DescribeDtsJobs\\&type=RPC\\&version=2020-01-01)
        

        @param request: DescribeDtsJobsRequest

        @return: DescribeDtsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_jobs_with_options(request, runtime)

    def describe_dts_service_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsServiceLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dts_service_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_service_log_with_options(request, runtime)

    def describe_endpoint_switch_status_with_options(self, request, runtime):
        """
        Before you call this operation, you must call the [SwitchSynchronizationEndpoint](~~201858~~) operation to change the database connection settings.
        

        @param request: DescribeEndpointSwitchStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEndpointSwitchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpointSwitchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_endpoint_switch_status(self, request):
        """
        Before you call this operation, you must call the [SwitchSynchronizationEndpoint](~~201858~~) operation to change the database connection settings.
        

        @param request: DescribeEndpointSwitchStatusRequest

        @return: DescribeEndpointSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_switch_status_with_options(request, runtime)

    def describe_etl_job_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEtlJobLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeEtlJobLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_etl_job_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_etl_job_logs_with_options(request, runtime)

    def describe_initialization_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInitializationStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeInitializationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_initialization_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_initialization_status_with_options(request, runtime)

    def describe_job_monitor_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeJobMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_job_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_job_monitor_rule_with_options(request, runtime)

    def describe_metric_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dts_job_id):
            body['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.metric_name):
            body['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            body['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetricList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    def describe_migration_job_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_job_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_alert_with_options(request, runtime)

    def describe_migration_job_detail_with_options(self, request, runtime):
        """
        When you call this operation, the data migration task must be in the Migrating, Failed, Paused, or Finished state.
        

        @param request: DescribeMigrationJobDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMigrationJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_job_detail(self, request):
        """
        When you call this operation, the data migration task must be in the Migrating, Failed, Paused, or Finished state.
        

        @param request: DescribeMigrationJobDetailRequest

        @return: DescribeMigrationJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_detail_with_options(request, runtime)

    def describe_migration_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    def describe_migration_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_jobs_with_options(request, runtime)

    def describe_pre_check_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribePreCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pre_check_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_status_with_options(request, runtime)

    def describe_subscription_instance_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_instance_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_alert_with_options(request, runtime)

    def describe_subscription_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_status_with_options(request, runtime)

    def describe_subscription_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instances_with_options(request, runtime)

    def describe_subscription_meta_with_options(self, tmp_req, runtime):
        """
        When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task.
        *   You can call the [DescribeDtsJobs](~~209702~~) operation to query the ID of the change tracking instance and the ID of the consumer group.
        

        @param tmp_req: DescribeSubscriptionMetaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSubscriptionMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.DescribeSubscriptionMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionMeta',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_meta(self, request):
        """
        When Data Transmission Service (DTS) tracks data changes from a PolarDB-X 1.0 instance, data is distributed across the attached ApsaraDB RDS for MySQL instances. DTS runs a subtask for each ApsaraDB RDS for MySQL instance. You can call this operation to query the details of the subtasks in a distributed change tracking task.
        *   You can call the [DescribeDtsJobs](~~209702~~) operation to query the ID of the change tracking instance and the ID of the consumer group.
        

        @param request: DescribeSubscriptionMetaRequest

        @return: DescribeSubscriptionMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_meta_with_options(request, runtime)

    def describe_synchronization_job_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_job_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_alert_with_options(request, runtime)

    def describe_synchronization_job_replicator_compare_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_job_replicator_compare(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_replicator_compare_with_options(request, runtime)

    def describe_synchronization_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_with_options(request, runtime)

    def describe_synchronization_job_status_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatusList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_job_status_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_list_with_options(request, runtime)

    def describe_synchronization_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_jobs_with_options(request, runtime)

    def describe_synchronization_object_modify_status_with_options(self, request, runtime):
        """
        Before you call this operation, you must call the [ModifySynchronizationObject](~~49451~~) operation to obtain the task ID.
        

        @param request: DescribeSynchronizationObjectModifyStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSynchronizationObjectModifyStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationObjectModifyStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_object_modify_status(self, request):
        """
        Before you call this operation, you must call the [ModifySynchronizationObject](~~49451~~) operation to obtain the task ID.
        

        @param request: DescribeSynchronizationObjectModifyStatusRequest

        @return: DescribeSynchronizationObjectModifyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    def describe_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    def describe_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagValues',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_values_with_options(request, runtime)

    def init_dts_rds_instance_with_options(self, request, runtime):
        """
        The node must be an ApsaraDB RDS for MySQL instance or a self-managed MySQL database that is connected over Cloud Enterprise Network (CEN).
        *   This operation is used to initialize the built-in account named rdsdt_dtsacct on a node of an active geo-redundancy database cluster. DTS uses this account to connect to the node and perform data synchronization tasks.
        

        @param request: InitDtsRdsInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InitDtsRdsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDtsRdsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.InitDtsRdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def init_dts_rds_instance(self, request):
        """
        The node must be an ApsaraDB RDS for MySQL instance or a self-managed MySQL database that is connected over Cloud Enterprise Network (CEN).
        *   This operation is used to initialize the built-in account named rdsdt_dtsacct on a node of an active geo-redundancy database cluster. DTS uses this account to connect to the node and perform data synchronization tasks.
        

        @param request: InitDtsRdsInstanceRequest

        @return: InitDtsRdsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_dts_rds_instance_with_options(request, runtime)

    def list_dedicated_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ListDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dedicated_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dedicated_cluster_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        ***\
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        ***\
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_consumer_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_consumer_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_channel_with_options(request, runtime)

    def modify_consumer_group_password_with_options(self, request, runtime):
        """
        >
        *   This operation is applicable to only the new version of the change tracking feature. To use the new version, you must specify the SubscriptionInstanceNetworkType parameter when you call the ConfigureSubscriptionInstance operation. If you use the previous version, you do not need to specify the **SubscriptionInstanceNetworkType** parameter.
        *   When you call this operation, the change tracking task must be in the NotStarted, Failed, Normal, or Abnormal state.
        

        @param request: ModifyConsumerGroupPasswordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyConsumerGroupPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerGroupPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_consumer_group_password(self, request):
        """
        >
        *   This operation is applicable to only the new version of the change tracking feature. To use the new version, you must specify the SubscriptionInstanceNetworkType parameter when you call the ConfigureSubscriptionInstance operation. If you use the previous version, you do not need to specify the **SubscriptionInstanceNetworkType** parameter.
        *   When you call this operation, the change tracking task must be in the NotStarted, Failed, Normal, or Abnormal state.
        

        @param request: ModifyConsumerGroupPasswordRequest

        @return: ModifyConsumerGroupPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_group_password_with_options(request, runtime)

    def modify_consumption_timestamp_with_options(self, request, runtime):
        """
        >
        *   This operation is applicable to only the previous version of the change tracking feature. To use the new version, you must specify the SubscriptionInstanceNetworkType parameter when you call the [ConfigureSubscriptionInstance](~~49437~~) operation. If you use the previous version, you do not need to specify the **SubscriptionInstanceNetworkType** parameter.
        *   If you use the new version, you need to set the consumption checkpoint on the change tracking client.
        *   When you call this operation, you must stop the change tracking client, and the change tracking task must be in the Normal state.
        

        @param request: ModifyConsumptionTimestampRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyConsumptionTimestampResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumptionTimestamp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumptionTimestampResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_consumption_timestamp(self, request):
        """
        >
        *   This operation is applicable to only the previous version of the change tracking feature. To use the new version, you must specify the SubscriptionInstanceNetworkType parameter when you call the [ConfigureSubscriptionInstance](~~49437~~) operation. If you use the previous version, you do not need to specify the **SubscriptionInstanceNetworkType** parameter.
        *   If you use the new version, you need to set the consumption checkpoint on the change tracking client.
        *   When you call this operation, you must stop the change tracking client, and the change tracking task must be in the Normal state.
        

        @param request: ModifyConsumptionTimestampRequest

        @return: ModifyConsumptionTimestampResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_consumption_timestamp_with_options(request, runtime)

    def modify_dedicated_cluster_with_options(self, request, runtime):
        """
        You can modify only the overcommit ratio.
        

        @param request: ModifyDedicatedClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDedicatedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oversold_ratio):
            query['OversoldRatio'] = request.oversold_ratio
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_cluster(self, request):
        """
        You can modify only the overcommit ratio.
        

        @param request: ModifyDedicatedClusterRequest

        @return: ModifyDedicatedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_cluster_with_options(request, runtime)

    def modify_dts_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.ModifyDtsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_list):
            request.db_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.file_oss_url):
            query['FileOssUrl'] = request.file_oss_url
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not UtilClient.is_unset(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not UtilClient.is_unset(request.filter_table_name):
            body['FilterTableName'] = request.filter_table_name
        if not UtilClient.is_unset(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not UtilClient.is_unset(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dts_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_with_options(request, runtime)

    def modify_dts_job_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Dts',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        modify_dts_job_req = dts_20200101_models.ModifyDtsJobRequest()
        OpenApiUtilClient.convert(request, modify_dts_job_req)
        if not UtilClient.is_unset(request.file_oss_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.file_oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            modify_dts_job_req.file_oss_url = 'http://%s.%s/%s' % (TeaConverter.to_unicode(auth_response.body.bucket), TeaConverter.to_unicode(auth_response.body.endpoint), TeaConverter.to_unicode(auth_response.body.object_key))
        modify_dts_job_resp = self.modify_dts_job_with_options(modify_dts_job_req, runtime)
        return modify_dts_job_resp

    def modify_dts_job_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dts_job_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_config_with_options(request, runtime)

    def modify_dts_job_dedicated_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dts_job_dedicated_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_dedicated_cluster_with_options(request, runtime)

    def modify_dts_job_du_limit_with_options(self, request, runtime):
        """
        DTS allows you to upgrade or downgrade the configurations of DTS instances in a dedicated cluster. You can adjust the resources that are occupied for task execution to dynamically adjust the number of tasks that can be scheduled in the cluster. This way, you can reduce the total number of DUs required for the cluster or release DUs.
        *   Before you modify the upper limit of DUs for a DTS task, make sure that sufficient DUs are available.
        

        @param request: ModifyDtsJobDuLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDtsJobDuLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.du_limit):
            query['DuLimit'] = request.du_limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobDuLimit',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobDuLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dts_job_du_limit(self, request):
        """
        DTS allows you to upgrade or downgrade the configurations of DTS instances in a dedicated cluster. You can adjust the resources that are occupied for task execution to dynamically adjust the number of tasks that can be scheduled in the cluster. This way, you can reduce the total number of DUs required for the cluster or release DUs.
        *   Before you modify the upper limit of DUs for a DTS task, make sure that sufficient DUs are available.
        

        @param request: ModifyDtsJobDuLimitRequest

        @return: ModifyDtsJobDuLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_du_limit_with_options(request, runtime)

    def modify_dts_job_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobNameResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dts_job_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_name_with_options(request, runtime)

    def modify_dts_job_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dts_job_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_password_with_options(request, runtime)

    def modify_dynamic_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_list):
            query['ConfigList'] = request.config_list
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.enable_limit):
            query['EnableLimit'] = request.enable_limit
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDynamicConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDynamicConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dynamic_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dynamic_config_with_options(request, runtime)

    def modify_subscription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_with_options(request, runtime)

    def modify_subscription_object_with_options(self, request, runtime):
        """
        When you call this operation, the change tracking task must be in the Normal, NotStarted, or Failed state.
        >
        *   If you call this operation to modify the objects of a change tracking task that is in the Normal state, DTS automatically calls the [StartSubscriptionInstance](~~49438~~) to restart the task.
        *   If you call this operation to modify the objects of a change tracking task that is in the NotStarted or Failed state, DTS does not automatically start the task. You must call the [StartSubscriptionInstance](~~49438~~) to restart the task.
        

        @param request: ModifySubscriptionObjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySubscriptionObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySubscriptionObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_subscription_object(self, request):
        """
        When you call this operation, the change tracking task must be in the Normal, NotStarted, or Failed state.
        >
        *   If you call this operation to modify the objects of a change tracking task that is in the Normal state, DTS automatically calls the [StartSubscriptionInstance](~~49438~~) to restart the task.
        *   If you call this operation to modify the objects of a change tracking task that is in the NotStarted or Failed state, DTS does not automatically start the task. You must call the [StartSubscriptionInstance](~~49438~~) to restart the task.
        

        @param request: ModifySubscriptionObjectRequest

        @return: ModifySubscriptionObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_object_with_options(request, runtime)

    def modify_synchronization_object_with_options(self, request, runtime):
        """
        >  When you call this operation, the data synchronization task must be in the Not Started or Synchronizing state.
        

        @param request: ModifySynchronizationObjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySynchronizationObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySynchronizationObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_synchronization_object(self, request):
        """
        >  When you call this operation, the data synchronization task must be in the Not Started or Synchronizing state.
        

        @param request: ModifySynchronizationObjectRequest

        @return: ModifySynchronizationObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def reset_dts_job_with_options(self, request, runtime):
        """
        >  If you clear the configurations of a data synchronization or change tracking task, DTS deletes the task. Then, DTS creates another task. The task is in the Not Configured state. You must call the [ConfigureDtsJob](~~208399~~) operation reconfigure the task.
        

        @param request: ResetDtsJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ResetDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_dts_job(self, request):
        """
        >  If you clear the configurations of a data synchronization or change tracking task, DTS deletes the task. Then, DTS creates another task. The task is in the Not Configured state. You must call the [ConfigureDtsJob](~~208399~~) operation reconfigure the task.
        

        @param request: ResetDtsJobRequest

        @return: ResetDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_dts_job_with_options(request, runtime)

    def reset_synchronization_job_with_options(self, request, runtime):
        """
        >  If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the *ConfigureSynchronizationJob** operation to reconfigure the task.
        

        @param request: ResetSynchronizationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ResetSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_synchronization_job(self, request):
        """
        >  If you clear the configurations of a data synchronization task, the task will be released. To start the task again, you must call the *ConfigureSynchronizationJob** operation to reconfigure the task.
        

        @param request: ResetSynchronizationJobRequest

        @return: ResetSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_synchronization_job_with_options(request, runtime)

    def reverse_two_way_direction_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.ignore_error_sub_job):
            query['IgnoreErrorSubJob'] = request.ignore_error_sub_job
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReverseTwoWayDirection',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ReverseTwoWayDirectionResponse(),
            self.call_api(params, req, runtime)
        )

    def reverse_two_way_direction(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reverse_two_way_direction_with_options(request, runtime)

    def shield_precheck_with_options(self, request, runtime):
        """
        If you call this operation to ignore all precheck items, you must call the [StartMigrationJob](https://www.alibabacloud.com/help/zh/doc-detail/49429.htm) or [StartSynchronizationJob](https://www.alibabacloud.com/help/zh/doc-detail/49448.htm) operation. DTS performs a precheck again. After the data migration or synchronization task passes the precheck, the task will be automatically started.
        

        @param request: ShieldPrecheckRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ShieldPrecheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ShieldPrecheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ShieldPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    def shield_precheck(self, request):
        """
        If you call this operation to ignore all precheck items, you must call the [StartMigrationJob](https://www.alibabacloud.com/help/zh/doc-detail/49429.htm) or [StartSynchronizationJob](https://www.alibabacloud.com/help/zh/doc-detail/49448.htm) operation. DTS performs a precheck again. After the data migration or synchronization task passes the precheck, the task will be automatically started.
        

        @param request: ShieldPrecheckRequest

        @return: ShieldPrecheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.shield_precheck_with_options(request, runtime)

    def skip_pre_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not UtilClient.is_unset(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipPreCheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SkipPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.skip_pre_check_with_options(request, runtime)

    def start_dts_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dts_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dts_job_with_options(request, runtime)

    def start_dts_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dts_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dts_jobs_with_options(request, runtime)

    def start_migration_job_with_options(self, request, runtime):
        """
        >  When you call this operation, the data migration task must be in the Not Started, Paused, or Migration Failed state.
        

        @param request: StartMigrationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_migration_job(self, request):
        """
        >  When you call this operation, the data migration task must be in the Not Started, Paused, or Migration Failed state.
        

        @param request: StartMigrationJobRequest

        @return: StartMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    def start_subscription_instance_with_options(self, request, runtime):
        """
        When you call this operation, the change tracking task must be in the NotStarted or Failed state.
        

        @param request: StartSubscriptionInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartSubscriptionInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_subscription_instance(self, request):
        """
        When you call this operation, the change tracking task must be in the NotStarted or Failed state.
        

        @param request: StartSubscriptionInstanceRequest

        @return: StartSubscriptionInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_subscription_instance_with_options(request, runtime)

    def start_synchronization_job_with_options(self, request, runtime):
        """
        >
        *   Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service) of Data Transmission Service (DTS).
        *   When you call this operation, the data synchronization task must be in the NotStarted, Failed, or Suspending state. If you call this operation to start a task that is in the NotStarted state, the task will be prechecked.
        

        @param request: StartSynchronizationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_synchronization_job(self, request):
        """
        >
        *   Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service) of Data Transmission Service (DTS).
        *   When you call this operation, the data synchronization task must be in the NotStarted, Failed, or Suspending state. If you call this operation to start a task that is in the NotStarted state, the task will be prechecked.
        

        @param request: StartSynchronizationJobRequest

        @return: StartSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    def stop_dedicated_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_name):
            query['DedicatedClusterName'] = request.dedicated_cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDedicatedCluster',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDedicatedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dedicated_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dedicated_cluster_with_options(request, runtime)

    def stop_dts_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dts_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dts_job_with_options(request, runtime)

    def stop_dts_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dts_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dts_jobs_with_options(request, runtime)

    def stop_migration_job_with_options(self, request, runtime):
        """
        >  After you call this operation to stop a data migration task, the status of the task changes to Finished and you cannot restart the task by calling the [StartMigrationJob](~~49429~~) operation.
        

        @param request: StopMigrationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_migration_job(self, request):
        """
        >  After you call this operation to stop a data migration task, the status of the task changes to Finished and you cannot restart the task by calling the [StartMigrationJob](~~49429~~) operation.
        

        @param request: StopMigrationJobRequest

        @return: StopMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    def summary_job_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SummaryJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def summary_job_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.summary_job_detail_with_options(request, runtime)

    def suspend_dts_job_with_options(self, request, runtime):
        """
        ***\
        

        @param request: SuspendDtsJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SuspendDtsJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_dts_job(self, request):
        """
        ***\
        

        @param request: SuspendDtsJobRequest

        @return: SuspendDtsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_dts_job_with_options(request, runtime)

    def suspend_dts_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_dts_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_dts_jobs_with_options(request, runtime)

    def suspend_migration_job_with_options(self, request, runtime):
        """
        >
        *   If a data migration task is performing incremental data migration, we recommend that you do not pause the task for more than 6 hours. Otherwise, you will not be able to call the [StartMigrationJob](~~49429~~) operation to restart the task.
        *   If you select incremental data migration as the migration type for a pay-as-you-go instance, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, incremental data migration consumes resources such as the bandwidth of the source database.
        

        @param request: SuspendMigrationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SuspendMigrationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_migration_job(self, request):
        """
        >
        *   If a data migration task is performing incremental data migration, we recommend that you do not pause the task for more than 6 hours. Otherwise, you will not be able to call the [StartMigrationJob](~~49429~~) operation to restart the task.
        *   If you select incremental data migration as the migration type for a pay-as-you-go instance, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, incremental data migration consumes resources such as the bandwidth of the source database.
        

        @param request: SuspendMigrationJobRequest

        @return: SuspendMigrationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    def suspend_synchronization_job_with_options(self, request, runtime):
        """
        >
        *   When you call this operation, the data synchronization task must be in the Synchronizing state.
        *   We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
        *   If the billing method is pay-as-you-go, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data synchronization consumes resources such as the bandwidth of the source database.
        

        @param request: SuspendSynchronizationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SuspendSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_synchronization_job(self, request):
        """
        >
        *   When you call this operation, the data synchronization task must be in the Synchronizing state.
        *   We recommend that you do not pause a data synchronization task for more than 6 hours. Otherwise, the task cannot be started again.
        *   If the billing method is pay-as-you-go, DTS charges a fee even when the task is paused. This is because DTS only stops writing data to the destination database. DTS continues to pull the logs of the source database so that the task can resume quickly after it is restarted. Therefore, data synchronization consumes resources such as the bandwidth of the source database.
        

        @param request: SuspendSynchronizationJobRequest

        @return: SuspendSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)

    def switch_physical_dts_job_to_cloud_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchPhysicalDtsJobToCloud',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SwitchPhysicalDtsJobToCloudResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_physical_dts_job_to_cloud(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_physical_dts_job_to_cloud_with_options(request, runtime)

    def switch_synchronization_endpoint_with_options(self, request, runtime):
        """
        If the source or destination database is a self-managed MySQL database connected over the Internet, Elastic Compute Service (ECS) or Express Connect, you must call this operation to update the connection settings.
        *   If the source or destination database is hosted on an ApsaraDB instance (such as ApsaraDB RDS instance and ApsaraDB for MongoDB instance), DTS automatically updates the connection settings. You do not need to call this operation.
        > *   For two-way synchronization tasks, if you perform a primary/secondary switchover on the source or destination database, you must call this operation twice to update the connection settings.
        For example, if you perform a primary/secondary switchover on the destination database of the forward direction, you must call this operation twice. In the first call, set the **SynchronizationDirection** parameter to **Forward**, set the **Endpoint.Type **parameter to **Destination**, and configure the connection settings. In the second call, set the **SynchronizationDirection** parameter to **Reverse**, set the **Endpoint.Type **parameter to **Source**, and configure the connection settings.
        

        @param request: SwitchSynchronizationEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchSynchronizationEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSynchronizationEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SwitchSynchronizationEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_synchronization_endpoint(self, request):
        """
        If the source or destination database is a self-managed MySQL database connected over the Internet, Elastic Compute Service (ECS) or Express Connect, you must call this operation to update the connection settings.
        *   If the source or destination database is hosted on an ApsaraDB instance (such as ApsaraDB RDS instance and ApsaraDB for MongoDB instance), DTS automatically updates the connection settings. You do not need to call this operation.
        > *   For two-way synchronization tasks, if you perform a primary/secondary switchover on the source or destination database, you must call this operation twice to update the connection settings.
        For example, if you perform a primary/secondary switchover on the destination database of the forward direction, you must call this operation twice. In the first call, set the **SynchronizationDirection** parameter to **Forward**, set the **Endpoint.Type **parameter to **Destination**, and configure the connection settings. In the second call, set the **SynchronizationDirection** parameter to **Reverse**, set the **Endpoint.Type **parameter to **Source**, and configure the connection settings.
        

        @param request: SwitchSynchronizationEndpointRequest

        @return: SwitchSynchronizationEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_synchronization_endpoint_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        If you have a large number of instances, you can create multiple tags and bind these tags to the instances. Then, you can filter the instances by tag.
        *   A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        *   If the tag that you specify does not exist, this tag is automatically created and bound to the specified instance.
        *   If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        *   You can bind up to 20 tags to each instance.
        *   You can bind tags to up to 50 instances in each call.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        If you have a large number of instances, you can create multiple tags and bind these tags to the instances. Then, you can filter the instances by tag.
        *   A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        *   If the tag that you specify does not exist, this tag is automatically created and bound to the specified instance.
        *   If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        *   You can bind up to 20 tags to each instance.
        *   You can bind tags to up to 50 instances in each call.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def transfer_instance_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInstanceClass',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TransferInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_instance_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_instance_class_with_options(request, runtime)

    def transfer_pay_type_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of DTS.
        *   The billing method of subscription instances cannot be changed to pay-as-you-go. To prevent resource waste, determine whether you need to change the billing method of your resources.
        *   Data migration instances are all pay-as-you-go instances. You do not need to change the billing method of data migration instances.
        *   After you change the billing method from pay-as-you-go to subscription, the DTS instance is not affected.
        

        @param request: TransferPayTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TransferPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferPayType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TransferPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_pay_type(self, request):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of DTS.
        *   The billing method of subscription instances cannot be changed to pay-as-you-go. To prevent resource waste, determine whether you need to change the billing method of your resources.
        *   Data migration instances are all pay-as-you-go instances. You do not need to change the billing method of data migration instances.
        *   After you change the billing method from pay-as-you-go to subscription, the DTS instance is not affected.
        

        @param request: TransferPayTypeRequest

        @return: TransferPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transfer_pay_type_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        >  If a tag is unbound from an instance and is not bound to other instances, the tag is deleted.
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        >  If a tag is unbound from an instance and is not bound to other instances, the tag is deleted.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upgrade_two_way_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS)
        When you call this operation, take note of the following information:
        *   The source and destination databases of the data synchronization task are both **MySQL** databases.
        *   The synchronization topology of the data synchronization task is **one-way synchronization**.
        *   The data synchronization task is in the **Synchronizing** state.
        *   The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.
        

        @param request: UpgradeTwoWayRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeTwoWayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeTwoWay',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.UpgradeTwoWayResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_two_way(self, request):
        """
        Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://www.alibabacloud.com/zh/product/data-transmission-service/pricing) of Data Transmission Service (DTS)
        When you call this operation, take note of the following information:
        *   The source and destination databases of the data synchronization task are both **MySQL** databases.
        *   The synchronization topology of the data synchronization task is **one-way synchronization**.
        *   The data synchronization task is in the **Synchronizing** state.
        *   The upgrade operation causes data synchronization latency of about 5 seconds. We recommend that you perform this operation during off-peak hours.
        

        @param request: UpgradeTwoWayRequest

        @return: UpgradeTwoWayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_two_way_with_options(request, runtime)

    def white_ip_list_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *WhiteIpList**.
        

        @param request: WhiteIpListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: WhiteIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WhiteIpList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.WhiteIpListResponse(),
            self.call_api(params, req, runtime)
        )

    def white_ip_list(self, request):
        """
        The operation that you want to perform. Set the value to *WhiteIpList**.
        

        @param request: WhiteIpListRequest

        @return: WhiteIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.white_ip_list_with_options(request, runtime)
