# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rds20140815 import models as rds_20140815_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'rds.aliyuncs.com',
            'cn-beijing': 'rds.aliyuncs.com',
            'cn-hangzhou': 'rds.aliyuncs.com',
            'cn-shanghai': 'rds.aliyuncs.com',
            'cn-shenzhen': 'rds.aliyuncs.com',
            'cn-heyuan': 'rds.aliyuncs.com',
            'cn-hongkong': 'rds.aliyuncs.com',
            'ap-southeast-1': 'rds.aliyuncs.com',
            'us-west-1': 'rds.aliyuncs.com',
            'us-east-1': 'rds.aliyuncs.com',
            'cn-shanghai-finance-1': 'rds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'rds.aliyuncs.com',
            'cn-north-2-gov-1': 'rds.aliyuncs.com',
            'ap-northeast-2-pop': 'rds.aliyuncs.com',
            'cn-beijing-finance-1': 'rds.aliyuncs.com',
            'cn-beijing-finance-pop': 'rds.aliyuncs.com',
            'cn-beijing-gov-1': 'rds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'rds.aliyuncs.com',
            'cn-edge-1': 'rds.aliyuncs.com',
            'cn-fujian': 'rds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'rds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'rds.aliyuncs.com',
            'cn-hangzhou-finance': 'rds-vpc.cn-hangzhou-finance.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'rds.aliyuncs.com',
            'cn-hangzhou-test-306': 'rds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'rds.aliyuncs.com',
            'cn-qingdao-nebula': 'rds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'rds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'rds.aliyuncs.com',
            'cn-shanghai-inner': 'rds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'rds.aliyuncs.com',
            'cn-shenzhen-inner': 'rds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'rds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'rds.aliyuncs.com',
            'cn-wuhan': 'rds.aliyuncs.com',
            'cn-yushanfang': 'rds.aliyuncs.com',
            'cn-zhangbei': 'rds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'rds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'rds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'rds.aliyuncs.com',
            'eu-west-1-oxs': 'rds.aliyuncs.com',
            'rus-west-1-pop': 'rds.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('rds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_migration_target_instance_with_options(self, request, runtime):
        """
        ## Prerequisites
        Before you call the ActivateMigrationTargetInstance operation, make sure that a cloud migration task is created by calling the [CreateCloudMigrationTask](~~411690~~) operation. In addition, make sure that the value that is returned for the **MigrateStage** parameter from the call of the [DescribeCloudMigrationResult](~~412150~~) operation is **increment**.
        

        @param request: ActivateMigrationTargetInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ActivateMigrationTargetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.force_switch):
            query['ForceSwitch'] = request.force_switch
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateMigrationTargetInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ActivateMigrationTargetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def activate_migration_target_instance(self, request):
        """
        ## Prerequisites
        Before you call the ActivateMigrationTargetInstance operation, make sure that a cloud migration task is created by calling the [CreateCloudMigrationTask](~~411690~~) operation. In addition, make sure that the value that is returned for the **MigrateStage** parameter from the call of the [DescribeCloudMigrationResult](~~412150~~) operation is **increment**.
        

        @param request: ActivateMigrationTargetInstanceRequest

        @return: ActivateMigrationTargetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_migration_target_instance_with_options(request, runtime)

    def add_tags_to_resource_with_options(self, request, runtime):
        """
        This operation has the following limits:
        *   Each tag consists of a TagKey and a TagValue. The TagKey is required, and the TagValue is optional.
        *   The values of TagKey and TagValue cannot start with aliyun.
        *   The values of TagKey and TagValue are not case-sensitive.
        *   The maximum length of a TagKey is 64 characters, and the maximum length of a TagValue is 128 characters.
        *   Each instance can be bound to a maximum of 10 tags. Each tag that is bound to the same instance must have a unique TagKey. If you bind a new tag to the instance and the TagKey of the new tag is the same as that of an existing tag, the new tag overwrites the existing tag.
        

        @param request: AddTagsToResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTagsToResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagsToResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AddTagsToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags_to_resource(self, request):
        """
        This operation has the following limits:
        *   Each tag consists of a TagKey and a TagValue. The TagKey is required, and the TagValue is optional.
        *   The values of TagKey and TagValue cannot start with aliyun.
        *   The values of TagKey and TagValue are not case-sensitive.
        *   The maximum length of a TagKey is 64 characters, and the maximum length of a TagValue is 128 characters.
        *   Each instance can be bound to a maximum of 10 tags. Each tag that is bound to the same instance must have a unique TagKey. If you bind a new tag to the instance and the TagKey of the new tag is the same as that of an existing tag, the new tag overwrites the existing tag.
        

        @param request: AddTagsToResourceRequest

        @return: AddTagsToResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_resource_with_options(request, runtime)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Apply for a public endpoint for an ApsaraDB RDS for MySQL instance](~~26128~~)
        *   [Apply for a public endpoint for an ApsaraDB RDS for PostgreSQL instance](~~97738~~)
        *   [Apply for a public endpoint for an ApsaraDB RDS for SQL Server instance](~~97736~~)
        *   [Apply for a public endpoint for an ApsaraDB RDS for MariaDB instance](~~97740~~)
        

        @param request: AllocateInstancePublicConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.babelfish_port):
            query['BabelfishPort'] = request.babelfish_port
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.general_group_name):
            query['GeneralGroupName'] = request.general_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pgbouncer_port):
            query['PGBouncerPort'] = request.pgbouncer_port
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_instance_public_connection(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Apply for a public endpoint for an ApsaraDB RDS for MySQL instance](~~26128~~)
        *   [Apply for a public endpoint for an ApsaraDB RDS for PostgreSQL instance](~~97738~~)
        *   [Apply for a public endpoint for an ApsaraDB RDS for SQL Server instance](~~97736~~)
        *   [Apply for a public endpoint for an ApsaraDB RDS for MariaDB instance](~~97740~~)
        

        @param request: AllocateInstancePublicConnectionRequest

        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def allocate_read_write_splitting_connection_with_options(self, request, runtime):
        """
        If read-only instances are attached to a primary ApsaraDB RDS for SQL Server instance, you can call this operation to apply for a unified read-only routing endpoint for the primary instance. After you apply for a read-only routing endpoint for a primary instance, the existing endpoints of the primary instance and its read-only instances remain valid. In addition, you can still apply for internal and public endpoints.
        Before you call this operation, make sure that the following requirements are met:
        *   If the instance runs MySQL, the instance uses a shared proxy.
        *   The instance is in the Running state.
        *   Read-only instances are attached to the primary instance.
        *   The instance does not have an ongoing Data Transmission Service (DTS) migration task.
        *   The instance runs one of the following database versions and RDS editions:
        *   SQL Server (cluster edition)
        *   MySQL 5.7 on RDS High-availability Edition with local SSDs
        *   MySQL 5.6
        

        @param request: AllocateReadWriteSplittingConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AllocateReadWriteSplittingConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.distribution_type):
            query['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.max_delay_time):
            query['MaxDelayTime'] = request.max_delay_time
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AllocateReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_read_write_splitting_connection(self, request):
        """
        If read-only instances are attached to a primary ApsaraDB RDS for SQL Server instance, you can call this operation to apply for a unified read-only routing endpoint for the primary instance. After you apply for a read-only routing endpoint for a primary instance, the existing endpoints of the primary instance and its read-only instances remain valid. In addition, you can still apply for internal and public endpoints.
        Before you call this operation, make sure that the following requirements are met:
        *   If the instance runs MySQL, the instance uses a shared proxy.
        *   The instance is in the Running state.
        *   Read-only instances are attached to the primary instance.
        *   The instance does not have an ongoing Data Transmission Service (DTS) migration task.
        *   The instance runs one of the following database versions and RDS editions:
        *   SQL Server (cluster edition)
        *   MySQL 5.7 on RDS High-availability Edition with local SSDs
        *   MySQL 5.6
        

        @param request: AllocateReadWriteSplittingConnectionRequest

        @return: AllocateReadWriteSplittingConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_read_write_splitting_connection_with_options(request, runtime)

    def attach_whitelist_template_to_instance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        

        @param request: AttachWhitelistTemplateToInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachWhitelistTemplateToInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachWhitelistTemplateToInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.AttachWhitelistTemplateToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_whitelist_template_to_instance(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        

        @param request: AttachWhitelistTemplateToInstanceRequest

        @return: AttachWhitelistTemplateToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_whitelist_template_to_instance_with_options(request, runtime)

    def calculate_dbinstance_weight_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   SQL Server
        ### [](#)Feature description
        When the [read/write splitting](~~51073~~) feature is enabled, this operation is used to calculate system-assigned read weights. For more information about custom read weights, see [DescribeDBInstanceNetInfo](~~610423~~).
        ### [](#)Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   If the instance runs MySQL, the instance uses a shared proxy.
        *   The instance runs one of the following MySQL versions and RDS editions:
        *   MySQL 5.7 on RDS High-availability Edition (with local disks)
        *   MySQL 5.6
        *   SQL Server on RDS Cluster Edition
        

        @param request: CalculateDBInstanceWeightRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CalculateDBInstanceWeightResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CalculateDBInstanceWeight',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CalculateDBInstanceWeightResponse(),
            self.call_api(params, req, runtime)
        )

    def calculate_dbinstance_weight(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   SQL Server
        ### [](#)Feature description
        When the [read/write splitting](~~51073~~) feature is enabled, this operation is used to calculate system-assigned read weights. For more information about custom read weights, see [DescribeDBInstanceNetInfo](~~610423~~).
        ### [](#)Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   If the instance runs MySQL, the instance uses a shared proxy.
        *   The instance runs one of the following MySQL versions and RDS editions:
        *   MySQL 5.7 on RDS High-availability Edition (with local disks)
        *   MySQL 5.6
        *   SQL Server on RDS Cluster Edition
        

        @param request: CalculateDBInstanceWeightRequest

        @return: CalculateDBInstanceWeightResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.calculate_dbinstance_weight_with_options(request, runtime)

    def cancel_import_with_options(self, request, runtime):
        """
        This operation is supported for instances that run SQL Server and belong to the dedicated or dedicated host instance family. For more information about how to start a migration task, see [ImportDatabaseBetweenInstances](~~26301~~).
        > This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        

        @param request: CancelImportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelImportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.import_id):
            query['ImportId'] = request.import_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelImport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CancelImportResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_import(self, request):
        """
        This operation is supported for instances that run SQL Server and belong to the dedicated or dedicated host instance family. For more information about how to start a migration task, see [ImportDatabaseBetweenInstances](~~26301~~).
        > This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        

        @param request: CancelImportRequest

        @return: CancelImportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_import_with_options(request, runtime)

    def check_account_name_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckAccountNameAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_account_name_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_available_with_options(request, runtime)

    def check_cloud_resource_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCloudResourceAuthorized',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    def check_cloud_resource_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    def check_create_ddr_dbinstance_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~).
        *   SQL Server. For more information, see [Back up an ApsaraDB RDS for SQL Server instance across regions](~~187923~~).
        *   PostgreSQL. For more information, see [Enable cross-region backups for an ApsaraDB RDS for PostgreSQL instance](~~206671~~).
        > : If your RDS instance uses the new architecture and is created after October 10, 2022, this feature is not supported for the RDS instance. For more information, see [\\[Notice\\] SLR authorization is required to create an ApsaraDB RDS for PostgreSQL instance from October 10, 2022](~~452313~~).
        

        @param request: CheckCreateDdrDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckCreateDdrDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateDdrDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckCreateDdrDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_create_ddr_dbinstance(self, request):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~).
        *   SQL Server. For more information, see [Back up an ApsaraDB RDS for SQL Server instance across regions](~~187923~~).
        *   PostgreSQL. For more information, see [Enable cross-region backups for an ApsaraDB RDS for PostgreSQL instance](~~206671~~).
        > : If your RDS instance uses the new architecture and is created after October 10, 2022, this feature is not supported for the RDS instance. For more information, see [\\[Notice\\] SLR authorization is required to create an ApsaraDB RDS for PostgreSQL instance from October 10, 2022](~~452313~~).
        

        @param request: CheckCreateDdrDBInstanceRequest

        @return: CheckCreateDdrDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_create_ddr_dbinstance_with_options(request, runtime)

    def check_dbname_available_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: CheckDBNameAvailableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckDBNameAvailableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDBNameAvailable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckDBNameAvailableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_dbname_available(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: CheckDBNameAvailableRequest

        @return: CheckDBNameAvailableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_available_with_options(request, runtime)

    def check_instance_exist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckInstanceExist',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckInstanceExistResponse(),
            self.call_api(params, req, runtime)
        )

    def check_instance_exist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_instance_exist_with_options(request, runtime)

    def check_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def check_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    def clone_dbinstance_with_options(self, tmp_req, runtime):
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The original instance is in the Running state.
        *   The original instance does not have ongoing migration tasks.
        *   The log backup feature is enabled for the original instance to support point-in-time recovery.
        *   If you want to clone the original instance by using backup sets, the original instance must have at least one backup set.
        > ApsaraDB RDS allows you to create a cloned instance by using the credentials of your RAM user. Make sure that your RAM user is granted the permissions that are required to clone an instance. For more information, see [Use RAM to manage ApsaraDB RDS permissions](~~58932~~).
        Take note of the following information:
        *   The new instance has the same IP address whitelist, SQL Explorer (SQL Audit), alert threshold, backup, and parameter settings as the original instance.
        *   The data and account information of the new instance is the same as that indicated by the backup set or point in time used for restoration of the original instance.
        

        @param tmp_req: CloneDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CloneDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.CloneDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.bpe_enabled):
            query['BpeEnabled'] = request.bpe_enabled
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.db_names):
            query['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_table):
            query['RestoreTable'] = request.restore_table
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not UtilClient.is_unset(request.table_meta):
            query['TableMeta'] = request.table_meta
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_slave_1):
            query['ZoneIdSlave1'] = request.zone_id_slave_1
        if not UtilClient.is_unset(request.zone_id_slave_2):
            query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_dbinstance(self, request):
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The original instance is in the Running state.
        *   The original instance does not have ongoing migration tasks.
        *   The log backup feature is enabled for the original instance to support point-in-time recovery.
        *   If you want to clone the original instance by using backup sets, the original instance must have at least one backup set.
        > ApsaraDB RDS allows you to create a cloned instance by using the credentials of your RAM user. Make sure that your RAM user is granted the permissions that are required to clone an instance. For more information, see [Use RAM to manage ApsaraDB RDS permissions](~~58932~~).
        Take note of the following information:
        *   The new instance has the same IP address whitelist, SQL Explorer (SQL Audit), alert threshold, backup, and parameter settings as the original instance.
        *   The data and account information of the new instance is the same as that indicated by the backup set or point in time used for restoration of the original instance.
        

        @param request: CloneDBInstanceRequest

        @return: CloneDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    def clone_parameter_group_with_options(self, request, runtime):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: CloneParameterGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CloneParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CloneParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_parameter_group(self, request):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: CloneParameterGroupRequest

        @return: CloneParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clone_parameter_group_with_options(request, runtime)

    def confirm_notify_with_options(self, tmp_req, runtime):
        """
        After you call the QueryNotify operation to query notifications for an instance, you can call this operation to mark the notifications as confirmed. For more information, see [Query notifications for an ApsaraDB RDS instance](~~427959~~).
        

        @param tmp_req: ConfirmNotifyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfirmNotifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.ConfirmNotifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notify_id_list):
            request.notify_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_id_list, 'NotifyIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.confirmor):
            body['Confirmor'] = request.confirmor
        if not UtilClient.is_unset(request.notify_id_list_shrink):
            body['NotifyIdList'] = request.notify_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmNotify',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ConfirmNotifyResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_notify(self, request):
        """
        After you call the QueryNotify operation to query notifications for an instance, you can call this operation to mark the notifications as confirmed. For more information, see [Query notifications for an ApsaraDB RDS instance](~~427959~~).
        

        @param request: ConfirmNotifyRequest

        @return: ConfirmNotifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_notify_with_options(request, runtime)

    def copy_database_with_options(self, request, runtime):
        """
        This operation is phased out.
        

        @param request: CopyDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CopyDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_database(self, request):
        """
        This operation is phased out.
        

        @param request: CopyDatabaseRequest

        @return: CopyDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_database_with_options(request, runtime)

    def copy_database_between_instances_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS SQL Server
        ### References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Replicate databases between ApsaraDB RDS for SQL Server instances](~~95702~~)
        

        @param request: CopyDatabaseBetweenInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CopyDatabaseBetweenInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.db_names):
            query['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.sync_user_privilege):
            query['SyncUserPrivilege'] = request.sync_user_privilege
        if not UtilClient.is_unset(request.target_dbinstance_id):
            query['TargetDBInstanceId'] = request.target_dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CopyDatabaseBetweenInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_database_between_instances(self, request):
        """
        ### Supported database engines
        RDS SQL Server
        ### References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Replicate databases between ApsaraDB RDS for SQL Server instances](~~95702~~)
        

        @param request: CopyDatabaseBetweenInstancesRequest

        @return: CopyDatabaseBetweenInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_database_between_instances_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Create an account on an ApsaraDB RDS for MySQL instance](~~96089~~)
        *   [Create an account on an ApsaraDB RDS for PostgreSQL instance](~~96753~~)
        *   [Create an account on an ApsaraDB RDS for SQL Server instance](~~95810~~)
        *   [Create an account on an ApsaraDB RDS for MariaDB instance](~~97132~~)
        

        @param request: CreateAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Create an account on an ApsaraDB RDS for MySQL instance](~~96089~~)
        *   [Create an account on an ApsaraDB RDS for PostgreSQL instance](~~96753~~)
        *   [Create an account on an ApsaraDB RDS for SQL Server instance](~~95810~~)
        *   [Create an account on an ApsaraDB RDS for MariaDB instance](~~97132~~)
        

        @param request: CreateAccountRequest

        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_backup_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### [](#)Feature description:
        This operation uses the backup feature of ApsaraDB RDS to create a backup set. You can also use an operation of Database Backup (DBS) to create a backup set. For more information, see [List of operations by function of DBS](~~437245~~).
        ### [](#)Precautions
        Before you call this operation, make sure that the following requirements are met:
        *   The instance is in the running state.
        *   The instance does not have ongoing backup tasks.
        *   The number of backup files that are created per day for an instance cannot exceed 20.
        

        @param request: CreateBackupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.backup_strategy):
            query['BackupStrategy'] = request.backup_strategy
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### [](#)Feature description:
        This operation uses the backup feature of ApsaraDB RDS to create a backup set. You can also use an operation of Database Backup (DBS) to create a backup set. For more information, see [List of operations by function of DBS](~~437245~~).
        ### [](#)Precautions
        Before you call this operation, make sure that the following requirements are met:
        *   The instance is in the running state.
        *   The instance does not have ongoing backup tasks.
        *   The number of backup files that are created per day for an instance cannot exceed 20.
        

        @param request: CreateBackupRequest

        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_cloud_migration_precheck_task_with_options(self, request, runtime):
        """
        ## Prerequisites
        The RDS instance meets the following requirements:
        * The RDS instance and the self-managed PostgreSQL instance run the same PostgreSQL version, which can be PostgreSQL 10, PostgreSQL 11, PostgreSQL 12, PostgreSQL 13, PostgreSQL 14, or PostgreSQL 15.
        * The RDS instance is a primary instance. Read-only RDS instances do not support cloud migration.
        * The RDS instance uses cloud disks.
        * The RDS instance is empty. The available storage of the RDS instance is greater than or equal to the size of the data in the self-managed PostgreSQL instance.
        The self-managed PostgreSQL instance meets the following requirements:
        * Network configurations
        |Migration source|Network configuration|
        |:---|---|
        |Self-managed ECS-based PostgreSQL Database|If the self-managed PostgreSQL instance resides on an Elastic Compute Service (ECS) instance, the ECS instance and the RDS instance must reside in the same virtual private cloud (VPC). If the ECS instance and the RDS instance reside in different VPCs, use Cloud Enterprise Network (CEN) to connect the VPCs. For more information, see [What is CEN?](~~181681~~)|
        |Self-managed PostgreSQL database in a data center (within the same VPC as the destination database)|The data center is able to communicate with the VPC to which the destination RDS instance belongs. For more information, see [Connect a data center to a VPC](~~97768~~).|
        * If the self-managed PostgreSQL instance resides on an ECS instance, an ECS security group is configured. For more information, see [(Optional) Configure an ECS security group on a self-managed PostgreSQL instance](~~369726~~).
        * The configurations that are described in [Configure a self-managed PostgreSQL instance to listen to remote connections](~~369727~~) are complete.
        * The configurations that are described in [Create an account for cloud migration on a self-managed PostgreSQL instance](~~369500~~) are complete.
        * The configurations that are described in [Update the pg\\_hba.conf file of a self-managed PostgreSQL instance](~~369728~~) are complete.
        * The configurations that are described in [Configure the firewall of the server on which a self-managed PostgreSQL instance resides](~~369729~~) are complete.
        

        @param request: CreateCloudMigrationPrecheckTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCloudMigrationPrecheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_account):
            query['SourceAccount'] = request.source_account
        if not UtilClient.is_unset(request.source_category):
            query['SourceCategory'] = request.source_category
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not UtilClient.is_unset(request.source_password):
            query['SourcePassword'] = request.source_password
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudMigrationPrecheckTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateCloudMigrationPrecheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cloud_migration_precheck_task(self, request):
        """
        ## Prerequisites
        The RDS instance meets the following requirements:
        * The RDS instance and the self-managed PostgreSQL instance run the same PostgreSQL version, which can be PostgreSQL 10, PostgreSQL 11, PostgreSQL 12, PostgreSQL 13, PostgreSQL 14, or PostgreSQL 15.
        * The RDS instance is a primary instance. Read-only RDS instances do not support cloud migration.
        * The RDS instance uses cloud disks.
        * The RDS instance is empty. The available storage of the RDS instance is greater than or equal to the size of the data in the self-managed PostgreSQL instance.
        The self-managed PostgreSQL instance meets the following requirements:
        * Network configurations
        |Migration source|Network configuration|
        |:---|---|
        |Self-managed ECS-based PostgreSQL Database|If the self-managed PostgreSQL instance resides on an Elastic Compute Service (ECS) instance, the ECS instance and the RDS instance must reside in the same virtual private cloud (VPC). If the ECS instance and the RDS instance reside in different VPCs, use Cloud Enterprise Network (CEN) to connect the VPCs. For more information, see [What is CEN?](~~181681~~)|
        |Self-managed PostgreSQL database in a data center (within the same VPC as the destination database)|The data center is able to communicate with the VPC to which the destination RDS instance belongs. For more information, see [Connect a data center to a VPC](~~97768~~).|
        * If the self-managed PostgreSQL instance resides on an ECS instance, an ECS security group is configured. For more information, see [(Optional) Configure an ECS security group on a self-managed PostgreSQL instance](~~369726~~).
        * The configurations that are described in [Configure a self-managed PostgreSQL instance to listen to remote connections](~~369727~~) are complete.
        * The configurations that are described in [Create an account for cloud migration on a self-managed PostgreSQL instance](~~369500~~) are complete.
        * The configurations that are described in [Update the pg\\_hba.conf file of a self-managed PostgreSQL instance](~~369728~~) are complete.
        * The configurations that are described in [Configure the firewall of the server on which a self-managed PostgreSQL instance resides](~~369729~~) are complete.
        

        @param request: CreateCloudMigrationPrecheckTaskRequest

        @return: CreateCloudMigrationPrecheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_migration_precheck_task_with_options(request, runtime)

    def create_cloud_migration_task_with_options(self, request, runtime):
        """
        ## Prerequisites
        Before you call this operation, make sure that the ApsaraDB RDS for PostgreSQL instance passes the cloud migration assessment.
        

        @param request: CreateCloudMigrationTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCloudMigrationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_account):
            query['SourceAccount'] = request.source_account
        if not UtilClient.is_unset(request.source_category):
            query['SourceCategory'] = request.source_category
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not UtilClient.is_unset(request.source_password):
            query['SourcePassword'] = request.source_password
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudMigrationTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateCloudMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cloud_migration_task(self, request):
        """
        ## Prerequisites
        Before you call this operation, make sure that the ApsaraDB RDS for PostgreSQL instance passes the cloud migration assessment.
        

        @param request: CreateCloudMigrationTaskRequest

        @return: CreateCloudMigrationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_migration_task_with_options(request, runtime)

    def create_dbinstance_with_options(self, tmp_req, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Fees are generated if the call is successful. Before you call this operation, carefully read the following documentation:
        *   [Create an ApsaraDB RDS for MySQL instance](~~148036~~)
        *   [Create a serverless ApsaraDB RDS for MySQL instance](~~412231~~)
        *   [Create an ApsaraDB RDS for PostgreSQL instance](~~148038~~)
        *   [Create a serverless ApsaraDB RDS for PostgreSQL instance](~~607753~~)
        *   [Enable Babelfish for an ApsaraDB RDS for PostgreSQL instance](~~428615~~)
        *   [Create an ApsaraDB RDS for SQL Server instance](~~148037~~)
        *   [Create a serverless ApsaraDB RDS for SQL Server instance](~~603465~~)
        *   [Create an ApsaraDB RDS for MariaDB instance](~~148040~~)
        

        @param tmp_req: CreateDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.babelfish_config):
            query['BabelfishConfig'] = request.babelfish_config
        if not UtilClient.is_unset(request.bpe_enabled):
            query['BpeEnabled'] = request.bpe_enabled
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.create_strategy):
            query['CreateStrategy'] = request.create_strategy
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.dbis_ignore_case):
            query['DBIsIgnoreCase'] = request.dbis_ignore_case
        if not UtilClient.is_unset(request.dbparam_group_id):
            query['DBParamGroupId'] = request.dbparam_group_id
        if not UtilClient.is_unset(request.dbtime_zone):
            query['DBTimeZone'] = request.dbtime_zone
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not UtilClient.is_unset(request.storage_auto_scale):
            query['StorageAutoScale'] = request.storage_auto_scale
        if not UtilClient.is_unset(request.storage_threshold):
            query['StorageThreshold'] = request.storage_threshold
        if not UtilClient.is_unset(request.storage_upper_bound):
            query['StorageUpperBound'] = request.storage_upper_bound
        if not UtilClient.is_unset(request.system_dbcharset):
            query['SystemDBCharset'] = request.system_dbcharset
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_log):
            query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_master):
            query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_slave):
            query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.user_backup_id):
            query['UserBackupId'] = request.user_backup_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_slave_1):
            query['ZoneIdSlave1'] = request.zone_id_slave_1
        if not UtilClient.is_unset(request.zone_id_slave_2):
            query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Fees are generated if the call is successful. Before you call this operation, carefully read the following documentation:
        *   [Create an ApsaraDB RDS for MySQL instance](~~148036~~)
        *   [Create a serverless ApsaraDB RDS for MySQL instance](~~412231~~)
        *   [Create an ApsaraDB RDS for PostgreSQL instance](~~148038~~)
        *   [Create a serverless ApsaraDB RDS for PostgreSQL instance](~~607753~~)
        *   [Enable Babelfish for an ApsaraDB RDS for PostgreSQL instance](~~428615~~)
        *   [Create an ApsaraDB RDS for SQL Server instance](~~148037~~)
        *   [Create a serverless ApsaraDB RDS for SQL Server instance](~~603465~~)
        *   [Create an ApsaraDB RDS for MariaDB instance](~~148040~~)
        

        @param request: CreateDBInstanceRequest

        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def create_dbinstance_endpoint_with_options(self, tmp_req, runtime):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        [Add a read-only endpoint for a cluster](~~464132~~)
        

        @param tmp_req: CreateDBInstanceEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBInstanceEndpointResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.CreateDBInstanceEndpointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_items):
            request.node_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_items, 'NodeItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_endpoint_description):
            query['DBInstanceEndpointDescription'] = request.dbinstance_endpoint_description
        if not UtilClient.is_unset(request.dbinstance_endpoint_type):
            query['DBInstanceEndpointType'] = request.dbinstance_endpoint_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_items_shrink):
            query['NodeItems'] = request.node_items_shrink
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstanceEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance_endpoint(self, request):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        [Add a read-only endpoint for a cluster](~~464132~~)
        

        @param request: CreateDBInstanceEndpointRequest

        @return: CreateDBInstanceEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_endpoint_with_options(request, runtime)

    def create_dbinstance_endpoint_address_with_options(self, request, runtime):
        """
        ### Supported database engine
        MySQL
        ### Precautions
        *   You can create a public endpoint of an endpoint type only when no public endpoint is created for this endpoint type.
        *   The node weights and other configurations are the same as those of the internal endpoint of this endpoint type. Only one public endpoint and one internal endpoint can be created for each endpoint type.
        

        @param request: CreateDBInstanceEndpointAddressRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBInstanceEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_endpoint_id):
            query['DBInstanceEndpointId'] = request.dbinstance_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstanceEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance_endpoint_address(self, request):
        """
        ### Supported database engine
        MySQL
        ### Precautions
        *   You can create a public endpoint of an endpoint type only when no public endpoint is created for this endpoint type.
        *   The node weights and other configurations are the same as those of the internal endpoint of this endpoint type. Only one public endpoint and one internal endpoint can be created for each endpoint type.
        

        @param request: CreateDBInstanceEndpointAddressRequest

        @return: CreateDBInstanceEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_endpoint_address_with_options(request, runtime)

    def create_dbinstance_for_rebuild_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Fees are generated if the call is successful. Before you call this operation, carefully read the following documentation:
        *   [Manage ApsaraDB RDS for MySQL instances in the recycle bin](~~96065~~)
        *   [Manage ApsaraDB RDS for PostgreSQL instances in the recycle bin](~~96752~~)
        *   [Manage ApsaraDB RDS for SQL Server instances in the recycle bin](~~95669~~)
        *   [Manage ApsaraDB RDS for MariaDB instances in the recycle bin](~~97131~~)
        

        @param request: CreateDBInstanceForRebuildRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBInstanceForRebuildResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_slave_1):
            query['ZoneIdSlave1'] = request.zone_id_slave_1
        if not UtilClient.is_unset(request.zone_id_slave_2):
            query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstanceForRebuild',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBInstanceForRebuildResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbinstance_for_rebuild(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Fees are generated if the call is successful. Before you call this operation, carefully read the following documentation:
        *   [Manage ApsaraDB RDS for MySQL instances in the recycle bin](~~96065~~)
        *   [Manage ApsaraDB RDS for PostgreSQL instances in the recycle bin](~~96752~~)
        *   [Manage ApsaraDB RDS for SQL Server instances in the recycle bin](~~95669~~)
        *   [Manage ApsaraDB RDS for MariaDB instances in the recycle bin](~~97131~~)
        

        @param request: CreateDBInstanceForRebuildRequest

        @return: CreateDBInstanceForRebuildResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_for_rebuild_with_options(request, runtime)

    def create_dbnodes_with_options(self, tmp_req, runtime):
        """
        ### Supported database engines
        MySQL
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Add a node to an ApsaraDB RDS for MySQL cluster](~~464129~~)
        

        @param tmp_req: CreateDBNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.CreateDBNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbnode):
            request.dbnode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbnode, 'DBNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnode_shrink):
            query['DBNode'] = request.dbnode_shrink
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBNodes',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbnodes(self, request):
        """
        ### Supported database engines
        MySQL
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Add a node to an ApsaraDB RDS for MySQL cluster](~~464129~~)
        

        @param request: CreateDBNodesRequest

        @return: CreateDBNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbnodes_with_options(request, runtime)

    def create_dbproxy_endpoint_address_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for MySQL instance](~~184921~~)
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for PostgreSQL instance](~~418274~~)
        

        @param request: CreateDBProxyEndpointAddressRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDBProxyEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_connect_string_net_type):
            query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        if not UtilClient.is_unset(request.dbproxy_endpoint_id):
            query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.dbproxy_new_connect_string_port):
            query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dbproxy_endpoint_address(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for MySQL instance](~~184921~~)
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for PostgreSQL instance](~~418274~~)
        

        @param request: CreateDBProxyEndpointAddressRequest

        @return: CreateDBProxyEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbproxy_endpoint_address_with_options(request, runtime)

    def create_database_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Create a database in an ApsaraDB RDS for MySQL instance](~~96105~~)
        *   [Create a database in an ApsaraDB RDS for PostgreSQL instance](~~96758~~)
        *   [Create a database in an ApsaraDB RDS for SQL Server instance](~~95698~~)
        *   [Create a database in an ApsaraDB RDS for MariaDB instance](~~97136~~)
        

        @param request: CreateDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not UtilClient.is_unset(request.dbdescription):
            query['DBDescription'] = request.dbdescription
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_database(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Create a database in an ApsaraDB RDS for MySQL instance](~~96105~~)
        *   [Create a database in an ApsaraDB RDS for PostgreSQL instance](~~96758~~)
        *   [Create a database in an ApsaraDB RDS for SQL Server instance](~~95698~~)
        *   [Create a database in an ApsaraDB RDS for MariaDB instance](~~97136~~)
        

        @param request: CreateDatabaseRequest

        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    def create_ddr_instance_with_options(self, request, runtime):
        """
        >  Before restoration, you can call the [CheckCreateDdrDBInstance](~~121721~~) operation to check whether a cross-region backup set can be used for cross-region restoration.
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: CreateDdrInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDdrInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.system_dbcharset):
            query['SystemDBCharset'] = request.system_dbcharset
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDdrInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDdrInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ddr_instance(self, request):
        """
        >  Before restoration, you can call the [CheckCreateDdrDBInstance](~~121721~~) operation to check whether a cross-region backup set can be used for cross-region restoration.
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: CreateDdrInstanceRequest

        @return: CreateDdrInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ddr_instance_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        """
        > This operation is no longer maintained. You can use the CreateDiagnosticReport operation of Database Autonomy Service (DAS) to create a diagnostic report.
        After you call this operation to create a diagnostic report, you can call the DescribeDiagnosticReportList operation to download the diagnostic report.
        

        @param request: CreateDiagnosticReportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDiagnosticReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_diagnostic_report(self, request):
        """
        > This operation is no longer maintained. You can use the CreateDiagnosticReport operation of Database Autonomy Service (DAS) to create a diagnostic report.
        After you call this operation to create a diagnostic report, you can call the DescribeDiagnosticReportList operation to download the diagnostic report.
        

        @param request: CreateDiagnosticReportRequest

        @return: CreateDiagnosticReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def create_gadinstance_with_options(self, request, runtime):
        """
        ### Prerequisites
        *   Your Alibaba Cloud account is used.
        *   The balance in your Alibaba Cloud account is greater than or equal to USD 100.
        *   A primary ApsaraDB RDS for MySQL instance is created, and the instance is not running as a node in a global active database cluster. You can call the [CreateDBInstance](~~26228~~) operation to create an instance.
        > You must create a primary ApsaraDB RDS for MySQL instance in one of the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Shenzhen), and China (Chengdu).
        For more information, see [Create and release an ApsaraDB RDS global active database cluster](~~328592~~).
        

        @param request: CreateGADInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateGADInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.central_dbinstance_id):
            query['CentralDBInstanceId'] = request.central_dbinstance_id
        if not UtilClient.is_unset(request.central_rds_dts_admin_account):
            query['CentralRdsDtsAdminAccount'] = request.central_rds_dts_admin_account
        if not UtilClient.is_unset(request.central_rds_dts_admin_password):
            query['CentralRdsDtsAdminPassword'] = request.central_rds_dts_admin_password
        if not UtilClient.is_unset(request.central_region_id):
            query['CentralRegionId'] = request.central_region_id
        if not UtilClient.is_unset(request.dblist):
            query['DBList'] = request.dblist
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unit_node):
            query['UnitNode'] = request.unit_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGADInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateGADInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gadinstance(self, request):
        """
        ### Prerequisites
        *   Your Alibaba Cloud account is used.
        *   The balance in your Alibaba Cloud account is greater than or equal to USD 100.
        *   A primary ApsaraDB RDS for MySQL instance is created, and the instance is not running as a node in a global active database cluster. You can call the [CreateDBInstance](~~26228~~) operation to create an instance.
        > You must create a primary ApsaraDB RDS for MySQL instance in one of the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Shenzhen), and China (Chengdu).
        For more information, see [Create and release an ApsaraDB RDS global active database cluster](~~328592~~).
        

        @param request: CreateGADInstanceRequest

        @return: CreateGADInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_gadinstance_with_options(request, runtime)

    def create_gad_instance_member_with_options(self, request, runtime):
        """
        ## Prerequisites
        An ApsaraDB RDS global active database cluster is created. You can call the [CreateGADInstance](~~336893~~) operation to create a global active database cluster.
        For more information, see [Add unit nodes to or move unit nodes from an ApsaraDB RDS global active database cluster](~~331851~~).
        

        @param request: CreateGadInstanceMemberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateGadInstanceMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.central_dbinstance_id):
            query['CentralDBInstanceId'] = request.central_dbinstance_id
        if not UtilClient.is_unset(request.central_rds_dts_admin_account):
            query['CentralRdsDtsAdminAccount'] = request.central_rds_dts_admin_account
        if not UtilClient.is_unset(request.central_rds_dts_admin_password):
            query['CentralRdsDtsAdminPassword'] = request.central_rds_dts_admin_password
        if not UtilClient.is_unset(request.central_region_id):
            query['CentralRegionId'] = request.central_region_id
        if not UtilClient.is_unset(request.dblist):
            query['DBList'] = request.dblist
        if not UtilClient.is_unset(request.gad_instance_id):
            query['GadInstanceId'] = request.gad_instance_id
        if not UtilClient.is_unset(request.unit_node):
            query['UnitNode'] = request.unit_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGadInstanceMember',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateGadInstanceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gad_instance_member(self, request):
        """
        ## Prerequisites
        An ApsaraDB RDS global active database cluster is created. You can call the [CreateGADInstance](~~336893~~) operation to create a global active database cluster.
        For more information, see [Add unit nodes to or move unit nodes from an ApsaraDB RDS global active database cluster](~~331851~~).
        

        @param request: CreateGadInstanceMemberRequest

        @return: CreateGadInstanceMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_gad_instance_member_with_options(request, runtime)

    def create_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.check_dbmode):
            query['CheckDBMode'] = request.check_dbmode
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.is_online_db):
            query['IsOnlineDB'] = request.is_online_db
        if not UtilClient.is_unset(request.migrate_task_id):
            query['MigrateTaskId'] = request.migrate_task_id
        if not UtilClient.is_unset(request.ossurls):
            query['OSSUrls'] = request.ossurls
        if not UtilClient.is_unset(request.oss_object_positions):
            query['OssObjectPositions'] = request.oss_object_positions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateMigrateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_with_options(request, runtime)

    def create_online_database_task_with_options(self, request, runtime):
        """
        This operation is used to migrate backup data to the cloud. Before you call this operation, make sure that you understand the descriptions in [Migrate the full backup data of a self-managed SQL Server database to an ApsaraDB RDS instance that runs SQL Server 2008 R2](~~95737~~), [Migrate the full backup data of a self-managed SQL Server database to an ApsaraDB RDS instance that runs SQL Server 2012, SQL Server 2014, SQL Server 2016, SQL Server 2017, or SQL Server 2019](~~95738~~), and [Migrate the incremental backup data of a self-managed SQL Server database to an ApsaraDB RDS instance that runs SQL Server 2012, SQL Server 2014, SQL Server 2016, SQL Server 2017, or SQL Server 2019](~~95736~~).
        

        @param request: CreateOnlineDatabaseTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateOnlineDatabaseTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_dbmode):
            query['CheckDBMode'] = request.check_dbmode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.migrate_task_id):
            query['MigrateTaskId'] = request.migrate_task_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOnlineDatabaseTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOnlineDatabaseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_online_database_task(self, request):
        """
        This operation is used to migrate backup data to the cloud. Before you call this operation, make sure that you understand the descriptions in [Migrate the full backup data of a self-managed SQL Server database to an ApsaraDB RDS instance that runs SQL Server 2008 R2](~~95737~~), [Migrate the full backup data of a self-managed SQL Server database to an ApsaraDB RDS instance that runs SQL Server 2012, SQL Server 2014, SQL Server 2016, SQL Server 2017, or SQL Server 2019](~~95738~~), and [Migrate the incremental backup data of a self-managed SQL Server database to an ApsaraDB RDS instance that runs SQL Server 2012, SQL Server 2014, SQL Server 2016, SQL Server 2017, or SQL Server 2019](~~95736~~).
        

        @param request: CreateOnlineDatabaseTaskRequest

        @return: CreateOnlineDatabaseTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_online_database_task_with_options(request, runtime)

    def create_order_for_create_dbnodes_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.CreateOrderForCreateDBNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbnode):
            request.dbnode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbnode, 'DBNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnode_shrink):
            query['DBNode'] = request.dbnode_shrink
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.promotion_code):
            query['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderForCreateDBNodes',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOrderForCreateDBNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_order_for_create_dbnodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_for_create_dbnodes_with_options(request, runtime)

    def create_order_for_delete_dbnodes_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.CreateOrderForDeleteDBNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbnode_id):
            request.dbnode_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbnode_id, 'DBNodeId', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnode_id_shrink):
            query['DBNodeId'] = request.dbnode_id_shrink
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.promotion_code):
            query['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderForDeleteDBNodes',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateOrderForDeleteDBNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_order_for_delete_dbnodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_order_for_delete_dbnodes_with_options(request, runtime)

    def create_parameter_group_with_options(self, request, runtime):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) and [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: CreateParameterGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_parameter_group(self, request):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) and [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: CreateParameterGroupRequest

        @return: CreateParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    def create_postgres_extensions_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        ### [](#)Precautions
        Install only the plug-ins that are supported by the major engine version of the instance. Otherwise, the installation fails.
        *   For more information, see [Extensions supported by ApsaraDB RDS for PostgreSQL](~~142340~~).
        *   You can call the [DescribeDBInstanceAttribute](~~610394~~) operation to query the major engine version of an instance.
        

        @param request: CreatePostgresExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePostgresExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnames):
            query['DBNames'] = request.dbnames
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_database):
            query['SourceDatabase'] = request.source_database
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePostgresExtensions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreatePostgresExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_postgres_extensions(self, request):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        ### [](#)Precautions
        Install only the plug-ins that are supported by the major engine version of the instance. Otherwise, the installation fails.
        *   For more information, see [Extensions supported by ApsaraDB RDS for PostgreSQL](~~142340~~).
        *   You can call the [DescribeDBInstanceAttribute](~~610394~~) operation to query the major engine version of an instance.
        

        @param request: CreatePostgresExtensionsRequest

        @return: CreatePostgresExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_postgres_extensions_with_options(request, runtime)

    def create_read_only_dbinstance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Create a read-only ApsaraDB RDS for MySQL instance](~~56991~~)
        *   [Create a read-only ApsaraDB RDS for PostgreSQL instance](~~108959~~)
        *   [Create a read-only ApsaraDB RDS for SQL Server instance](~~99005~~)
        

        @param request: CreateReadOnlyDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateReadOnlyDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bpe_enabled):
            query['BpeEnabled'] = request.bpe_enabled
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.gdn_instance_name):
            query['GdnInstanceName'] = request.gdn_instance_name
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instruction_set_arch):
            query['InstructionSetArch'] = request.instruction_set_arch
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_master):
            query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        if not UtilClient.is_unset(request.tddl_biz_type):
            query['TddlBizType'] = request.tddl_biz_type
        if not UtilClient.is_unset(request.tddl_region_config):
            query['TddlRegionConfig'] = request.tddl_region_config
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReadOnlyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateReadOnlyDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_read_only_dbinstance(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Create a read-only ApsaraDB RDS for MySQL instance](~~56991~~)
        *   [Create a read-only ApsaraDB RDS for PostgreSQL instance](~~108959~~)
        *   [Create a read-only ApsaraDB RDS for SQL Server instance](~~99005~~)
        

        @param request: CreateReadOnlyDBInstanceRequest

        @return: CreateReadOnlyDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_dbinstance_with_options(request, runtime)

    def create_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_names):
            query['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def create_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_secret_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Service-linked roles](~~342840~~)
        

        @param request: CreateServiceLinkedRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_linked_role(self, request):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Service-linked roles](~~342840~~)
        

        @param request: CreateServiceLinkedRoleRequest

        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def create_temp_dbinstance_with_options(self, request, runtime):
        """
        You can create a temporary instance based on a backup file or a point in time within the past seven days.
        Before you call this operation, make sure that the following requirements are met:
        *   Your instance runs SQL Server 2008 R2.
        *   Your instance is in the Running state.
        *   Your instance does not have ongoing migration tasks.
        *   The last creation of a backup file is completed.
        > After a temporary instance is created, the temporary instance inherits the data in the backup file.
        

        @param request: CreateTempDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTempDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTempDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.CreateTempDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_temp_dbinstance(self, request):
        """
        You can create a temporary instance based on a backup file or a point in time within the past seven days.
        Before you call this operation, make sure that the following requirements are met:
        *   Your instance runs SQL Server 2008 R2.
        *   Your instance is in the Running state.
        *   Your instance does not have ongoing migration tasks.
        *   The last creation of a backup file is completed.
        > After a temporary instance is created, the temporary instance inherits the data in the backup file.
        

        @param request: CreateTempDBInstanceRequest

        @return: CreateTempDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_temp_dbinstance_with_options(request, runtime)

    def delete_adsetting_with_options(self, request, runtime):
        """
        This operation is available only for ApsaraDB RDS for SQL Server instances.
        

        @param request: DeleteADSettingRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteADSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteADSetting',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteADSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_adsetting(self, request):
        """
        This operation is available only for ApsaraDB RDS for SQL Server instances.
        

        @param request: DeleteADSettingRequest

        @return: DeleteADSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_adsetting_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Delete a database account from an ApsaraDB RDS for MySQL instance](~~96104~~)
        *   [Delete a database account from an ApsaraDB RDS for PostgreSQL instance](~~147649~~)
        *   [Delete a database account from an ApsaraDB RDS for SQL Server instance](~~95694~~)
        *   [Delete a database account from an ApsaraDB RDS for MariaDB instance](~~97135~~)
        

        @param request: DeleteAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_account(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Delete a database account from an ApsaraDB RDS for MySQL instance](~~96104~~)
        *   [Delete a database account from an ApsaraDB RDS for PostgreSQL instance](~~147649~~)
        *   [Delete a database account from an ApsaraDB RDS for SQL Server instance](~~95694~~)
        *   [Delete a database account from an ApsaraDB RDS for MariaDB instance](~~97135~~)
        

        @param request: DeleteAccountRequest

        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_backup_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        > Only instances that run RDS High-availability Edition are supported.
        ### Description
        You can call this operation to delete backup sets of the instance itself. Backup sets of the associated instances such as read-only, disaster recovery, and cloned instances are not deleted.
        ### Precautions
        Before you call this operation, make sure that the following requirements are met:
        *   The instance is in the Running state.
        *   If the log backup feature is disabled, instances cannot be restored by point in time. You can delete data backup sets that are retained for more than seven days.
        *   If the log backup feature is enabled and the log backup retention period is shorter than the data backup retention period, you can delete the data backup files that are retained for a period longer than the log backup retention period.
        

        @param request: DeleteBackupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        > Only instances that run RDS High-availability Edition are supported.
        ### Description
        You can call this operation to delete backup sets of the instance itself. Backup sets of the associated instances such as read-only, disaster recovery, and cloned instances are not deleted.
        ### Precautions
        Before you call this operation, make sure that the following requirements are met:
        *   The instance is in the Running state.
        *   If the log backup feature is disabled, instances cannot be restored by point in time. You can delete data backup sets that are retained for more than seven days.
        *   If the log backup feature is enabled and the log backup retention period is shorter than the data backup retention period, you can delete the data backup files that are retained for a period longer than the log backup retention period.
        

        @param request: DeleteBackupRequest

        @return: DeleteBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    def delete_backup_file_with_options(self, request, runtime):
        """
        ### Supported database engine
        SQL Server
        ### Usage notes
        This operation is available for users whose accounts are added to the whitelist. If your account is not added to the whitelist, you can join the Database Backup (DBS) DingTalk group whose ID is 35585947 and contact the on-duty engineer to add your account to the whitelist.
        

        @param request: DeleteBackupFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_time):
            query['BackupTime'] = request.backup_time
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_file(self, request):
        """
        ### Supported database engine
        SQL Server
        ### Usage notes
        This operation is available for users whose accounts are added to the whitelist. If your account is not added to the whitelist, you can join the Database Backup (DBS) DingTalk group whose ID is 35585947 and contact the on-duty engineer to add your account to the whitelist.
        

        @param request: DeleteBackupFileRequest

        @return: DeleteBackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Note Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Release an ApsaraDB RDS for MySQL instance](~~96057~~)
        *   [Release an ApsaraDB RDS for PostgreSQL instance](~~96749~~)
        *   [Release an ApsaraDB RDS for SQL Server instance](~~95662~~)
        *   [Release an ApsaraDB RDS for MariaDB instance](~~97128~~)
        

        @param request: DeleteDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.released_keep_policy):
            query['ReleasedKeepPolicy'] = request.released_keep_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbinstance(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Note Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Release an ApsaraDB RDS for MySQL instance](~~96057~~)
        *   [Release an ApsaraDB RDS for PostgreSQL instance](~~96749~~)
        *   [Release an ApsaraDB RDS for SQL Server instance](~~95662~~)
        *   [Release an ApsaraDB RDS for MariaDB instance](~~97128~~)
        

        @param request: DeleteDBInstanceRequest

        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def delete_dbinstance_endpoint_with_options(self, request, runtime):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Delete the read-only endpoint of an ApsaraDB RDS for MySQL cluster](~~464133~~)
        

        @param request: DeleteDBInstanceEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBInstanceEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_endpoint_id):
            query['DBInstanceEndpointId'] = request.dbinstance_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstanceEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbinstance_endpoint(self, request):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Delete the read-only endpoint of an ApsaraDB RDS for MySQL cluster](~~464133~~)
        

        @param request: DeleteDBInstanceEndpointRequest

        @return: DeleteDBInstanceEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_endpoint_with_options(request, runtime)

    def delete_dbinstance_endpoint_address_with_options(self, request, runtime):
        """
        ### Supported database engine
        MySQL
        ### Precautions
        You can delete only the public endpoint of each endpoint type from the instance. If you want to delete an internal endpoint of any endpoint type, you can delete the type of endpoint.
        

        @param request: DeleteDBInstanceEndpointAddressRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBInstanceEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.connection_string):
            body['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_endpoint_id):
            body['DBInstanceEndpointId'] = request.dbinstance_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDBInstanceEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBInstanceEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbinstance_endpoint_address(self, request):
        """
        ### Supported database engine
        MySQL
        ### Precautions
        You can delete only the public endpoint of each endpoint type from the instance. If you want to delete an internal endpoint of any endpoint type, you can delete the type of endpoint.
        

        @param request: DeleteDBInstanceEndpointAddressRequest

        @return: DeleteDBInstanceEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_endpoint_address_with_options(request, runtime)

    def delete_dbnodes_with_options(self, tmp_req, runtime):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Delete a node from an ApsaraDB RDS for MySQL instance that runs RDS Cluster Edition](~~464130~~)
        

        @param tmp_req: DeleteDBNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.DeleteDBNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbnode_id):
            request.dbnode_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbnode_id, 'DBNodeId', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnode_id_shrink):
            query['DBNodeId'] = request.dbnode_id_shrink
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBNodes',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbnodes(self, request):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Delete a node from an ApsaraDB RDS for MySQL instance that runs RDS Cluster Edition](~~464130~~)
        

        @param request: DeleteDBNodesRequest

        @return: DeleteDBNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbnodes_with_options(request, runtime)

    def delete_dbproxy_endpoint_address_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for MySQL instance](~~184921~~)
        *   [Configure the dedicated proxy endpoint for an ApsaraDB RDS for PostgreSQL instance](~~418274~~)
        

        @param request: DeleteDBProxyEndpointAddressRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDBProxyEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_connect_string_net_type):
            query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        if not UtilClient.is_unset(request.dbproxy_endpoint_id):
            query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dbproxy_endpoint_address(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for MySQL instance](~~184921~~)
        *   [Configure the dedicated proxy endpoint for an ApsaraDB RDS for PostgreSQL instance](~~418274~~)
        

        @param request: DeleteDBProxyEndpointAddressRequest

        @return: DeleteDBProxyEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbproxy_endpoint_address_with_options(request, runtime)

    def delete_database_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Delete a database from an ApsaraDB RDS for MySQL instance](~~96106~~)
        *   [Delete a database from an ApsaraDB RDS for PostgreSQL instance](~~96759~~)
        *   [Delete a database from an ApsaraDB RDS for SQL Server instance](~~95699~~)
        *   [Delete a database from an ApsaraDB RDS for MariaDB instance](~~97137~~)
        

        @param request: DeleteDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_database(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Delete a database from an ApsaraDB RDS for MySQL instance](~~96106~~)
        *   [Delete a database from an ApsaraDB RDS for PostgreSQL instance](~~96759~~)
        *   [Delete a database from an ApsaraDB RDS for SQL Server instance](~~95699~~)
        *   [Delete a database from an ApsaraDB RDS for MariaDB instance](~~97137~~)
        

        @param request: DeleteDatabaseRequest

        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    def delete_gad_instance_with_options(self, request, runtime):
        """
        ## Precautions
        *   A global active database cluster cannot be restored after it is deleted. Proceed with caution when you delete a global active database cluster.
        *   If you delete a global active database cluster, the system removes all nodes and Data Transmission Service (DTS) synchronization tasks from the cluster. However, the system does not release the ApsaraDB RDS for MySQL instances that run as nodes in the cluster. If you no longer need the ApsaraDB RDS for MySQL instances, you can call the [DeleteDBInstance](~~26229~~) to release the instances one after another.
        

        @param request: DeleteGadInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteGadInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gad_instance_name):
            query['GadInstanceName'] = request.gad_instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGadInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteGadInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gad_instance(self, request):
        """
        ## Precautions
        *   A global active database cluster cannot be restored after it is deleted. Proceed with caution when you delete a global active database cluster.
        *   If you delete a global active database cluster, the system removes all nodes and Data Transmission Service (DTS) synchronization tasks from the cluster. However, the system does not release the ApsaraDB RDS for MySQL instances that run as nodes in the cluster. If you no longer need the ApsaraDB RDS for MySQL instances, you can call the [DeleteDBInstance](~~26229~~) to release the instances one after another.
        

        @param request: DeleteGadInstanceRequest

        @return: DeleteGadInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gad_instance_with_options(request, runtime)

    def delete_parameter_group_with_options(self, request, runtime):
        """
        You can apply a parameter template to an instance to manage a number of parameters at a time. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        >
        *   If you delete a parameter template, the instances to which the parameter template is applied are not affected.
        *   Before you can delete a parameter template in ApsaraDB RDS for PostgreSQL, you must apply another parameter template to the ApsaraDB RDS for PostgreSQL instances to which the parameter template is applied. You can call the [DescribeParameterGroup](~~144842~~) operation to query the instances to which a parameter template is applied.
        

        @param request: DeleteParameterGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_parameter_group(self, request):
        """
        You can apply a parameter template to an instance to manage a number of parameters at a time. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        >
        *   If you delete a parameter template, the instances to which the parameter template is applied are not affected.
        *   Before you can delete a parameter template in ApsaraDB RDS for PostgreSQL, you must apply another parameter template to the ApsaraDB RDS for PostgreSQL instances to which the parameter template is applied. You can call the [DescribeParameterGroup](~~144842~~) operation to query the instances to which a parameter template is applied.
        

        @param request: DeleteParameterGroupRequest

        @return: DeleteParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    def delete_postgres_extensions_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS PostgreSQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        

        @param request: DeletePostgresExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePostgresExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnames):
            query['DBNames'] = request.dbnames
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePostgresExtensions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeletePostgresExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_postgres_extensions(self, request):
        """
        ### Supported database engines
        RDS PostgreSQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        

        @param request: DeletePostgresExtensionsRequest

        @return: DeletePostgresExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_postgres_extensions_with_options(request, runtime)

    def delete_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secret_arn):
            query['SecretArn'] = request.secret_arn
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_with_options(request, runtime)

    def delete_slot_with_options(self, request, runtime):
        """
        This operation is available only for ApsaraDB RDS for PostgreSQL instances.
        *   You can delete a replication slot only when the status of the slot is **INACTIVE**. You can call the DescribeSlots operation to query the status of a replication slot.
        

        @param request: DeleteSlotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSlotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slot_name):
            query['SlotName'] = request.slot_name
        if not UtilClient.is_unset(request.slot_status):
            query['SlotStatus'] = request.slot_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSlot',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteSlotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_slot(self, request):
        """
        This operation is available only for ApsaraDB RDS for PostgreSQL instances.
        *   You can delete a replication slot only when the status of the slot is **INACTIVE**. You can call the DescribeSlots operation to query the status of a replication slot.
        

        @param request: DeleteSlotRequest

        @return: DeleteSlotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_slot_with_options(request, runtime)

    def delete_user_backup_file_with_options(self, request, runtime):
        """
        >
        *   A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        *   This operation deletes full backup files only from the ApsaraDB RDS console. This operation does not affect the full backup files that are stored as objects in Object Storage Service (OSS) buckets. After you call this operation to delete a full backup file, you can call the [ImportUserBackupFile](~~260266~~) operation to reimport the full backup file.
        

        @param request: DeleteUserBackupFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteUserBackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DeleteUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_backup_file(self, request):
        """
        >
        *   A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        *   This operation deletes full backup files only from the ApsaraDB RDS console. This operation does not affect the full backup files that are stored as objects in Object Storage Service (OSS) buckets. After you call this operation to delete a full backup file, you can call the [ImportUserBackupFile](~~260266~~) operation to reimport the full backup file.
        

        @param request: DeleteUserBackupFileRequest

        @return: DeleteUserBackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_backup_file_with_options(request, runtime)

    def descibe_imports_from_database_with_options(self, request, runtime):
        """
        This operation is suitable only for the instances that run MySQL or SQL Server. For more information about how to run a migration task, see [ImportDatabaseBetweenInstances](~~26301~~).
        

        @param request: DescibeImportsFromDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescibeImportsFromDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.import_id):
            query['ImportId'] = request.import_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescibeImportsFromDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescibeImportsFromDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def descibe_imports_from_database(self, request):
        """
        This operation is suitable only for the instances that run MySQL or SQL Server. For more information about how to run a migration task, see [ImportDatabaseBetweenInstances](~~26301~~).
        

        @param request: DescibeImportsFromDatabaseRequest

        @return: DescibeImportsFromDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.descibe_imports_from_database_with_options(request, runtime)

    def describe_adinfo_with_options(self, request, runtime):
        """
        This operation is available only for ApsaraDB RDS for SQL Server instances.
        

        @param request: DescribeADInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeADInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeADInfo',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeADInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_adinfo(self, request):
        """
        This operation is available only for ApsaraDB RDS for SQL Server instances.
        

        @param request: DescribeADInfoRequest

        @return: DescribeADInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_adinfo_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeAccountsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accounts(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeAccountsRequest

        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def describe_action_event_policy_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeActionEventPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeActionEventPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeActionEventPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_action_event_policy(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeActionEventPolicyRequest

        @return: DescribeActionEventPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_action_event_policy_with_options(request, runtime)

    def describe_active_operation_tasks_with_options(self, request, runtime):
        """
        After you call this operation and obtain the information about a specific O\\&M task, you can call the [ModifyActiveOperationTask](~~611454~~) operation to modify the scheduled switching time of the O\\&M task. You can also view the task and modify the scheduled switching time on the Task Center page of the ApsaraDB RDS console.
        

        @param request: DescribeActiveOperationTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not UtilClient.is_unset(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not UtilClient.is_unset(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveOperationTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_active_operation_tasks(self, request):
        """
        After you call this operation and obtain the information about a specific O\\&M task, you can call the [ModifyActiveOperationTask](~~611454~~) operation to modify the scheduled switching time of the O\\&M task. You can also view the task and modify the scheduled switching time on the Task Center page of the ApsaraDB RDS console.
        

        @param request: DescribeActiveOperationTasksRequest

        @return: DescribeActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    def describe_all_whitelist_template_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeAllWhitelistTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAllWhitelistTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_search):
            query['FuzzySearch'] = request.fuzzy_search
        if not UtilClient.is_unset(request.max_records_per_page):
            query['MaxRecordsPerPage'] = request.max_records_per_page
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllWhitelistTemplate',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAllWhitelistTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_whitelist_template(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeAllWhitelistTemplateRequest

        @return: DescribeAllWhitelistTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_whitelist_template_with_options(request, runtime)

    def describe_analyticdb_by_primary_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalyticdbByPrimaryDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAnalyticdbByPrimaryDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_analyticdb_by_primary_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_analyticdb_by_primary_dbinstance_with_options(request, runtime)

    def describe_available_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableClassesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_classes_with_options(request, runtime)

    def describe_available_cross_region_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: DescribeAvailableCrossRegionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableCrossRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCrossRegion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableCrossRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_cross_region(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: DescribeAvailableCrossRegionRequest

        @return: DescribeAvailableCrossRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_region_with_options(request, runtime)

    def describe_available_metrics_with_options(self, request, runtime):
        """
        ### Prerequisites
        The instance runs PostgreSQL.
        For more information, see [View the Enhanced Monitoring metrics of an ApsaraDB RDS for PostgreSQL instance](~~299200~~).
        

        @param request: DescribeAvailableMetricsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableMetrics',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_metrics(self, request):
        """
        ### Prerequisites
        The instance runs PostgreSQL.
        For more information, see [View the Enhanced Monitoring metrics of an ApsaraDB RDS for PostgreSQL instance](~~299200~~).
        

        @param request: DescribeAvailableMetricsRequest

        @return: DescribeAvailableMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_metrics_with_options(request, runtime)

    def describe_available_recovery_time_with_options(self, request, runtime):
        """
        >  To view the time range within which you can restore data from a standard backup set, see [DescribeBackups](~~26273~~)
        ### [](#)Supported database engines
        MySQL
        ### [](#)References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        

        @param request: DescribeAvailableRecoveryTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableRecoveryTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_backup_id):
            query['CrossBackupId'] = request.cross_backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_recovery_time(self, request):
        """
        >  To view the time range within which you can restore data from a standard backup set, see [DescribeBackups](~~26273~~)
        ### [](#)Supported database engines
        MySQL
        ### [](#)References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        

        @param request: DescribeAvailableRecoveryTimeRequest

        @return: DescribeAvailableRecoveryTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_recovery_time_with_options(request, runtime)

    def describe_available_zones_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeAvailableZonesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dispense_mode):
            query['DispenseMode'] = request.dispense_mode
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_zones(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeAvailableZonesRequest

        @return: DescribeAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zones_with_options(request, runtime)

    def describe_backup_database_with_options(self, request, runtime):
        """
        > This operation is phased out.
        

        @param request: DescribeBackupDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupDatabase',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_database(self, request):
        """
        > This operation is phased out.
        

        @param request: DescribeBackupDatabaseRequest

        @return: DescribeBackupDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_database_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeBackupPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_policy_mode):
            query['BackupPolicyMode'] = request.backup_policy_mode
        if not UtilClient.is_unset(request.compress_type):
            query['CompressType'] = request.compress_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.released_keep_policy):
            query['ReleasedKeepPolicy'] = request.released_keep_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policy(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeBackupPolicyRequest

        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backup_tasks_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeBackupTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.backup_job_status):
            query['BackupJobStatus'] = request.backup_job_status
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_tasks(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeBackupTasksRequest

        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeBackupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not UtilClient.is_unset(request.backup_type):
            query['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backups(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeBackupsRequest

        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_binlog_files_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   MariaDB
        ### Usage notes
        *   If the return value of the **DownloadLink** parameter is NULL, ApsaraDB RDS does not provide a download URL.
        *   If the return value of the **DownloadLink** parameter is not NULL, ApsaraDB RDS provides a URL for you to download backup files. The expiration time of the URL is specified by the **LinkExpiredTime** parameter. You must download the backup files before the expiration time.
        *   If you use a RAM user to download backup files, you must grant permissions to the RAM user. For more information, see [Grant backup file download permissions to a RAM user with read-only permissions](~~100043~~).
        *   Each log file that is returned by this operation contains the log entries that are generated over the time range that is specified by the StartTime and EndTime parameters.
        

        @param request: DescribeBinlogFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBinlogFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBinlogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeBinlogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_binlog_files(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   MariaDB
        ### Usage notes
        *   If the return value of the **DownloadLink** parameter is NULL, ApsaraDB RDS does not provide a download URL.
        *   If the return value of the **DownloadLink** parameter is not NULL, ApsaraDB RDS provides a URL for you to download backup files. The expiration time of the URL is specified by the **LinkExpiredTime** parameter. You must download the backup files before the expiration time.
        *   If you use a RAM user to download backup files, you must grant permissions to the RAM user. For more information, see [Grant backup file download permissions to a RAM user with read-only permissions](~~100043~~).
        *   Each log file that is returned by this operation contains the log entries that are generated over the time range that is specified by the StartTime and EndTime parameters.
        

        @param request: DescribeBinlogFilesRequest

        @return: DescribeBinlogFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_binlog_files_with_options(request, runtime)

    def describe_character_set_name_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeCharacterSetNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCharacterSetNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCharacterSetName',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCharacterSetNameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_character_set_name(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeCharacterSetNameRequest

        @return: DescribeCharacterSetNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    def describe_class_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.class_code):
            query['ClassCode'] = request.class_code
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClassDetails',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeClassDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_class_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_class_details_with_options(request, runtime)

    def describe_cloud_migration_precheck_result_with_options(self, request, runtime):
        """
        ## Prerequisites
        Before you call the DescribeCloudMigrationPrecheckResult operation, make sure that the CreateCloudMigrationPrecheckTask operation is called to create a cloud migration assessment task for the ApsaraDB RDS for PostgreSQL instance.
        

        @param request: DescribeCloudMigrationPrecheckResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCloudMigrationPrecheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMigrationPrecheckResult',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCloudMigrationPrecheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_migration_precheck_result(self, request):
        """
        ## Prerequisites
        Before you call the DescribeCloudMigrationPrecheckResult operation, make sure that the CreateCloudMigrationPrecheckTask operation is called to create a cloud migration assessment task for the ApsaraDB RDS for PostgreSQL instance.
        

        @param request: DescribeCloudMigrationPrecheckResultRequest

        @return: DescribeCloudMigrationPrecheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_migration_precheck_result_with_options(request, runtime)

    def describe_cloud_migration_result_with_options(self, request, runtime):
        """
        ## Prerequisites
        Before you call the DescribeCloudMigrationResult operation, make sure that cloud migration tasks are created by calling the [CreateCloudMigrationTask](~~411690~~) operation.
        

        @param request: DescribeCloudMigrationResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCloudMigrationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMigrationResult',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCloudMigrationResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_migration_result(self, request):
        """
        ## Prerequisites
        Before you call the DescribeCloudMigrationResult operation, make sure that cloud migration tasks are created by calling the [CreateCloudMigrationTask](~~411690~~) operation.
        

        @param request: DescribeCloudMigrationResultRequest

        @return: DescribeCloudMigrationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_migration_result_with_options(request, runtime)

    def describe_collation_time_zones_with_options(self, request, runtime):
        """
        ### Supported database engine
        SQL Server
        

        @param request: DescribeCollationTimeZonesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCollationTimeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCollationTimeZones',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCollationTimeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_collation_time_zones(self, request):
        """
        ### Supported database engine
        SQL Server
        

        @param request: DescribeCollationTimeZonesRequest

        @return: DescribeCollationTimeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_collation_time_zones_with_options(request, runtime)

    def describe_cross_backup_meta_list_with_options(self, request, runtime):
        """
        ApsaraDB RDS for MySQL instances support cross-region backup and restoration. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~) and [Restore the data of an ApsaraDB RDS for MySQL instance across regions](~~120875~~).
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~).
        *   SQL Server. For more information, see [Back up an ApsaraDB RDS for SQL Server instance across regions](~~187923~~).
        *   PostgreSQL. For more information, see [Enable cross-region backups for an ApsaraDB RDS for PostgreSQL instance](~~206671~~).
        

        @param request: DescribeCrossBackupMetaListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCrossBackupMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.get_db_name):
            query['GetDbName'] = request.get_db_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern):
            query['Pattern'] = request.pattern
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossBackupMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossBackupMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_backup_meta_list(self, request):
        """
        ApsaraDB RDS for MySQL instances support cross-region backup and restoration. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~) and [Restore the data of an ApsaraDB RDS for MySQL instance across regions](~~120875~~).
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~).
        *   SQL Server. For more information, see [Back up an ApsaraDB RDS for SQL Server instance across regions](~~187923~~).
        *   PostgreSQL. For more information, see [Enable cross-region backups for an ApsaraDB RDS for PostgreSQL instance](~~206671~~).
        

        @param request: DescribeCrossBackupMetaListRequest

        @return: DescribeCrossBackupMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_backup_meta_list_with_options(request, runtime)

    def describe_cross_region_backup_dbinstance_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~).
        *   SQL Server. For more information, see [Back up an ApsaraDB RDS for SQL Server instance across regions](~~187923~~).
        *   PostgreSQL. For more information, see [Enable cross-region backups for an ApsaraDB RDS for PostgreSQL instance](~~206671~~).
        

        @param request: DescribeCrossRegionBackupDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCrossRegionBackupDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackupDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_region_backup_dbinstance(self, request):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL. For more information, see [Back up an ApsaraDB RDS for MySQL instance across regions](~~120824~~).
        *   SQL Server. For more information, see [Back up an ApsaraDB RDS for SQL Server instance across regions](~~187923~~).
        *   PostgreSQL. For more information, see [Enable cross-region backups for an ApsaraDB RDS for PostgreSQL instance](~~206671~~).
        

        @param request: DescribeCrossRegionBackupDBInstanceRequest

        @return: DescribeCrossRegionBackupDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backup_dbinstance_with_options(request, runtime)

    def describe_cross_region_backups_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature for an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        >  For more information about how to query cross-region log backup files, see [DescribeCrossRegionLogBackupFiles](~~121734~~).
        

        @param request: DescribeCrossRegionBackupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCrossRegionBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.cross_backup_id):
            query['CrossBackupId'] = request.cross_backup_id
        if not UtilClient.is_unset(request.cross_backup_region):
            query['CrossBackupRegion'] = request.cross_backup_region
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_region_backups(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature for an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        >  For more information about how to query cross-region log backup files, see [DescribeCrossRegionLogBackupFiles](~~121734~~).
        

        @param request: DescribeCrossRegionBackupsRequest

        @return: DescribeCrossRegionBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backups_with_options(request, runtime)

    def describe_cross_region_log_backup_files_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        >  For more information about how to query cross-region data backup files, see [DescribeCrossRegionBackups](~~121733~~).
        

        @param request: DescribeCrossRegionLogBackupFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCrossRegionLogBackupFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cross_backup_region):
            query['CrossBackupRegion'] = request.cross_backup_region
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCrossRegionLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cross_region_log_backup_files(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        >  For more information about how to query cross-region data backup files, see [DescribeCrossRegionBackups](~~121733~~).
        

        @param request: DescribeCrossRegionLogBackupFilesRequest

        @return: DescribeCrossRegionLogBackupFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_log_backup_files_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeDBInstanceAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_attribute(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeDBInstanceAttributeRequest

        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def describe_dbinstance_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceByTags',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceByTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_by_tags_with_options(request, runtime)

    def describe_dbinstance_detail_with_options(self, request, runtime):
        """
        This operation is phased out.
        

        @param request: DescribeDBInstanceDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDetail',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_detail(self, request):
        """
        This operation is phased out.
        

        @param request: DescribeDBInstanceDetailRequest

        @return: DescribeDBInstanceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_detail_with_options(request, runtime)

    def describe_dbinstance_encryption_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEncryptionKey',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_encryption_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    def describe_dbinstance_endpoints_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS MySQL
        

        @param request: DescribeDBInstanceEndpointsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_endpoint_id):
            query['DBInstanceEndpointId'] = request.dbinstance_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceEndpoints',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_endpoints(self, request):
        """
        ### [](#)Supported database engines
        RDS MySQL
        

        @param request: DescribeDBInstanceEndpointsRequest

        @return: DescribeDBInstanceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_endpoints_with_options(request, runtime)

    def describe_dbinstance_haconfig_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Query the data replication mode of an ApsaraDB RDS for MySQL instance](~~96055~~)
        *   [Query the data replication mode of an ApsaraDB RDS for PostgreSQL instance](~~151265~~)
        *   [Query the data replication mode of an ApsaraDB RDS for SQL Server instance](~~415433~~)
        

        @param request: DescribeDBInstanceHAConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceHAConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceHAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_haconfig(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Query the data replication mode of an ApsaraDB RDS for MySQL instance](~~96055~~)
        *   [Query the data replication mode of an ApsaraDB RDS for PostgreSQL instance](~~151265~~)
        *   [Query the data replication mode of an ApsaraDB RDS for SQL Server instance](~~415433~~)
        

        @param request: DescribeDBInstanceHAConfigRequest

        @return: DescribeDBInstanceHAConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_haconfig_with_options(request, runtime)

    def describe_dbinstance_iparray_list_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeDBInstanceIPArrayListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceIPArrayListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.whitelist_network_type):
            query['WhitelistNetworkType'] = request.whitelist_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIPArrayListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_iparray_list(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeDBInstanceIPArrayListRequest

        @return: DescribeDBInstanceIPArrayListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    def describe_dbinstance_ip_hostname_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS SQL Server
        ### [](#)Prerequisites
        *   The RDS instance runs RDS Basic Edition, RDS High-availability Edition, or RDS Cluster Edition. If your RDS instance runs RDS High-availability Edition, make sure that the instance runs SQL Server 2012 or later.
        *   The RDS instance belongs to a general-purpose or dedicated instance family. The shared instance family is not supported.
        *   If the RDS instance runs RDS Basic Edition, the instance is created on or after September 02, 2022. You can view the Creation Time
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Configure a distributed transaction whitelist](~~124321~~)
        

        @param request: DescribeDBInstanceIpHostnameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceIpHostnameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIpHostname',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceIpHostnameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_ip_hostname(self, request):
        """
        ### [](#)Supported database engines
        RDS SQL Server
        ### [](#)Prerequisites
        *   The RDS instance runs RDS Basic Edition, RDS High-availability Edition, or RDS Cluster Edition. If your RDS instance runs RDS High-availability Edition, make sure that the instance runs SQL Server 2012 or later.
        *   The RDS instance belongs to a general-purpose or dedicated instance family. The shared instance family is not supported.
        *   If the RDS instance runs RDS Basic Edition, the instance is created on or after September 02, 2022. You can view the Creation Time
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Configure a distributed transaction whitelist](~~124321~~)
        

        @param request: DescribeDBInstanceIpHostnameRequest

        @return: DescribeDBInstanceIpHostnameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_ip_hostname_with_options(request, runtime)

    def describe_dbinstance_metrics_with_options(self, request, runtime):
        """
        ### Prerequisites
        The instance runs PostgreSQL.
        For more information, see [View the Enhanced Monitoring metrics of an ApsaraDB RDS for PostgreSQL instance](~~299200~~).
        

        @param request: DescribeDBInstanceMetricsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMetrics',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_metrics(self, request):
        """
        ### Prerequisites
        The instance runs PostgreSQL.
        For more information, see [View the Enhanced Monitoring metrics of an ApsaraDB RDS for PostgreSQL instance](~~299200~~).
        

        @param request: DescribeDBInstanceMetricsRequest

        @return: DescribeDBInstanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_metrics_with_options(request, runtime)

    def describe_dbinstance_monitor_with_options(self, request, runtime):
        """
        >  This operation is not supported for RDS instances that run PostgreSQL. The monitoring frequency of such an instance varies based on the query time range. For more information, see [Query performance metrics](~~26280~~).
        

        @param request: DescribeDBInstanceMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_monitor(self, request):
        """
        >  This operation is not supported for RDS instances that run PostgreSQL. The monitoring frequency of such an instance varies based on the query time range. For more information, see [Query performance metrics](~~26280~~).
        

        @param request: DescribeDBInstanceMonitorRequest

        @return: DescribeDBInstanceMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    def describe_dbinstance_net_info_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeDBInstanceNetInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_rwsplit_type):
            query['DBInstanceNetRWSplitType'] = request.dbinstance_net_rwsplit_type
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.general_group_name):
            query['GeneralGroupName'] = request.general_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_net_info(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeDBInstanceNetInfoRequest

        @return: DescribeDBInstanceNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    def describe_dbinstance_net_info_for_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_rwsplit_type):
            query['DBInstanceNetRWSplitType'] = request.dbinstance_net_rwsplit_type
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfoForChannel',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceNetInfoForChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_net_info_for_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_for_channel_with_options(request, runtime)

    def describe_dbinstance_performance_with_options(self, request, runtime):
        """
        You can query the performance of an instance over a specific time range based on its performance metrics. Performance metrics are generated by using one of the following methods based on the database engine and version, RDS edition, [monitoring frequency](~~26200~~) ([ModifyDBInstanceMonitor](~~26282~~)), and query time range:
        *   For instances that do not run MySQL on RDS High-availability Edition with standard SSDs or enhanced SSDs (ESSDs) and those that do not run MariaDB TX:
        *   5-second monitoring frequency
        *   If the query time range is greater than seven days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than one day but less than or equal to seven days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is greater than or equal to an hour but less than or equal to one day, performance metrics are collected at 1-minute intervals.
        *   If the query time range is less than an hour, performance metrics are collected at 5-second intervals.
        *   60-second monitoring frequency
        *   If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is less than or equal to seven days, performance metrics are collected at 1-minute intervals.
        *   300-second monitoring frequency
        *   If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is less than or equal to seven days, performance metrics are collected at 5-minute intervals.
        *   For instances that are running MySQL on RDS High-availability Edition with standard SSDs or ESSDs and those that are running MariaDB TX:
        *   If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is less than or equal to seven days, performance metrics are collected at 1-minute intervals.
        *   For instances that run PostgreSQL with local SSDs, standard SSDs, or ESSDs:
        *   If the query time range is less than or equal to an hour, performance metrics are collected at 5-second intervals.
        *   If the query time range is less than or equal to 2 hours, performance metrics are collected at 10-second intervals.
        *   If the query time range is less than or equal to 6 hours, performance metrics are collected at 30-second intervals.
        *   If the query time range is less than or equal to 12 hours, performance metrics are collected at 1-minute intervals.
        *   If the query time range is less than or equal to one day, performance metrics are collected at 2-minute intervals.
        *   If the query time range is less than or equal to five days, performance metrics are collected at 10-minute intervals.
        *   If the query time range is less than or equal to 15 days, performance metrics are collected at 30-minute intervals.
        *   If the query time range is less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        

        @param request: DescribeDBInstancePerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_performance(self, request):
        """
        You can query the performance of an instance over a specific time range based on its performance metrics. Performance metrics are generated by using one of the following methods based on the database engine and version, RDS edition, [monitoring frequency](~~26200~~) ([ModifyDBInstanceMonitor](~~26282~~)), and query time range:
        *   For instances that do not run MySQL on RDS High-availability Edition with standard SSDs or enhanced SSDs (ESSDs) and those that do not run MariaDB TX:
        *   5-second monitoring frequency
        *   If the query time range is greater than seven days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than one day but less than or equal to seven days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is greater than or equal to an hour but less than or equal to one day, performance metrics are collected at 1-minute intervals.
        *   If the query time range is less than an hour, performance metrics are collected at 5-second intervals.
        *   60-second monitoring frequency
        *   If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is less than or equal to seven days, performance metrics are collected at 1-minute intervals.
        *   300-second monitoring frequency
        *   If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is less than or equal to seven days, performance metrics are collected at 5-minute intervals.
        *   For instances that are running MySQL on RDS High-availability Edition with standard SSDs or ESSDs and those that are running MariaDB TX:
        *   If the query time range is greater than 30 days, performance metrics are collected at 1-day intervals.
        *   If the query time range is greater than seven days but less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        *   If the query time range is less than or equal to seven days, performance metrics are collected at 1-minute intervals.
        *   For instances that run PostgreSQL with local SSDs, standard SSDs, or ESSDs:
        *   If the query time range is less than or equal to an hour, performance metrics are collected at 5-second intervals.
        *   If the query time range is less than or equal to 2 hours, performance metrics are collected at 10-second intervals.
        *   If the query time range is less than or equal to 6 hours, performance metrics are collected at 30-second intervals.
        *   If the query time range is less than or equal to 12 hours, performance metrics are collected at 1-minute intervals.
        *   If the query time range is less than or equal to one day, performance metrics are collected at 2-minute intervals.
        *   If the query time range is less than or equal to five days, performance metrics are collected at 10-minute intervals.
        *   If the query time range is less than or equal to 15 days, performance metrics are collected at 30-minute intervals.
        *   If the query time range is less than or equal to 30 days, performance metrics are collected at 1-hour intervals.
        

        @param request: DescribeDBInstancePerformanceRequest

        @return: DescribeDBInstancePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    def describe_dbinstance_promote_activity_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: DescribeDBInstancePromoteActivityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancePromoteActivityResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.db_instance_name):
            query['DbInstanceName'] = request.db_instance_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePromoteActivity',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancePromoteActivityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_promote_activity(self, request):
        """
        @deprecated
        

        @param request: DescribeDBInstancePromoteActivityRequest

        @return: DescribeDBInstancePromoteActivityResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_promote_activity_with_options(request, runtime)

    def describe_dbinstance_proxy_configuration_with_options(self, request, runtime):
        """
        This operation is used to query the original settings of shared proxies rather than the latest settings of dedicated proxies. For more information about how to query the settings of dedicated proxies, see [DescribeDBProxy](~~141055~~).
        Before you call this operation, make sure that the following requirements are met:
        *   The shared proxy feature must be enabled for the primary instance.
        *   The read/write splitting feature must be enabled for the primary instance.
        

        @param request: DescribeDBInstanceProxyConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceProxyConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_proxy_configuration(self, request):
        """
        This operation is used to query the original settings of shared proxies rather than the latest settings of dedicated proxies. For more information about how to query the settings of dedicated proxies, see [DescribeDBProxy](~~141055~~).
        Before you call this operation, make sure that the following requirements are met:
        *   The shared proxy feature must be enabled for the primary instance.
        *   The read/write splitting feature must be enabled for the primary instance.
        

        @param request: DescribeDBInstanceProxyConfigurationRequest

        @return: DescribeDBInstanceProxyConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_proxy_configuration_with_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeDBInstanceSSLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_ssl(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeDBInstanceSSLRequest

        @return: DescribeDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    def describe_dbinstance_tdewith_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        

        @param request: DescribeDBInstanceTDERequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstance_tde(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        

        @param request: DescribeDBInstanceTDERequest

        @return: DescribeDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    def describe_dbinstances_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeDBInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_level):
            query['InstanceLevel'] = request.instance_level
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeDBInstancesRequest

        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dbinstances_as_csv_with_options(self, request, runtime):
        """
        @deprecated : DescribeDBInstancesAsCsv is deprecated, please use Rds::2014-08-15::DescribeDBInstances instead.
        **\
        **Description:** This operation is phased out. Use the [DescribeDBInstances](~~610396~~) operation instead.
        

        @param request: DescribeDBInstancesAsCsvRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancesAsCsvResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cached_async):
            query['CachedAsync'] = request.cached_async
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.export_key):
            query['ExportKey'] = request.export_key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesAsCsv',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesAsCsvResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_as_csv(self, request):
        """
        @deprecated : DescribeDBInstancesAsCsv is deprecated, please use Rds::2014-08-15::DescribeDBInstances instead.
        **\
        **Description:** This operation is phased out. Use the [DescribeDBInstances](~~610396~~) operation instead.
        

        @param request: DescribeDBInstancesAsCsvRequest

        @return: DescribeDBInstancesAsCsvResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_as_csv_with_options(request, runtime)

    def describe_dbinstances_by_expire_time_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeDBInstancesByExpireTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancesByExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_period):
            query['ExpirePeriod'] = request.expire_period
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_by_expire_time(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: DescribeDBInstancesByExpireTimeRequest

        @return: DescribeDBInstancesByExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_expire_time_with_options(request, runtime)

    def describe_dbinstances_by_performance_with_options(self, request, runtime):
        """
        This operation is phased out.
        

        @param request: DescribeDBInstancesByPerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancesByPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.sort_method):
            query['SortMethod'] = request.sort_method
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesByPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesByPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_by_performance(self, request):
        """
        This operation is phased out.
        

        @param request: DescribeDBInstancesByPerformanceRequest

        @return: DescribeDBInstancesByPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_performance_with_options(request, runtime)

    def describe_dbinstances_for_clone_with_options(self, request, runtime):
        """
        This operation is phased out.
        

        @param request: DescribeDBInstancesForCloneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBInstancesForCloneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.current_instance_id):
            query['CurrentInstanceId'] = request.current_instance_id
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancesForClone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBInstancesForCloneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbinstances_for_clone(self, request):
        """
        This operation is phased out.
        

        @param request: DescribeDBInstancesForCloneRequest

        @return: DescribeDBInstancesForCloneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_clone_with_options(request, runtime)

    def describe_dbmini_engine_versions_with_options(self, request, runtime):
        """
        Before you purchase or upgrade an instance that runs MySQL or PostgreSQL, you can call the DescribeDBMiniEngineVersions operation to query the minor engine versions that are available for the instance.
        

        @param request: DescribeDBMiniEngineVersionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBMiniEngineVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.minor_version_tag):
            query['MinorVersionTag'] = request.minor_version_tag
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBMiniEngineVersions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBMiniEngineVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbmini_engine_versions(self, request):
        """
        Before you purchase or upgrade an instance that runs MySQL or PostgreSQL, you can call the DescribeDBMiniEngineVersions operation to query the minor engine versions that are available for the instance.
        

        @param request: DescribeDBMiniEngineVersionsRequest

        @return: DescribeDBMiniEngineVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbmini_engine_versions_with_options(request, runtime)

    def describe_dbproxy_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        

        @param request: DescribeDBProxyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbproxy(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        

        @param request: DescribeDBProxyRequest

        @return: DescribeDBProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_with_options(request, runtime)

    def describe_dbproxy_endpoint_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        

        @param request: DescribeDBProxyEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBProxyEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_connect_string):
            query['DBProxyConnectString'] = request.dbproxy_connect_string
        if not UtilClient.is_unset(request.dbproxy_endpoint_id):
            query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbproxy_endpoint(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        

        @param request: DescribeDBProxyEndpointRequest

        @return: DescribeDBProxyEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_endpoint_with_options(request, runtime)

    def describe_dbproxy_performance_with_options(self, request, runtime):
        """
        Before you call the DescribeDBProxyPerformance operation, make sure that the [ModifyDBProxy](~~141054~~) operation is called to enable the database proxy feature for the instance.
        *   The dedicated proxy feature of ApsaraDB RDS for MySQL provides capabilities such as read/write splitting and short-lived connection optimization. For more information, see [What are database proxies?](~~138705~~)
        *   The database proxy feature of ApsaraDB RDS for PostgreSQL supports read/write splitting. For more information, see [What are database proxies?](~~412194~~)
        

        @param request: DescribeDBProxyPerformanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDBProxyPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.dbproxy_instance_type):
            query['DBProxyInstanceType'] = request.dbproxy_instance_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metrics_name):
            query['MetricsName'] = request.metrics_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyPerformance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDBProxyPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dbproxy_performance(self, request):
        """
        Before you call the DescribeDBProxyPerformance operation, make sure that the [ModifyDBProxy](~~141054~~) operation is called to enable the database proxy feature for the instance.
        *   The dedicated proxy feature of ApsaraDB RDS for MySQL provides capabilities such as read/write splitting and short-lived connection optimization. For more information, see [What are database proxies?](~~138705~~)
        *   The database proxy feature of ApsaraDB RDS for PostgreSQL supports read/write splitting. For more information, see [What are database proxies?](~~412194~~)
        

        @param request: DescribeDBProxyPerformanceRequest

        @return: DescribeDBProxyPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        """
        For more information, see [Configure a distributed transaction whitelist](~~124321~~).
        This operation is applicable to instances that run one of the following SQL Server versions on RDS High-Availability Edition: SQL Server 2012 SE, SQL Server 2012 EE, SQL Server 2014 SE, SQL Server 2016 SE, SQL Server 2016 EE, and SQL Server 2017 SE.
        

        @param request: DescribeDTCSecurityIpHostsForSQLServerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDTCSecurityIpHostsForSQLServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        """
        For more information, see [Configure a distributed transaction whitelist](~~124321~~).
        This operation is applicable to instances that run one of the following SQL Server versions on RDS High-Availability Edition: SQL Server 2012 SE, SQL Server 2012 EE, SQL Server 2014 SE, SQL Server 2016 SE, SQL Server 2016 EE, and SQL Server 2017 SE.
        

        @param request: DescribeDTCSecurityIpHostsForSQLServerRequest

        @return: DescribeDTCSecurityIpHostsForSQLServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def describe_databases_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeDatabasesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.dbstatus):
            query['DBStatus'] = request.dbstatus
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_databases(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeDatabasesRequest

        @return: DescribeDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    def describe_dedicated_host_groups_with_options(self, request, runtime):
        """
        Dedicated clusters allow you to manage a number of instances in a cluster at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: DescribeDedicatedHostGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDedicatedHostGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_groups(self, request):
        """
        Dedicated clusters allow you to manage a number of instances in a cluster at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: DescribeDedicatedHostGroupsRequest

        @return: DescribeDedicatedHostGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        """
        Dedicated clusters allow you to manage a number of instances at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: DescribeDedicatedHostsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDedicatedHostsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_status):
            query['AllocationStatus'] = request.allocation_status
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.host_status):
            query['HostStatus'] = request.host_status
        if not UtilClient.is_unset(request.host_type):
            query['HostType'] = request.host_type
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_hosts(self, request):
        """
        Dedicated clusters allow you to manage a number of instances at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: DescribeDedicatedHostsRequest

        @return: DescribeDedicatedHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_detached_backups_with_options(self, request, runtime):
        """
        ### Supported database engine
        MySQL
        > This operation is available only for instances that use local disks.
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        For more information about how to retain the data backup files of an instance after the instance is released, see [Configure automatic backup](~~98818~~).
        

        @param request: DescribeDetachedBackupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDetachedBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDetachedBackups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDetachedBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_detached_backups(self, request):
        """
        ### Supported database engine
        MySQL
        > This operation is available only for instances that use local disks.
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        For more information about how to retain the data backup files of an instance after the instance is released, see [Configure automatic backup](~~98818~~).
        

        @param request: DescribeDetachedBackupsRequest

        @return: DescribeDetachedBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        """
        @deprecated
        >  This operation is phased out.
        

        @param request: DescribeDiagnosticReportListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnosticReportListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeDiagnosticReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnostic_report_list(self, request):
        """
        @deprecated
        >  This operation is phased out.
        

        @param request: DescribeDiagnosticReportListRequest

        @return: DescribeDiagnosticReportListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def describe_error_logs_with_options(self, request, runtime):
        """
        Error logs contain the time when they were generated and the error messages.
        

        @param request: DescribeErrorLogsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeErrorLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeErrorLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_error_logs(self, request):
        """
        Error logs contain the time when they were generated and the error messages.
        

        @param request: DescribeErrorLogsRequest

        @return: DescribeErrorLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_error_logs_with_options(request, runtime)

    def describe_events_with_options(self, request, runtime):
        """
        The event history feature enables you to view the events that occurred within a region over a specific time range. Historical events include instance creation and parameter modification. For more information, see [View the event history of an ApsaraDB RDS instance](~~129759~~).
        Before you call this operation, make sure that the event history feature is enabled. Otherwise, this operation fails.
        

        @param request: DescribeEventsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_events(self, request):
        """
        The event history feature enables you to view the events that occurred within a region over a specific time range. Historical events include instance creation and parameter modification. For more information, see [View the event history of an ApsaraDB RDS instance](~~129759~~).
        Before you call this operation, make sure that the event history feature is enabled. Otherwise, this operation fails.
        

        @param request: DescribeEventsRequest

        @return: DescribeEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    def describe_gad_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gad_instance_name):
            query['GadInstanceName'] = request.gad_instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGadInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeGadInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gad_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gad_instances_with_options(request, runtime)

    def describe_hadiagnose_config_with_options(self, request, runtime):
        """
        By default, Alibaba Cloud uses persistent connections to check the availability of an instance. For more information, see [What is availability detection?](~~207467~~)
        

        @param request: DescribeHADiagnoseConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHADiagnoseConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHADiagnoseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hadiagnose_config(self, request):
        """
        By default, Alibaba Cloud uses persistent connections to check the availability of an instance. For more information, see [What is availability detection?](~~207467~~)
        

        @param request: DescribeHADiagnoseConfigRequest

        @return: DescribeHADiagnoseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hadiagnose_config_with_options(request, runtime)

    def describe_haswitch_config_with_options(self, request, runtime):
        """
        After a primary/secondary switchover is complete, the primary instance is demoted to the secondary instance and the secondary instance is promoted to primary. For more information, see [Switch workloads over between primary and secondary ApsaraDB RDS instances](~~96054~~).
        When you call this operation, you must make sure that the instance runs RDS High-availability Edition, RDS Enterprise Edition, and RDS Cluster Edition. RDS Cluster Edition is supported for ApsaraDB RDS for MySQL and ApsaraDB RDS for SQL Server.
        

        @param request: DescribeHASwitchConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHASwitchConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHASwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_haswitch_config(self, request):
        """
        After a primary/secondary switchover is complete, the primary instance is demoted to the secondary instance and the secondary instance is promoted to primary. For more information, see [Switch workloads over between primary and secondary ApsaraDB RDS instances](~~96054~~).
        When you call this operation, you must make sure that the instance runs RDS High-availability Edition, RDS Enterprise Edition, and RDS Cluster Edition. RDS Cluster Edition is supported for ApsaraDB RDS for MySQL and ApsaraDB RDS for SQL Server.
        

        @param request: DescribeHASwitchConfigRequest

        @return: DescribeHASwitchConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_haswitch_config_with_options(request, runtime)

    def describe_history_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not UtilClient.is_unset(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not UtilClient.is_unset(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHistoryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_history_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_history_tasks_with_options(request, runtime)

    def describe_host_web_shell_with_options(self, request, runtime):
        """
        > This operation supports only for ApsaraDB RDS for SQL Server instances and is available only to specific customers. If you want to call this operation, contact *Alibaba Cloud technical support**.
        ### Prerequisites
        The instance meets the following requirements:
        *   The instance resides in a region other than the China (Zhangjiakou) region.
        *   The instance runs RDS Basic Edition, runs SQL Server 2012 or later on RDS High-availability Edition, or runs RDS Cluster Edition.
        *   The instance belongs to the general-purpose or dedicated instance family. The shared instance family is not supported.
        *   The instance resides in a virtual private cloud (VPC). For more information about how to change the network type of an instance, see [Change the network type of an ApsaraDB RDS for SQL Server instance](~~95707~~).
        *   If the instance runs RDS High-availability Edition or RDS Cluster Edition, make sure that the instance is created on or after January 01, 2021. If the instance runs RDS Basic Edition, make sure that the instance is created on or after September 02, 2022. You can view the **Creation Time** parameter of an instance in the **Status** section of the **Basic Information** page in the ApsaraDB RDS console.
        Your **Alibaba Cloud account** is used for logons.
        

        @param request: DescribeHostWebShellRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHostWebShellResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionID'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHostWebShell',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeHostWebShellResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_host_web_shell(self, request):
        """
        > This operation supports only for ApsaraDB RDS for SQL Server instances and is available only to specific customers. If you want to call this operation, contact *Alibaba Cloud technical support**.
        ### Prerequisites
        The instance meets the following requirements:
        *   The instance resides in a region other than the China (Zhangjiakou) region.
        *   The instance runs RDS Basic Edition, runs SQL Server 2012 or later on RDS High-availability Edition, or runs RDS Cluster Edition.
        *   The instance belongs to the general-purpose or dedicated instance family. The shared instance family is not supported.
        *   The instance resides in a virtual private cloud (VPC). For more information about how to change the network type of an instance, see [Change the network type of an ApsaraDB RDS for SQL Server instance](~~95707~~).
        *   If the instance runs RDS High-availability Edition or RDS Cluster Edition, make sure that the instance is created on or after January 01, 2021. If the instance runs RDS Basic Edition, make sure that the instance is created on or after September 02, 2022. You can view the **Creation Time** parameter of an instance in the **Status** section of the **Basic Information** page in the ApsaraDB RDS console.
        Your **Alibaba Cloud account** is used for logons.
        

        @param request: DescribeHostWebShellRequest

        @return: DescribeHostWebShellResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_host_web_shell_with_options(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    def describe_instance_cross_backup_policy_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: DescribeInstanceCrossBackupPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceCrossBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_cross_backup_policy(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: DescribeInstanceCrossBackupPolicyRequest

        @return: DescribeInstanceCrossBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_cross_backup_policy_with_options(request, runtime)

    def describe_instance_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceKeywords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_keywords_with_options(request, runtime)

    def describe_instance_linked_whitelist_template_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeInstanceLinkedWhitelistTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceLinkedWhitelistTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLinkedWhitelistTemplate',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeInstanceLinkedWhitelistTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_linked_whitelist_template(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeInstanceLinkedWhitelistTemplateRequest

        @return: DescribeInstanceLinkedWhitelistTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_linked_whitelist_template_with_options(request, runtime)

    def describe_local_available_recovery_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLocalAvailableRecoveryTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_local_available_recovery_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_local_available_recovery_time_with_options(request, runtime)

    def describe_log_backup_files_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS SQL Server
        >  You can call the [DescribeBinlogFiles](~~610550~~) operation to query the log files of other database engines.
        

        @param request: DescribeLogBackupFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLogBackupFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeLogBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_backup_files(self, request):
        """
        ### [](#)Supported database engines
        RDS SQL Server
        >  You can call the [DescribeBinlogFiles](~~610550~~) operation to query the log files of other database engines.
        

        @param request: DescribeLogBackupFilesRequest

        @return: DescribeLogBackupFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_files_with_options(request, runtime)

    def describe_meta_list_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        MySQL
        > This operation is available for RDS instances that run MySQL 8.0, MySQL 5.7, and MySQL 5.6 on RDS High-availability Edition with local disks.
        ### [](#)Description
        Before you call the [RestoreTable](~~131510~~) operation to restore individual databases or tables of an ApsaraDB RDS for MySQL instance, you can call this operation to query the information about the databases and tables that can be restored. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](~~103175~~).
        

        @param request: DescribeMetaListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.get_db_name):
            query['GetDbName'] = request.get_db_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern):
            query['Pattern'] = request.pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetaList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meta_list(self, request):
        """
        ### [](#)Supported database engines
        MySQL
        > This operation is available for RDS instances that run MySQL 8.0, MySQL 5.7, and MySQL 5.6 on RDS High-availability Edition with local disks.
        ### [](#)Description
        Before you call the [RestoreTable](~~131510~~) operation to restore individual databases or tables of an ApsaraDB RDS for MySQL instance, you can call this operation to query the information about the databases and tables that can be restored. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](~~103175~~).
        

        @param request: DescribeMetaListRequest

        @return: DescribeMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_list_with_options(request, runtime)

    def describe_migrate_task_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.migrate_task_id):
            query['MigrateTaskId'] = request.migrate_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTaskById',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migrate_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_task_by_id_with_options(request, runtime)

    def describe_migrate_tasks_with_options(self, request, runtime):
        """
        This operation allows you to query the migration tasks that are created for the instance over the last week.
        >
        *   This operation is supported only for migration tasks that are created to migrate full backup files.
        *   This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        

        @param request: DescribeMigrateTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMigrateTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrateTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeMigrateTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migrate_tasks(self, request):
        """
        This operation allows you to query the migration tasks that are created for the instance over the last week.
        >
        *   This operation is supported only for migration tasks that are created to migrate full backup files.
        *   This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        

        @param request: DescribeMigrateTasksRequest

        @return: DescribeMigrateTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_with_options(request, runtime)

    def describe_modify_pghba_config_log_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        

        @param request: DescribeModifyPGHbaConfigLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeModifyPGHbaConfigLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModifyPGHbaConfigLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeModifyPGHbaConfigLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_modify_pghba_config_log(self, request):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        

        @param request: DescribeModifyPGHbaConfigLogRequest

        @return: DescribeModifyPGHbaConfigLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_pghba_config_log_with_options(request, runtime)

    def describe_modify_parameter_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeModifyParameterLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_modify_parameter_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    def describe_oss_downloads_with_options(self, request, runtime):
        """
        >  This operation is not supported for instances that run SQL Server 2017 EE or SQL Server 2019 EE.
        

        @param request: DescribeOssDownloadsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOssDownloadsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.migrate_task_id):
            query['MigrateTaskId'] = request.migrate_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssDownloads',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeOssDownloadsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_downloads(self, request):
        """
        >  This operation is not supported for instances that run SQL Server 2017 EE or SQL Server 2019 EE.
        

        @param request: DescribeOssDownloadsRequest

        @return: DescribeOssDownloadsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_with_options(request, runtime)

    def describe_pghba_config_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        

        @param request: DescribePGHbaConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePGHbaConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePGHbaConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePGHbaConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pghba_config(self, request):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        

        @param request: DescribePGHbaConfigRequest

        @return: DescribePGHbaConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pghba_config_with_options(request, runtime)

    def describe_parameter_group_with_options(self, request, runtime):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to instances. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: DescribeParameterGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_group(self, request):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to instances. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: DescribeParameterGroupRequest

        @return: DescribeParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    def describe_parameter_groups_with_options(self, request, runtime):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: DescribeParameterGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_groups(self, request):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: DescribeParameterGroupsRequest

        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL 5.5, 5.6, 5.7, and 8.0
        *   SQL Server 2008 R2
        *   PostgreSQL 9.4, 10, 11, and 12
        *   MariaDB 10.3
        

        @param request: DescribeParameterTemplatesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameter_templates(self, request):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL 5.5, 5.6, 5.7, and 8.0
        *   SQL Server 2008 R2
        *   PostgreSQL 9.4, 10, 11, and 12
        *   MariaDB 10.3
        

        @param request: DescribeParameterTemplatesRequest

        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        """
        ### Applicable engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeParametersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameters(self, request):
        """
        ### Applicable engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeParametersRequest

        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_postgres_extensions_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS PostgreSQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        

        @param request: DescribePostgresExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePostgresExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePostgresExtensions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePostgresExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_postgres_extensions(self, request):
        """
        ### Supported database engines
        RDS PostgreSQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        

        @param request: DescribePostgresExtensionsRequest

        @return: DescribePostgresExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_postgres_extensions_with_options(request, runtime)

    def describe_price_with_options(self, tmp_req, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param tmp_req: DescribePriceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.DescribePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbnode):
            request.dbnode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbnode, 'DBNode', 'json')
        if not UtilClient.is_unset(tmp_req.serverless_config):
            request.serverless_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_config, 'ServerlessConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.dbnode_shrink):
            query['DBNode'] = request.dbnode_shrink
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_used_type):
            query['InstanceUsedType'] = request.instance_used_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serverless_config_shrink):
            query['ServerlessConfig'] = request.serverless_config_shrink
        if not UtilClient.is_unset(request.time_type):
            query['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_price(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribePriceRequest

        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_rds_resource_settings_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: DescribeRdsResourceSettingsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRdsResourceSettingsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_niche):
            query['ResourceNiche'] = request.resource_niche
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsResourceSettings',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRdsResourceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_resource_settings(self, request):
        """
        @deprecated
        

        @param request: DescribeRdsResourceSettingsRequest

        @return: DescribeRdsResourceSettingsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_resource_settings_with_options(request, runtime)

    def describe_read_dbinstance_delay_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The primary instance must run the MySQL or PostgreSQL database engine.
        *   The primary instance must be attached with a read-only instance.
        

        @param request: DescribeReadDBInstanceDelayRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeReadDBInstanceDelayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_instance_id):
            query['ReadInstanceId'] = request.read_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReadDBInstanceDelay',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeReadDBInstanceDelayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_read_dbinstance_delay(self, request):
        """
        Before you call this operation, make sure that the following requirements are met:
        *   The primary instance must run the MySQL or PostgreSQL database engine.
        *   The primary instance must be attached with a read-only instance.
        

        @param request: DescribeReadDBInstanceDelayRequest

        @return: DescribeReadDBInstanceDelayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_read_dbinstance_delay_with_options(request, runtime)

    def describe_region_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionInfos',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_region_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_region_infos_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        """
        Before you call the [CreateDBInstance](~~26228~~) operation to create an RDS instance, you can call the DescribeRegions operation to query the available regions and zones.
        >  If a zone supports the multi-zone deployment method, the value of the ZoneId parameter for the zone contains an MAZ part. Examples: cn-hangzhou-MAZ6(b,f) and cn-hangzhou-MAZ5(b,e,f).
        

        @param request: DescribeRegionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        """
        Before you call the [CreateDBInstance](~~26228~~) operation to create an RDS instance, you can call the DescribeRegions operation to query the available regions and zones.
        >  If a zone supports the multi-zone deployment method, the value of the ZoneId parameter for the zone contains an MAZ part. Examples: cn-hangzhou-MAZ6(b,f) and cn-hangzhou-MAZ5(b,e,f).
        

        @param request: DescribeRegionsRequest

        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeRenewalPriceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRenewalPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.time_type):
            query['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeRenewalPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_renewal_price(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeRenewalPriceRequest

        @return: DescribeRenewalPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_resource_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    def describe_sqlcollector_policy_with_options(self, request, runtime):
        """
        This operation is applicable to the following database engine versions:
        *   MySQL
        *   SQL Server 2008 R2
        *   PostgreSQL
        

        @param request: DescribeSQLCollectorPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLCollectorPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqlcollector_policy(self, request):
        """
        This operation is applicable to the following database engine versions:
        *   MySQL
        *   SQL Server 2008 R2
        *   PostgreSQL
        

        @param request: DescribeSQLCollectorPolicyRequest

        @return: DescribeSQLCollectorPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    def describe_sqlcollector_retention_with_options(self, request, runtime):
        """
        The SQL explorer feature must be enabled for the instance.
        The instance must run MySQL. For more information, see [SQL Explorer](~~96123~~).
        

        @param request: DescribeSQLCollectorRetentionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLCollectorRetentionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLCollectorRetentionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqlcollector_retention(self, request):
        """
        The SQL explorer feature must be enabled for the instance.
        The instance must run MySQL. For more information, see [SQL Explorer](~~96123~~).
        

        @param request: DescribeSQLCollectorRetentionRequest

        @return: DescribeSQLCollectorRetentionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_retention_with_options(request, runtime)

    def describe_sqllog_files_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL
        *   SQL Server 2008 R2
        *   PostgreSQL
        >
        *   The DescribeSQLLogFiles operation cannot be called to query the log files that are generated by SQL Explorer Trial Edition for an ApsaraDB RDS for MySQL instance.
        *   The DescribeSQLLogFiles operation cannot be called to query the log files that are generated by the SQL Explorer feature and manually exported from the ApsaraDB RDS console. The DescribeSQLLogFiles operation can be called to query the SQL Explorer log files that are generated by calling the [DescribeSQLLogRecords](~~610533~~) operation with the request parameter **Form** set to **File**.
        

        @param request: DescribeSQLLogFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLLogFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_files(self, request):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL
        *   SQL Server 2008 R2
        *   PostgreSQL
        >
        *   The DescribeSQLLogFiles operation cannot be called to query the log files that are generated by SQL Explorer Trial Edition for an ApsaraDB RDS for MySQL instance.
        *   The DescribeSQLLogFiles operation cannot be called to query the log files that are generated by the SQL Explorer feature and manually exported from the ApsaraDB RDS console. The DescribeSQLLogFiles operation can be called to query the SQL Explorer log files that are generated by calling the [DescribeSQLLogRecords](~~610533~~) operation with the request parameter **Form** set to **File**.
        

        @param request: DescribeSQLLogFilesRequest

        @return: DescribeSQLLogFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    def describe_sqllog_records_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL
        *   SQL Server
        *   PostgreSQL
        >
        *   You can call this operation up to 1,000 times per minute per account. The calls initiated by using both your Alibaba Cloud account and RAM users within your Alibaba Cloud account are counted.
        *   This operation cannot be used to query the logs that are generated by SQL Explorer Trial Edition for an ApsaraDB RDS for MySQL instance.
        *   When you call this operation and set the **Form** parameter to **File** to generate an audit file, a maximum of 1 million log entries can be recorded in the audit file, and you cannot filter log entries by keyword.
        

        @param request: DescribeSQLLogRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSQLLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqlid):
            query['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_records(self, request):
        """
        Before you call this operation, make sure that the instance runs one of the following database engines:
        *   MySQL
        *   SQL Server
        *   PostgreSQL
        >
        *   You can call this operation up to 1,000 times per minute per account. The calls initiated by using both your Alibaba Cloud account and RAM users within your Alibaba Cloud account are counted.
        *   This operation cannot be used to query the logs that are generated by SQL Explorer Trial Edition for an ApsaraDB RDS for MySQL instance.
        *   When you call this operation and set the **Form** parameter to **File** to generate an audit file, a maximum of 1 million log entries can be recorded in the audit file, and you cannot filter log entries by keyword.
        

        @param request: DescribeSQLLogRecordsRequest

        @return: DescribeSQLLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    def describe_sqllog_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogReportList',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSQLLogReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqllog_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_report_list_with_options(request, runtime)

    def describe_secrets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecrets',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_secrets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_secrets_with_options(request, runtime)

    def describe_security_group_configuration_with_options(self, request, runtime):
        """
        After an RDS instance is added to an ECS security group, all ECS instances in the security group can access the RDS instance. For more information, see [Configure a whitelist for an RDS instance](~~96118~~).
        

        @param request: DescribeSecurityGroupConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_group_configuration(self, request):
        """
        After an RDS instance is added to an ECS security group, all ECS instances in the security group can access the RDS instance. For more information, see [Configure a whitelist for an RDS instance](~~96118~~).
        

        @param request: DescribeSecurityGroupConfigurationRequest

        @return: DescribeSecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    def describe_slots_with_options(self, request, runtime):
        """
        This operation is available only for ApsaraDB RDS for PostgreSQL instances.
        

        @param request: DescribeSlotsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSlotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlots',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slots(self, request):
        """
        This operation is available only for ApsaraDB RDS for PostgreSQL instances.
        

        @param request: DescribeSlotsRequest

        @return: DescribeSlotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slots_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### Precautions
        The response parameters returned by this operation are updated every minute.
        

        @param request: DescribeSlowLogRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqlhash):
            query['SQLHASH'] = request.sqlhash
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_log_records(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### Precautions
        The response parameters returned by this operation are updated every minute.
        

        @param request: DescribeSlowLogRecordsRequest

        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_slow_logs_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        **\
        **Note**MySQL 5.7 on RDS Basic Edition is not supported.
        *   SQL Server
        **\
        **Note**Only SQL Server 2008 R2 is supported.
        *   MariaDB
        ### Usage notes
        Slow query logs are not collected in real time and may show a latency of 6 hours to 8 hours.
        

        @param request: DescribeSlowLogsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSlowLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogs',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_logs(self, request):
        """
        ### Supported database engines
        *   MySQL
        **\
        **Note**MySQL 5.7 on RDS Basic Edition is not supported.
        *   SQL Server
        **\
        **Note**Only SQL Server 2008 R2 is supported.
        *   MariaDB
        ### Usage notes
        Slow query logs are not collected in real time and may show a latency of 6 hours to 8 hours.
        

        @param request: DescribeSlowLogsRequest

        @return: DescribeSlowLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    def describe_support_online_resize_disk_with_options(self, request, runtime):
        """
        ### Supported database engine
        SQL Server
        

        @param request: DescribeSupportOnlineResizeDiskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSupportOnlineResizeDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportOnlineResizeDisk',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeSupportOnlineResizeDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_support_online_resize_disk(self, request):
        """
        ### Supported database engine
        SQL Server
        

        @param request: DescribeSupportOnlineResizeDiskRequest

        @return: DescribeSupportOnlineResizeDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_support_online_resize_disk_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the following requirements are met:
        *   If an instance ID is specified, all tags that are added to this instance are queried, and other filter conditions are invalid.
        *   If you specify only TagKey, the results that match the specified TagKey are returned. If you specify both TagKey and TagValue, the results that match both the specified TagKey and TagValue are returned.
        

        @param request: DescribeTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags(self, request):
        """
        Before you call this operation, make sure that the following requirements are met:
        *   If an instance ID is specified, all tags that are added to this instance are queried, and other filter conditions are invalid.
        *   If you specify only TagKey, the results that match the specified TagKey are returned. If you specify both TagKey and TagValue, the results that match both the specified TagKey and TagValue are returned.
        

        @param request: DescribeTagsRequest

        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        """
        This operation is phased out.
        

        @param request: DescribeTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tasks(self, request):
        """
        This operation is phased out.
        

        @param request: DescribeTasksRequest

        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def describe_upgrade_major_version_precheck_task_with_options(self, request, runtime):
        """
        Before you upgrade the major engine version of an ApsaraDB RDS for PostgreSQL instance, you must perform an upgrade check and make sure that the check result is *Success**. You can call this operation to query the upgrade check report.
        If the check result is **Fail**, you must handle the errors that occurred. For more information about how to handle common errors, see [Introduction to the check report for a major engine version upgrade to an ApsaraDB RDS for PostgreSQL instance](https://www.alibabacloud.com/help/en/apsaradb-for-rds/latest/introduction-to-the-check-report-of-a-major-engine-version-upgrade-for-an-apsaradb-rds-for-postgresql-instance).
        

        @param request: DescribeUpgradeMajorVersionPrecheckTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeUpgradeMajorVersionPrecheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_major_version):
            query['TargetMajorVersion'] = request.target_major_version
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeMajorVersionPrecheckTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeUpgradeMajorVersionPrecheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_upgrade_major_version_precheck_task(self, request):
        """
        Before you upgrade the major engine version of an ApsaraDB RDS for PostgreSQL instance, you must perform an upgrade check and make sure that the check result is *Success**. You can call this operation to query the upgrade check report.
        If the check result is **Fail**, you must handle the errors that occurred. For more information about how to handle common errors, see [Introduction to the check report for a major engine version upgrade to an ApsaraDB RDS for PostgreSQL instance](https://www.alibabacloud.com/help/en/apsaradb-for-rds/latest/introduction-to-the-check-report-of-a-major-engine-version-upgrade-for-an-apsaradb-rds-for-postgresql-instance).
        

        @param request: DescribeUpgradeMajorVersionPrecheckTaskRequest

        @return: DescribeUpgradeMajorVersionPrecheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_major_version_precheck_task_with_options(request, runtime)

    def describe_upgrade_major_version_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_major_version):
            query['TargetMajorVersion'] = request.target_major_version
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeMajorVersionTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeUpgradeMajorVersionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_upgrade_major_version_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_major_version_tasks_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeVSwitchesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vswitches(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: DescribeVSwitchesRequest

        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    def describe_whitelist_template_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeWhitelistTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeWhitelistTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWhitelistTemplate',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeWhitelistTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_whitelist_template(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeWhitelistTemplateRequest

        @return: DescribeWhitelistTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_template_with_options(request, runtime)

    def describe_whitelist_template_linked_instance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeWhitelistTemplateLinkedInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeWhitelistTemplateLinkedInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWhitelistTemplateLinkedInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DescribeWhitelistTemplateLinkedInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_whitelist_template_linked_instance(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DescribeWhitelistTemplateLinkedInstanceRequest

        @return: DescribeWhitelistTemplateLinkedInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_template_linked_instance_with_options(request, runtime)

    def destroy_dbinstance_with_options(self, request, runtime):
        """
        The DestroyDBInstance operation is phased out.
        

        @param request: DestroyDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DestroyDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DestroyDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DestroyDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def destroy_dbinstance(self, request):
        """
        The DestroyDBInstance operation is phased out.
        

        @param request: DestroyDBInstanceRequest

        @return: DestroyDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.destroy_dbinstance_with_options(request, runtime)

    def detach_gad_instance_member_with_options(self, request, runtime):
        """
        ## Precautions
        This operation can be used to remove only unit nodes.
        

        @param request: DetachGadInstanceMemberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachGadInstanceMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gad_instance_name):
            query['GadInstanceName'] = request.gad_instance_name
        if not UtilClient.is_unset(request.member_instance_name):
            query['MemberInstanceName'] = request.member_instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachGadInstanceMember',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DetachGadInstanceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_gad_instance_member(self, request):
        """
        ## Precautions
        This operation can be used to remove only unit nodes.
        

        @param request: DetachGadInstanceMemberRequest

        @return: DetachGadInstanceMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_gad_instance_member_with_options(request, runtime)

    def detach_whitelist_template_to_instance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DetachWhitelistTemplateToInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachWhitelistTemplateToInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ins_name):
            query['InsName'] = request.ins_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachWhitelistTemplateToInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.DetachWhitelistTemplateToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_whitelist_template_to_instance(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: DetachWhitelistTemplateToInstanceRequest

        @return: DetachWhitelistTemplateToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_whitelist_template_to_instance_with_options(request, runtime)

    def get_dbinstance_topology_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: GetDBInstanceTopologyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDBInstanceTopologyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBInstanceTopology',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GetDBInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dbinstance_topology(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: GetDBInstanceTopologyRequest

        @return: GetDBInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dbinstance_topology_with_options(request, runtime)

    def get_db_proxy_instance_ssl_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS MySQL
        

        @param request: GetDbProxyInstanceSslRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDbProxyInstanceSslResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GetDbProxyInstanceSslResponse(),
            self.call_api(params, req, runtime)
        )

    def get_db_proxy_instance_ssl(self, request):
        """
        ### [](#)Supported database engines
        RDS MySQL
        

        @param request: GetDbProxyInstanceSslRequest

        @return: GetDbProxyInstanceSslResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_db_proxy_instance_ssl_with_options(request, runtime)

    def grant_account_privilege_with_options(self, request, runtime):
        """
        Each account can be granted permissions on one or more databases. Before you call this operation, make sure that the instance is in the Running state.
        > This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition or run PostgreSQL with local disks.
        

        @param request: GrantAccountPrivilegeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_account_privilege(self, request):
        """
        Each account can be granted permissions on one or more databases. Before you call this operation, make sure that the instance is in the Running state.
        > This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition or run PostgreSQL with local disks.
        

        @param request: GrantAccountPrivilegeRequest

        @return: GrantAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    def grant_operator_permission_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Grant permissions to the service account of an ApsaraDB RDS for MySQL instance](~~96102~~)
        *   [Grant permissions to the service account of an ApsaraDB RDS for SQL Server instance](~~95693~~)
        

        @param request: GrantOperatorPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.privileges):
            query['Privileges'] = request.privileges
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.GrantOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_operator_permission(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Grant permissions to the service account of an ApsaraDB RDS for MySQL instance](~~96102~~)
        *   [Grant permissions to the service account of an ApsaraDB RDS for SQL Server instance](~~95693~~)
        

        @param request: GrantOperatorPermissionRequest

        @return: GrantOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    def import_database_between_instances_with_options(self, request, runtime):
        """
        We recommend that you use Data Transmission Service (DTS). DTS provides data migration, subscription, and synchronization features that allow you to establish stable, secure transmission links. For more information, see [DTS API overview](~~49456~~).
        During the migration, the source instance is in the **Migrating** state, and the destination instance is in the **Importing** state.
        Before you call this operation, make sure that the following requirements are met:
        *   The source and destination instances must run SQL Server and belong to the dedicated or dedicated host instance family. For more information about the supported instance types, see [Primary instance types](~~26312~~).
        *   The source and destination instances must be created by using the same user credentials.
        *   The instance is in the Running state.
        *   The source and destination databases must be in the Running state.
        *   The remaining storage of the destination instance must be greater than the storage capacity of the source instance.
        >
        *   This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        *   You can migrate the data of multiple databases at a time.
        

        @param request: ImportDatabaseBetweenInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportDatabaseBetweenInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinfo):
            query['DBInfo'] = request.dbinfo
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbinstance_id):
            query['SourceDBInstanceId'] = request.source_dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDatabaseBetweenInstances',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportDatabaseBetweenInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_database_between_instances(self, request):
        """
        We recommend that you use Data Transmission Service (DTS). DTS provides data migration, subscription, and synchronization features that allow you to establish stable, secure transmission links. For more information, see [DTS API overview](~~49456~~).
        During the migration, the source instance is in the **Migrating** state, and the destination instance is in the **Importing** state.
        Before you call this operation, make sure that the following requirements are met:
        *   The source and destination instances must run SQL Server and belong to the dedicated or dedicated host instance family. For more information about the supported instance types, see [Primary instance types](~~26312~~).
        *   The source and destination instances must be created by using the same user credentials.
        *   The instance is in the Running state.
        *   The source and destination databases must be in the Running state.
        *   The remaining storage of the destination instance must be greater than the storage capacity of the source instance.
        >
        *   This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition.
        *   You can migrate the data of multiple databases at a time.
        

        @param request: ImportDatabaseBetweenInstancesRequest

        @return: ImportDatabaseBetweenInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_database_between_instances_with_options(request, runtime)

    def import_user_backup_file_with_options(self, request, runtime):
        """
        > A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance.
        Before you call this operation, make sure that the following requirements are met:
        *   The self-managed MySQL database runs MySQL 5.7 and is backed up by using XtraBackup. The name of the backup file ends with `_qp.xb`. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        *   The full backup file of the self-managed MySQL database is uploaded to an Object Storage Service (OSS) bucket in the region of the ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        > This operation is supported only for MySQL 5.7.
        

        @param request: ImportUserBackupFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportUserBackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_file):
            query['BackupFile'] = request.backup_file
        if not UtilClient.is_unset(request.bucket_region):
            query['BucketRegion'] = request.bucket_region
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_size):
            query['RestoreSize'] = request.restore_size
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ImportUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def import_user_backup_file(self, request):
        """
        > A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance.
        Before you call this operation, make sure that the following requirements are met:
        *   The self-managed MySQL database runs MySQL 5.7 and is backed up by using XtraBackup. The name of the backup file ends with `_qp.xb`. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        *   The full backup file of the self-managed MySQL database is uploaded to an Object Storage Service (OSS) bucket in the region of the ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        > This operation is supported only for MySQL 5.7.
        

        @param request: ImportUserBackupFileRequest

        @return: ImportUserBackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_user_backup_file_with_options(request, runtime)

    def list_classes_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: ListClassesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListClassesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListClassesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_classes(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        

        @param request: ListClassesRequest

        @return: ListClassesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_classes_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_backup_files_with_options(self, request, runtime):
        """
        >
        *   A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        *   Before you call the [CreateDBInstance](~~26228~~) operation to create an ApsaraDB RDS for MySQL instance into which you want to import full backup files, you can call this operation to query the IDs of full backup files.
        *   You can call the [ImportUserBackupFile](~~260266~~) operation to import a full backup file into an ApsaraDB RDS for MySQL instance.
        

        @param request: ListUserBackupFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListUserBackupFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.oss_url):
            query['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserBackupFiles',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ListUserBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_backup_files(self, request):
        """
        >
        *   A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 instance to the cloud](~~251779~~).
        *   Before you call the [CreateDBInstance](~~26228~~) operation to create an ApsaraDB RDS for MySQL instance into which you want to import full backup files, you can call this operation to query the IDs of full backup files.
        *   You can call the [ImportUserBackupFile](~~260266~~) operation to import a full backup file into an ApsaraDB RDS for MySQL instance.
        

        @param request: ListUserBackupFilesRequest

        @return: ListUserBackupFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_backup_files_with_options(request, runtime)

    def lock_account_with_options(self, request, runtime):
        """
        You cannot use a locked account to log on to the corresponding instance. You must first unlock the account. For more information, see [Lock and delete an account](~~147649~~).
        

        @param request: LockAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: LockAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.LockAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_account(self, request):
        """
        You cannot use a locked account to log on to the corresponding instance. You must first unlock the account. For more information, see [Lock and delete an account](~~147649~~).
        

        @param request: LockAccountRequest

        @return: LockAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_account_with_options(request, runtime)

    def migrate_connection_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateConnectionToOtherZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateConnectionToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_connection_to_other_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_connection_to_other_zone_with_options(request, runtime)

    def migrate_dbinstance_with_options(self, request, runtime):
        """
        Dedicated clusters allow you to manage a number of instances at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: MigrateDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MigrateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.specified_time):
            query['SpecifiedTime'] = request.specified_time
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_master):
            query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_slave):
            query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        if not UtilClient.is_unset(request.zone_id_for_follower):
            query['ZoneIdForFollower'] = request.zone_id_for_follower
        if not UtilClient.is_unset(request.zone_id_for_log):
            query['ZoneIdForLog'] = request.zone_id_for_log
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_dbinstance(self, request):
        """
        Dedicated clusters allow you to manage a number of instances at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: MigrateDBInstanceRequest

        @return: MigrateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    def migrate_security_ipmode_with_options(self, request, runtime):
        """
        In standard whitelist mode, IP addresses in the whitelist apply to both the classic network and VPCs. To minimize security risks, we recommend that you use the enhanced whitelist mode.
        *   In enhanced whitelist mode, IP addresses in the whitelist are divided into VPC IP addresses and IP addresses of the classic network and Internet.
        >
        *   You cannot change the whitelist mode from the enhanced whitelist mode to the standard whitelist mode.
        *   This operation is not supported for instances that run SQL Server and MariaDB.
        

        @param request: MigrateSecurityIPModeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MigrateSecurityIPModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateSecurityIPMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateSecurityIPModeResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_security_ipmode(self, request):
        """
        In standard whitelist mode, IP addresses in the whitelist apply to both the classic network and VPCs. To minimize security risks, we recommend that you use the enhanced whitelist mode.
        *   In enhanced whitelist mode, IP addresses in the whitelist are divided into VPC IP addresses and IP addresses of the classic network and Internet.
        >
        *   You cannot change the whitelist mode from the enhanced whitelist mode to the standard whitelist mode.
        *   This operation is not supported for instances that run SQL Server and MariaDB.
        

        @param request: MigrateSecurityIPModeRequest

        @return: MigrateSecurityIPModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_security_ipmode_with_options(request, runtime)

    def migrate_to_other_zone_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Migrate an ApsaraDB RDS for MySQL instance across zones in the same region](~~96053~~)
        *   [Migrate an ApsaraDB RDS for PostgreSQL instance across zones in the same region](~~96746~~)
        *   [Migrate an ApsaraDB RDS for SQL Server instance across zones in the same region](~~95658~~)
        

        @param request: MigrateToOtherZoneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MigrateToOtherZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.is_modify_spec):
            query['IsModifySpec'] = request.is_modify_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_slave_1):
            query['ZoneIdSlave1'] = request.zone_id_slave_1
        if not UtilClient.is_unset(request.zone_id_slave_2):
            query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_to_other_zone(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Migrate an ApsaraDB RDS for MySQL instance across zones in the same region](~~96053~~)
        *   [Migrate an ApsaraDB RDS for PostgreSQL instance across zones in the same region](~~96746~~)
        *   [Migrate an ApsaraDB RDS for SQL Server instance across zones in the same region](~~95658~~)
        

        @param request: MigrateToOtherZoneRequest

        @return: MigrateToOtherZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    def modify_adinfo_with_options(self, request, runtime):
        """
        This operation is available only for ApsaraDB RDS for SQL Server instances.
        

        @param request: ModifyADInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyADInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adaccount_name):
            query['ADAccountName'] = request.adaccount_name
        if not UtilClient.is_unset(request.addns):
            query['ADDNS'] = request.addns
        if not UtilClient.is_unset(request.adpassword):
            query['ADPassword'] = request.adpassword
        if not UtilClient.is_unset(request.adserver_ip_address):
            query['ADServerIpAddress'] = request.adserver_ip_address
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADInfo',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyADInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_adinfo(self, request):
        """
        This operation is available only for ApsaraDB RDS for SQL Server instances.
        

        @param request: ModifyADInfoRequest

        @return: ModifyADInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_adinfo_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: ModifyAccountDescriptionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_account_description(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: ModifyAccountDescriptionRequest

        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def modify_action_event_policy_with_options(self, request, runtime):
        """
        The event history feature enables you to view historical events that occurred in a region over a specific time range. These events include instance creation and parameter reconfiguration. For more information, see [Event history](~~129759~~).
        

        @param request: ModifyActionEventPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyActionEventPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_event_log):
            query['EnableEventLog'] = request.enable_event_log
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActionEventPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyActionEventPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_action_event_policy(self, request):
        """
        The event history feature enables you to view historical events that occurred in a region over a specific time range. These events include instance creation and parameter reconfiguration. For more information, see [Event history](~~129759~~).
        

        @param request: ModifyActionEventPolicyRequest

        @return: ModifyActionEventPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_policy_with_options(request, runtime)

    def modify_active_operation_tasks_with_options(self, request, runtime):
        """
        O\\&M tasks such as instance migration and version upgrades are notified by text message, phone call, email, internal message, or in the ApsaraDB RDS console. You can call this operation to change the scheduled switching time. You can also view the task and change the switching time on the Task Center page.
        

        @param request: ModifyActiveOperationTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyActiveOperationTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyActiveOperationTasks',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_active_operation_tasks(self, request):
        """
        O\\&M tasks such as instance migration and version upgrades are notified by text message, phone call, email, internal message, or in the ApsaraDB RDS console. You can call this operation to change the scheduled switching time. You can also view the task and change the switching time on the Task Center page.
        

        @param request: ModifyActiveOperationTasksRequest

        @return: ModifyActiveOperationTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure an automatic backup policy for an ApsaraDB RDS for MySQL instance](~~98818~~)
        *   [Configure an automatic backup policy for an ApsaraDB RDS for PostgreSQL instance](~~96772~~)
        *   [Configure an automatic backup policy for an ApsaraDB RDS for SQL Server instance](~~95717~~)
        *   [Configure an automatic backup policy for an ApsaraDB RDS for MariaDB instance](~~97147~~)
        

        @param request: ModifyBackupPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.archive_backup_keep_count):
            query['ArchiveBackupKeepCount'] = request.archive_backup_keep_count
        if not UtilClient.is_unset(request.archive_backup_keep_policy):
            query['ArchiveBackupKeepPolicy'] = request.archive_backup_keep_policy
        if not UtilClient.is_unset(request.archive_backup_retention_period):
            query['ArchiveBackupRetentionPeriod'] = request.archive_backup_retention_period
        if not UtilClient.is_unset(request.backup_interval):
            query['BackupInterval'] = request.backup_interval
        if not UtilClient.is_unset(request.backup_log):
            query['BackupLog'] = request.backup_log
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.backup_policy_mode):
            query['BackupPolicyMode'] = request.backup_policy_mode
        if not UtilClient.is_unset(request.backup_priority):
            query['BackupPriority'] = request.backup_priority
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.compress_type):
            query['CompressType'] = request.compress_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.enable_increment_data_backup):
            query['EnableIncrementDataBackup'] = request.enable_increment_data_backup
        if not UtilClient.is_unset(request.high_space_usage_protection):
            query['HighSpaceUsageProtection'] = request.high_space_usage_protection
        if not UtilClient.is_unset(request.local_log_retention_hours):
            query['LocalLogRetentionHours'] = request.local_log_retention_hours
        if not UtilClient.is_unset(request.local_log_retention_space):
            query['LocalLogRetentionSpace'] = request.local_log_retention_space
        if not UtilClient.is_unset(request.log_backup_frequency):
            query['LogBackupFrequency'] = request.log_backup_frequency
        if not UtilClient.is_unset(request.log_backup_local_retention_number):
            query['LogBackupLocalRetentionNumber'] = request.log_backup_local_retention_number
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.released_keep_policy):
            query['ReleasedKeepPolicy'] = request.released_keep_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_policy(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure an automatic backup policy for an ApsaraDB RDS for MySQL instance](~~98818~~)
        *   [Configure an automatic backup policy for an ApsaraDB RDS for PostgreSQL instance](~~96772~~)
        *   [Configure an automatic backup policy for an ApsaraDB RDS for SQL Server instance](~~95717~~)
        *   [Configure an automatic backup policy for an ApsaraDB RDS for MariaDB instance](~~97147~~)
        

        @param request: ModifyBackupPolicyRequest

        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_collation_time_zone_with_options(self, request, runtime):
        """
        > This operation is phased out.
        

        @param request: ModifyCollationTimeZoneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyCollationTimeZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collation):
            query['Collation'] = request.collation
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCollationTimeZone',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyCollationTimeZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_collation_time_zone(self, request):
        """
        > This operation is phased out.
        

        @param request: ModifyCollationTimeZoneRequest

        @return: ModifyCollationTimeZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_collation_time_zone_with_options(request, runtime)

    def modify_dbdescription_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: ModifyDBDescriptionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbdescription):
            query['DBDescription'] = request.dbdescription
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbdescription(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        

        @param request: ModifyDBDescriptionRequest

        @return: ModifyDBDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    def modify_dbinstance_auto_upgrade_minor_version_with_options(self, request, runtime):
        """
        This operation is supported only for instances that run MySQL.
        

        @param request: ModifyDBInstanceAutoUpgradeMinorVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceAutoUpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_upgrade_minor_version):
            query['AutoUpgradeMinorVersion'] = request.auto_upgrade_minor_version
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAutoUpgradeMinorVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_auto_upgrade_minor_version(self, request):
        """
        This operation is supported only for instances that run MySQL.
        

        @param request: ModifyDBInstanceAutoUpgradeMinorVersionRequest

        @return: ModifyDBInstanceAutoUpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_minor_version_with_options(request, runtime)

    def modify_dbinstance_config_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        > : The configuration item that is supported is [PgBouncer](~~2398301~~) of ApsaraDB RDS for PostgreSQL instances.
        

        @param request: ModifyDBInstanceConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_config(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        > : The configuration item that is supported is [PgBouncer](~~2398301~~) of ApsaraDB RDS for PostgreSQL instances.
        

        @param request: ModifyDBInstanceConfigRequest

        @return: ModifyDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    def modify_dbinstance_connection_mode_with_options(self, request, runtime):
        """
        > The API has been taken offline
        

        @param request: ModifyDBInstanceConnectionModeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceConnectionModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionMode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_connection_mode(self, request):
        """
        > The API has been taken offline
        

        @param request: ModifyDBInstanceConnectionModeRequest

        @return: ModifyDBInstanceConnectionModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_mode_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        *   [Change the endpoint and port number of an ApsaraDB RDS for MySQL instance](~~96163~~)
        *   [Change the endpoint and port number of an ApsaraDB RDS for PostgreSQL instance](~~96788~~)
        *   [Change the endpoint and port number of an ApsaraDB RDS for SQL Server instance](~~95740~~)
        *   [Change the endpoint and port number of an ApsaraDB RDS for MariaDB instance](~~97157~~)
        

        @param request: ModifyDBInstanceConnectionStringRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.babelfish_port):
            query['BabelfishPort'] = request.babelfish_port
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.general_group_name):
            query['GeneralGroupName'] = request.general_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pgbouncer_port):
            query['PGBouncerPort'] = request.pgbouncer_port
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_connection_string(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        *   [Change the endpoint and port number of an ApsaraDB RDS for MySQL instance](~~96163~~)
        *   [Change the endpoint and port number of an ApsaraDB RDS for PostgreSQL instance](~~96788~~)
        *   [Change the endpoint and port number of an ApsaraDB RDS for SQL Server instance](~~95740~~)
        *   [Change the endpoint and port number of an ApsaraDB RDS for MariaDB instance](~~97157~~)
        

        @param request: ModifyDBInstanceConnectionStringRequest

        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    def modify_dbinstance_delayed_replication_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_sqlreplication_time):
            query['ReadSQLReplicationTime'] = request.read_sqlreplication_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDelayedReplicationTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceDelayedReplicationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_delayed_replication_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_delayed_replication_time_with_options(request, runtime)

    def modify_dbinstance_deletion_protection_with_options(self, request, runtime):
        """
        For more information, see [Enable or disable the release protection feature for an ApsaraDB RDS for MySQL instance](~~414512~~).
        

        @param request: ModifyDBInstanceDeletionProtectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDeletionProtection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_deletion_protection(self, request):
        """
        For more information, see [Enable or disable the release protection feature for an ApsaraDB RDS for MySQL instance](~~414512~~).
        

        @param request: ModifyDBInstanceDeletionProtectionRequest

        @return: ModifyDBInstanceDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_deletion_protection_with_options(request, runtime)

    def modify_dbinstance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_dbinstance_endpoint_with_options(self, tmp_req, runtime):
        """
        ### [](#)Supported database engines
        RDS MySQL
        

        @param tmp_req: ModifyDBInstanceEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceEndpointResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.ModifyDBInstanceEndpointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_items):
            request.node_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_items, 'NodeItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_endpoint_description):
            query['DBInstanceEndpointDescription'] = request.dbinstance_endpoint_description
        if not UtilClient.is_unset(request.dbinstance_endpoint_id):
            query['DBInstanceEndpointId'] = request.dbinstance_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_items_shrink):
            query['NodeItems'] = request.node_items_shrink
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_endpoint(self, request):
        """
        ### [](#)Supported database engines
        RDS MySQL
        

        @param request: ModifyDBInstanceEndpointRequest

        @return: ModifyDBInstanceEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_endpoint_with_options(request, runtime)

    def modify_dbinstance_endpoint_address_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS MySQL
        ### [](#)Precautions
        *   You can modify the following information about the endpoint of an instance: the public and internal endpoints, the public and internal ports, and the virtual private cloud (VPC), vSwitch, and IP address of the internal endpoint.
        *   The VPC and vSwitch must be modified at the same time. If you specify the VPC, vSwitch, and IP address of the internal endpoint, you do not need to specify the endpoint and port. If you specify the endpoint and port, you do not need to specify the VPC, vSwitch, and IP address of the internal endpoint.
        

        @param request: ModifyDBInstanceEndpointAddressRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_endpoint_id):
            query['DBInstanceEndpointId'] = request.dbinstance_endpoint_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_endpoint_address(self, request):
        """
        ### [](#)Supported database engines
        RDS MySQL
        ### [](#)Precautions
        *   You can modify the following information about the endpoint of an instance: the public and internal endpoints, the public and internal ports, and the virtual private cloud (VPC), vSwitch, and IP address of the internal endpoint.
        *   The VPC and vSwitch must be modified at the same time. If you specify the VPC, vSwitch, and IP address of the internal endpoint, you do not need to specify the endpoint and port. If you specify the endpoint and port, you do not need to specify the VPC, vSwitch, and IP address of the internal endpoint.
        

        @param request: ModifyDBInstanceEndpointAddressRequest

        @return: ModifyDBInstanceEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_endpoint_address_with_options(request, runtime)

    def modify_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.hamode):
            query['HAMode'] = request.hamode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sync_mode):
            query['SyncMode'] = request.sync_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceHAConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceHAConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_haconfig_with_options(request, runtime)

    def modify_dbinstance_maintain_time_with_options(self, request, runtime):
        """
        You can set the maintenance time to a period of time during off-peak hours. Alibaba Cloud performs routine maintenance within the maintenance time to minimize impacts on your business.
        

        @param request: ModifyDBInstanceMaintainTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(self, request):
        """
        You can set the maintenance time to a period of time during off-peak hours. Alibaba Cloud performs routine maintenance within the maintenance time to minimize impacts on your business.
        

        @param request: ModifyDBInstanceMaintainTimeRequest

        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    def modify_dbinstance_metrics_with_options(self, request, runtime):
        """
        ## Prerequisites
        Before you call this operation, make sure that the instance runs PostgreSQL.
        For more information, see [View the Enhanced Monitoring metrics of an ApsaraDB RDS for PostgreSQL instance](~~299200~~).
        

        @param request: ModifyDBInstanceMetricsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.metrics_config):
            query['MetricsConfig'] = request.metrics_config
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMetrics',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_metrics(self, request):
        """
        ## Prerequisites
        Before you call this operation, make sure that the instance runs PostgreSQL.
        For more information, see [View the Enhanced Monitoring metrics of an ApsaraDB RDS for PostgreSQL instance](~~299200~~).
        

        @param request: ModifyDBInstanceMetricsRequest

        @return: ModifyDBInstanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_metrics_with_options(request, runtime)

    def modify_dbinstance_monitor_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of ApsaraDB RDS. For more information, see [Billable items, billing methods, and pricing](~~45020~~).
        Alibaba Cloud provides different monitoring frequencies for different instances. For more information, see [Set monitoring frequencies](~~26200~~).
        > * If your want to set the monitoring frequency to every few seconds, you are charged additional fees. For more information, see [Billable items, billing methods, and pricing](~~45020~~).
        > * This operation is not supported for ApsaraDB RDS for PostgreSQL instances. The monitoring frequency of an ApsaraDB RDS for PostgreSQL instance varies based on the query time range. For more information, see [Query performance metrics](~~26280~~).
        

        @param request: ModifyDBInstanceMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMonitor',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_monitor(self, request):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of ApsaraDB RDS. For more information, see [Billable items, billing methods, and pricing](~~45020~~).
        Alibaba Cloud provides different monitoring frequencies for different instances. For more information, see [Set monitoring frequencies](~~26200~~).
        > * If your want to set the monitoring frequency to every few seconds, you are charged additional fees. For more information, see [Billable items, billing methods, and pricing](~~45020~~).
        > * This operation is not supported for ApsaraDB RDS for PostgreSQL instances. The monitoring frequency of an ApsaraDB RDS for PostgreSQL instance varies based on the query time range. For more information, see [Query performance metrics](~~26280~~).
        

        @param request: ModifyDBInstanceMonitorRequest

        @return: ModifyDBInstanceMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    def modify_dbinstance_network_expire_time_with_options(self, request, runtime):
        """
        When an ApsaraDB for RDS instance is in the hybrid access mode, which uses both a VPC endpoint and a classic network endpoint, this operation is used to extend the expiration time of the classic network endpoint.
        

        @param request: ModifyDBInstanceNetworkExpireTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceNetworkExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkExpireTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_network_expire_time(self, request):
        """
        When an ApsaraDB for RDS instance is in the hybrid access mode, which uses both a VPC endpoint and a classic network endpoint, this operation is used to extend the expiration time of the classic network endpoint.
        

        @param request: ModifyDBInstanceNetworkExpireTimeRequest

        @return: ModifyDBInstanceNetworkExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_expire_time_with_options(request, runtime)

    def modify_dbinstance_network_type_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Change the network type of an ApsaraDB RDS for MySQL instance](~~96109~~)
        *   [Change the network type of an ApsaraDB RDS for PostgreSQL instance](~~96761~~)
        *   [Change the network type of an ApsaraDB RDS for SQL Server instance](~~95707~~)
        

        @param request: ModifyDBInstanceNetworkTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceNetworkTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.read_write_splitting_classic_expired_days):
            query['ReadWriteSplittingClassicExpiredDays'] = request.read_write_splitting_classic_expired_days
        if not UtilClient.is_unset(request.read_write_splitting_private_ip_address):
            query['ReadWriteSplittingPrivateIpAddress'] = request.read_write_splitting_private_ip_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_network_type(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Change the network type of an ApsaraDB RDS for MySQL instance](~~96109~~)
        *   [Change the network type of an ApsaraDB RDS for PostgreSQL instance](~~96761~~)
        *   [Change the network type of an ApsaraDB RDS for SQL Server instance](~~95707~~)
        

        @param request: ModifyDBInstanceNetworkTypeRequest

        @return: ModifyDBInstanceNetworkTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    def modify_dbinstance_pay_type_with_options(self, request, runtime):
        """
        This operation is used to change only the billing method of an instance from pay-as-you-go to subscription.
        The following requirements must be met:
        *   The instance belongs to the current account.
        *   The instance uses one of the most recent instance types. For more information, see [Instance types](~~26312~~).
        **\
        **Note**You cannot change the billing method of an instance that uses a phased-out instance type from pay-as-you-go to subscription. If you want to change the billing method of an instance that uses a phased-out instance type from pay-as-you-go to subscription, you must change the instance type of the instance to one of the most recent instance types. Then, you can change the billing method of the instance from pay-as-you-go to subscription. To change the instance type of an instance, you can change the instance specifications of the instance. For more information, see [Change the specifications of an ApsaraDB RDS instance](~~96061~~).
        *   The instance uses the pay-as-you-go billing method and is in the Running state.
        *   Your Alibaba Cloud account has no unpaid orders for the instance for which you want to change the billing method.
        

        @param request: ModifyDBInstancePayTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstancePayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_pay_type(self, request):
        """
        This operation is used to change only the billing method of an instance from pay-as-you-go to subscription.
        The following requirements must be met:
        *   The instance belongs to the current account.
        *   The instance uses one of the most recent instance types. For more information, see [Instance types](~~26312~~).
        **\
        **Note**You cannot change the billing method of an instance that uses a phased-out instance type from pay-as-you-go to subscription. If you want to change the billing method of an instance that uses a phased-out instance type from pay-as-you-go to subscription, you must change the instance type of the instance to one of the most recent instance types. Then, you can change the billing method of the instance from pay-as-you-go to subscription. To change the instance type of an instance, you can change the instance specifications of the instance. For more information, see [Change the specifications of an ApsaraDB RDS instance](~~96061~~).
        *   The instance uses the pay-as-you-go billing method and is in the Running state.
        *   Your Alibaba Cloud account has no unpaid orders for the instance for which you want to change the billing method.
        

        @param request: ModifyDBInstancePayTypeRequest

        @return: ModifyDBInstancePayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    def modify_dbinstance_proxy_configuration_with_options(self, request, runtime):
        """
        > This operation is phased out.
        

        @param request: ModifyDBInstanceProxyConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceProxyConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.proxy_configuration_key):
            query['ProxyConfigurationKey'] = request.proxy_configuration_key
        if not UtilClient.is_unset(request.proxy_configuration_value):
            query['ProxyConfigurationValue'] = request.proxy_configuration_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceProxyConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_proxy_configuration(self, request):
        """
        > This operation is phased out.
        

        @param request: ModifyDBInstanceProxyConfigurationRequest

        @return: ModifyDBInstanceProxyConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_proxy_configuration_with_options(request, runtime)

    def modify_dbinstance_sslwith_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Use the SSL encryption feature for an ApsaraDB RDS for MySQL instance](~~96120~~)
        *   [Use the SSL encryption feature for an ApsaraDB RDS for PostgreSQL instance](~~229517~~)
        *   [Use the SSL encryption feature for an ApsaraDB RDS for SQL Server instance](~~95715~~)
        

        @param request: ModifyDBInstanceSSLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl):
            query['ACL'] = request.acl
        if not UtilClient.is_unset(request.catype):
            query['CAType'] = request.catype
        if not UtilClient.is_unset(request.client_cacert):
            query['ClientCACert'] = request.client_cacert
        if not UtilClient.is_unset(request.client_caenabled):
            query['ClientCAEnabled'] = request.client_caenabled
        if not UtilClient.is_unset(request.client_cert_revocation_list):
            query['ClientCertRevocationList'] = request.client_cert_revocation_list
        if not UtilClient.is_unset(request.client_crl_enabled):
            query['ClientCrlEnabled'] = request.client_crl_enabled
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replication_acl):
            query['ReplicationACL'] = request.replication_acl
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not UtilClient.is_unset(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_ssl(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Use the SSL encryption feature for an ApsaraDB RDS for MySQL instance](~~96120~~)
        *   [Use the SSL encryption feature for an ApsaraDB RDS for PostgreSQL instance](~~229517~~)
        *   [Use the SSL encryption feature for an ApsaraDB RDS for SQL Server instance](~~95715~~)
        

        @param request: ModifyDBInstanceSSLRequest

        @return: ModifyDBInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    def modify_dbinstance_spec_with_options(self, tmp_req, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Fees are generated if the call is successful. Before you call this operation, carefully read the following documentation:
        *   [Change the specifications of an ApsaraDB RDS for MySQL instance](~~96061~~)
        *   [Change the specifications of an ApsaraDB RDS for PostgreSQL instance](~~96750~~)
        *   [Change the specifications of an ApsaraDB RDS for SQL Server instance](~~95665~~)
        *   [Change the specifications of an ApsaraDB RDS for MariaDB instance](~~97129~~)
        

        @param tmp_req: ModifyDBInstanceSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.ModifyDBInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.serverless_configuration):
            request.serverless_configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.serverless_configuration, 'ServerlessConfiguration', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.serverless_configuration_shrink):
            query['ServerlessConfiguration'] = request.serverless_configuration_shrink
        if not UtilClient.is_unset(request.source_biz):
            query['SourceBiz'] = request.source_biz
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSpec',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_spec(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Fees are generated if the call is successful. Before you call this operation, carefully read the following documentation:
        *   [Change the specifications of an ApsaraDB RDS for MySQL instance](~~96061~~)
        *   [Change the specifications of an ApsaraDB RDS for PostgreSQL instance](~~96750~~)
        *   [Change the specifications of an ApsaraDB RDS for SQL Server instance](~~95665~~)
        *   [Change the specifications of an ApsaraDB RDS for MariaDB instance](~~97129~~)
        

        @param request: ModifyDBInstanceSpecRequest

        @return: ModifyDBInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    def modify_dbinstance_tdewith_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure TDE for an ApsaraDB RDS for MySQL instance](~~96121~~)
        *   [Configure TDE for an ApsaraDB RDS for PostgreSQL instance](~~465652~~)
        *   [Configure TDE for an ApsaraDB RDS for SQL Server instance](~~95716~~)
        

        @param request: ModifyDBInstanceTDERequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBInstanceTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.is_rotate):
            query['IsRotate'] = request.is_rotate
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pass_word):
            query['PassWord'] = request.pass_word
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceTDE',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbinstance_tde(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure TDE for an ApsaraDB RDS for MySQL instance](~~96121~~)
        *   [Configure TDE for an ApsaraDB RDS for PostgreSQL instance](~~465652~~)
        *   [Configure TDE for an ApsaraDB RDS for SQL Server instance](~~95716~~)
        

        @param request: ModifyDBInstanceTDERequest

        @return: ModifyDBInstanceTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    def modify_dbnode_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rds_20140815_models.ModifyDBNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbnode):
            request.dbnode_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbnode, 'DBNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.dbnode_shrink):
            query['DBNode'] = request.dbnode_shrink
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.produce_async):
            query['ProduceAsync'] = request.produce_async
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNode',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbnode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbnode_with_options(request, runtime)

    def modify_dbproxy_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Enable and configure the dedicated proxy feature for an ApsaraDB RDS for MySQL instance](~~197456~~)
        *   [Enable and configure the dedicated proxy feature for an ApsaraDB RDS for PostgreSQL instance](~~418272~~)
        

        @param request: ModifyDBProxyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_dbproxy_service):
            query['ConfigDBProxyService'] = request.config_dbproxy_service
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.dbproxy_instance_num):
            query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBProxy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Enable and configure the dedicated proxy feature for an ApsaraDB RDS for MySQL instance](~~197456~~)
        *   [Enable and configure the dedicated proxy feature for an ApsaraDB RDS for PostgreSQL instance](~~418272~~)
        

        @param request: ModifyDBProxyRequest

        @return: ModifyDBProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_with_options(request, runtime)

    def modify_dbproxy_endpoint_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Enable and configure the dedicated proxy feature](~~197456~~)
        *   [Create a database proxy terminal for an ApsaraDB RDS for PostgreSQL instance](~~418273~~)
        

        @param request: ModifyDBProxyEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBProxyEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_dbproxy_features):
            query['ConfigDBProxyFeatures'] = request.config_dbproxy_features
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_endpoint_id):
            query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.db_endpoint_aliases):
            query['DbEndpointAliases'] = request.db_endpoint_aliases
        if not UtilClient.is_unset(request.db_endpoint_operator):
            query['DbEndpointOperator'] = request.db_endpoint_operator
        if not UtilClient.is_unset(request.db_endpoint_read_write_mode):
            query['DbEndpointReadWriteMode'] = request.db_endpoint_read_write_mode
        if not UtilClient.is_unset(request.db_endpoint_type):
            query['DbEndpointType'] = request.db_endpoint_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_only_instance_distribution_type):
            query['ReadOnlyInstanceDistributionType'] = request.read_only_instance_distribution_type
        if not UtilClient.is_unset(request.read_only_instance_max_delay_time):
            query['ReadOnlyInstanceMaxDelayTime'] = request.read_only_instance_max_delay_time
        if not UtilClient.is_unset(request.read_only_instance_weight):
            query['ReadOnlyInstanceWeight'] = request.read_only_instance_weight
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpoint',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy_endpoint(self, request):
        """
        ### [](#)Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Enable and configure the dedicated proxy feature](~~197456~~)
        *   [Create a database proxy terminal for an ApsaraDB RDS for PostgreSQL instance](~~418273~~)
        

        @param request: ModifyDBProxyEndpointRequest

        @return: ModifyDBProxyEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_with_options(request, runtime)

    def modify_dbproxy_endpoint_address_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for MySQL instance](~~184921~~)
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for PostgreSQL instance](~~418274~~)
        

        @param request: ModifyDBProxyEndpointAddressRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBProxyEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_connect_string_net_type):
            query['DBProxyConnectStringNetType'] = request.dbproxy_connect_string_net_type
        if not UtilClient.is_unset(request.dbproxy_endpoint_id):
            query['DBProxyEndpointId'] = request.dbproxy_endpoint_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.dbproxy_new_connect_string):
            query['DBProxyNewConnectString'] = request.dbproxy_new_connect_string
        if not UtilClient.is_unset(request.dbproxy_new_connect_string_port):
            query['DBProxyNewConnectStringPort'] = request.dbproxy_new_connect_string_port
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyEndpointAddress',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy_endpoint_address(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for MySQL instance](~~184921~~)
        *   [Configure the dedicated proxy endpoint of an ApsaraDB RDS for PostgreSQL instance](~~418274~~)
        

        @param request: ModifyDBProxyEndpointAddressRequest

        @return: ModifyDBProxyEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_address_with_options(request, runtime)

    def modify_dbproxy_instance_with_options(self, request, runtime):
        """
        Before you call the ModifyDBProxyInstance operation, make sure that the [ModifyDBProxy](~~141054~~) operation is called to enable the database proxy feature for the instance.
        *   The dedicated proxy feature of ApsaraDB RDS for MySQL provides capabilities such as read/write splitting and short-lived connection optimization. For more information, see [What are database proxies?](~~138705~~)
        *   The database proxy feature of ApsaraDB RDS for PostgreSQL supports read/write splitting. For more information, see [What are database proxies?](~~412194~~)
        

        @param request: ModifyDBProxyInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDBProxyInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.dbproxy_instance_num):
            query['DBProxyInstanceNum'] = request.dbproxy_instance_num
        if not UtilClient.is_unset(request.dbproxy_instance_type):
            query['DBProxyInstanceType'] = request.dbproxy_instance_type
        if not UtilClient.is_unset(request.effective_specific_time):
            query['EffectiveSpecificTime'] = request.effective_specific_time
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBProxyInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDBProxyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dbproxy_instance(self, request):
        """
        Before you call the ModifyDBProxyInstance operation, make sure that the [ModifyDBProxy](~~141054~~) operation is called to enable the database proxy feature for the instance.
        *   The dedicated proxy feature of ApsaraDB RDS for MySQL provides capabilities such as read/write splitting and short-lived connection optimization. For more information, see [What are database proxies?](~~138705~~)
        *   The database proxy feature of ApsaraDB RDS for PostgreSQL supports read/write splitting. For more information, see [What are database proxies?](~~412194~~)
        

        @param request: ModifyDBProxyInstanceRequest

        @return: ModifyDBProxyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_instance_with_options(request, runtime)

    def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        """
        Distributed transaction whitelists allow for distributed transactions between an Elastic Compute Service (ECS) instance and an RDS instance. For more information, see [Configure a distributed transaction whitelist](~~124321~~).
        This operation is applicable to instances that run one of the following SQL Server versions in the RDS High-Availability Edition: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE.
        

        @param request: ModifyDTCSecurityIpHostsForSQLServerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDTCSecurityIpHostsForSQLServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_hosts):
            query['SecurityIpHosts'] = request.security_ip_hosts
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.white_list_group_name):
            query['WhiteListGroupName'] = request.white_list_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDTCSecurityIpHostsForSQLServer',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        """
        Distributed transaction whitelists allow for distributed transactions between an Elastic Compute Service (ECS) instance and an RDS instance. For more information, see [Configure a distributed transaction whitelist](~~124321~~).
        This operation is applicable to instances that run one of the following SQL Server versions in the RDS High-Availability Edition: 2012 SE, 2012 EE, 2014 SE, 2016 SE, 2016 EE, and 2017 SE.
        

        @param request: ModifyDTCSecurityIpHostsForSQLServerRequest

        @return: ModifyDTCSecurityIpHostsForSQLServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def modify_das_instance_config_with_options(self, request, runtime):
        """
        This operation is supported for ApsaraDB RDS for MySQL instances that run RDS High-availability Edition and use standard SSDs or enhanced SSDs (ESSDs) and ApsaraDB RDS for PostgreSQL instances that use standard SSDs or ESSDs. If the available storage reaches the specified threshold, ApsaraDB RDS increases the storage capacity of the instance to meet your storage requirements. In most cases, no transient connections occur during the expansion process. For more information, see [Configure automatic storage expansion for an ApsaraDB RDS for MySQL instance](~~173826~~) and [Configure automatic storage expansion for an ApsaraDB RDS for PostgreSQL instance](~~432496~~).
        >  If an automatic storage expansion is triggered, ApsaraDB RDS increases the storage capacity based on the larger value between 15% of the purchased storage capacity and 5 GB.
        

        @param request: ModifyDasInstanceConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDasInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_auto_scale):
            query['StorageAutoScale'] = request.storage_auto_scale
        if not UtilClient.is_unset(request.storage_threshold):
            query['StorageThreshold'] = request.storage_threshold
        if not UtilClient.is_unset(request.storage_upper_bound):
            query['StorageUpperBound'] = request.storage_upper_bound
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDasInstanceConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDasInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_das_instance_config(self, request):
        """
        This operation is supported for ApsaraDB RDS for MySQL instances that run RDS High-availability Edition and use standard SSDs or enhanced SSDs (ESSDs) and ApsaraDB RDS for PostgreSQL instances that use standard SSDs or ESSDs. If the available storage reaches the specified threshold, ApsaraDB RDS increases the storage capacity of the instance to meet your storage requirements. In most cases, no transient connections occur during the expansion process. For more information, see [Configure automatic storage expansion for an ApsaraDB RDS for MySQL instance](~~173826~~) and [Configure automatic storage expansion for an ApsaraDB RDS for PostgreSQL instance](~~432496~~).
        >  If an automatic storage expansion is triggered, ApsaraDB RDS increases the storage capacity based on the larger value between 15% of the purchased storage capacity and 5 GB.
        

        @param request: ModifyDasInstanceConfigRequest

        @return: ModifyDasInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_das_instance_config_with_options(request, runtime)

    def modify_database_config_with_options(self, request, runtime):
        """
        ### [](#)Supported database engine
        *   SQL Server
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Manage advanced features of an ApsaraDB RDS for SQL Server instance](~~2401398~~)
        

        @param request: ModifyDatabaseConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDatabaseConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.database_property_name):
            query['DatabasePropertyName'] = request.database_property_name
        if not UtilClient.is_unset(request.database_property_value):
            query['DatabasePropertyValue'] = request.database_property_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDatabaseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_database_config(self, request):
        """
        ### [](#)Supported database engine
        *   SQL Server
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Manage advanced features of an ApsaraDB RDS for SQL Server instance](~~2401398~~)
        

        @param request: ModifyDatabaseConfigRequest

        @return: ModifyDatabaseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_config_with_options(request, runtime)

    def modify_db_proxy_instance_ssl_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS MySQL
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        [Configure SSL encryption for a proxy endpoint](~~188164~~)
        

        @param request: ModifyDbProxyInstanceSslRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDbProxyInstanceSslResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_proxy_connect_string):
            query['DbProxyConnectString'] = request.db_proxy_connect_string
        if not UtilClient.is_unset(request.db_proxy_endpoint_id):
            query['DbProxyEndpointId'] = request.db_proxy_endpoint_id
        if not UtilClient.is_unset(request.db_proxy_ssl_enabled):
            query['DbProxySslEnabled'] = request.db_proxy_ssl_enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDbProxyInstanceSsl',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyDbProxyInstanceSslResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_db_proxy_instance_ssl(self, request):
        """
        ### [](#)Supported database engines
        RDS MySQL
        ### [](#)References
        > : Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        [Configure SSL encryption for a proxy endpoint](~~188164~~)
        

        @param request: ModifyDbProxyInstanceSslRequest

        @return: ModifyDbProxyInstanceSslResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_db_proxy_instance_ssl_with_options(request, runtime)

    def modify_hadiagnose_config_with_options(self, request, runtime):
        """
        By default, Alibaba Cloud uses persistent connections to check the availability of an instance. For more information, see [What is availability detection?](~~207467~~)
        

        @param request: ModifyHADiagnoseConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHADiagnoseConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tcp_connection_type):
            query['TcpConnectionType'] = request.tcp_connection_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHADiagnoseConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHADiagnoseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hadiagnose_config(self, request):
        """
        By default, Alibaba Cloud uses persistent connections to check the availability of an instance. For more information, see [What is availability detection?](~~207467~~)
        

        @param request: ModifyHADiagnoseConfigRequest

        @return: ModifyHADiagnoseConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hadiagnose_config_with_options(request, runtime)

    def modify_haswitch_config_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### [](#)References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for MySQL instance](~~96054~~)
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for PostgreSQL instance](~~96747~~)
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for SQL Server instance](~~95659~~)
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for MariaDB instance](~~97127~~)
        

        @param request: ModifyHASwitchConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHASwitchConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.haconfig):
            query['HAConfig'] = request.haconfig
        if not UtilClient.is_unset(request.manual_hatime):
            query['ManualHATime'] = request.manual_hatime
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHASwitchConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyHASwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_haswitch_config(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### [](#)References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for MySQL instance](~~96054~~)
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for PostgreSQL instance](~~96747~~)
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for SQL Server instance](~~95659~~)
        *   [Use the automatic primary/secondary switchover feature for an ApsaraDB RDS for MariaDB instance](~~97127~~)
        

        @param request: ModifyHASwitchConfigRequest

        @return: ModifyHASwitchConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_haswitch_config_with_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        """
        If you enable auto-renewal for your instance, you do not need to manually renew your subscription or be concerned about business interruptions caused by subscription expiration. For more information, see [Configure auto-renewal](~~96049~~).
        

        @param request: ModifyInstanceAutoRenewalAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewalAttribute',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(self, request):
        """
        If you enable auto-renewal for your instance, you do not need to manually renew your subscription or be concerned about business interruptions caused by subscription expiration. For more information, see [Configure auto-renewal](~~96049~~).
        

        @param request: ModifyInstanceAutoRenewalAttributeRequest

        @return: ModifyInstanceAutoRenewalAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def modify_instance_cross_backup_policy_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: ModifyInstanceCrossBackupPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyInstanceCrossBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_enabled):
            query['BackupEnabled'] = request.backup_enabled
        if not UtilClient.is_unset(request.cross_backup_region):
            query['CrossBackupRegion'] = request.cross_backup_region
        if not UtilClient.is_unset(request.cross_backup_type):
            query['CrossBackupType'] = request.cross_backup_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.log_backup_enabled):
            query['LogBackupEnabled'] = request.log_backup_enabled
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retent_type):
            query['RetentType'] = request.retent_type
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceCrossBackupPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_cross_backup_policy(self, request):
        """
        ### [](#)Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### [](#)References
        *   [Use the cross-region backup feature of an ApsaraDB RDS for MySQL instance](~~120824~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for PostgreSQL instance](~~206671~~)
        *   [Use the cross-region backup feature for an ApsaraDB RDS for SQL Server instance](~~187923~~)
        

        @param request: ModifyInstanceCrossBackupPolicyRequest

        @return: ModifyInstanceCrossBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_cross_backup_policy_with_options(request, runtime)

    def modify_pghba_config_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Connect an ApsaraDB RDS for PostgreSQL instance to a self-managed AD domain](~~349288~~)
        *   [The pg_hba.conf File](https://www.postgresql.org/docs/11/auth-pg-hba-conf.html)
        

        @param request: ModifyPGHbaConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyPGHbaConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.hba_item):
            query['HbaItem'] = request.hba_item
        if not UtilClient.is_unset(request.ops_type):
            query['OpsType'] = request.ops_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPGHbaConfig',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyPGHbaConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_pghba_config(self, request):
        """
        ### [](#)Supported database engines
        RDS PostgreSQL
        ### [](#)References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Connect an ApsaraDB RDS for PostgreSQL instance to a self-managed AD domain](~~349288~~)
        *   [The pg_hba.conf File](https://www.postgresql.org/docs/11/auth-pg-hba-conf.html)
        

        @param request: ModifyPGHbaConfigRequest

        @return: ModifyPGHbaConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_pghba_config_with_options(request, runtime)

    def modify_parameter_with_options(self, request, runtime):
        """
        You can modify the parameters directly or by using a parameter template. After you submit the parameter modification request, ApsaraDB RDS starts a task to apply the new parameter values to the instance. If a new parameter value takes effect only after the instance restarts, ApsaraDB RDS restarts the instance. For information about configurable parameters, see [Configure the parameters of an ApsaraDB RDS for MySQL instance](~~96063~~).
        > Before the system runs a parameter modification task, the system checks whether the parameters exist, whether they are configurable, and whether the new parameter values are valid.
        

        @param request: ModifyParameterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyParameterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.forcerestart):
            query['Forcerestart'] = request.forcerestart
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameter',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameter(self, request):
        """
        You can modify the parameters directly or by using a parameter template. After you submit the parameter modification request, ApsaraDB RDS starts a task to apply the new parameter values to the instance. If a new parameter value takes effect only after the instance restarts, ApsaraDB RDS restarts the instance. For information about configurable parameters, see [Configure the parameters of an ApsaraDB RDS for MySQL instance](~~96063~~).
        > Before the system runs a parameter modification task, the system checks whether the parameters exist, whether they are configurable, and whether the new parameter values are valid.
        

        @param request: ModifyParameterRequest

        @return: ModifyParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    def modify_parameter_group_with_options(self, request, runtime):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: ModifyParameterGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameterGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameter_group(self, request):
        """
        You can configure a number of parameters at a time by using a parameter template and then apply the parameter template to an instance. For more information, see [Use a parameter template to configure the parameters of ApsaraDB RDS for MySQL instances](~~130565~~) or [Use a parameter template to configure the parameters of ApsaraDB RDS for PostgreSQL instances](~~457176~~).
        > This operation is supported only when your instance runs MySQL or PostgreSQL.
        

        @param request: ModifyParameterGroupRequest

        @return: ModifyParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    def modify_read_write_splitting_connection_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   The shared proxy feature is enabled for your ApsaraDB RDS for MySQL instance.
        *   The read/write splitting feature is enabled for your ApsaraDB RDS for MySQL instance.
        *   The instance must run one of the following database engine versions and RDS editions:
        *   MySQL 5.7 on RDS High-availability Edition (with local disks)
        *   MySQL 5.6
        *   SQL Server on RDS Cluster Edition
        

        @param request: ModifyReadWriteSplittingConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyReadWriteSplittingConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.distribution_type):
            query['DistributionType'] = request.distribution_type
        if not UtilClient.is_unset(request.max_delay_time):
            query['MaxDelayTime'] = request.max_delay_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_read_write_splitting_connection(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   The shared proxy feature is enabled for your ApsaraDB RDS for MySQL instance.
        *   The read/write splitting feature is enabled for your ApsaraDB RDS for MySQL instance.
        *   The instance must run one of the following database engine versions and RDS editions:
        *   MySQL 5.7 on RDS High-availability Edition (with local disks)
        *   MySQL 5.6
        *   SQL Server on RDS Cluster Edition
        

        @param request: ModifyReadWriteSplittingConnectionRequest

        @return: ModifyReadWriteSplittingConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_read_write_splitting_connection_with_options(request, runtime)

    def modify_readonly_instance_delay_replication_time_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS MySQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Set the data replication latency of a read-only ApsaraDB RDS for MySQL instance](~~96056~~)
        

        @param request: ModifyReadonlyInstanceDelayReplicationTimeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyReadonlyInstanceDelayReplicationTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.read_sqlreplication_time):
            query['ReadSQLReplicationTime'] = request.read_sqlreplication_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReadonlyInstanceDelayReplicationTime',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_readonly_instance_delay_replication_time(self, request):
        """
        ### Supported database engines
        RDS MySQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Set the data replication latency of a read-only ApsaraDB RDS for MySQL instance](~~96056~~)
        

        @param request: ModifyReadonlyInstanceDelayReplicationTimeRequest

        @return: ModifyReadonlyInstanceDelayReplicationTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_readonly_instance_delay_replication_time_with_options(request, runtime)

    def modify_resource_group_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Transfer resources across resource groups](~~94487~~)
        

        @param request: ModifyResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceGroup',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_resource_group(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Transfer resources across resource groups](~~94487~~)
        

        @param request: ModifyResourceGroupRequest

        @return: ModifyResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    def modify_sqlcollector_policy_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Use the SQL Explorer and Audit feature for an ApsaraDB RDS for MySQL instance](~~476574~~)
        *   [Use the SQL Audit feature for an ApsaraDB RDS for PostgreSQL instance](~~96766~~)
        *   [Use the SQL Audit feature for an ApsaraDB RDS for SQL Server instance](~~95712~~)
        

        @param request: ModifySQLCollectorPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySQLCollectorPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqlcollector_status):
            query['SQLCollectorStatus'] = request.sqlcollector_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_sqlcollector_policy(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Use the SQL Explorer and Audit feature for an ApsaraDB RDS for MySQL instance](~~476574~~)
        *   [Use the SQL Audit feature for an ApsaraDB RDS for PostgreSQL instance](~~96766~~)
        *   [Use the SQL Audit feature for an ApsaraDB RDS for SQL Server instance](~~95712~~)
        

        @param request: ModifySQLCollectorPolicyRequest

        @return: ModifySQLCollectorPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    def modify_sqlcollector_retention_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS MySQL
        ### Precautions
        After you shorten the log backup retention period, log backup files that are stored longer than the specified log backup retention period are immediately deleted.
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Use the SQL Explorer and Audit feature](~~476574~~)
        

        @param request: ModifySQLCollectorRetentionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySQLCollectorRetentionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorRetention',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySQLCollectorRetentionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_sqlcollector_retention(self, request):
        """
        ### Supported database engines
        RDS MySQL
        ### Precautions
        After you shorten the log backup retention period, log backup files that are stored longer than the specified log backup retention period are immediately deleted.
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Use the SQL Explorer and Audit feature](~~476574~~)
        

        @param request: ModifySQLCollectorRetentionRequest

        @return: ModifySQLCollectorRetentionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_retention_with_options(request, runtime)

    def modify_security_group_configuration_with_options(self, request, runtime):
        """
        After an RDS instance is added to an ECS security group, all ECS instances in the security group can access the RDS instance. For more information, see [Configure a whitelist for an RDS instance](~~96118~~).
        

        @param request: ModifySecurityGroupConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySecurityGroupConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupConfiguration',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_group_configuration(self, request):
        """
        After an RDS instance is added to an ECS security group, all ECS instances in the security group can access the RDS instance. For more information, see [Configure a whitelist for an RDS instance](~~96118~~).
        

        @param request: ModifySecurityGroupConfigurationRequest

        @return: ModifySecurityGroupConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure an IP address whitelist for an ApsaraDB RDS for MySQL instance](~~96118~~)
        *   [Configure an IP address whitelist for an ApsaraDB RDS for PostgreSQL instance](~~43187~~)
        *   [Configure an IP address whitelist for an ApsaraDB RDS for SQL Server instance](~~43186~~)
        *   [Configure an IP address whitelist for an ApsaraDB RDS for MariaDB instance](~~90336~~)
        

        @param request: ModifySecurityIpsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.fresh_white_list_readins):
            query['FreshWhiteListReadins'] = request.fresh_white_list_readins
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iptype):
            query['SecurityIPType'] = request.security_iptype
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.whitelist_network_type):
            query['WhitelistNetworkType'] = request.whitelist_network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_ips(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Configure an IP address whitelist for an ApsaraDB RDS for MySQL instance](~~96118~~)
        *   [Configure an IP address whitelist for an ApsaraDB RDS for PostgreSQL instance](~~43187~~)
        *   [Configure an IP address whitelist for an ApsaraDB RDS for SQL Server instance](~~43186~~)
        *   [Configure an IP address whitelist for an ApsaraDB RDS for MariaDB instance](~~90336~~)
        

        @param request: ModifySecurityIpsRequest

        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_whitelist_template_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: ModifyWhitelistTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyWhitelistTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWhitelistTemplate',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ModifyWhitelistTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_whitelist_template(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        

        @param request: ModifyWhitelistTemplateRequest

        @return: ModifyWhitelistTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_whitelist_template_with_options(request, runtime)

    def purge_dbinstance_log_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Description
        The system automatically uploads log backup files to Object Storage Service (OSS) buckets. If the remaining storage of an instance is insufficient, you can call this operation to upload the log backup files of the instance to OSS buckets. After the upload is complete, the system deletes these files from the instance to release storage. This operation is called to upload log backup files from an instance to OSS buckets and then delete these files from the instance. If the instance runs SQL Server, transaction log backup files are compressed before they are uploaded.
        ### Precautions
        *   When you upload log backup files, the data restoration feature is not affected.
        *   This operation is called to release storage. The backup storage usage is not reduced.
        *   The OSS buckets to which log backup files are uploaded are provided by the system. You do not need to purchase these OSS buckets. In addition, you cannot access these OSS buckets.
        

        @param request: PurgeDBInstanceLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PurgeDBInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeDBInstanceLog',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.PurgeDBInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    def purge_dbinstance_log(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Description
        The system automatically uploads log backup files to Object Storage Service (OSS) buckets. If the remaining storage of an instance is insufficient, you can call this operation to upload the log backup files of the instance to OSS buckets. After the upload is complete, the system deletes these files from the instance to release storage. This operation is called to upload log backup files from an instance to OSS buckets and then delete these files from the instance. If the instance runs SQL Server, transaction log backup files are compressed before they are uploaded.
        ### Precautions
        *   When you upload log backup files, the data restoration feature is not affected.
        *   This operation is called to release storage. The backup storage usage is not reduced.
        *   The OSS buckets to which log backup files are uploaded are provided by the system. You do not need to purchase these OSS buckets. In addition, you cannot access these OSS buckets.
        

        @param request: PurgeDBInstanceLogRequest

        @return: PurgeDBInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.purge_dbinstance_log_with_options(request, runtime)

    def query_notify_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### Feature description
        The notifications are highlighted at the top of the ApsaraDB RDS console. The notifications include renewal reminders and reminders of instance creation failures.
        After you call this operation to query notifications, you can call the [ConfirmNotify](~~610444~~) operation to mark the notifications as confirmed, which means that you understand the content of the notifications.
        

        @param request: QueryNotifyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryNotifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.with_confirmed):
            body['WithConfirmed'] = request.with_confirmed
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryNotify',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.QueryNotifyResponse(),
            self.call_api(params, req, runtime)
        )

    def query_notify(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### Feature description
        The notifications are highlighted at the top of the ApsaraDB RDS console. The notifications include renewal reminders and reminders of instance creation failures.
        After you call this operation to query notifications, you can call the [ConfirmNotify](~~610444~~) operation to mark the notifications as confirmed, which means that you understand the content of the notifications.
        

        @param request: QueryNotifyRequest

        @return: QueryNotifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_notify_with_options(request, runtime)

    def rebuild_dbinstance_with_options(self, request, runtime):
        """
        Dedicated clusters allow you to manage a number of instances at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: RebuildDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RebuildDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rebuild_node_type):
            query['RebuildNodeType'] = request.rebuild_node_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RebuildDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def rebuild_dbinstance(self, request):
        """
        Dedicated clusters allow you to manage a number of instances at a time. You can create multiple dedicated clusters in a single region. Each dedicated cluster consists of multiple hosts. You can create multiple instances on each host. For more information, see [What is ApsaraDB MyBase?](~~141455~~)
        

        @param request: RebuildDBInstanceRequest

        @return: RebuildDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebuild_dbinstance_with_options(request, runtime)

    def receive_dbinstance_with_options(self, request, runtime):
        """
        ## Prerequisites
        A disaster recovery instance is created.
        

        @param request: ReceiveDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReceiveDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.guard_dbinstance_id):
            query['GuardDBInstanceId'] = request.guard_dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReceiveDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReceiveDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def receive_dbinstance(self, request):
        """
        ## Prerequisites
        A disaster recovery instance is created.
        

        @param request: ReceiveDBInstanceRequest

        @return: ReceiveDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.receive_dbinstance_with_options(request, runtime)

    def recovery_dbinstance_with_options(self, request, runtime):
        """
        You can call this operation to restore databases to a new instance or an existing instance. If you want to restore databases to an existing instance, we recommend that you call the [Copy databases](~~88810~~) operation.
        If you want to restore databases to a new instance, you must create an instance and then restore specific or all databases to the new instance.
        *   If you specify the name of a database, only the specified database is restored to the new instance.
        *   If you do not specify the name of a database, all databases are restored to the new instance.
        > This operation is supported only for instances that run SQL Server 2012 or later.
        

        @param request: RecoveryDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RecoveryDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.db_names):
            query['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.target_dbinstance_id):
            query['TargetDBInstanceId'] = request.target_dbinstance_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RecoveryDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def recovery_dbinstance(self, request):
        """
        You can call this operation to restore databases to a new instance or an existing instance. If you want to restore databases to an existing instance, we recommend that you call the [Copy databases](~~88810~~) operation.
        If you want to restore databases to a new instance, you must create an instance and then restore specific or all databases to the new instance.
        *   If you specify the name of a database, only the specified database is restored to the new instance.
        *   If you do not specify the name of a database, all databases are restored to the new instance.
        > This operation is supported only for instances that run SQL Server 2012 or later.
        

        @param request: RecoveryDBInstanceRequest

        @return: RecoveryDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recovery_dbinstance_with_options(request, runtime)

    def release_instance_connection_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        *   [Release the public endpoint of an ApsaraDB RDS for MySQL instance](~~26128~~)
        *   [Release the public endpoint of an ApsaraDB RDS for PostgreSQL instance](~~97738~~)
        *   [Release the public endpoint of an ApsaraDB RDS for SQL Server instance](~~97736~~)
        *   [Release the public endpoint of an ApsaraDB RDS for MariaDB instance](~~97740~~)
        

        @param request: ReleaseInstanceConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReleaseInstanceConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstanceConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstanceConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance_connection(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        *   [Release the public endpoint of an ApsaraDB RDS for MySQL instance](~~26128~~)
        *   [Release the public endpoint of an ApsaraDB RDS for PostgreSQL instance](~~97738~~)
        *   [Release the public endpoint of an ApsaraDB RDS for SQL Server instance](~~97736~~)
        *   [Release the public endpoint of an ApsaraDB RDS for MariaDB instance](~~97740~~)
        

        @param request: ReleaseInstanceConnectionRequest

        @return: ReleaseInstanceConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_connection_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        """
        To ensure data security, you can release the public endpoint when you do not need to access the database from the Internet.
        

        @param request: ReleaseInstancePublicConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance_public_connection(self, request):
        """
        To ensure data security, you can release the public endpoint when you do not need to access the database from the Internet.
        

        @param request: ReleaseInstancePublicConnectionRequest

        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def release_read_write_splitting_connection_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   The shared proxy feature is enabled for your ApsaraDB RDS for MySQL instance.
        *   The read/write splitting feature is enabled for the instance.
        *   The instance must run one of the following database engine versions and RDS editions:
        *   MySQL 5.7 on RDS High-availability Edition (with local disks)
        *   MySQL 5.6
        *   SQL Server on RDS Cluster Edition
        

        @param request: ReleaseReadWriteSplittingConnectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReleaseReadWriteSplittingConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseReadWriteSplittingConnection',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_read_write_splitting_connection(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   The shared proxy feature is enabled for your ApsaraDB RDS for MySQL instance.
        *   The read/write splitting feature is enabled for the instance.
        *   The instance must run one of the following database engine versions and RDS editions:
        *   MySQL 5.7 on RDS High-availability Edition (with local disks)
        *   MySQL 5.6
        *   SQL Server on RDS Cluster Edition
        

        @param request: ReleaseReadWriteSplittingConnectionRequest

        @return: ReleaseReadWriteSplittingConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_read_write_splitting_connection_with_options(request, runtime)

    def remove_tags_from_resource_with_options(self, request, runtime):
        """
        The following list describes the limits:
        *   Up to 10 tags can be unbound in a single request.
        *   If a tag is unbound from all instances to which the tag has been bound, the tag is automatically deleted.
        *   If you specify only a TagKey, all tags that match the TagKey condition are unbound.
        *   You must specify at least a TagKey or a set of a TagKey and a TagValue.
        

        @param request: RemoveTagsFromResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveTagsFromResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.proxy_id):
            query['proxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTagsFromResource',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RemoveTagsFromResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tags_from_resource(self, request):
        """
        The following list describes the limits:
        *   Up to 10 tags can be unbound in a single request.
        *   If a tag is unbound from all instances to which the tag has been bound, the tag is automatically deleted.
        *   If you specify only a TagKey, all tags that match the TagKey condition are unbound.
        *   You must specify at least a TagKey or a set of a TagKey and a TagValue.
        

        @param request: RemoveTagsFromResourceRequest

        @return: RemoveTagsFromResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_resource_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of ApsaraDB RDS. For more information, see [Billable items, billing methods, and pricing](~~45020~~).
        Before you call this operation, make sure that the following requirements are met:
        *   The instance is a subscription instance.
        *   Your account supports credit card payments or balance payments.
        **\
        **Note**By default, coupons available for your account are preferentially used for payment.
        

        @param request: RenewInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        """
        Before you call this operation, make sure that you understand the billing methods and pricing of ApsaraDB RDS. For more information, see [Billable items, billing methods, and pricing](~~45020~~).
        Before you call this operation, make sure that the following requirements are met:
        *   The instance is a subscription instance.
        *   Your account supports credit card payments or balance payments.
        **\
        **Note**By default, coupons available for your account are preferentially used for payment.
        

        @param request: RenewInstanceRequest

        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def reset_account_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Reset of the permissions of privileged accounts](~~140724~~)
        

        @param request: ResetAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Reset of the permissions of privileged accounts](~~140724~~)
        

        @param request: ResetAccountRequest

        @return: ResetAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Reset the password of an ApsaraDB RDS for MySQL instance](~~96100~~)
        *   [Reset the password of an ApsaraDB RDS for PostgreSQL instance](~~96814~~)
        *   [Reset the password of an ApsaraDB RDS for SQL Server instance](~~95691~~)
        *   [Reset the password of an ApsaraDB RDS for MariaDB instance](~~97133~~)
        

        @param request: ResetAccountPasswordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account_password(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Reset the password of an ApsaraDB RDS for MySQL instance](~~96100~~)
        *   [Reset the password of an ApsaraDB RDS for PostgreSQL instance](~~96814~~)
        *   [Reset the password of an ApsaraDB RDS for SQL Server instance](~~95691~~)
        *   [Reset the password of an ApsaraDB RDS for MariaDB instance](~~97133~~)
        

        @param request: ResetAccountPasswordRequest

        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def restart_dbinstance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Restart an ApsaraDB RDS for MySQL instance](~~96051~~)
        *   [Restart an ApsaraDB RDS for PostgreSQL instance](~~96798~~)
        *   [Restart an ApsaraDB RDS for SQL Server instance](~~95656~~)
        *   [Restart an ApsaraDB RDS for MariaDB instance](~~97472~~)
        

        @param request: RestartDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_dbinstance(self, request):
        """
        ### Supported database engines
        *   RDS MySQL
        *   RDS PostgreSQL
        *   RDS SQL Server
        *   RDS MariaDB
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        *   [Restart an ApsaraDB RDS for MySQL instance](~~96051~~)
        *   [Restart an ApsaraDB RDS for PostgreSQL instance](~~96798~~)
        *   [Restart an ApsaraDB RDS for SQL Server instance](~~95656~~)
        *   [Restart an ApsaraDB RDS for MariaDB instance](~~97472~~)
        

        @param request: RestartDBInstanceRequest

        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def restore_ddr_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not UtilClient.is_unset(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.table_meta):
            query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreDdrTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreDdrTableResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_ddr_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_ddr_table_with_options(request, runtime)

    def restore_table_with_options(self, request, runtime):
        """
        ### [](#)Supported database engines
        MySQL
        ### [](#)Description
        ApsaraDB RDS for MySQL supports the restoration of individual databases and tables. If you delete databases or tables from an instance, you can restore the databases or tables by using a backup file. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](~~103175~~). Before you call this operation, make sure that the following requirements are met:
        *   The instance is in the Running state.
        *   The instance does not have ongoing migration tasks.
        *   If you want to restore data to a specific point in time, make sure that the log backup feature is enabled for the instance. For more information, see [Back up an ApsaraDB RDS for MySQL instance](~~98818~~).
        *   The restoration of individual databases or tables is enabled, and new backups are created. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](~~103175~~).
        *   The names that you want to use for the restored tables do not exist in the instance.
        

        @param request: RestoreTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestoreTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instant_recovery):
            query['InstantRecovery'] = request.instant_recovery
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.table_meta):
            query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreTable',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RestoreTableResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_table(self, request):
        """
        ### [](#)Supported database engines
        MySQL
        ### [](#)Description
        ApsaraDB RDS for MySQL supports the restoration of individual databases and tables. If you delete databases or tables from an instance, you can restore the databases or tables by using a backup file. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](~~103175~~). Before you call this operation, make sure that the following requirements are met:
        *   The instance is in the Running state.
        *   The instance does not have ongoing migration tasks.
        *   If you want to restore data to a specific point in time, make sure that the log backup feature is enabled for the instance. For more information, see [Back up an ApsaraDB RDS for MySQL instance](~~98818~~).
        *   The restoration of individual databases or tables is enabled, and new backups are created. For more information, see [Restore individual databases and tables of an ApsaraDB RDS for MySQL instance](~~103175~~).
        *   The names that you want to use for the restored tables do not exist in the instance.
        

        @param request: RestoreTableRequest

        @return: RestoreTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    def revoke_account_privilege_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        *   MariaDB
        ### Prerequisites
        *   The RDS instance is in the Running state.
        *   The database is in the Running state.
        ### Usage notes
        *   The permissions that can be revoked include SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, and TRIGGER.
        *   This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition or run PostgreSQL.
        

        @param request: RevokeAccountPrivilegeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeAccountPrivilege',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_account_privilege(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        *   MariaDB
        ### Prerequisites
        *   The RDS instance is in the Running state.
        *   The database is in the Running state.
        ### Usage notes
        *   The permissions that can be revoked include SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, and TRIGGER.
        *   This operation is not supported for instances that run SQL Server 2017 on RDS Cluster Edition or run PostgreSQL.
        

        @param request: RevokeAccountPrivilegeRequest

        @return: RevokeAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    def revoke_operator_permission_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Grant permissions to the service account of an ApsaraDB RDS for MySQL instance](~~96102~~)
        *   [Grant permissions to the service account of an ApsaraDB RDS for PostgreSQL instance](~~146887~~)
        *   [Grant permissions to the service account of an ApsaraDB RDS for SQL Server instance](~~95693~~)
        

        @param request: RevokeOperatorPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeOperatorPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeOperatorPermission',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.RevokeOperatorPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_operator_permission(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Grant permissions to the service account of an ApsaraDB RDS for MySQL instance](~~96102~~)
        *   [Grant permissions to the service account of an ApsaraDB RDS for PostgreSQL instance](~~146887~~)
        *   [Grant permissions to the service account of an ApsaraDB RDS for SQL Server instance](~~95693~~)
        

        @param request: RevokeOperatorPermissionRequest

        @return: RevokeOperatorPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    def start_dbinstance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        *   [Resume an ApsaraDB RDS for MySQL instance](~~427093~~)
        *   [Resume an ApsaraDB RDS for PostgreSQL instance](~~452314~~)
        *   [Resume an ApsaraDB RDS for SQL Server instance](~~462504~~)
        

        @param request: StartDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_trans_type):
            query['DBInstanceTransType'] = request.dbinstance_trans_type
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.specified_time):
            query['SpecifiedTime'] = request.specified_time
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.target_dbinstance_class):
            query['TargetDBInstanceClass'] = request.target_dbinstance_class
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_log):
            query['TargetDedicatedHostIdForLog'] = request.target_dedicated_host_id_for_log
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_master):
            query['TargetDedicatedHostIdForMaster'] = request.target_dedicated_host_id_for_master
        if not UtilClient.is_unset(request.target_dedicated_host_id_for_slave):
            query['TargetDedicatedHostIdForSlave'] = request.target_dedicated_host_id_for_slave
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dbinstance(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation:
        *   [Resume an ApsaraDB RDS for MySQL instance](~~427093~~)
        *   [Resume an ApsaraDB RDS for PostgreSQL instance](~~452314~~)
        *   [Resume an ApsaraDB RDS for SQL Server instance](~~462504~~)
        

        @param request: StartDBInstanceRequest

        @return: StartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    def stop_dbinstance_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Suspend an ApsaraDB RDS for MySQL instance](~~427093~~)
        *   [Suspend an ApsaraDB RDS for PostgreSQL instance](~~452314~~)
        *   [Suspend an ApsaraDB RDS for SQL Server instance](~~462504~~)
        

        @param request: StopDBInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.StopDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dbinstance(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Suspend an ApsaraDB RDS for MySQL instance](~~427093~~)
        *   [Suspend an ApsaraDB RDS for PostgreSQL instance](~~452314~~)
        *   [Suspend an ApsaraDB RDS for SQL Server instance](~~462504~~)
        

        @param request: StopDBInstanceRequest

        @return: StopDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    def switch_dbinstance_hawith_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Switch workloads between primary and secondary ApsaraDB RDS for MySQL instances](~~96054~~)
        *   [Switch workloads between primary and secondary ApsaraDB RDS for PostgreSQL instances](~~96747~~)
        *   [Switch workloads between primary and secondary ApsaraDB RDS for SQL Server instances](~~95659~~)
        *   [Switch workloads between primary and secondary ApsaraDB RDS for MariaDB instances](~~97127~~)
        

        @param request: SwitchDBInstanceHARequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchDBInstanceHAResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceHA',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_ha(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Switch workloads between primary and secondary ApsaraDB RDS for MySQL instances](~~96054~~)
        *   [Switch workloads between primary and secondary ApsaraDB RDS for PostgreSQL instances](~~96747~~)
        *   [Switch workloads between primary and secondary ApsaraDB RDS for SQL Server instances](~~95659~~)
        *   [Switch workloads between primary and secondary ApsaraDB RDS for MariaDB instances](~~97127~~)
        

        @param request: SwitchDBInstanceHARequest

        @return: SwitchDBInstanceHAResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    def switch_dbinstance_net_type_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Prerequisites
        *   The instance is connected by using its internal or public endpoint.
        *   The instance is in the Running state.
        *   The number of times that you have switched the instance between its internal and public endpoints within the last 24 hours does not reach 20.
        *   The instance resides in the classic network.
        ### Usage notes
        After the endpoint that is used to connect to the instance is changed, you must update the endpoint information in the code of your application and restart the application.
        

        @param request: SwitchDBInstanceNetTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchDBInstanceNetTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.connection_string_type):
            query['ConnectionStringType'] = request.connection_string_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_net_type(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   SQL Server
        ### Prerequisites
        *   The instance is connected by using its internal or public endpoint.
        *   The instance is in the Running state.
        *   The number of times that you have switched the instance between its internal and public endpoints within the last 24 hours does not reach 20.
        *   The instance resides in the classic network.
        ### Usage notes
        After the endpoint that is used to connect to the instance is changed, you must update the endpoint information in the code of your application and restart the application.
        

        @param request: SwitchDBInstanceNetTypeRequest

        @return: SwitchDBInstanceNetTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    def switch_dbinstance_vpc_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Change the VPC and vSwitch for an ApsaraDB RDS for MySQL instance](~~137567~~)
        *   [Change the vSwitch for an ApsaraDB RDS for PostgreSQL instance](~~146885~~)
        *   [Change the VPC and vSwitch for an ApsaraDB RDS for SQL Server instance](~~347675~~)
        

        @param request: SwitchDBInstanceVpcRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchDBInstanceVpcResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceVpc',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchDBInstanceVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dbinstance_vpc(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Change the VPC and vSwitch for an ApsaraDB RDS for MySQL instance](~~137567~~)
        *   [Change the vSwitch for an ApsaraDB RDS for PostgreSQL instance](~~146885~~)
        *   [Change the VPC and vSwitch for an ApsaraDB RDS for SQL Server instance](~~347675~~)
        

        @param request: SwitchDBInstanceVpcRequest

        @return: SwitchDBInstanceVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_vpc_with_options(request, runtime)

    def switch_guard_to_master_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchGuardToMasterInstance',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.SwitchGuardToMasterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_guard_to_master_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_guard_to_master_instance_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can query instances by tag.
        *   A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        *   If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        *   If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        *   You can add up to 20 tags to an instance.
        *   You can add tags to up to 50 instances in each call.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        If you have a large number of instances, you can create multiple tags and add these tags to the instances. Then, you can query instances by tag.
        *   A tag consists of a key and a value. Each key must be unique in a region for an Alibaba Cloud account. Different keys can be mapped to the same value.
        *   If the tag that you specify does not exist, this tag is automatically created and added to the specified instance.
        *   If the key of the specified tag is the same as that of an existing tag, the specified tag overwrites the existing tag.
        *   You can add up to 20 tags to an instance.
        *   You can add tags to up to 50 instances in each call.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def terminate_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.migrate_task_id):
            query['MigrateTaskId'] = request.migrate_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateMigrateTask',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TerminateMigrateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_migrate_task_with_options(request, runtime)

    def transform_dbinstance_pay_type_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Fees are generated if the call is successful. Before you call this operation, you must read the following documentation.
        *   [Change the billing method of an ApsaraDB RDS for MySQL instance from pay-as-you-go to subscription](~~96048~~) or [Change the billing method of an ApsaraDB RDS for MySQL instance from subscription to pay-as-you-go](~~161875~~)
        *   [Change the billing method of an ApsaraDB RDS for PostgreSQL instance from pay-as-you-go to subscription](~~96743~~) or [Change the billing method of an ApsaraDB RDS for PostgreSQL instance from subscription to pay-as-you-go](~~162756~~)
        *   [Change the billing method of an ApsaraDB RDS for SQL Server instance from pay-as-you-go to subscription](~~95631~~) or [Change the billing method of an ApsaraDB RDS for SQL Server instance from subscription to pay-as-you-go](~~162755~~)
        *   [Change the billing method of an ApsaraDB RDS for MariaDB instance from pay-as-you-go to subscription](~~97120~~) or [Change the billing method of an ApsaraDB RDS for MariaDB instance from subscription to pay-as-you-go](~~169252~~)
        

        @param request: TransformDBInstancePayTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TransformDBInstancePayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformDBInstancePayType',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.TransformDBInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def transform_dbinstance_pay_type(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        *   MariaDB
        ### References
        > Fees are generated if the call is successful. Before you call this operation, you must read the following documentation.
        *   [Change the billing method of an ApsaraDB RDS for MySQL instance from pay-as-you-go to subscription](~~96048~~) or [Change the billing method of an ApsaraDB RDS for MySQL instance from subscription to pay-as-you-go](~~161875~~)
        *   [Change the billing method of an ApsaraDB RDS for PostgreSQL instance from pay-as-you-go to subscription](~~96743~~) or [Change the billing method of an ApsaraDB RDS for PostgreSQL instance from subscription to pay-as-you-go](~~162756~~)
        *   [Change the billing method of an ApsaraDB RDS for SQL Server instance from pay-as-you-go to subscription](~~95631~~) or [Change the billing method of an ApsaraDB RDS for SQL Server instance from subscription to pay-as-you-go](~~162755~~)
        *   [Change the billing method of an ApsaraDB RDS for MariaDB instance from pay-as-you-go to subscription](~~97120~~) or [Change the billing method of an ApsaraDB RDS for MariaDB instance from subscription to pay-as-you-go](~~169252~~)
        

        @param request: TransformDBInstancePayTypeRequest

        @return: TransformDBInstancePayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transform_dbinstance_pay_type_with_options(request, runtime)

    def unlock_account_with_options(self, request, runtime):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Lock an account of an ApsaraDB RDS for PostgreSQL instance](~~147649~~)
        

        @param request: UnlockAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnlockAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockAccount',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UnlockAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_account(self, request):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Lock an account of an ApsaraDB RDS for PostgreSQL instance](~~147649~~)
        

        @param request: UnlockAccountRequest

        @return: UnlockAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_account_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        >    You can remove up to 20 tags at a time.
        > *   If a tag is removed from an instance and is not added to other instances, the tag is automatically deleted.
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        >    You can remove up to 20 tags at a time.
        > *   If a tag is removed from an instance and is not added to other instances, the tag is automatically deleted.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_postgres_extensions_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS PostgreSQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        

        @param request: UpdatePostgresExtensionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePostgresExtensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbnames):
            query['DBNames'] = request.dbnames
        if not UtilClient.is_unset(request.extensions):
            query['Extensions'] = request.extensions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePostgresExtensions',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpdatePostgresExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_postgres_extensions(self, request):
        """
        ### Supported database engines
        RDS PostgreSQL
        ### References
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Manage extensions](~~2402409~~)
        

        @param request: UpdatePostgresExtensionsRequest

        @return: UpdatePostgresExtensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_postgres_extensions_with_options(request, runtime)

    def update_user_backup_file_with_options(self, request, runtime):
        """
        ### Supported database engines
        RDS MySQL
        ### References
        A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 or MySQL 8.0 instance to an ApsaraDB RDS for MySQL instance](~~251779~~).
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        

        @param request: UpdateUserBackupFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateUserBackupFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserBackupFile',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpdateUserBackupFileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_backup_file(self, request):
        """
        ### Supported database engines
        RDS MySQL
        ### References
        A full backup file contains the data of a self-managed MySQL database. You can restore the data of a self-managed MySQL database from a full backup file to an ApsaraDB RDS for MySQL instance. For more information, see [Migrate the data of a self-managed MySQL 5.7 or MySQL 8.0 instance to an ApsaraDB RDS for MySQL instance](~~251779~~).
        > : Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        

        @param request: UpdateUserBackupFileRequest

        @return: UpdateUserBackupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_backup_file_with_options(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(self, request, runtime):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Upgrade the major engine version of an ApsaraDB RDS for MySQL instance](~~96058~~)
        

        @param request: UpgradeDBInstanceEngineVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBInstanceEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance_engine_version(self, request):
        """
        ### Supported database engine
        MySQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        [Upgrade the major engine version of an ApsaraDB RDS for MySQL instance](~~96058~~)
        

        @param request: UpgradeDBInstanceEngineVersionRequest

        @return: UpgradeDBInstanceEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Update the minor engine version of an ApsaraDB RDS for MySQL instance](~~96059~~)
        *   [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~)
        *   [Update the minor engine version of an ApsaraDB RDS for SQL Server instance](~~213582~~)
        

        @param request: UpgradeDBInstanceKernelVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBInstanceKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        if not UtilClient.is_unset(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance_kernel_version(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        *   SQL Server
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Update the minor engine version of an ApsaraDB RDS for MySQL instance](~~96059~~)
        *   [Update the minor engine version of an ApsaraDB RDS for PostgreSQL instance](~~146895~~)
        *   [Update the minor engine version of an ApsaraDB RDS for SQL Server instance](~~213582~~)
        

        @param request: UpgradeDBInstanceKernelVersionRequest

        @return: UpgradeDBInstanceKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    def upgrade_dbinstance_major_version_with_options(self, request, runtime):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        Fees are generated if the call is successful. Before you call this operation, read the following documentation and make sure that you fully understand the billing rules, prerequisites, and impacts of this operation.
        [Upgrade the major engine version of an ApsaraDB RDS for PostgreSQL instance](~~203309~~)
        

        @param request: UpgradeDBInstanceMajorVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBInstanceMajorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collect_stat_mode):
            query['CollectStatMode'] = request.collect_stat_mode
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not UtilClient.is_unset(request.dbinstance_storage_type):
            query['DBInstanceStorageType'] = request.dbinstance_storage_type
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_over):
            query['SwitchOver'] = request.switch_over
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_major_version):
            query['TargetMajorVersion'] = request.target_major_version
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_id_slave_1):
            query['ZoneIdSlave1'] = request.zone_id_slave_1
        if not UtilClient.is_unset(request.zone_id_slave_2):
            query['ZoneIdSlave2'] = request.zone_id_slave_2
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceMajorVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceMajorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance_major_version(self, request):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        Fees are generated if the call is successful. Before you call this operation, read the following documentation and make sure that you fully understand the billing rules, prerequisites, and impacts of this operation.
        [Upgrade the major engine version of an ApsaraDB RDS for PostgreSQL instance](~~203309~~)
        

        @param request: UpgradeDBInstanceMajorVersionRequest

        @return: UpgradeDBInstanceMajorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_major_version_with_options(request, runtime)

    def upgrade_dbinstance_major_version_precheck_with_options(self, request, runtime):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Upgrade the major engine version of an ApsaraDB RDS for PostgreSQL instance](~~203309~~)
        

        @param request: UpgradeDBInstanceMajorVersionPrecheckRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBInstanceMajorVersionPrecheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_major_version):
            query['TargetMajorVersion'] = request.target_major_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceMajorVersionPrecheck',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBInstanceMajorVersionPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbinstance_major_version_precheck(self, request):
        """
        ### Supported database engine
        PostgreSQL
        ### References
        > Before you call this operation, carefully read the following documentation. Make sure that you fully understand the prerequisites and impacts for calling this operation.
        [Upgrade the major engine version of an ApsaraDB RDS for PostgreSQL instance](~~203309~~)
        

        @param request: UpgradeDBInstanceMajorVersionPrecheckRequest

        @return: UpgradeDBInstanceMajorVersionPrecheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_major_version_precheck_with_options(request, runtime)

    def upgrade_dbproxy_instance_kernel_version_with_options(self, request, runtime):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Upgrade the dedicated proxy version of an ApsaraDB RDS for MySQL instance](~~197465~~)
        *   [Upgrade the dedicated proxy version of an ApsaraDB RDS for PostgreSQL instance](~~418469~~)
        

        @param request: UpgradeDBProxyInstanceKernelVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeDBProxyInstanceKernelVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbproxy_engine_type):
            query['DBProxyEngineType'] = request.dbproxy_engine_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBProxyInstanceKernelVersion',
            version='2014-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_dbproxy_instance_kernel_version(self, request):
        """
        ### Supported database engines
        *   MySQL
        *   PostgreSQL
        ### References
        > Before you call this operation, read the following documentation and make sure that you fully understand the prerequisites and impacts of this operation.
        *   [Upgrade the dedicated proxy version of an ApsaraDB RDS for MySQL instance](~~197465~~)
        *   [Upgrade the dedicated proxy version of an ApsaraDB RDS for PostgreSQL instance](~~418469~~)
        

        @param request: UpgradeDBProxyInstanceKernelVersionRequest

        @return: UpgradeDBProxyInstanceKernelVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbproxy_instance_kernel_version_with_options(request, runtime)
