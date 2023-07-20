# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sas20181203 import models as sas_20181203_models
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
            'cn-hangzhou': 'tds.aliyuncs.com',
            'ap-southeast-1': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'tds.ap-southeast-3.aliyuncs.com',
            'ap-northeast-1': 'sas.aliyuncs.com',
            'ap-northeast-2-pop': 'sas.aliyuncs.com',
            'ap-south-1': 'sas.aliyuncs.com',
            'ap-southeast-2': 'sas.aliyuncs.com',
            'ap-southeast-5': 'sas.aliyuncs.com',
            'cn-beijing': 'sas.aliyuncs.com',
            'cn-beijing-finance-1': 'sas.aliyuncs.com',
            'cn-beijing-finance-pop': 'sas.aliyuncs.com',
            'cn-beijing-gov-1': 'sas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'sas.aliyuncs.com',
            'cn-chengdu': 'sas.aliyuncs.com',
            'cn-edge-1': 'sas.aliyuncs.com',
            'cn-fujian': 'sas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'sas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'sas.aliyuncs.com',
            'cn-hangzhou-finance': 'sas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'sas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'sas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'sas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'sas.aliyuncs.com',
            'cn-hangzhou-test-306': 'sas.aliyuncs.com',
            'cn-hongkong': 'sas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'sas.aliyuncs.com',
            'cn-huhehaote': 'sas.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'sas.aliyuncs.com',
            'cn-north-2-gov-1': 'sas.aliyuncs.com',
            'cn-qingdao': 'sas.aliyuncs.com',
            'cn-qingdao-nebula': 'sas.aliyuncs.com',
            'cn-shanghai': 'sas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'sas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'sas.aliyuncs.com',
            'cn-shanghai-finance-1': 'sas.aliyuncs.com',
            'cn-shanghai-inner': 'sas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'sas.aliyuncs.com',
            'cn-shenzhen': 'sas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'sas.aliyuncs.com',
            'cn-shenzhen-inner': 'sas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'sas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'sas.aliyuncs.com',
            'cn-wuhan': 'sas.aliyuncs.com',
            'cn-wulanchabu': 'sas.aliyuncs.com',
            'cn-yushanfang': 'sas.aliyuncs.com',
            'cn-zhangbei': 'sas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'sas.aliyuncs.com',
            'cn-zhangjiakou': 'sas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'sas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'sas.aliyuncs.com',
            'eu-central-1': 'sas.aliyuncs.com',
            'eu-west-1': 'sas.aliyuncs.com',
            'eu-west-1-oxs': 'sas.aliyuncs.com',
            'me-east-1': 'sas.aliyuncs.com',
            'rus-west-1-pop': 'sas.aliyuncs.com',
            'us-east-1': 'sas.aliyuncs.com',
            'us-west-1': 'sas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_asset_selection_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_operation):
            query['CriteriaOperation'] = request.criteria_operation
        if not UtilClient.is_unset(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not UtilClient.is_unset(request.target_operation_list):
            query['TargetOperationList'] = request.target_operation_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAssetSelectionCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddAssetSelectionCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def add_asset_selection_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_asset_selection_criteria_with_options(request, runtime)

    def add_check_instance_result_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_group_id):
            query['CheckGroupId'] = request.check_group_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCheckInstanceResultWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddCheckInstanceResultWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_check_instance_result_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_check_instance_result_white_list_with_options(request, runtime)

    def add_check_result_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCheckResultWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddCheckResultWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_check_result_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_check_result_white_list_with_options(request, runtime)

    def add_client_user_define_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.md_5list):
            query['Md5List'] = request.md_5list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_file_path):
            query['NewFilePath'] = request.new_file_path
        if not UtilClient.is_unset(request.parent_cmdline):
            query['ParentCmdline'] = request.parent_cmdline
        if not UtilClient.is_unset(request.parent_proc_path):
            query['ParentProcPath'] = request.parent_proc_path
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.port_str):
            query['PortStr'] = request.port_str
        if not UtilClient.is_unset(request.proc_path):
            query['ProcPath'] = request.proc_path
        if not UtilClient.is_unset(request.registry_content):
            query['RegistryContent'] = request.registry_content
        if not UtilClient.is_unset(request.registry_key):
            query['RegistryKey'] = request.registry_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientUserDefineRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddClientUserDefineRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_client_user_define_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_client_user_define_rule_with_options(request, runtime)

    def add_image_vul_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImageVulWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddImageVulWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_image_vul_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_image_vul_white_list_with_options(request, runtime)

    def add_install_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expired_date):
            query['ExpiredDate'] = request.expired_date
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.only_image):
            query['OnlyImage'] = request.only_image
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.proxy_cluster):
            query['ProxyCluster'] = request.proxy_cluster
        if not UtilClient.is_unset(request.vendor_name):
            query['VendorName'] = request.vendor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddInstallCode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddInstallCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_install_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_install_code_with_options(request, runtime)

    def add_private_registry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.registry_host_ip):
            query['RegistryHostIp'] = request.registry_host_ip
        if not UtilClient.is_unset(request.registry_region_id):
            query['RegistryRegionId'] = request.registry_region_id
        if not UtilClient.is_unset(request.registry_type):
            query['RegistryType'] = request.registry_type
        if not UtilClient.is_unset(request.registry_version):
            query['RegistryVersion'] = request.registry_version
        if not UtilClient.is_unset(request.trans_per_hour):
            query['TransPerHour'] = request.trans_per_hour
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrivateRegistry',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddPrivateRegistryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_private_registry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_private_registry_with_options(request, runtime)

    def add_tag_with_uuid_with_options(self, request, runtime):
        """
        Security Center provides asset importance tags and custom tags. You can call the AddTagWithUuid operation to add only a custom tag to assets.
        

        @param request: AddTagWithUuidRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTagWithUuidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddTagWithUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tag_with_uuid(self, request):
        """
        Security Center provides asset importance tags and custom tags. You can call the AddTagWithUuid operation to add only a custom tag to assets.
        

        @param request: AddTagWithUuidRequest

        @return: AddTagWithUuidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tag_with_uuid_with_options(request, runtime)

    def add_uninstall_clients_by_uuids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_method):
            query['CallMethod'] = request.call_method
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUninstallClientsByUuids',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddUninstallClientsByUuidsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_uninstall_clients_by_uuids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_uninstall_clients_by_uuids_with_options(request, runtime)

    def add_vpc_honey_pot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AddVpcHoneyPotResponse(),
            self.call_api(params, req, runtime)
        )

    def add_vpc_honey_pot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vpc_honey_pot_with_options(request, runtime)

    def advance_security_event_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AdvanceSecurityEventOperations',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.AdvanceSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def advance_security_event_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.advance_security_event_operations_with_options(request, runtime)

    def batch_operate_common_overall_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.type_list):
            query['TypeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchOperateCommonOverallConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.BatchOperateCommonOverallConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_operate_common_overall_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_operate_common_overall_config_with_options(request, runtime)

    def bind_auth_to_machine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_version):
            query['AuthVersion'] = request.auth_version
        if not UtilClient.is_unset(request.auto_bind):
            query['AutoBind'] = request.auto_bind
        if not UtilClient.is_unset(request.bind):
            query['Bind'] = request.bind
        if not UtilClient.is_unset(request.bind_all):
            query['BindAll'] = request.bind_all
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.un_bind):
            query['UnBind'] = request.un_bind
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAuthToMachine',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.BindAuthToMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_auth_to_machine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_auth_to_machine_with_options(request, runtime)

    def cancel_once_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOnceTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CancelOnceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_once_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_once_task_with_options(request, runtime)

    def change_asset_refresh_task_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_refresh_configs):
            query['AssetRefreshConfigs'] = request.asset_refresh_configs
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAssetRefreshTaskConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ChangeAssetRefreshTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def change_asset_refresh_task_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_asset_refresh_task_config_with_options(request, runtime)

    def change_check_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.added_check):
            query['AddedCheck'] = request.added_check
        if not UtilClient.is_unset(request.cycle_days):
            query['CycleDays'] = request.cycle_days
        if not UtilClient.is_unset(request.enable_add_check):
            query['EnableAddCheck'] = request.enable_add_check
        if not UtilClient.is_unset(request.enable_auto_check):
            query['EnableAutoCheck'] = request.enable_auto_check
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removed_check):
            query['RemovedCheck'] = request.removed_check
        if not UtilClient.is_unset(request.standard_ids):
            query['StandardIds'] = request.standard_ids
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeCheckConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ChangeCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def change_check_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_check_config_with_options(request, runtime)

    def change_check_custom_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.custom_configs):
            query['CustomConfigs'] = request.custom_configs
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeCheckCustomConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ChangeCheckCustomConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def change_check_custom_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_check_custom_config_with_options(request, runtime)

    def check_quara_file_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.quara_file_ids):
            query['QuaraFileIds'] = request.quara_file_ids
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckQuaraFileId',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckQuaraFileIdResponse(),
            self.call_api(params, req, runtime)
        )

    def check_quara_file_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_quara_file_id_with_options(request, runtime)

    def check_security_event_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSecurityEventId',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckSecurityEventIdResponse(),
            self.call_api(params, req, runtime)
        )

    def check_security_event_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_security_event_id_with_options(request, runtime)

    def check_user_has_ecs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserHasEcs',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckUserHasEcsResponse(),
            self.call_api(params, req, runtime)
        )

    def check_user_has_ecs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_user_has_ecs_with_options(request, runtime)

    def confirm_virus_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_all):
            query['OperationAll'] = request.operation_all
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_range):
            query['OperationRange'] = request.operation_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmVirusEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ConfirmVirusEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_virus_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_virus_events_with_options(request, runtime)

    def create_agentless_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_delete_days):
            query['AutoDeleteDays'] = request.auto_delete_days
        if not UtilClient.is_unset(request.release_after_scan):
            query['ReleaseAfterScan'] = request.release_after_scan
        if not UtilClient.is_unset(request.scan_data_disk):
            query['ScanDataDisk'] = request.scan_data_disk
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAgentlessScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAgentlessScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_agentless_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_agentless_scan_task_with_options(request, runtime)

    def create_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.fail_count):
            query['FailCount'] = request.fail_count
        if not UtilClient.is_unset(request.forbidden_time):
            query['ForbiddenTime'] = request.forbidden_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.span):
            query['Span'] = request.span
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_anti_brute_force_rule_with_options(request, runtime)

    def create_asset_selection_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAssetSelectionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAssetSelectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_asset_selection_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_asset_selection_config_with_options(request, runtime)

    def create_backup_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.CreateBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.policy_region_id):
            query['PolicyRegionId'] = request.policy_region_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    def create_container_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_ids):
            query['ContainerIds'] = request.container_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateContainerScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateContainerScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_container_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_container_scan_task_with_options(request, runtime)

    def create_custom_block_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.bound):
            query['Bound'] = request.bound
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomBlockRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateCustomBlockRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_block_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_block_record_with_options(request, runtime)

    def create_cycle_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.first_date_str):
            query['FirstDateStr'] = request.first_date_str
        if not UtilClient.is_unset(request.interval_period):
            query['IntervalPeriod'] = request.interval_period
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.target_end_time):
            query['TargetEndTime'] = request.target_end_time
        if not UtilClient.is_unset(request.target_start_time):
            query['TargetStartTime'] = request.target_start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCycleTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateCycleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cycle_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cycle_task_with_options(request, runtime)

    def create_file_detect_with_options(self, request, runtime):
        """
        You can call this operation to push a file to the cloud for detection. Before you call this operation, make sure that the file is uploaded. You can call the CreateFileDetectUploadUrl operation to upload the file.
        The HashKey parameter is included in all API operations that are related to the file detection feature. The parameter specifies the unique identifier of a file. Only hexadecimal MD5 hash values of complete file content are supported. You must calculate the MD5 hash value before you call this operation.
        To calculate the hexadecimal MD5 hash value for a file, you can perform the following steps:
        1\\. Use the MD5 algorithm to encrypt data and generate a 128-bit hash value. You can use a tool such as MessageDigest for Java and the hashlib module for Python.
        2\\. Convert the hash value to a hexadecimal string. You can use a tool such as Codec for Java and the hex() function for Python.
        

        @param request: CreateFileDetectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFileDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.hash_key):
            query['HashKey'] = request.hash_key
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileDetect',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateFileDetectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file_detect(self, request):
        """
        You can call this operation to push a file to the cloud for detection. Before you call this operation, make sure that the file is uploaded. You can call the CreateFileDetectUploadUrl operation to upload the file.
        The HashKey parameter is included in all API operations that are related to the file detection feature. The parameter specifies the unique identifier of a file. Only hexadecimal MD5 hash values of complete file content are supported. You must calculate the MD5 hash value before you call this operation.
        To calculate the hexadecimal MD5 hash value for a file, you can perform the following steps:
        1\\. Use the MD5 algorithm to encrypt data and generate a 128-bit hash value. You can use a tool such as MessageDigest for Java and the hashlib module for Python.
        2\\. Convert the hash value to a hexadecimal string. You can use a tool such as Codec for Java and the hex() function for Python.
        

        @param request: CreateFileDetectRequest

        @return: CreateFileDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_detect_with_options(request, runtime)

    def create_file_detect_upload_url_with_options(self, request, runtime):
        """
        You can call this operation to query the parameters that are required to upload a file for detection. If the value of the response parameter FileExist is true, the file that you want to upload for detection already exists in the cloud. In this case, you can directly push the file for detection. If the value of the response parameter FileExist is false, you must use the form upload method to upload the file to the specified Object Storage Service (OSS) bucket based on the response parameters of this operation.
        The form upload method is provided by OSS. For more information, see [Form upload](~~84788~~).
        The HashKey parameter is included in all API operations that are related to the file detection feature. The parameter specifies the unique identifier of a file. Only MD5 hash values are supported. Before you call this operation, calculate the MD5 hash value of the file.
        

        @param request: CreateFileDetectUploadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFileDetectUploadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hash_key_context_list):
            query['HashKeyContextList'] = request.hash_key_context_list
        if not UtilClient.is_unset(request.hash_key_list):
            query['HashKeyList'] = request.hash_key_list
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileDetectUploadUrl',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateFileDetectUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_file_detect_upload_url(self, request):
        """
        You can call this operation to query the parameters that are required to upload a file for detection. If the value of the response parameter FileExist is true, the file that you want to upload for detection already exists in the cloud. In this case, you can directly push the file for detection. If the value of the response parameter FileExist is false, you must use the form upload method to upload the file to the specified Object Storage Service (OSS) bucket based on the response parameters of this operation.
        The form upload method is provided by OSS. For more information, see [Form upload](~~84788~~).
        The HashKey parameter is included in all API operations that are related to the file detection feature. The parameter specifies the unique identifier of a file. Only MD5 hash values are supported. Before you call this operation, calculate the MD5 hash value of the file.
        

        @param request: CreateFileDetectUploadUrlRequest

        @return: CreateFileDetectUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_detect_upload_url_with_options(request, runtime)

    def create_honeypot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_image_id):
            query['HoneypotImageId'] = request.honeypot_image_id
        if not UtilClient.is_unset(request.honeypot_image_name):
            query['HoneypotImageName'] = request.honeypot_image_name
        if not UtilClient.is_unset(request.honeypot_name):
            query['HoneypotName'] = request.honeypot_name
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHoneypot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateHoneypotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_honeypot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_honeypot_with_options(request, runtime)

    def create_honeypot_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_honeypot_access_internet):
            query['AllowHoneypotAccessInternet'] = request.allow_honeypot_access_internet
        if not UtilClient.is_unset(request.available_probe_num):
            query['AvailableProbeNum'] = request.available_probe_num
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.security_group_probe_ip_list):
            query['SecurityGroupProbeIpList'] = request.security_group_probe_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHoneypotNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateHoneypotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_honeypot_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_honeypot_node_with_options(request, runtime)

    def create_honeypot_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_image_name):
            query['HoneypotImageName'] = request.honeypot_image_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.preset_name):
            query['PresetName'] = request.preset_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHoneypotPreset',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateHoneypotPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_honeypot_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_honeypot_preset_with_options(request, runtime)

    def create_honeypot_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arp):
            query['Arp'] = request.arp
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.control_node_id):
            query['ControlNodeId'] = request.control_node_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.honeypot_bind_list):
            query['HoneypotBindList'] = request.honeypot_bind_list
        if not UtilClient.is_unset(request.ping):
            query['Ping'] = request.ping
        if not UtilClient.is_unset(request.probe_type):
            query['ProbeType'] = request.probe_type
        if not UtilClient.is_unset(request.probe_version):
            query['ProbeVersion'] = request.probe_version
        if not UtilClient.is_unset(request.proxy_ip):
            query['ProxyIp'] = request.proxy_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHoneypotProbe',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateHoneypotProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_honeypot_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_honeypot_probe_with_options(request, runtime)

    def create_interception_rule_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.CreateInterceptionRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dst_target_list):
            request.dst_target_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dst_target_list, 'DstTargetList', 'json')
        if not UtilClient.is_unset(tmp_req.src_target):
            request.src_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_target, 'SrcTarget', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.dst_target_list_shrink):
            query['DstTargetList'] = request.dst_target_list_shrink
        if not UtilClient.is_unset(request.intercept_type):
            query['InterceptType'] = request.intercept_type
        if not UtilClient.is_unset(request.order_index):
            query['OrderIndex'] = request.order_index
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.src_target_shrink):
            query['SrcTarget'] = request.src_target_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInterceptionRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateInterceptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_interception_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_interception_rule_with_options(request, runtime)

    def create_interception_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.image_list):
            query['ImageList'] = request.image_list
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInterceptionTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateInterceptionTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_interception_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_interception_target_with_options(request, runtime)

    def create_jenkins_image_registry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.extra_param):
            body['ExtraParam'] = request.extra_param
        if not UtilClient.is_unset(request.net_type):
            body['NetType'] = request.net_type
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.persistence_day):
            body['PersistenceDay'] = request.persistence_day
        if not UtilClient.is_unset(request.protocol_type):
            body['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registry_host_ip):
            body['RegistryHostIp'] = request.registry_host_ip
        if not UtilClient.is_unset(request.registry_name):
            body['RegistryName'] = request.registry_name
        if not UtilClient.is_unset(request.registry_type):
            body['RegistryType'] = request.registry_type
        if not UtilClient.is_unset(request.registry_version):
            body['RegistryVersion'] = request.registry_version
        if not UtilClient.is_unset(request.trans_per_hour):
            body['TransPerHour'] = request.trans_per_hour
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.white_list):
            body['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJenkinsImageRegistry',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateJenkinsImageRegistryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_jenkins_image_registry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_jenkins_image_registry_with_options(request, runtime)

    def create_or_update_asset_group_with_options(self, request, runtime):
        """
        A server can belong only to one server group. If you call the CreateOrUpdateAssetGroup operation and the server specified in request parameters belongs to Server Group A, the server is removed from Server Group A and then added to the newly created or specified server group after the call is complete.
        

        @param request: CreateOrUpdateAssetGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateOrUpdateAssetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateAssetGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateOrUpdateAssetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_asset_group(self, request):
        """
        A server can belong only to one server group. If you call the CreateOrUpdateAssetGroup operation and the server specified in request parameters belongs to Server Group A, the server is removed from Server Group A and then added to the newly created or specified server group after the call is complete.
        

        @param request: CreateOrUpdateAssetGroupRequest

        @return: CreateOrUpdateAssetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_asset_group_with_options(request, runtime)

    def create_or_update_ding_talk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_list):
            query['ConfigList'] = request.config_list
        if not UtilClient.is_unset(request.ding_talk_lang):
            query['DingTalkLang'] = request.ding_talk_lang
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.interval_time):
            query['IntervalTime'] = request.interval_time
        if not UtilClient.is_unset(request.rule_action_name):
            query['RuleActionName'] = request.rule_action_name
        if not UtilClient.is_unset(request.send_url):
            query['SendUrl'] = request.send_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateDingTalk',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateOrUpdateDingTalkResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_ding_talk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_ding_talk_with_options(request, runtime)

    def create_restore_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.includes):
            query['Includes'] = request.includes
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_version):
            query['SnapshotVersion'] = request.snapshot_version
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRestoreJob',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_restore_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_restore_job_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        """
        For more information about service-linked roles, see [Service-linked roles](~~160674~~).
        

        @param request: CreateServiceLinkedRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_linked_role(self, request):
        """
        For more information about service-linked roles, see [Service-linked roles](~~160674~~).
        

        @param request: CreateServiceLinkedRoleRequest

        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def create_service_trail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceTrail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateServiceTrailResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_trail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_trail_with_options(request, runtime)

    def create_similar_security_events_query_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.similar_event_scenario_code):
            query['SimilarEventScenarioCode'] = request.similar_event_scenario_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarSecurityEventsQueryTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_similar_security_events_query_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_similar_security_events_query_task_with_options(request, runtime)

    def create_susp_event_note_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSuspEventNote',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateSuspEventNoteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_susp_event_note(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_susp_event_note_with_options(request, runtime)

    def create_uni_backup_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.CreateUniBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.full_plan):
            request.full_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.full_plan, 'FullPlan', 'json')
        if not UtilClient.is_unset(tmp_req.inc_plan):
            request.inc_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inc_plan, 'IncPlan', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.database_add_by_user):
            query['DatabaseAddByUser'] = request.database_add_by_user
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.full_plan_shrink):
            query['FullPlan'] = request.full_plan_shrink
        if not UtilClient.is_unset(request.inc_plan_shrink):
            query['IncPlan'] = request.inc_plan_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.speed_limiter):
            query['SpeedLimiter'] = request.speed_limiter
        if not UtilClient.is_unset(request.uni_region_id):
            query['UniRegionId'] = request.uni_region_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUniBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateUniBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_uni_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_uni_backup_policy_with_options(request, runtime)

    def create_uni_restore_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.reset_scn):
            query['ResetScn'] = request.reset_scn
        if not UtilClient.is_unset(request.reset_time):
            query['ResetTime'] = request.reset_time
        if not UtilClient.is_unset(request.restore_info):
            query['RestoreInfo'] = request.restore_info
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUniRestorePlan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateUniRestorePlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_uni_restore_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_uni_restore_plan_with_options(request, runtime)

    def create_vul_auto_repair_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_auto_repair_config_list):
            query['VulAutoRepairConfigList'] = request.vul_auto_repair_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVulAutoRepairConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateVulAutoRepairConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vul_auto_repair_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vul_auto_repair_config_with_options(request, runtime)

    def delete_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_anti_brute_force_rule_with_options(request, runtime)

    def delete_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_with_options(request, runtime)

    def delete_backup_policy_machine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicyMachine',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backup_policy_machine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_machine_with_options(request, runtime)

    def delete_binary_security_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBinarySecurityPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBinarySecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_binary_security_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_binary_security_policy_with_options(request, runtime)

    def delete_client_user_define_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id_list):
            query['IdList'] = request.id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientUserDefineRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteClientUserDefineRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_client_user_define_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_client_user_define_rule_with_options(request, runtime)

    def delete_custom_block_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomBlockRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteCustomBlockRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_block_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_block_record_with_options(request, runtime)

    def delete_cycle_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCycleTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteCycleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cycle_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cycle_task_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        """
        The *Default** server group that is provided by Security Center cannot be deleted. After you delete a group, the assets in this group are moved to the **Default** group.
        

        @param request: DeleteGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, request):
        """
        The *Default** server group that is provided by Security Center cannot be deleted. After you delete a group, the assets in this group are moved to the **Default** group.
        

        @param request: DeleteGroupRequest

        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_honeypot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_id):
            query['HoneypotId'] = request.honeypot_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHoneypot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteHoneypotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_honeypot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_honeypot_with_options(request, runtime)

    def delete_honeypot_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHoneypotNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteHoneypotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_honeypot_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_honeypot_node_with_options(request, runtime)

    def delete_honeypot_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_preset_id):
            query['HoneypotPresetId'] = request.honeypot_preset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHoneypotPreset',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteHoneypotPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_honeypot_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_honeypot_preset_with_options(request, runtime)

    def delete_honeypot_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.probe_id):
            query['ProbeId'] = request.probe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHoneypotProbe',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteHoneypotProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_honeypot_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_honeypot_probe_with_options(request, runtime)

    def delete_install_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.captcha_code):
            query['CaptchaCode'] = request.captcha_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstallCode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteInstallCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_install_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_install_code_with_options(request, runtime)

    def delete_interception_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInterceptionRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteInterceptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_interception_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_interception_rule_with_options(request, runtime)

    def delete_interception_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInterceptionTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteInterceptionTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_interception_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_interception_target_with_options(request, runtime)

    def delete_login_base_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoginBaseConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteLoginBaseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_login_base_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_login_base_config_with_options(request, runtime)

    def delete_private_registry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.registry_id):
            query['RegistryId'] = request.registry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrivateRegistry',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeletePrivateRegistryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_private_registry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_private_registry_with_options(request, runtime)

    def delete_security_event_mark_miss_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityEventMarkMissList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteSecurityEventMarkMissListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_security_event_mark_miss_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_event_mark_miss_list_with_options(request, runtime)

    def delete_service_trail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceTrail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteServiceTrailResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_trail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_trail_with_options(request, runtime)

    def delete_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_strategy_with_options(request, runtime)

    def delete_susp_event_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note_id):
            query['NoteId'] = request.note_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSuspEventNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteSuspEventNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_susp_event_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_susp_event_node_with_options(request, runtime)

    def delete_tag_with_uuid_with_options(self, request, runtime):
        """
        Security Center provides asset importance tags and custom tags. You can call this operation to remove only the custom tag that is added to an asset.
        

        @param request: DeleteTagWithUuidRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTagWithUuidResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteTagWithUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag_with_uuid(self, request):
        """
        Security Center provides asset importance tags and custom tags. You can call this operation to remove only the custom tag that is added to an asset.
        

        @param request: DeleteTagWithUuidRequest

        @return: DeleteTagWithUuidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_uuid_with_options(request, runtime)

    def delete_uni_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUniBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteUniBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_uni_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_uni_backup_policy_with_options(request, runtime)

    def delete_vpc_honey_pot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteVpcHoneyPotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vpc_honey_pot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_honey_pot_with_options(request, runtime)

    def delete_vul_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteVulWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vul_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vul_whitelist_with_options(request, runtime)

    def describe_access_key_leak_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessKeyLeakDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAccessKeyLeakDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_key_leak_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_key_leak_detail_with_options(request, runtime)

    def describe_accesskey_leak_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccesskeyLeakList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAccesskeyLeakListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accesskey_leak_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accesskey_leak_list_with_options(request, runtime)

    def describe_affected_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['Current'] = request.current
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAffectedAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAffectedAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_affected_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_affected_assets_with_options(request, runtime)

    def describe_affected_malicious_file_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.malicious_md_5):
            query['MaliciousMd5'] = request.malicious_md_5
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod):
            query['Pod'] = request.pod
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAffectedMaliciousFileImages',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_affected_malicious_file_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_affected_malicious_file_images_with_options(request, runtime)

    def describe_agent_install_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAgentInstallStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAgentInstallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_agent_install_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_agent_install_status_with_options(request, runtime)

    def describe_alarm_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alarm_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_detail_with_options(request, runtime)

    def describe_alarm_event_stack_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventStackInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventStackInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alarm_event_stack_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_stack_info_with_options(request, runtime)

    def describe_all_entity_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAllEntity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_entity(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_entity_with_options(runtime)

    def describe_all_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllGroups',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_groups_with_options(request, runtime)

    def describe_all_image_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllImageBaseline',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllImageBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_image_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_image_baseline_with_options(request, runtime)

    def describe_anti_brute_force_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAntiBruteForceRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAntiBruteForceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_anti_brute_force_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_anti_brute_force_rules_with_options(request, runtime)

    def describe_app_vul_scan_cycle_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAppVulScanCycle',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAppVulScanCycleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_vul_scan_cycle(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_vul_scan_cycle_with_options(runtime)

    def describe_asset_detail_by_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetDetailByUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_asset_detail_by_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_detail_by_uuid_with_options(request, runtime)

    def describe_asset_detail_by_uuids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetDetailByUuids',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_asset_detail_by_uuids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_detail_by_uuids_with_options(request, runtime)

    def describe_asset_summary_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAssetSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_asset_summary(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_summary_with_options(runtime)

    def describe_assets_security_event_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetsSecurityEventSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetsSecurityEventSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_assets_security_event_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_assets_security_event_summary_with_options(request, runtime)

    def describe_attack_analysis_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_64):
            query['Base64'] = request.base_64
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackAnalysisData',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAttackAnalysisDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_attack_analysis_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_analysis_data_with_options(request, runtime)

    def describe_auto_del_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAutoDelConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAutoDelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_del_config(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_del_config_with_options(runtime)

    def describe_back_up_export_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackUpExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackUpExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_back_up_export_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_back_up_export_info_with_options(request, runtime)

    def describe_backup_clients_with_options(self, request, runtime):
        """
        You can call the DescribeBackupClients operation to query the servers on which the anti-ransomware agent is installed in a specified region.
        

        @param request: DescribeBackupClientsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.support_region_id):
            query['SupportRegionId'] = request.support_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupClients',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_clients(self, request):
        """
        You can call the DescribeBackupClients operation to query the servers on which the anti-ransomware agent is installed in a specified region.
        

        @param request: DescribeBackupClientsRequest

        @return: DescribeBackupClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_clients_with_options(request, runtime)

    def describe_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_files_with_options(request, runtime)

    def describe_backup_machine_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupMachineStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupMachineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_machine_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_machine_status_with_options(request, runtime)

    def describe_backup_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicies',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policies_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backup_restore_count_with_options(self, runtime):
        """
        If you have created restoration tasks, you can call this operation to query the number of restoration tasks that are in the *restored** or **being restored** state.
        

        @param request: DescribeBackupRestoreCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBackupRestoreCountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBackupRestoreCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupRestoreCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backup_restore_count(self):
        """
        If you have created restoration tasks, you can call this operation to query the number of restoration tasks that are in the *restored** or **being restored** state.
        

        @return: DescribeBackupRestoreCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_restore_count_with_options(runtime)

    def describe_brute_force_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBruteForceRecords',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBruteForceRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_brute_force_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_brute_force_records_with_options(request, runtime)

    def describe_brute_force_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBruteForceSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBruteForceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_brute_force_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_brute_force_summary_with_options(request, runtime)

    def describe_check_ecs_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckEcsWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckEcsWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_ecs_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_ecs_warnings_with_options(request, runtime)

    def describe_check_fix_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckFixDetails',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckFixDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_fix_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_fix_details_with_options(request, runtime)

    def describe_check_warning_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_warning_id):
            query['CheckWarningId'] = request.check_warning_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_warning_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_detail_with_options(request, runtime)

    def describe_check_warning_machines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_warning_machines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_machines_with_options(request, runtime)

    def describe_check_warning_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_name):
            query['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarningSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_warning_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_summary_with_options(request, runtime)

    def describe_check_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_check_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warnings_with_options(request, runtime)

    def describe_client_conf_setup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.strategy_tag):
            query['StrategyTag'] = request.strategy_tag
        if not UtilClient.is_unset(request.strategy_tag_value):
            query['StrategyTagValue'] = request.strategy_tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientConfSetup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeClientConfSetupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_conf_setup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_conf_setup_with_options(request, runtime)

    def describe_client_conf_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientConfStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeClientConfStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_conf_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_conf_strategy_with_options(request, runtime)

    def describe_cloud_center_instances_with_options(self, request, runtime):
        """
        You can search for assets by using search conditions, such as the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can also configure a logical relationship between multiple search conditions to search for the assets that meet the search conditions.
        

        @param request: DescribeCloudCenterInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCloudCenterInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.importance):
            query['Importance'] = request.importance
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.no_group_trace):
            query['NoGroupTrace'] = request.no_group_trace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.use_next_token):
            query['UseNextToken'] = request.use_next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudCenterInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudCenterInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_center_instances(self, request):
        """
        You can search for assets by using search conditions, such as the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can also configure a logical relationship between multiple search conditions to search for the assets that meet the search conditions.
        

        @param request: DescribeCloudCenterInstancesRequest

        @return: DescribeCloudCenterInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_center_instances_with_options(request, runtime)

    def describe_cloud_product_field_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudProductFieldStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudProductFieldStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_product_field_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_product_field_statistics_with_options(runtime)

    def describe_cluster_basic_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterBasicInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeClusterBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_basic_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_basic_info_with_options(request, runtime)

    def describe_cluster_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterInfoList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeClusterInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_info_list_with_options(request, runtime)

    def describe_cluster_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetwork',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeClusterNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_network_with_options(request, runtime)

    def describe_cluster_vul_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterVulStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeClusterVulStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_vul_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_vul_statistics_with_options(request, runtime)

    def describe_common_overall_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommonOverallConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCommonOverallConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_common_overall_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_common_overall_config_with_options(request, runtime)

    def describe_common_overall_config_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type_list):
            query['TypeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommonOverallConfigList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCommonOverallConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_common_overall_config_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_common_overall_config_list_with_options(request, runtime)

    def describe_common_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommonTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCommonTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_common_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_common_target_config_with_options(request, runtime)

    def describe_common_target_result_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommonTargetResultList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCommonTargetResultListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_common_target_result_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_common_target_result_list_with_options(request, runtime)

    def describe_concern_necessity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConcernNecessity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeConcernNecessityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_concern_necessity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_concern_necessity_with_options(request, runtime)

    def describe_container_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_criteria_with_options(request, runtime)

    def describe_container_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_instances_with_options(request, runtime)

    def describe_container_statistics_with_options(self, request, runtime):
        """
        Only users who created a Container Registry Enterprise Edition instance can call this operation.
        

        @param request: DescribeContainerStatisticsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeContainerStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_statistics(self, request):
        """
        Only users who created a Container Registry Enterprise Edition instance can call this operation.
        

        @param request: DescribeContainerStatisticsRequest

        @return: DescribeContainerStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_statistics_with_options(request, runtime)

    def describe_container_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_name):
            query['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerTags',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_tags_with_options(request, runtime)

    def describe_count_not_scanned_image_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCountNotScannedImage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCountNotScannedImageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_count_not_scanned_image(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_count_not_scanned_image_with_options(runtime)

    def describe_count_scanned_image_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCountScannedImage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCountScannedImageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_count_scanned_image(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_count_scanned_image_with_options(runtime)

    def describe_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.support_auto_tag):
            query['SupportAutoTag'] = request.support_auto_tag
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_criteria_with_options(request, runtime)

    def describe_custom_block_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomBlockRecords',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCustomBlockRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_block_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_block_records_with_options(request, runtime)

    def describe_cycle_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCycleTaskList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCycleTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cycle_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cycle_task_list_with_options(request, runtime)

    def describe_ding_talk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_action_name):
            query['RuleActionName'] = request.rule_action_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDingTalk',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDingTalkResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ding_talk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ding_talk_with_options(request, runtime)

    def describe_domain_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_count_with_options(request, runtime)

    def describe_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    def describe_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.fuzzy_domain):
            query['FuzzyDomain'] = request.fuzzy_domain
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_list_with_options(request, runtime)

    def describe_emg_user_agreement_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEmgUserAgreement',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEmgUserAgreementResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_emg_user_agreement(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_emg_user_agreement_with_options(runtime)

    def describe_emg_vul_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_status):
            query['RiskStatus'] = request.risk_status
        if not UtilClient.is_unset(request.scan_type):
            query['ScanType'] = request.scan_type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEmgVulItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEmgVulItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_emg_vul_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_emg_vul_item_with_options(request, runtime)

    def describe_event_level_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.container_ids):
            query['ContainerIds'] = request.container_ids
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventLevelCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEventLevelCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_level_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_level_count_with_options(request, runtime)

    def describe_event_on_stage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventOnStage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEventOnStageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_on_stage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_on_stage_with_options(request, runtime)

    def describe_exclude_system_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExcludeSystemPath',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExcludeSystemPathResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exclude_system_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exclude_system_path_with_options(request, runtime)

    def describe_export_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_export_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_export_info_with_options(request, runtime)

    def describe_exposed_check_warning_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedCheckWarning',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedCheckWarningResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exposed_check_warning(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_check_warning_with_options(request, runtime)

    def describe_exposed_instance_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exposed_instance_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_criteria_with_options(request, runtime)

    def describe_exposed_instance_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exposed_instance_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_detail_with_options(request, runtime)

    def describe_exposed_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.exposure_component):
            query['ExposureComponent'] = request.exposure_component
        if not UtilClient.is_unset(request.exposure_ip):
            query['ExposureIp'] = request.exposure_ip
        if not UtilClient.is_unset(request.exposure_port):
            query['ExposurePort'] = request.exposure_port
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vul_status):
            query['VulStatus'] = request.vul_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedInstanceList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exposed_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_list_with_options(request, runtime)

    def describe_exposed_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeExposedStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exposed_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_with_options(runtime)

    def describe_exposed_statistics_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.statistics_type):
            query['StatisticsType'] = request.statistics_type
        if not UtilClient.is_unset(request.statistics_type_gateway_type):
            query['StatisticsTypeGatewayType'] = request.statistics_type_gateway_type
        if not UtilClient.is_unset(request.statistics_type_instance_value):
            query['StatisticsTypeInstanceValue'] = request.statistics_type_instance_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExposedStatisticsDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exposed_statistics_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_detail_with_options(request, runtime)

    def describe_field_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFieldStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeFieldStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_field_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_field_statistics_with_options(request, runtime)

    def describe_front_vul_patch_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFrontVulPatchList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeFrontVulPatchListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_front_vul_patch_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    def describe_group_struct_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupStruct',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupStructResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_struct(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_group_struct_with_options(request, runtime)

    def describe_grouped_container_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedContainerInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedContainerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grouped_container_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_container_instances_with_options(request, runtime)

    def describe_grouped_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_field):
            query['GroupField'] = request.group_field
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.no_page):
            query['NoPage'] = request.no_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sale_version_check_code):
            query['SaleVersionCheckCode'] = request.sale_version_check_code
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        if not UtilClient.is_unset(request.vendors):
            query['Vendors'] = request.vendors
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grouped_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_instances_with_options(request, runtime)

    def describe_grouped_malicious_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.fuzzy_malicious_name):
            query['FuzzyMaliciousName'] = request.fuzzy_malicious_name
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.malicious_md_5):
            query['MaliciousMd5'] = request.malicious_md_5
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedMaliciousFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedMaliciousFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grouped_malicious_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_malicious_files_with_options(request, runtime)

    def describe_grouped_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedTags',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grouped_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_tags_with_options(request, runtime)

    def describe_grouped_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedVulResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grouped_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    def describe_hc_export_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHcExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHcExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hc_export_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hc_export_info_with_options(request, runtime)

    def describe_honey_pot_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHoneyPotAuth',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_honey_pot_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_auth_with_options(request, runtime)

    def describe_honey_pot_susp_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.statistics_days):
            query['StatisticsDays'] = request.statistics_days
        if not UtilClient.is_unset(request.statistics_key_type):
            query['StatisticsKeyType'] = request.statistics_key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHoneyPotSuspStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_honey_pot_susp_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_susp_statistics_with_options(request, runtime)

    def describe_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_instance_id):
            query['ImageInstanceId'] = request.image_instance_id
        if not UtilClient.is_unset(request.image_region_id):
            query['ImageRegionId'] = request.image_region_id
        if not UtilClient.is_unset(request.image_repo_id):
            query['ImageRepoId'] = request.image_repo_id
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_with_options(request, runtime)

    def describe_image_baseline_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_uuid):
            query['ImageUuid'] = request.image_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_baseline_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_baseline_check_result_with_options(request, runtime)

    def describe_image_baseline_check_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineCheckSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_baseline_check_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_baseline_check_summary_with_options(request, runtime)

    def describe_image_baseline_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_item_key):
            query['BaselineItemKey'] = request.baseline_item_key
        if not UtilClient.is_unset(request.image_uuid):
            query['ImageUuid'] = request.image_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_baseline_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_baseline_detail_with_options(request, runtime)

    def describe_image_baseline_item_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_class_key):
            query['BaselineClassKey'] = request.baseline_class_key
        if not UtilClient.is_unset(request.baseline_name_key):
            query['BaselineNameKey'] = request.baseline_name_key
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_uuid):
            query['ImageUuid'] = request.image_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineItemList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineItemListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_baseline_item_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_baseline_item_list_with_options(request, runtime)

    def describe_image_baseline_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageBaselineStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageBaselineStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_baseline_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_baseline_strategy_with_options(request, runtime)

    def describe_image_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_criteria_with_options(request, runtime)

    def describe_image_fix_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFixTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageFixTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_fix_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_fix_task_with_options(request, runtime)

    def describe_image_grouped_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.cve_id):
            query['CveId'] = request.cve_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.image_layer):
            query['ImageLayer'] = request.image_layer
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.is_latest):
            query['IsLatest'] = request.is_latest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.patch_id):
            query['PatchId'] = request.patch_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageGroupedVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageGroupedVulListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_grouped_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_grouped_vul_list_with_options(request, runtime)

    def describe_image_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageInfoList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_info_list_with_options(request, runtime)

    def describe_image_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scanned):
            query['Scanned'] = request.scanned
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_instances_with_options(request, runtime)

    def describe_image_latest_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageLatestScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageLatestScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_latest_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_latest_scan_task_with_options(request, runtime)

    def describe_image_list_by_sensitive_file_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.DescribeImageListBySensitiveFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scan_range):
            request.scan_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scan_range, 'ScanRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.scan_range_shrink):
            query['ScanRange'] = request.scan_range_shrink
        if not UtilClient.is_unset(request.sensitive_file_key):
            query['SensitiveFileKey'] = request.sensitive_file_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageListBySensitiveFile',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageListBySensitiveFileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_list_by_sensitive_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_list_by_sensitive_file_with_options(request, runtime)

    def describe_image_list_with_baseline_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_name_key):
            query['BaselineNameKey'] = request.baseline_name_key
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_digest):
            query['ImageDigest'] = request.image_digest
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod):
            query['Pod'] = request.pod
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageListWithBaselineName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageListWithBaselineNameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_list_with_baseline_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_list_with_baseline_name_with_options(request, runtime)

    def describe_image_repo_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageRepoCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageRepoCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_repo_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_repo_criteria_with_options(request, runtime)

    def describe_image_repo_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageRepoDetailList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageRepoDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_repo_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_repo_detail_list_with_options(request, runtime)

    def describe_image_repo_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_name):
            query['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageRepoList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageRepoListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_repo_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_repo_list_with_options(request, runtime)

    def describe_image_scan_auth_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageScanAuthCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageScanAuthCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_scan_auth_count(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_scan_auth_count_with_options(runtime)

    def describe_image_scan_authorization_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageScanAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageScanAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_scan_authorization(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_scan_authorization_with_options(runtime)

    def describe_image_sensitive_file_by_key_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.DescribeImageSensitiveFileByKeyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scan_range):
            request.scan_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scan_range, 'ScanRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_uuid):
            query['ImageUuid'] = request.image_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scan_range_shrink):
            query['ScanRange'] = request.scan_range_shrink
        if not UtilClient.is_unset(request.sensitive_file_key):
            query['SensitiveFileKey'] = request.sensitive_file_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageSensitiveFileByKey',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageSensitiveFileByKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_sensitive_file_by_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_sensitive_file_by_key_with_options(request, runtime)

    def describe_image_sensitive_file_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.DescribeImageSensitiveFileListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scan_range):
            request.scan_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scan_range, 'ScanRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_uuid):
            query['ImageUuid'] = request.image_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.scan_range_shrink):
            query['ScanRange'] = request.scan_range_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageSensitiveFileList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageSensitiveFileListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_sensitive_file_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_sensitive_file_list_with_options(request, runtime)

    def describe_image_statistics_with_options(self, runtime):
        """
        Security Center can scan for security risks and collect statistics only for *Container Registry Enterprise Edition instances**.
        >  Security Center cannot scan for security risks or collect statistics for **default** Container Registry instances.
        

        @param request: DescribeImageStatisticsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeImageStatisticsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeImageStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_statistics(self):
        """
        Security Center can scan for security risks and collect statistics only for *Container Registry Enterprise Edition instances**.
        >  Security Center cannot scan for security risks or collect statistics for **default** Container Registry instances.
        

        @return: DescribeImageStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_statistics_with_options(runtime)

    def describe_image_vul_list_with_options(self, request, runtime):
        """
        To query the information about the recently detected image vulnerabilities, call the [PublicCreateImageScanTask](~~PublicCreateImageScanTask~~) operation. Wait 1 to 5 minutes until the call is successful and call the DescribeImageVulList operation.
        

        @param request: DescribeImageVulListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeImageVulListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod):
            query['Pod'] = request.pod
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.repo_instance_id):
            query['RepoInstanceId'] = request.repo_instance_id
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        if not UtilClient.is_unset(request.repo_namespace):
            query['RepoNamespace'] = request.repo_namespace
        if not UtilClient.is_unset(request.repo_region_id):
            query['RepoRegionId'] = request.repo_region_id
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageVulListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_vul_list(self, request):
        """
        To query the information about the recently detected image vulnerabilities, call the [PublicCreateImageScanTask](~~PublicCreateImageScanTask~~) operation. Wait 1 to 5 minutes until the call is successful and call the DescribeImageVulList operation.
        

        @param request: DescribeImageVulListRequest

        @return: DescribeImageVulListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_vul_list_with_options(request, runtime)

    def describe_image_vul_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageVulWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageVulWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_vul_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_vul_white_list_with_options(request, runtime)

    def describe_install_captcha_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deadline):
            query['Deadline'] = request.deadline
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstallCaptcha',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCaptchaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_install_captcha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_install_captcha_with_options(request, runtime)

    def describe_install_code_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstallCode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_install_code(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_install_code_with_options(runtime)

    def describe_install_codes_with_options(self, runtime):
        """
        You can call the DescribeInstallCodes operation to query the commands that are used to manually install the Security Center agent. The returned results contain the installation verification code and the server information. If you want to manually install the Security Center agent on your server, you can call this operation to query installation commands.
        # Limits
        You can call this API operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeInstallCodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstallCodesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstallCodes',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCodesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_install_codes(self):
        """
        You can call the DescribeInstallCodes operation to query the commands that are used to manually install the Security Center agent. The returned results contain the installation verification code and the server information. If you want to manually install the Security Center agent on your server, you can call this operation to query installation commands.
        # Limits
        You can call this API operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @return: DescribeInstallCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_install_codes_with_options(runtime)

    def describe_instance_anti_brute_force_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAntiBruteForceRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_anti_brute_force_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_anti_brute_force_rules_with_options(request, runtime)

    def describe_instance_reboot_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRebootStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceRebootStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_reboot_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_reboot_status_with_options(request, runtime)

    def describe_instance_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    def describe_ip_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpTags',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeIpTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_tags_with_options(request, runtime)

    def describe_latest_scan_task_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeLatestScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLatestScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_latest_scan_task(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_scan_task_with_options(runtime)

    def describe_log_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMeta',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLogMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_meta_with_options(request, runtime)

    def describe_log_shipper_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogShipperStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLogShipperStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_shipper_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_shipper_status_with_options(request, runtime)

    def describe_login_base_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoginBaseConfigs',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLoginBaseConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_login_base_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_login_base_configs_with_options(request, runtime)

    def describe_login_switch_configs_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeLoginSwitchConfigs',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLoginSwitchConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_login_switch_configs(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_login_switch_configs_with_options(runtime)

    def describe_logstore_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogstoreStorage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLogstoreStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_logstore_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_logstore_storage_with_options(request, runtime)

    def describe_machine_can_reboot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMachineCanReboot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeMachineCanRebootResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_machine_can_reboot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_machine_can_reboot_with_options(request, runtime)

    def describe_module_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeModuleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeModuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_module_config(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_module_config_with_options(runtime)

    def describe_monitor_accounts_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitorAccounts',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeMonitorAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_accounts(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_accounts_with_options(runtime)

    def describe_notice_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNoticeConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeNoticeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_notice_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notice_config_with_options(request, runtime)

    def describe_nsas_susp_event_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNsasSuspEventType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeNsasSuspEventTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nsas_susp_event_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nsas_susp_event_type_with_options(request, runtime)

    def describe_offline_machines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id_str):
            query['RegionIdStr'] = request.region_id_str
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOfflineMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeOfflineMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_offline_machines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_offline_machines_with_options(request, runtime)

    def describe_once_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time_query):
            query['EndTimeQuery'] = request.end_time_query
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.root_task_id):
            query['RootTaskId'] = request.root_task_id
        if not UtilClient.is_unset(request.start_time_query):
            query['StartTimeQuery'] = request.start_time_query
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnceTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeOnceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_once_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_once_task_with_options(request, runtime)

    def describe_once_task_leaf_record_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.relate_info):
            query['RelateInfo'] = request.relate_info
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnceTaskLeafRecordPage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeOnceTaskLeafRecordPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_once_task_leaf_record_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_once_task_leaf_record_page_with_options(request, runtime)

    def describe_property_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_count_with_options(request, runtime)

    def describe_property_cron_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCronDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCronDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_cron_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_cron_detail_with_options(request, runtime)

    def describe_property_cron_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyCronItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCronItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_cron_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_cron_item_with_options(request, runtime)

    def describe_property_port_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_ip):
            query['BindIp'] = request.bind_ip
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.proc_name):
            query['ProcName'] = request.proc_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyPortDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_port_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_port_detail_with_options(request, runtime)

    def describe_property_port_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyPortItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_port_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_port_item_with_options(request, runtime)

    def describe_property_proc_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proc_time_end):
            query['ProcTimeEnd'] = request.proc_time_end
        if not UtilClient.is_unset(request.proc_time_start):
            query['ProcTimeStart'] = request.proc_time_start
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyProcDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_proc_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_proc_detail_with_options(request, runtime)

    def describe_property_proc_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyProcItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_proc_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_proc_item_with_options(request, runtime)

    def describe_property_sca_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.process_started_end):
            query['ProcessStartedEnd'] = request.process_started_end
        if not UtilClient.is_unset(request.process_started_start):
            query['ProcessStartedStart'] = request.process_started_start
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.sca_name):
            query['ScaName'] = request.sca_name
        if not UtilClient.is_unset(request.sca_name_pattern):
            query['ScaNamePattern'] = request.sca_name_pattern
        if not UtilClient.is_unset(request.sca_version):
            query['ScaVersion'] = request.sca_version
        if not UtilClient.is_unset(request.search_info):
            query['SearchInfo'] = request.search_info
        if not UtilClient.is_unset(request.search_info_sub):
            query['SearchInfoSub'] = request.search_info_sub
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.search_item_sub):
            query['SearchItemSub'] = request.search_item_sub
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyScaDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyScaDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_sca_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_sca_detail_with_options(request, runtime)

    def describe_property_sca_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_info):
            query['SearchInfo'] = request.search_info
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyScaItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyScaItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_sca_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_sca_item_with_options(request, runtime)

    def describe_property_schedule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_schedule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_schedule_config_with_options(request, runtime)

    def describe_property_software_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.install_time_end):
            query['InstallTimeEnd'] = request.install_time_end
        if not UtilClient.is_unset(request.install_time_start):
            query['InstallTimeStart'] = request.install_time_start
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.software_version):
            query['SoftwareVersion'] = request.software_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertySoftwareDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_software_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_software_detail_with_options(request, runtime)

    def describe_property_software_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertySoftwareItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_software_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_software_item_with_options(request, runtime)

    def describe_property_type_sca_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyTypeScaItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyTypeScaItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_type_sca_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_type_sca_item_with_options(request, runtime)

    def describe_property_usage_newest_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUsageNewest',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUsageNewestResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_usage_newest(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_usage_newest_with_options(request, runtime)

    def describe_property_user_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.is_root):
            query['IsRoot'] = request.is_root
        if not UtilClient.is_unset(request.last_login_time_end):
            query['LastLoginTimeEnd'] = request.last_login_time_end
        if not UtilClient.is_unset(request.last_login_time_start):
            query['LastLoginTimeStart'] = request.last_login_time_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUserDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_user_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_user_detail_with_options(request, runtime)

    def describe_property_user_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePropertyUserItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_property_user_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_user_item_with_options(request, runtime)

    def describe_quara_file_download_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.quara_file_id):
            query['QuaraFileId'] = request.quara_file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQuaraFileDownloadInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeQuaraFileDownloadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quara_file_download_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_quara_file_download_info_with_options(request, runtime)

    def describe_restore_jobs_with_options(self, request, runtime):
        """
        If the data on your servers is encrypted by ransomware, you can create a restoration task to restore the data on your servers by using backup data in Security Center.
        >  After you enable an anti-ransomware policy, the data on your servers is backed up based on the policy. For more information about anti-ransomware policies, see [Manage protection policies](~~164781~~).
        

        @param request: DescribeRestoreJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRestoreJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreJobs',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRestoreJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_restore_jobs(self, request):
        """
        If the data on your servers is encrypted by ransomware, you can create a restoration task to restore the data on your servers by using backup data in Security Center.
        >  After you enable an anti-ransomware policy, the data on your servers is backed up based on the policy. For more information about anti-ransomware policies, see [Manage protection policies](~~164781~~).
        

        @param request: DescribeRestoreJobsRequest

        @return: DescribeRestoreJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_jobs_with_options(request, runtime)

    def describe_restore_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestorePlans',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRestorePlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_restore_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_plans_with_options(request, runtime)

    def describe_risk_check_item_result_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckInstanceResult operation.
        

        @param request: DescribeRiskCheckItemResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskCheckItemResultResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckItemResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckItemResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_check_item_result(self, request):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckInstanceResult operation.
        

        @param request: DescribeRiskCheckItemResultRequest

        @return: DescribeRiskCheckItemResultResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_item_result_with_options(request, runtime)

    def describe_risk_check_result_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckResult operation.
        

        @param request: DescribeRiskCheckResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskCheckResultResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_ids):
            query['ItemIds'] = request.item_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_flag):
            query['QueryFlag'] = request.query_flag
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_check_result(self, request):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckResult operation.
        

        @param request: DescribeRiskCheckResultRequest

        @return: DescribeRiskCheckResultResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_result_with_options(request, runtime)

    def describe_risk_check_summary_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the GetCheckSummary operation.
        

        @param request: DescribeRiskCheckSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskCheckSummaryResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_check_summary(self, request):
        """
        @deprecated
        This operation is phased out. You can use the GetCheckSummary operation.
        

        @param request: DescribeRiskCheckSummaryRequest

        @return: DescribeRiskCheckSummaryResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_summary_with_options(request, runtime)

    def describe_risk_item_type_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckStandard operation instead.
        

        @param request: DescribeRiskItemTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskItemTypeResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskItemType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskItemTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_item_type(self, request):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckStandard operation instead.
        

        @param request: DescribeRiskItemTypeRequest

        @return: DescribeRiskItemTypeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_item_type_with_options(request, runtime)

    def describe_risk_list_check_result_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckResult operation. When you call the ListCheckResult operation, set the Statuses parameter to NOT_PASS.
        

        @param request: DescribeRiskListCheckResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskListCheckResultResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskListCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskListCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_list_check_result(self, request):
        """
        @deprecated
        This operation is phased out. You can use the ListCheckResult operation. When you call the ListCheckResult operation, set the Statuses parameter to NOT_PASS.
        

        @param request: DescribeRiskListCheckResultRequest

        @return: DescribeRiskListCheckResultResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_list_check_result_with_options(request, runtime)

    def describe_risk_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_type_with_options(request, runtime)

    def describe_risks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.risk_name):
            query['RiskName'] = request.risk_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRisks',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRisksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risks_with_options(request, runtime)

    def describe_sas_pm_agent_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSasPmAgentList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSasPmAgentListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sas_pm_agent_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sas_pm_agent_list_with_options(request, runtime)

    def describe_scan_task_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskProgress',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeScanTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scan_task_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    def describe_scan_task_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeScanTaskStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scan_task_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_statistics_with_options(request, runtime)

    def describe_search_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSearchCondition',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSearchConditionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_search_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_search_condition_with_options(request, runtime)

    def describe_secure_suggestion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecureSuggestion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecureSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_secure_suggestion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_secure_suggestion_with_options(request, runtime)

    def describe_security_check_schedule_config_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the GetCheckConfig operation.
        

        @param request: DescribeSecurityCheckScheduleConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSecurityCheckScheduleConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityCheckScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_check_schedule_config(self, request):
        """
        @deprecated
        This operation is phased out. You can use the GetCheckConfig operation.
        

        @param request: DescribeSecurityCheckScheduleConfigRequest

        @return: DescribeSecurityCheckScheduleConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_check_schedule_config_with_options(request, runtime)

    def describe_security_event_mark_miss_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventMarkMissList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventMarkMissListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_event_mark_miss_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_mark_miss_list_with_options(request, runtime)

    def describe_security_event_operation_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperationStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_event_operation_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    def describe_security_event_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperations',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_event_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    def describe_security_stat_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityStatInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_stat_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_stat_info_with_options(request, runtime)

    def describe_service_linked_role_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLinkedRoleStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeServiceLinkedRoleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_linked_role_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_linked_role_status_with_options(request, runtime)

    def describe_similar_event_scenarios_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimilarEventScenarios',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarEventScenariosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_similar_event_scenarios(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_similar_event_scenarios_with_options(request, runtime)

    def describe_similar_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimilarSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_similar_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_similar_security_events_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_ali_yun_ecs):
            query['IsAliYunEcs'] = request.is_ali_yun_ecs
        if not UtilClient.is_unset(request.machine_region):
            query['MachineRegion'] = request.machine_region
        if not UtilClient.is_unset(request.machine_remark):
            query['MachineRemark'] = request.machine_remark
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_type):
            query['CustomType'] = request.custom_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_ids):
            query['StrategyIds'] = request.strategy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_with_options(request, runtime)

    def describe_strategy_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_strategy_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_detail_with_options(request, runtime)

    def describe_strategy_exec_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyExecDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyExecDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_strategy_exec_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_exec_detail_with_options(request, runtime)

    def describe_strategy_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStrategyTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_strategy_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_target_with_options(request, runtime)

    def describe_summary_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_summary_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_summary_info_with_options(request, runtime)

    def describe_support_region_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportRegion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSupportRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_support_region(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_support_region_with_options(runtime)

    def describe_susp_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.suspicious_event_id):
            query['SuspiciousEventId'] = request.suspicious_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_detail_with_options(request, runtime)

    def describe_susp_event_export_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_event_export_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_export_info_with_options(request, runtime)

    def describe_susp_event_quara_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.grouping_id):
            query['GroupingId'] = request.grouping_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.quara_tag):
            query['QuaraTag'] = request.quara_tag
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventQuaraFiles',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventQuaraFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_event_quara_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    def describe_susp_event_user_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventUserSetting',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_event_user_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_user_setting_with_options(request, runtime)

    def describe_susp_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.assets_type_list):
            query['AssetsTypeList'] = request.assets_type_list
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.event_names):
            query['EventNames'] = request.event_names
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not UtilClient.is_unset(request.operate_time_end):
            query['OperateTimeEnd'] = request.operate_time_end
        if not UtilClient.is_unset(request.operate_time_start):
            query['OperateTimeStart'] = request.operate_time_start
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not UtilClient.is_unset(request.tactic_id):
            body['TacticId'] = request.tactic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    def describe_suspicious_overall_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspiciousOverallConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspiciousOverallConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_suspicious_overall_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_suspicious_overall_config_with_options(request, runtime)

    def describe_suspicious_uuidconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspiciousUUIDConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspiciousUUIDConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_suspicious_uuidconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_suspicious_uuidconfig_with_options(request, runtime)

    def describe_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_target_with_options(request, runtime)

    def describe_task_error_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_task_id):
            query['BuildTaskId'] = request.build_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskErrorLog',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeTaskErrorLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task_error_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_task_error_log_with_options(request, runtime)

    def describe_total_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTotalStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeTotalStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_total_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_total_statistics_with_options(request, runtime)

    def describe_trace_info_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.incident_time):
            query['IncidentTime'] = request.incident_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vertex_id):
            query['VertexId'] = request.vertex_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceInfoDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeTraceInfoDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trace_info_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_info_detail_with_options(request, runtime)

    def describe_trace_info_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.incident_time):
            query['IncidentTime'] = request.incident_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vertex_id):
            query['VertexId'] = request.vertex_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceInfoNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeTraceInfoNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trace_info_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_info_node_with_options(request, runtime)

    def describe_uni_backup_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.uni_region_id):
            query['UniRegionId'] = request.uni_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUniBackupDatabase',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUniBackupDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_uni_backup_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uni_backup_database_with_options(request, runtime)

    def describe_uni_backup_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUniBackupPolicies',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUniBackupPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_uni_backup_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uni_backup_policies_with_options(request, runtime)

    def describe_uni_backup_policy_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUniBackupPolicyDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUniBackupPolicyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_uni_backup_policy_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uni_backup_policy_detail_with_options(request, runtime)

    def describe_uni_recoverable_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUniRecoverableList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUniRecoverableListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_uni_recoverable_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uni_recoverable_list_with_options(request, runtime)

    def describe_uni_support_region_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUniSupportRegion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUniSupportRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_uni_support_region(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_uni_support_region_with_options(runtime)

    def describe_user_backup_machines_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeUserBackupMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBackupMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_backup_machines(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_backup_machines_with_options(runtime)

    def describe_user_baseline_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBaselineAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBaselineAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_baseline_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_baseline_authorization_with_options(request, runtime)

    def describe_user_layout_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLayoutAuthorization',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserLayoutAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_layout_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_layout_authorization_with_options(request, runtime)

    def describe_uuids_by_vul_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.field_name):
            query['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        if not UtilClient.is_unset(request.vul_names):
            query['VulNames'] = request.vul_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUuidsByVulNames',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUuidsByVulNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_uuids_by_vul_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uuids_by_vul_names_with_options(request, runtime)

    def describe_vendor_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVendorList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVendorListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vendor_list(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_vendor_list_with_options(runtime)

    def describe_version_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVersionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVersionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_version_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_version_config_with_options(request, runtime)

    def describe_vpc_honey_pot_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcHoneyPotCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vpc_honey_pot_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_criteria_with_options(request, runtime)

    def describe_vpc_honey_pot_list_with_options(self, request, runtime):
        """
        If you specify only the Action request parameter in your request, Security Center returns the list of all VPCs regardless of whether a honeypot is deployed on a VPC.
        

        @param request: DescribeVpcHoneyPotListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVpcHoneyPotListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.honey_pot_existence):
            query['HoneyPotExistence'] = request.honey_pot_existence
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcHoneyPotList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vpc_honey_pot_list(self, request):
        """
        If you specify only the Action request parameter in your request, Security Center returns the list of all VPCs regardless of whether a honeypot is deployed on a VPC.
        

        @param request: DescribeVpcHoneyPotListRequest

        @return: DescribeVpcHoneyPotListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_list_with_options(request, runtime)

    def describe_vpc_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVpcList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vpc_list(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_list_with_options(runtime)

    def describe_vul_check_task_status_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulCheckTaskStatusDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulCheckTaskStatusDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_check_task_status_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_check_task_status_detail_with_options(request, runtime)

    def describe_vul_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_config_with_options(request, runtime)

    def describe_vul_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulDetails',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    def describe_vul_export_info_with_options(self, request, runtime):
        """
        If the value of ExportStatus is success, the URL at which you can download the exported Excel file is returned.
        

        @param request: DescribeVulExportInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVulExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_export_info(self, request):
        """
        If the value of ExportStatus is success, the URL at which you can download the exported Excel file is returned.
        

        @param request: DescribeVulExportInfoRequest

        @return: DescribeVulExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_export_info_with_options(request, runtime)

    def describe_vul_fix_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVulFixStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulFixStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_fix_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_fix_statistics_with_options(runtime)

    def describe_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    def describe_vul_list_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.cve_id):
            query['CveId'] = request.cve_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vul_name_like):
            query['VulNameLike'] = request.vul_name_like
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulListPage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulListPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_list_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_page_with_options(request, runtime)

    def describe_vul_num_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulNumStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulNumStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_num_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_num_statistics_with_options(request, runtime)

    def describe_vul_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_target_config_with_options(request, runtime)

    def describe_vul_target_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulTargetStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulTargetStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_target_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_target_statistics_with_options(request, runtime)

    def describe_vul_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_whitelist_with_options(request, runtime)

    def describe_warning_export_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWarningExportInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWarningExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_warning_export_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_warning_export_info_with_options(request, runtime)

    def describe_warning_machines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.have_risk):
            query['HaveRisk'] = request.have_risk
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_name):
            query['MachineName'] = request.machine_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWarningMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWarningMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_warning_machines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_warning_machines_with_options(request, runtime)

    def describe_web_lock_bind_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockBindList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockBindListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_bind_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_bind_list_with_options(request, runtime)

    def describe_web_lock_config_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockConfigList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_config_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_config_list_with_options(request, runtime)

    def describe_web_lock_exclusive_file_type_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeWebLockExclusiveFileType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockExclusiveFileTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_exclusive_file_type(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_exclusive_file_type_with_options(runtime)

    def describe_web_lock_file_change_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockFileChangeStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockFileChangeStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_file_change_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_file_change_statistics_with_options(request, runtime)

    def describe_web_lock_file_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.ts_begin):
            query['TsBegin'] = request.ts_begin
        if not UtilClient.is_unset(request.ts_end):
            query['TsEnd'] = request.ts_end
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockFileEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockFileEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_file_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_file_events_with_options(request, runtime)

    def describe_web_lock_file_type_summary_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeWebLockFileTypeSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockFileTypeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_file_type_summary(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_file_type_summary_with_options(runtime)

    def describe_web_lock_inclusive_file_type_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeWebLockInclusiveFileType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockInclusiveFileTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_inclusive_file_type(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_inclusive_file_type_with_options(runtime)

    def describe_web_lock_process_block_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockProcessBlockStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockProcessBlockStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_process_block_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_process_block_statistics_with_options(request, runtime)

    def describe_web_lock_process_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockProcessList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_process_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_process_list_with_options(request, runtime)

    def describe_web_lock_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebLockStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_status_with_options(request, runtime)

    def describe_web_lock_total_file_change_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeWebLockTotalFileChangeCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockTotalFileChangeCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_lock_total_file_change_count(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_total_file_change_count_with_options(runtime)

    def describe_web_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebPath',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebPathResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_path_with_options(request, runtime)

    def disable_brute_force_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.bound):
            query['Bound'] = request.bound
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBruteForceRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DisableBruteForceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_brute_force_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_brute_force_record_with_options(request, runtime)

    def disable_custom_block_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.bound):
            query['Bound'] = request.bound
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCustomBlockRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.DisableCustomBlockRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_custom_block_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_custom_block_record_with_options(request, runtime)

    def enable_brute_force_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.bound):
            query['Bound'] = request.bound
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBruteForceRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.EnableBruteForceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_brute_force_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_brute_force_record_with_options(request, runtime)

    def enable_custom_block_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.bound):
            query['Bound'] = request.bound
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCustomBlockRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.EnableCustomBlockRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_custom_block_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_custom_block_record_with_options(request, runtime)

    def exec_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExecStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def exec_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exec_strategy_with_options(request, runtime)

    def export_record_with_options(self, request, runtime):
        """
        You can call the operation to export the following check result lists:
        *   The list of servers on the Host page.
        *   The lists of image system vulnerabilities, image application vulnerabilities, image baseline check results, and malicious image samples on the Image Security page.
        *   The list of attack analysis data on the Attack Awareness page.
        *   The list of check results for AccessKey pair leaks on the AK leak detection page.
        

        @param request: ExportRecordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def export_record(self, request):
        """
        You can call the operation to export the following check result lists:
        *   The list of servers on the Host page.
        *   The lists of image system vulnerabilities, image application vulnerabilities, image baseline check results, and malicious image samples on the Image Security page.
        *   The list of attack analysis data on the Attack Awareness page.
        *   The list of check results for AccessKey pair leaks on the AK leak detection page.
        

        @param request: ExportRecordRequest

        @return: ExportRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_record_with_options(request, runtime)

    def export_susp_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assets_type_list):
            query['AssetsTypeList'] = request.assets_type_list
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def export_susp_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_susp_events_with_options(request, runtime)

    def export_vul_with_options(self, request, runtime):
        """
        You can call the ExportVul operation to export the following types of vulnerabilities: Linux software vulnerabilities, Windows system vulnerabilities, Web-CMS vulnerabilities, application vulnerabilities, and urgent vulnerabilities.
        You can use this operation together with the DescribeVulExportInfo operation. After you call the ExportVul operation to create a vulnerability export task, you can call the DescribeVulExportInfo operation to query the progress of the task by specifying the ID of the task.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ExportVulRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportVulResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attach_types):
            query['AttachTypes'] = request.attach_types
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.search_tags):
            query['SearchTags'] = request.search_tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vpc_instance_ids):
            query['VpcInstanceIds'] = request.vpc_instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportVulResponse(),
            self.call_api(params, req, runtime)
        )

    def export_vul(self, request):
        """
        You can call the ExportVul operation to export the following types of vulnerabilities: Linux software vulnerabilities, Windows system vulnerabilities, Web-CMS vulnerabilities, application vulnerabilities, and urgent vulnerabilities.
        You can use this operation together with the DescribeVulExportInfo operation. After you call the ExportVul operation to create a vulnerability export task, you can call the DescribeVulExportInfo operation to query the progress of the task by specifying the ID of the task.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ExportVulRequest

        @return: ExportVulResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_vul_with_options(request, runtime)

    def export_warning_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.is_cleartext_pwd):
            query['IsCleartextPwd'] = request.is_cleartext_pwd
        if not UtilClient.is_unset(request.is_summary_export):
            query['IsSummaryExport'] = request.is_summary_export
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.risk_ids):
            query['RiskIds'] = request.risk_ids
        if not UtilClient.is_unset(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not UtilClient.is_unset(request.risk_name):
            query['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.sub_type_names):
            query['SubTypeNames'] = request.sub_type_names
        if not UtilClient.is_unset(request.type_name):
            query['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.type_names):
            query['TypeNames'] = request.type_names
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportWarning',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportWarningResponse(),
            self.call_api(params, req, runtime)
        )

    def export_warning(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_warning_with_options(request, runtime)

    def find_container_network_connect_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.FindContainerNetworkConnectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dst_node):
            request.dst_node_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dst_node, 'DstNode', 'json')
        if not UtilClient.is_unset(tmp_req.src_node):
            request.src_node_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_node, 'SrcNode', 'json')
        query = {}
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_node_shrink):
            query['DstNode'] = request.dst_node_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.src_node_shrink):
            query['SrcNode'] = request.src_node_shrink
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindContainerNetworkConnect',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.FindContainerNetworkConnectResponse(),
            self.call_api(params, req, runtime)
        )

    def find_container_network_connect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_container_network_connect_with_options(request, runtime)

    def fix_check_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_params):
            query['CheckParams'] = request.check_params
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FixCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.FixCheckWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    def fix_check_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fix_check_warnings_with_options(request, runtime)

    def generate_once_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateOnceTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GenerateOnceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_once_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_once_task_with_options(request, runtime)

    def get_agentless_task_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAgentlessTaskCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAgentlessTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_agentless_task_count(self):
        runtime = util_models.RuntimeOptions()
        return self.get_agentless_task_count_with_options(runtime)

    def get_alarm_machine_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlarmMachineCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAlarmMachineCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alarm_machine_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alarm_machine_count_with_options(request, runtime)

    def get_app_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppNetwork',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAppNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_network_with_options(request, runtime)

    def get_asset_detail_by_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAssetDetailByUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAssetDetailByUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def get_asset_detail_by_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_asset_detail_by_uuid_with_options(request, runtime)

    def get_asset_selection_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAssetSelectionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAssetSelectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_asset_selection_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_asset_selection_config_with_options(request, runtime)

    def get_assets_property_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.item_name):
            query['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.search_criteria_list):
            query['SearchCriteriaList'] = request.search_criteria_list
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAssetsPropertyDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAssetsPropertyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_assets_property_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_assets_property_detail_with_options(request, runtime)

    def get_assets_property_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.force_flush):
            query['ForceFlush'] = request.force_flush
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_info):
            query['SearchInfo'] = request.search_info
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAssetsPropertyItem',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetAssetsPropertyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def get_assets_property_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_assets_property_item_with_options(request, runtime)

    def get_backup_storage_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetBackupStorageCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetBackupStorageCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_backup_storage_count(self):
        runtime = util_models.RuntimeOptions()
        return self.get_backup_storage_count_with_options(runtime)

    def get_check_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCheckConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_check_config(self):
        runtime = util_models.RuntimeOptions()
        return self.get_check_config_with_options(runtime)

    def get_check_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCheckDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_check_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_check_detail_with_options(request, runtime)

    def get_check_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckProcess',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCheckProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def get_check_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_check_process_with_options(request, runtime)

    def get_check_risk_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckRiskStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCheckRiskStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_check_risk_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_check_risk_statistics_with_options(request, runtime)

    def get_check_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCheckSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_check_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_check_summary_with_options(request, runtime)

    def get_client_ratio_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_directory_account_id):
            query['ResourceDirectoryAccountId'] = request.resource_directory_account_id
        if not UtilClient.is_unset(request.statistic_types):
            query['StatisticTypes'] = request.statistic_types
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientRatioStatistic',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetClientRatioStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_client_ratio_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_client_ratio_statistic_with_options(request, runtime)

    def get_client_user_define_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientUserDefineRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetClientUserDefineRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_client_user_define_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_client_user_define_rule_with_options(request, runtime)

    def get_cloud_asset_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_asset_types):
            query['CloudAssetTypes'] = request.cloud_asset_types
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudAssetCriteria',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCloudAssetCriteriaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_asset_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_asset_criteria_with_options(request, runtime)

    def get_cloud_asset_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_sub_type):
            query['AssetSubType'] = request.asset_sub_type
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.cloud_asset_instances):
            query['CloudAssetInstances'] = request.cloud_asset_instances
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudAssetDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCloudAssetDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_asset_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_asset_detail_with_options(request, runtime)

    def get_cloud_asset_summary_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCloudAssetSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetCloudAssetSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_asset_summary(self):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_asset_summary_with_options(runtime)

    def get_cluster_check_item_warning_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterCheckItemWarningStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetClusterCheckItemWarningStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_check_item_warning_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_check_item_warning_statistics_with_options(request, runtime)

    def get_cluster_rule_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterRuleSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetClusterRuleSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_rule_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_rule_summary_with_options(request, runtime)

    def get_cluster_susp_event_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterSuspEventStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetClusterSuspEventStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_susp_event_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_susp_event_statistics_with_options(request, runtime)

    def get_file_detect_api_invoke_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetFileDetectApiInvokeInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetFileDetectApiInvokeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_detect_api_invoke_info(self):
        runtime = util_models.RuntimeOptions()
        return self.get_file_detect_api_invoke_info_with_options(runtime)

    def get_file_detect_result_with_options(self, request, runtime):
        """
        The HashKey parameter is included in all API operations that are related to the file detection feature. The parameter specifies the unique identifier of a file. Only MD5 hash values are supported. Before you call this operation, calculate the MD5 hash value of the file.
        

        @param request: GetFileDetectResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFileDetectResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hash_key_list):
            query['HashKeyList'] = request.hash_key_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileDetectResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetFileDetectResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_detect_result(self, request):
        """
        The HashKey parameter is included in all API operations that are related to the file detection feature. The parameter specifies the unique identifier of a file. Only MD5 hash values are supported. Before you call this operation, calculate the MD5 hash value of the file.
        

        @param request: GetFileDetectResultRequest

        @return: GetFileDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_detect_result_with_options(request, runtime)

    def get_honeypot_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHoneypotNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetHoneypotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_honeypot_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_honeypot_node_with_options(request, runtime)

    def get_honeypot_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_preset_id):
            query['HoneypotPresetId'] = request.honeypot_preset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHoneypotPreset',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetHoneypotPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_honeypot_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_honeypot_preset_with_options(request, runtime)

    def get_honeypot_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.probe_id):
            query['ProbeId'] = request.probe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHoneypotProbe',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetHoneypotProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_honeypot_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_honeypot_probe_with_options(request, runtime)

    def get_image_scan_num_in_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.past_day):
            query['PastDay'] = request.past_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageScanNumInPeriod',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetImageScanNumInPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_scan_num_in_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_scan_num_in_period_with_options(request, runtime)

    def get_interception_rule_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterceptionRuleDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetInterceptionRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_interception_rule_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_interception_rule_detail_with_options(request, runtime)

    def get_interception_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterceptionSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetInterceptionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_interception_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_interception_summary_with_options(request, runtime)

    def get_interception_target_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInterceptionTargetDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetInterceptionTargetDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_interception_target_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_interception_target_detail_with_options(request, runtime)

    def get_last_once_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLastOnceTaskInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetLastOnceTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_last_once_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_last_once_task_info_with_options(request, runtime)

    def get_module_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModuleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetModuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_module_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_module_config_with_options(request, runtime)

    def get_once_task_result_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnceTaskResultInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetOnceTaskResultInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_once_task_result_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_once_task_result_info_with_options(request, runtime)

    def get_property_schedule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPropertyScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetPropertyScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_property_schedule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_property_schedule_config_with_options(request, runtime)

    def get_rules_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRulesCount',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetRulesCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rules_count(self):
        runtime = util_models.RuntimeOptions()
        return self.get_rules_count_with_options(runtime)

    def get_service_trail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTrail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetServiceTrailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_trail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_trail_with_options(request, runtime)

    def get_suspicious_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSuspiciousStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetSuspiciousStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_suspicious_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_suspicious_statistics_with_options(request, runtime)

    def get_vul_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id_list):
            query['GroupIdList'] = request.group_id_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type_list):
            query['TypeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVulStatistics',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetVulStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vul_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vul_statistics_with_options(request, runtime)

    def get_vul_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vul_whitelist_id):
            query['VulWhitelistId'] = request.vul_whitelist_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.GetVulWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vul_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vul_whitelist_with_options(request, runtime)

    def handle_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not UtilClient.is_unset(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def handle_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    def handle_similar_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSimilarSecurityEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSimilarSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def handle_similar_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_similar_security_events_with_options(request, runtime)

    def ignore_check_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_and_risk_type_list):
            query['CheckAndRiskTypeList'] = request.check_and_risk_type_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreCheckItems',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.IgnoreCheckItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def ignore_check_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ignore_check_items_with_options(request, runtime)

    def ignore_hc_check_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        if not UtilClient.is_unset(request.check_warning_ids):
            query['CheckWarningIds'] = request.check_warning_ids
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.risk_id):
            query['RiskId'] = request.risk_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreHcCheckWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.IgnoreHcCheckWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    def ignore_hc_check_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ignore_hc_check_warnings_with_options(request, runtime)

    def install_backup_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallBackupClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    def install_backup_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_backup_client_with_options(request, runtime)

    def install_cloud_monitor_with_options(self, request, runtime):
        """
        > Before you call this operation, make sure that the Security Center agent on your servers is online and the servers can access Alibaba Cloud services.
        

        @param request: InstallCloudMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallCloudMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_access_key):
            query['AgentAccessKey'] = request.agent_access_key
        if not UtilClient.is_unset(request.agent_secret_key):
            query['AgentSecretKey'] = request.agent_secret_key
        if not UtilClient.is_unset(request.argus_version):
            query['ArgusVersion'] = request.argus_version
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudMonitor',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallCloudMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def install_cloud_monitor(self, request):
        """
        > Before you call this operation, make sure that the Security Center agent on your servers is online and the servers can access Alibaba Cloud services.
        

        @param request: InstallCloudMonitorRequest

        @return: InstallCloudMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_monitor_with_options(request, runtime)

    def install_pm_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallPmAgent',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallPmAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def install_pm_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_pm_agent_with_options(request, runtime)

    def install_uni_backup_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallUniBackupAgent',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallUniBackupAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def install_uni_backup_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_uni_backup_agent_with_options(request, runtime)

    def join_web_lock_process_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.process_paths):
            query['ProcessPaths'] = request.process_paths
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinWebLockProcessWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.JoinWebLockProcessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def join_web_lock_process_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_web_lock_process_white_list_with_options(request, runtime)

    def list_agentless_region_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAgentlessRegion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAgentlessRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_agentless_region(self):
        runtime = util_models.RuntimeOptions()
        return self.list_agentless_region_with_options(runtime)

    def list_agentless_relate_malicious_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentlessRelateMalicious',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAgentlessRelateMaliciousResponse(),
            self.call_api(params, req, runtime)
        )

    def list_agentless_relate_malicious(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agentless_relate_malicious_with_options(request, runtime)

    def list_agentless_risk_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.intranet_ip):
            query['IntranetIp'] = request.intranet_ip
        if not UtilClient.is_unset(request.machine_name):
            query['MachineName'] = request.machine_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk):
            query['Risk'] = request.risk
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentlessRiskUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAgentlessRiskUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def list_agentless_risk_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agentless_risk_uuid_with_options(request, runtime)

    def list_agentless_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.intranet_ip):
            query['IntranetIp'] = request.intranet_ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.machine_name):
            query['MachineName'] = request.machine_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.root_task):
            query['RootTask'] = request.root_task
        if not UtilClient.is_unset(request.root_task_id):
            query['RootTaskId'] = request.root_task_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgentlessTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAgentlessTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_agentless_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agentless_task_with_options(request, runtime)

    def list_asset_refresh_task_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAssetRefreshTaskConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAssetRefreshTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_asset_refresh_task_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_asset_refresh_task_config_with_options(request, runtime)

    def list_asset_selection_selected_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.selection_key):
            query['SelectionKey'] = request.selection_key
        if not UtilClient.is_unset(request.target_list):
            query['TargetList'] = request.target_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAssetSelectionSelectedTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAssetSelectionSelectedTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def list_asset_selection_selected_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_asset_selection_selected_target_with_options(request, runtime)

    def list_asset_selection_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.selection_key):
            query['SelectionKey'] = request.selection_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAssetSelectionTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAssetSelectionTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def list_asset_selection_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_asset_selection_target_with_options(request, runtime)

    def list_available_honeypot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableHoneypot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListAvailableHoneypotResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_honeypot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_honeypot_with_options(request, runtime)

    def list_check_instance_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id_key):
            query['InstanceIdKey'] = request.instance_id_key
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_name_key):
            query['InstanceNameKey'] = request.instance_name_key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id_key):
            query['RegionIdKey'] = request.region_id_key
        if not UtilClient.is_unset(request.sort_types):
            query['SortTypes'] = request.sort_types
        if not UtilClient.is_unset(request.statuses):
            query['Statuses'] = request.statuses
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckInstanceResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListCheckInstanceResultResponse(),
            self.call_api(params, req, runtime)
        )

    def list_check_instance_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_check_instance_result_with_options(request, runtime)

    def list_check_item_warning_machine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.risk_type):
            query['RiskType'] = request.risk_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckItemWarningMachine',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListCheckItemWarningMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def list_check_item_warning_machine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_check_item_warning_machine_with_options(request, runtime)

    def list_check_item_warning_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_item_fuzzy):
            query['CheckItemFuzzy'] = request.check_item_fuzzy
        if not UtilClient.is_unset(request.check_level):
            query['CheckLevel'] = request.check_level
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.check_warning_status):
            query['CheckWarningStatus'] = request.check_warning_status
        if not UtilClient.is_unset(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not UtilClient.is_unset(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_type):
            query['RiskType'] = request.risk_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckItemWarningSummary',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListCheckItemWarningSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_check_item_warning_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_check_item_warning_summary_with_options(request, runtime)

    def list_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_key):
            query['CheckKey'] = request.check_key
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.custom_param):
            query['CustomParam'] = request.custom_param
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.requirement_ids):
            query['RequirementIds'] = request.requirement_ids
        if not UtilClient.is_unset(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not UtilClient.is_unset(request.sort_types):
            query['SortTypes'] = request.sort_types
        if not UtilClient.is_unset(request.standard_ids):
            query['StandardIds'] = request.standard_ids
        if not UtilClient.is_unset(request.statuses):
            query['Statuses'] = request.statuses
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.vendors):
            query['Vendors'] = request.vendors
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def list_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_check_result_with_options(request, runtime)

    def list_check_standard_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_sub_types):
            query['InstanceSubTypes'] = request.instance_sub_types
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.vendors):
            query['Vendors'] = request.vendors
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCheckStandard',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListCheckStandardResponse(),
            self.call_api(params, req, runtime)
        )

    def list_check_standard(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_check_standard_with_options(request, runtime)

    def list_client_user_define_rule_types_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListClientUserDefineRuleTypes',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListClientUserDefineRuleTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_client_user_define_rule_types(self):
        runtime = util_models.RuntimeOptions()
        return self.list_client_user_define_rule_types_with_options(runtime)

    def list_client_user_define_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientUserDefineRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListClientUserDefineRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_client_user_define_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_client_user_define_rules_with_options(request, runtime)

    def list_cloud_asset_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_asset_types):
            query['CloudAssetTypes'] = request.cloud_asset_types
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.logical_exp):
            query['LogicalExp'] = request.logical_exp
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudAssetInstances',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListCloudAssetInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cloud_asset_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_asset_instances_with_options(request, runtime)

    def list_cluster_cnnf_status_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterCnnfStatusDetail',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListClusterCnnfStatusDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_cnnf_status_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_cnnf_status_detail_with_options(request, runtime)

    def list_cluster_interception_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_cnnfstatus):
            query['ClusterCNNFStatus'] = request.cluster_cnnfstatus
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterInterceptionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListClusterInterceptionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_interception_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_interception_config_with_options(request, runtime)

    def list_honeypot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.honeypot_ids):
            query['HoneypotIds'] = request.honeypot_ids
        if not UtilClient.is_unset(request.honeypot_name):
            query['HoneypotName'] = request.honeypot_name
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHoneypot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListHoneypotResponse(),
            self.call_api(params, req, runtime)
        )

    def list_honeypot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_honeypot_with_options(request, runtime)

    def list_honeypot_alarm_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHoneypotAlarmEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListHoneypotAlarmEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_honeypot_alarm_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_honeypot_alarm_events_with_options(request, runtime)

    def list_honeypot_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHoneypotNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListHoneypotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_honeypot_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_honeypot_node_with_options(request, runtime)

    def list_honeypot_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.honeypot_image_name):
            query['HoneypotImageName'] = request.honeypot_image_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.preset_name):
            query['PresetName'] = request.preset_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHoneypotPreset',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListHoneypotPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def list_honeypot_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_honeypot_preset_with_options(request, runtime)

    def list_honeypot_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.probe_status):
            query['ProbeStatus'] = request.probe_status
        if not UtilClient.is_unset(request.probe_type):
            query['ProbeType'] = request.probe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHoneypotProbe',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListHoneypotProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_honeypot_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_honeypot_probe_with_options(request, runtime)

    def list_image_registry_region_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListImageRegistryRegion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListImageRegistryRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_image_registry_region(self):
        runtime = util_models.RuntimeOptions()
        return self.list_image_registry_region_with_options(runtime)

    def list_image_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageRisk',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListImageRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_image_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_image_risk_with_options(request, runtime)

    def list_instance_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.requirement_ids):
            query['RequirementIds'] = request.requirement_ids
        if not UtilClient.is_unset(request.standard_ids):
            query['StandardIds'] = request.standard_ids
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceCatalog',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListInstanceCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_catalog_with_options(request, runtime)

    def list_interception_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.history_name):
            query['HistoryName'] = request.history_name
        if not UtilClient.is_unset(request.interception_types):
            query['InterceptionTypes'] = request.interception_types
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterceptionHistory',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListInterceptionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_interception_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interception_history_with_options(request, runtime)

    def list_interception_rule_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.criteria):
            query['Criteria'] = request.criteria
        if not UtilClient.is_unset(request.criteria_type):
            query['CriteriaType'] = request.criteria_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterceptionRulePage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListInterceptionRulePageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_interception_rule_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interception_rule_page_with_options(request, runtime)

    def list_interception_target_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.image_list):
            query['ImageList'] = request.image_list
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterceptionTargetPage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListInterceptionTargetPageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_interception_target_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interception_target_page_with_options(request, runtime)

    def list_plugin_for_uuid_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ListPluginForUuidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = {}
        if not UtilClient.is_unset(request.types_shrink):
            query['Types'] = request.types_shrink
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPluginForUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListPluginForUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def list_plugin_for_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_plugin_for_uuid_with_options(request, runtime)

    def list_pod_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPodRisk',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListPodRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pod_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pod_risk_with_options(request, runtime)

    def list_private_registry_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.registry_type):
            query['RegistryType'] = request.registry_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateRegistryList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListPrivateRegistryListResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_registry_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_registry_list_with_options(request, runtime)

    def list_private_registry_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateRegistryType',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListPrivateRegistryTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_registry_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_registry_type_with_options(request, runtime)

    def list_query_rasp_app_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryRaspAppInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListQueryRaspAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_query_rasp_app_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_query_rasp_app_info_with_options(request, runtime)

    def list_rule_target_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuleTargetAll',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListRuleTargetAllResponse(),
            self.call_api(params, req, runtime)
        )

    def list_rule_target_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_target_all_with_options(request, runtime)

    def list_system_aggregation_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemAggregationRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListSystemAggregationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_aggregation_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_aggregation_rules_with_options(request, runtime)

    def list_system_client_rule_types_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSystemClientRuleTypes',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListSystemClientRuleTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_client_rule_types(self):
        runtime = util_models.RuntimeOptions()
        return self.list_system_client_rule_types_with_options(runtime)

    def list_system_client_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregation_ids):
            query['AggregationIds'] = request.aggregation_ids
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_container):
            query['IsContainer'] = request.is_container
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_types):
            query['RuleTypes'] = request.rule_types
        if not UtilClient.is_unset(request.system_type):
            query['SystemType'] = request.system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemClientRules',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListSystemClientRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_client_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_client_rules_with_options(request, runtime)

    def list_system_rule_aggregation_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemRuleAggregationTypes',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListSystemRuleAggregationTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_rule_aggregation_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_rule_aggregation_types_with_options(request, runtime)

    def list_uninstall_aegis_machines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id_str):
            query['RegionIdStr'] = request.region_id_str
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUninstallAegisMachines',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListUninstallAegisMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_uninstall_aegis_machines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_uninstall_aegis_machines_with_options(request, runtime)

    def list_uuids_by_web_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.web_path):
            query['WebPath'] = request.web_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUuidsByWebPath',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListUuidsByWebPathResponse(),
            self.call_api(params, req, runtime)
        )

    def list_uuids_by_web_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_uuids_by_web_path_with_options(request, runtime)

    def list_vul_auto_repair_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVulAutoRepairConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ListVulAutoRepairConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vul_auto_repair_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vul_auto_repair_config_with_options(request, runtime)

    def modify_access_key_leak_deal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.id_list):
            query['IdList'] = request.id_list
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessKeyLeakDeal',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAccessKeyLeakDealResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_access_key_leak_deal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_access_key_leak_deal_with_options(request, runtime)

    def modify_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.fail_count):
            query['FailCount'] = request.fail_count
        if not UtilClient.is_unset(request.forbidden_time):
            query['ForbiddenTime'] = request.forbidden_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.span):
            query['Span'] = request.span
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_anti_brute_force_rule_with_options(request, runtime)

    def modify_app_vul_scan_cycle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle):
            query['Cycle'] = request.cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppVulScanCycle',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAppVulScanCycleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app_vul_scan_cycle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_vul_scan_cycle_with_options(request, runtime)

    def modify_asset_group_with_options(self, request, runtime):
        """
        You can call the ModifyAssetGroup operation to change the server group to which one or more servers belong. After you create a server group by calling the [CreateOrUpdateAssetGroup](~~CreateOrUpdateAssetGroup~~) operation, you can call the ModifyAssetGroup operation to change the server group to which your servers belong.
        ### Limits
        You can call this API operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyAssetGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAssetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAssetGroup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAssetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_asset_group(self, request):
        """
        You can call the ModifyAssetGroup operation to change the server group to which one or more servers belong. After you create a server group by calling the [CreateOrUpdateAssetGroup](~~CreateOrUpdateAssetGroup~~) operation, you can call the ModifyAssetGroup operation to change the server group to which your servers belong.
        ### Limits
        You can call this API operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyAssetGroupRequest

        @return: ModifyAssetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_asset_group_with_options(request, runtime)

    def modify_asset_important_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.important_code):
            query['ImportantCode'] = request.important_code
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAssetImportant',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAssetImportantResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_asset_important(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_asset_important_with_options(request, runtime)

    def modify_auto_del_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoDelConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAutoDelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_auto_del_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_del_config_with_options(request, runtime)

    def modify_backup_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ModifyBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_shrink):
            query['Policy'] = request.policy_shrink
        if not UtilClient.is_unset(request.policy_region_id):
            query['PolicyRegionId'] = request.policy_region_id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_backup_policy_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicyStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backup_policy_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_status_with_options(request, runtime)

    def modify_clear_logstore_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_log_store):
            query['UserLogStore'] = request.user_log_store
        if not UtilClient.is_unset(request.user_project):
            query['UserProject'] = request.user_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClearLogstoreStorage',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyClearLogstoreStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_clear_logstore_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_clear_logstore_storage_with_options(request, runtime)

    def modify_client_conf_setup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.strategy_config):
            query['StrategyConfig'] = request.strategy_config
        if not UtilClient.is_unset(request.strategy_tag):
            query['StrategyTag'] = request.strategy_tag
        if not UtilClient.is_unset(request.strategy_tag_value):
            query['StrategyTagValue'] = request.strategy_tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClientConfSetup',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyClientConfSetupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_client_conf_setup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_client_conf_setup_with_options(request, runtime)

    def modify_client_conf_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_ext):
            query['TagExt'] = request.tag_ext
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClientConfStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyClientConfStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_client_conf_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_client_conf_strategy_with_options(request, runtime)

    def modify_client_user_define_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.cmdline):
            query['Cmdline'] = request.cmdline
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.md_5list):
            query['Md5List'] = request.md_5list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_file_path):
            query['NewFilePath'] = request.new_file_path
        if not UtilClient.is_unset(request.parent_cmdline):
            query['ParentCmdline'] = request.parent_cmdline
        if not UtilClient.is_unset(request.parent_proc_path):
            query['ParentProcPath'] = request.parent_proc_path
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.port_str):
            query['PortStr'] = request.port_str
        if not UtilClient.is_unset(request.proc_path):
            query['ProcPath'] = request.proc_path
        if not UtilClient.is_unset(request.registry_content):
            query['RegistryContent'] = request.registry_content
        if not UtilClient.is_unset(request.registry_key):
            query['RegistryKey'] = request.registry_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClientUserDefineRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyClientUserDefineRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_client_user_define_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_client_user_define_rule_with_options(request, runtime)

    def modify_cluster_cnnf_status_user_confirm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.user_confirm):
            query['UserConfirm'] = request.user_confirm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterCnnfStatusUserConfirm',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyClusterCnnfStatusUserConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_cnnf_status_user_confirm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_cnnf_status_user_confirm_with_options(request, runtime)

    def modify_concern_necessity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concern_necessity):
            query['ConcernNecessity'] = request.concern_necessity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConcernNecessity',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyConcernNecessityResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_concern_necessity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_concern_necessity_with_options(request, runtime)

    def modify_create_vul_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCreateVulWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyCreateVulWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_create_vul_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_create_vul_whitelist_with_options(request, runtime)

    def modify_custom_block_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ip):
            query['BlockIp'] = request.block_ip
        if not UtilClient.is_unset(request.bound):
            query['Bound'] = request.bound
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomBlockRecord',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyCustomBlockRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_custom_block_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_custom_block_record_with_options(request, runtime)

    def modify_cycle_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.first_date_str):
            query['FirstDateStr'] = request.first_date_str
        if not UtilClient.is_unset(request.interval_period):
            query['IntervalPeriod'] = request.interval_period
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.target_end_time):
            query['TargetEndTime'] = request.target_end_time
        if not UtilClient.is_unset(request.target_start_time):
            query['TargetStartTime'] = request.target_start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCycleTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyCycleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cycle_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cycle_task_with_options(request, runtime)

    def modify_emg_vul_submit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.user_agreement):
            query['UserAgreement'] = request.user_agreement
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEmgVulSubmit',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyEmgVulSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_emg_vul_submit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_emg_vul_submit_with_options(request, runtime)

    def modify_group_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupProperty',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyGroupPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_group_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_group_property_with_options(request, runtime)

    def modify_instance_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_rule_id):
            query['NewRuleId'] = request.new_rule_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAntiBruteForceRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_anti_brute_force_rule_with_options(request, runtime)

    def modify_interception_rule_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ModifyInterceptionRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dst_target):
            request.dst_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dst_target, 'DstTarget', 'json')
        if not UtilClient.is_unset(tmp_req.src_target):
            request.src_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_target, 'SrcTarget', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dst_target_shrink):
            query['DstTarget'] = request.dst_target_shrink
        if not UtilClient.is_unset(request.intercept_type):
            query['InterceptType'] = request.intercept_type
        if not UtilClient.is_unset(request.order_index):
            query['OrderIndex'] = request.order_index
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.src_target_shrink):
            query['SrcTarget'] = request.src_target_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInterceptionRule',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInterceptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_interception_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_interception_rule_with_options(request, runtime)

    def modify_interception_rule_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInterceptionRuleSwitch',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInterceptionRuleSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_interception_rule_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_interception_rule_switch_with_options(request, runtime)

    def modify_interception_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.image_list):
            query['ImageList'] = request.image_list
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_name):
            query['TargetName'] = request.target_name
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInterceptionTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInterceptionTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_interception_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_interception_target_with_options(request, runtime)

    def modify_log_meta_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogMetaStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLogMetaStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_log_meta_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_meta_status_with_options(request, runtime)

    def modify_login_base_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoginBaseConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginBaseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_login_base_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_login_base_config_with_options(request, runtime)

    def modify_login_switch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item):
            query['Item'] = request.item
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoginSwitchConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginSwitchConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_login_switch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_login_switch_config_with_options(request, runtime)

    def modify_notice_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.route):
            query['Route'] = request.route
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.time_limit):
            query['TimeLimit'] = request.time_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNoticeConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyNoticeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_notice_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_notice_config_with_options(request, runtime)

    def modify_open_log_shipper_with_options(self, request, runtime):
        """
        *Prerequisites** A service-linked role is created, and Security Center is authorized to access cloud resources. You can call the [CreateServiceLinkedRole](~~CreateServiceLinkedRole~~) operation to create service-linked roles and authorize Security Center to access cloud resources. **Scenarios** Before you use the log analysis feature of Security Center, you must call the ModifyOpenLogShipper operation to activate Log Service.
        

        @param request: ModifyOpenLogShipperRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyOpenLogShipperResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOpenLogShipper',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOpenLogShipperResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_open_log_shipper(self, request):
        """
        *Prerequisites** A service-linked role is created, and Security Center is authorized to access cloud resources. You can call the [CreateServiceLinkedRole](~~CreateServiceLinkedRole~~) operation to create service-linked roles and authorize Security Center to access cloud resources. **Scenarios** Before you use the log analysis feature of Security Center, you must call the ModifyOpenLogShipper operation to activate Log Service.
        

        @param request: ModifyOpenLogShipperRequest

        @return: ModifyOpenLogShipperResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_open_log_shipper_with_options(request, runtime)

    def modify_operate_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOperateVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOperateVulResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_operate_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    def modify_property_schedule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPropertyScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyPropertyScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_property_schedule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_property_schedule_config_with_options(request, runtime)

    def modify_push_all_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tasks):
            query['Tasks'] = request.tasks
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPushAllTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyPushAllTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_push_all_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_push_all_task_with_options(request, runtime)

    def modify_refresh_process_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRefreshProcessInfo',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRefreshProcessInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_refresh_process_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_refresh_process_info_with_options(request, runtime)

    def modify_risk_check_status_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the following operations:
        \\-To **ignore a check item**, use the AddCheckResultWhiteList operation.
        \\-To **cancel ignoring a check item**, use the RemoveCheckResultWhiteList operation.
        

        @param request: ModifyRiskCheckStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyRiskCheckStatusResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRiskCheckStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_risk_check_status(self, request):
        """
        @deprecated
        This operation is phased out. You can use the following operations:
        \\-To **ignore a check item**, use the AddCheckResultWhiteList operation.
        \\-To **cancel ignoring a check item**, use the RemoveCheckResultWhiteList operation.
        

        @param request: ModifyRiskCheckStatusRequest

        @return: ModifyRiskCheckStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_risk_check_status_with_options(request, runtime)

    def modify_risk_single_result_status_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the following operations:
        \\-To **ignore a risk item**, use the AddCheckInstanceResultWhiteList operation.
        \\-To **cancel ignoring a risk item**, use the RemoveCheckInstanceResultWhiteList operation.
        

        @param request: ModifyRiskSingleResultStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyRiskSingleResultStatusResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRiskSingleResultStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskSingleResultStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_risk_single_result_status(self, request):
        """
        @deprecated
        This operation is phased out. You can use the following operations:
        \\-To **ignore a risk item**, use the AddCheckInstanceResultWhiteList operation.
        \\-To **cancel ignoring a risk item**, use the RemoveCheckInstanceResultWhiteList operation.
        

        @param request: ModifyRiskSingleResultStatusRequest

        @return: ModifyRiskSingleResultStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_risk_single_result_status_with_options(request, runtime)

    def modify_security_check_schedule_config_with_options(self, request, runtime):
        """
        @deprecated
        This operation is phased out. You can use the ChangeCheckConfig operation.
        

        @param request: ModifySecurityCheckScheduleConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySecurityCheckScheduleConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.days_of_week):
            query['DaysOfWeek'] = request.days_of_week
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityCheckScheduleConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifySecurityCheckScheduleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_check_schedule_config(self, request):
        """
        @deprecated
        This operation is phased out. You can use the ChangeCheckConfig operation.
        

        @param request: ModifySecurityCheckScheduleConfigRequest

        @return: ModifySecurityCheckScheduleConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_check_schedule_config_with_options(request, runtime)

    def modify_security_event_mark_miss_individually_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        body = {}
        if not UtilClient.is_unset(request.delete_mark_miss_param):
            body['DeleteMarkMissParam'] = request.delete_mark_miss_param
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.insert_mark_miss_param):
            body['InsertMarkMissParam'] = request.insert_mark_miss_param
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySecurityEventMarkMissIndividually',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifySecurityEventMarkMissIndividuallyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_event_mark_miss_individually(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_event_mark_miss_individually_with_options(request, runtime)

    def modify_start_vul_scan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStartVulScan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStartVulScanResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_start_vul_scan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_start_vul_scan_with_options(request, runtime)

    def modify_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_type):
            query['CustomType'] = request.custom_type
        if not UtilClient.is_unset(request.cycle_days):
            query['CycleDays'] = request.cycle_days
        if not UtilClient.is_unset(request.cycle_start_time):
            query['CycleStartTime'] = request.cycle_start_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.risk_custom_params):
            query['RiskCustomParams'] = request.risk_custom_params
        if not UtilClient.is_unset(request.risk_sub_type_name):
            query['RiskSubTypeName'] = request.risk_sub_type_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_strategy_with_options(request, runtime)

    def modify_strategy_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStrategyTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStrategyTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_strategy_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_strategy_target_with_options(request, runtime)

    def modify_tag_with_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.machine_types):
            query['MachineTypes'] = request.machine_types
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTagWithUuid',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyTagWithUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tag_with_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_with_uuid_with_options(request, runtime)

    def modify_uni_backup_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ModifyUniBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.full_plan):
            request.full_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.full_plan, 'FullPlan', 'json')
        if not UtilClient.is_unset(tmp_req.inc_plan):
            request.inc_plan_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inc_plan, 'IncPlan', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.full_plan_shrink):
            query['FullPlan'] = request.full_plan_shrink
        if not UtilClient.is_unset(request.inc_plan_shrink):
            query['IncPlan'] = request.inc_plan_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_status):
            query['PolicyStatus'] = request.policy_status
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.speed_limiter):
            query['SpeedLimiter'] = request.speed_limiter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUniBackupPolicy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyUniBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_uni_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_uni_backup_policy_with_options(request, runtime)

    def modify_vpc_honey_pot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honey_pot_action):
            query['HoneyPotAction'] = request.honey_pot_action
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcHoneyPot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVpcHoneyPotResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vpc_honey_pot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_honey_pot_with_options(request, runtime)

    def modify_vul_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVulConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vul_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vul_config_with_options(request, runtime)

    def modify_vul_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVulTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vul_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vul_target_with_options(request, runtime)

    def modify_vul_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVulTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vul_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vul_target_config_with_options(request, runtime)

    def modify_vul_whitelist_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVulWhitelistTarget',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulWhitelistTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vul_whitelist_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vul_whitelist_target_with_options(request, runtime)

    def modify_web_lock_create_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.inclusive_file):
            query['InclusiveFile'] = request.inclusive_file
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockCreateConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockCreateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_create_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_create_config_with_options(request, runtime)

    def modify_web_lock_delete_config_with_options(self, request, runtime):
        """
        After you delete a directory that has web tamper proofing enabled on a server, files in the directory are no longer protected by web tamper proofing. The information about the websites that are hosted on the server may be maliciously modified by attackers. Proceed with caution.
        

        @param request: ModifyWebLockDeleteConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyWebLockDeleteConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockDeleteConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockDeleteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_delete_config(self, request):
        """
        After you delete a directory that has web tamper proofing enabled on a server, files in the directory are no longer protected by web tamper proofing. The information about the websites that are hosted on the server may be maliciously modified by attackers. Proceed with caution.
        

        @param request: ModifyWebLockDeleteConfigRequest

        @return: ModifyWebLockDeleteConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_delete_config_with_options(request, runtime)

    def modify_web_lock_process_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deal_all):
            query['DealAll'] = request.deal_all
        if not UtilClient.is_unset(request.operate_info):
            query['OperateInfo'] = request.operate_info
        if not UtilClient.is_unset(request.process_path):
            query['ProcessPath'] = request.process_path
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockProcessStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockProcessStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_process_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_process_status_with_options(request, runtime)

    def modify_web_lock_start_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockStart',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStartResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_start(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_start_with_options(request, runtime)

    def modify_web_lock_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockStatus',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_status_with_options(request, runtime)

    def modify_web_lock_unbind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockUnbind',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockUnbindResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_unbind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_unbind_with_options(request, runtime)

    def modify_web_lock_update_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defence_mode):
            query['DefenceMode'] = request.defence_mode
        if not UtilClient.is_unset(request.dir):
            query['Dir'] = request.dir
        if not UtilClient.is_unset(request.exclusive_dir):
            query['ExclusiveDir'] = request.exclusive_dir
        if not UtilClient.is_unset(request.exclusive_file):
            query['ExclusiveFile'] = request.exclusive_file
        if not UtilClient.is_unset(request.exclusive_file_type):
            query['ExclusiveFileType'] = request.exclusive_file_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.inclusive_file):
            query['InclusiveFile'] = request.inclusive_file
        if not UtilClient.is_unset(request.inclusive_file_type):
            query['InclusiveFileType'] = request.inclusive_file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_backup_dir):
            query['LocalBackupDir'] = request.local_backup_dir
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebLockUpdateConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockUpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_lock_update_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_update_config_with_options(request, runtime)

    def modify_web_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPath',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebPathResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_path_with_options(request, runtime)

    def open_sensitive_file_scan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_on):
            query['SwitchOn'] = request.switch_on
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenSensitiveFileScan',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OpenSensitiveFileScanResponse(),
            self.call_api(params, req, runtime)
        )

    def open_sensitive_file_scan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_sensitive_file_scan_with_options(request, runtime)

    def operate_agent_client_install_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAgentClientInstall',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateAgentClientInstallResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_agent_client_install(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_agent_client_install_with_options(request, runtime)

    def operate_common_overall_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateCommonOverallConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateCommonOverallConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_common_overall_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_common_overall_config_with_options(request, runtime)

    def operate_common_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field_name):
            query['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_operations):
            query['TargetOperations'] = request.target_operations
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateCommonTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateCommonTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_common_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_common_target_config_with_options(request, runtime)

    def operate_image_baseline_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_item_key_list):
            query['BaselineItemKeyList'] = request.baseline_item_key_list
        if not UtilClient.is_unset(request.image_uuid):
            query['ImageUuid'] = request.image_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateImageBaselineWhitelist',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateImageBaselineWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_image_baseline_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_image_baseline_whitelist_with_options(request, runtime)

    def operate_image_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.info):
            query['Info'] = request.info
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateImageVul',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateImageVulResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_image_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_image_vul_with_options(request, runtime)

    def operate_suspicious_overall_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.no_target_as_on):
            query['NoTargetAsOn'] = request.no_target_as_on
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateSuspiciousOverallConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateSuspiciousOverallConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_suspicious_overall_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_suspicious_overall_config_with_options(request, runtime)

    def operate_suspicious_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.target_operations):
            query['TargetOperations'] = request.target_operations
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateSuspiciousTargetConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateSuspiciousTargetConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_suspicious_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_suspicious_target_config_with_options(request, runtime)

    def operate_virus_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_all):
            query['OperationAll'] = request.operation_all
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_range):
            query['OperationRange'] = request.operation_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVirusEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateVirusEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_virus_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_virus_events_with_options(request, runtime)

    def operate_vuls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.vul_names):
            query['VulNames'] = request.vul_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVuls',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateVulsResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_vuls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    def operate_web_lock_file_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deal_all):
            query['DealAll'] = request.deal_all
        if not UtilClient.is_unset(request.event_ids):
            query['EventIds'] = request.event_ids
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateWebLockFileEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateWebLockFileEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_web_lock_file_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_web_lock_file_events_with_options(request, runtime)

    def operation_cancel_ignore_susp_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperationCancelIgnoreSuspEvent',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperationCancelIgnoreSuspEventResponse(),
            self.call_api(params, req, runtime)
        )

    def operation_cancel_ignore_susp_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operation_cancel_ignore_susp_event_with_options(request, runtime)

    def operation_susp_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.sub_operation):
            query['SubOperation'] = request.sub_operation
        if not UtilClient.is_unset(request.suspicious_event_ids):
            query['SuspiciousEventIds'] = request.suspicious_event_ids
        if not UtilClient.is_unset(request.warn_type):
            query['WarnType'] = request.warn_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperationSuspEvents',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.OperationSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def operation_susp_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operation_susp_events_with_options(request, runtime)

    def page_image_registry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.registry_name_like):
            body['RegistryNameLike'] = request.registry_name_like
        if not UtilClient.is_unset(request.registry_type_in_list):
            body['RegistryTypeInList'] = request.registry_type_in_list
        if not UtilClient.is_unset(request.registry_type_not_in_list):
            body['RegistryTypeNotInList'] = request.registry_type_not_in_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageImageRegistry',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PageImageRegistryResponse(),
            self.call_api(params, req, runtime)
        )

    def page_image_registry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.page_image_registry_with_options(request, runtime)

    def pause_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PauseClientResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pause_client_with_options(request, runtime)

    def public_create_image_scan_task_with_options(self, request, runtime):
        """
        Before you call the PublicCreateImageScanTask operation, we recommend that you call the [PublicPreCheckImageScanTask](~~PublicPreCheckImageScanTask~~) operation to query the number of images to scan and the quota for container image scan to be consumed by the image scan task. Make sure that the remaining quota for container image scan is sufficient. This prevents the task from being stopped due to an insufficient quota.
        

        @param request: PublicCreateImageScanTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublicCreateImageScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digests):
            query['Digests'] = request.digests
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_ids):
            query['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.registry_types):
            query['RegistryTypes'] = request.registry_types
        if not UtilClient.is_unset(request.repo_ids):
            query['RepoIds'] = request.repo_ids
        if not UtilClient.is_unset(request.repo_names):
            query['RepoNames'] = request.repo_names
        if not UtilClient.is_unset(request.repo_namespaces):
            query['RepoNamespaces'] = request.repo_namespaces
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublicCreateImageScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PublicCreateImageScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def public_create_image_scan_task(self, request):
        """
        Before you call the PublicCreateImageScanTask operation, we recommend that you call the [PublicPreCheckImageScanTask](~~PublicPreCheckImageScanTask~~) operation to query the number of images to scan and the quota for container image scan to be consumed by the image scan task. Make sure that the remaining quota for container image scan is sufficient. This prevents the task from being stopped due to an insufficient quota.
        

        @param request: PublicCreateImageScanTaskRequest

        @return: PublicCreateImageScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.public_create_image_scan_task_with_options(request, runtime)

    def public_pre_check_image_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.digests):
            query['Digests'] = request.digests
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_ids):
            query['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.registry_types):
            query['RegistryTypes'] = request.registry_types
        if not UtilClient.is_unset(request.repo_ids):
            query['RepoIds'] = request.repo_ids
        if not UtilClient.is_unset(request.repo_names):
            query['RepoNames'] = request.repo_names
        if not UtilClient.is_unset(request.repo_namespaces):
            query['RepoNamespaces'] = request.repo_namespaces
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublicPreCheckImageScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PublicPreCheckImageScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def public_pre_check_image_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.public_pre_check_image_scan_task_with_options(request, runtime)

    def public_sync_and_create_image_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublicSyncAndCreateImageScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.PublicSyncAndCreateImageScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def public_sync_and_create_image_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.public_sync_and_create_image_scan_task_with_options(request, runtime)

    def query_discover_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_mark):
            query['CreateMark'] = request.create_mark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDiscoverDatabase',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryDiscoverDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def query_discover_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_discover_database_with_options(request, runtime)

    def query_group_id_by_group_name_with_options(self, request, runtime):
        """
        You can call the QueryGroupIdByGroupName operation to query the ID of an asset group to which your assets belong by using the name of the asset group. When you call operations such as [GetSuspiciousStatistics](~~GetSuspiciousStatistics~~) and [DeleteGroup](~~DeleteGroup~~), you must specify the ID of the asset group. To query the ID of an asset group, call the QueryGroupIdByGroupName operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryGroupIdByGroupNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryGroupIdByGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGroupIdByGroupName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryGroupIdByGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    def query_group_id_by_group_name(self, request):
        """
        You can call the QueryGroupIdByGroupName operation to query the ID of an asset group to which your assets belong by using the name of the asset group. When you call operations such as [GetSuspiciousStatistics](~~GetSuspiciousStatistics~~) and [DeleteGroup](~~DeleteGroup~~), you must specify the ID of the asset group. To query the ID of an asset group, call the QueryGroupIdByGroupName operation.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryGroupIdByGroupNameRequest

        @return: QueryGroupIdByGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_group_id_by_group_name_with_options(request, runtime)

    def query_grouped_security_event_mark_miss_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disposal_way):
            query['DisposalWay'] = request.disposal_way
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGroupedSecurityEventMarkMissList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryGroupedSecurityEventMarkMissListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_grouped_security_event_mark_miss_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_grouped_security_event_mark_miss_list_with_options(request, runtime)

    def query_jenkins_image_registry_persistence_day_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJenkinsImageRegistryPersistenceDay',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryJenkinsImageRegistryPersistenceDayResponse(),
            self.call_api(params, req, runtime)
        )

    def query_jenkins_image_registry_persistence_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_jenkins_image_registry_persistence_day_with_options(request, runtime)

    def query_pre_check_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uni_region_id):
            query['UniRegionId'] = request.uni_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPreCheckDatabase',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.QueryPreCheckDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def query_pre_check_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_pre_check_database_with_options(request, runtime)

    def reboot_machine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootMachine',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RebootMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def reboot_machine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_machine_with_options(request, runtime)

    def refresh_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.cloud_asset_sub_type):
            query['CloudAssetSubType'] = request.cloud_asset_sub_type
        if not UtilClient.is_unset(request.cloud_asset_type):
            query['CloudAssetType'] = request.cloud_asset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_assets_with_options(request, runtime)

    def refresh_container_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshContainerAssets',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshContainerAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_container_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_container_assets_with_options(request, runtime)

    def remove_check_instance_result_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCheckInstanceResultWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RemoveCheckInstanceResultWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_check_instance_result_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_check_instance_result_white_list_with_options(request, runtime)

    def remove_check_result_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_group_id):
            query['CheckGroupId'] = request.check_group_id
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCheckResultWhiteList',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RemoveCheckResultWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_check_result_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_check_result_white_list_with_options(request, runtime)

    def rollback_susp_event_quara_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.quara_file_id):
            query['QuaraFileId'] = request.quara_file_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSuspEventQuaraFile',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.RollbackSuspEventQuaraFileResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_susp_event_quara_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    def sas_install_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SasInstallCode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SasInstallCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def sas_install_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sas_install_code_with_options(request, runtime)

    def save_image_baseline_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_item_list):
            query['BaselineItemList'] = request.baseline_item_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveImageBaselineStrategy',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SaveImageBaselineStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def save_image_baseline_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_image_baseline_strategy_with_options(request, runtime)

    def save_susp_event_user_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.levels_on):
            query['LevelsOn'] = request.levels_on
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSuspEventUserSetting',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SaveSuspEventUserSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def save_susp_event_user_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_susp_event_user_setting_with_options(request, runtime)

    def set_cluster_interception_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.switch_on):
            query['SwitchOn'] = request.switch_on
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetClusterInterceptionConfig',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SetClusterInterceptionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cluster_interception_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cluster_interception_config_with_options(request, runtime)

    def set_registry_scan_day_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scan_day_num):
            query['ScanDayNum'] = request.scan_day_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRegistryScanDayNum',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SetRegistryScanDayNumResponse(),
            self.call_api(params, req, runtime)
        )

    def set_registry_scan_day_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_registry_scan_day_num_with_options(request, runtime)

    def start_baseline_security_check_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: StartBaselineSecurityCheckRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartBaselineSecurityCheckResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_ids):
            query['ItemIds'] = request.item_ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBaselineSecurityCheck',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartBaselineSecurityCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def start_baseline_security_check(self, request):
        """
        @deprecated
        

        @param request: StartBaselineSecurityCheckRequest

        @return: StartBaselineSecurityCheckResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.start_baseline_security_check_with_options(request, runtime)

    def start_discover_database_task_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='StartDiscoverDatabaseTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartDiscoverDatabaseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_discover_database_task(self):
        runtime = util_models.RuntimeOptions()
        return self.start_discover_database_task_with_options(runtime)

    def start_pre_check_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not UtilClient.is_unset(request.uni_region_id):
            query['UniRegionId'] = request.uni_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPreCheckDatabase',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartPreCheckDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def start_pre_check_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_pre_check_database_with_options(request, runtime)

    def start_virus_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.target_info):
            query['TargetInfo'] = request.target_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVirusScanTask',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.StartVirusScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_virus_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    def submit_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCheck',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.SubmitCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_check_with_options(request, runtime)

    def unbind_aegis_with_options(self, request, runtime):
        """
        If you no longer require protection for servers that are not deployed on Alibaba Cloud, you can call this operation to unbind the servers from Security Center. After you unbind a server that is not deployed on Alibaba Cloud from Security Center, the server no longer consumes the quota of protected servers or protected server vCPUs. This way, you can install the Security Center agent on other servers to meet your business requirements.
        > You can unbind only the servers that are not deployed on Alibaba Cloud from Security Center. If you use an Alibaba Cloud Elastic Compute Service (ECS) instance, you do not need to unbind the ECS instance. If you uninstall the Security Center agent from an ECS instance, the ECS instance still exists as a disconnected server in the asset list of the Security Center console. The ECS instance is not removed from the asset list.
        **Prerequisites**\
        *   The server that you want to unbind from Security Center is not deployed on Alibaba Cloud and the Security Center agent is disabled for the server. In this case, the agent is in the Close state and Security Center does not protect the server. You can call the [PauseClient](~~PauseClient~~) operation to disable the agent.
        *   The client protection feature is disabled for the server that you want to unbind from Security Center. For more information about how to disable the client protection feature, see [Use the client protection feature](https://www.alibabacloud.com/help/en/security-center/latest/local-file-detection-engine).
        

        @param request: UnbindAegisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnbindAegisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAegis',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UnbindAegisResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_aegis(self, request):
        """
        If you no longer require protection for servers that are not deployed on Alibaba Cloud, you can call this operation to unbind the servers from Security Center. After you unbind a server that is not deployed on Alibaba Cloud from Security Center, the server no longer consumes the quota of protected servers or protected server vCPUs. This way, you can install the Security Center agent on other servers to meet your business requirements.
        > You can unbind only the servers that are not deployed on Alibaba Cloud from Security Center. If you use an Alibaba Cloud Elastic Compute Service (ECS) instance, you do not need to unbind the ECS instance. If you uninstall the Security Center agent from an ECS instance, the ECS instance still exists as a disconnected server in the asset list of the Security Center console. The ECS instance is not removed from the asset list.
        **Prerequisites**\
        *   The server that you want to unbind from Security Center is not deployed on Alibaba Cloud and the Security Center agent is disabled for the server. In this case, the agent is in the Close state and Security Center does not protect the server. You can call the [PauseClient](~~PauseClient~~) operation to disable the agent.
        *   The client protection feature is disabled for the server that you want to unbind from Security Center. For more information about how to disable the client protection feature, see [Use the client protection feature](https://www.alibabacloud.com/help/en/security-center/latest/local-file-detection-engine).
        

        @param request: UnbindAegisRequest

        @return: UnbindAegisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_aegis_with_options(request, runtime)

    def uninstall_backup_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_version):
            query['PolicyVersion'] = request.policy_version
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.uuid_list):
            query['UuidList'] = request.uuid_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallBackupClient',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UninstallBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_backup_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_backup_client_with_options(request, runtime)

    def uninstall_uni_backup_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallUniBackupAgent',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UninstallUniBackupAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_uni_backup_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_uni_backup_agent_with_options(request, runtime)

    def update_honeypot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_id):
            query['HoneypotId'] = request.honeypot_id
        if not UtilClient.is_unset(request.honeypot_name):
            query['HoneypotName'] = request.honeypot_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHoneypot',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpdateHoneypotResponse(),
            self.call_api(params, req, runtime)
        )

    def update_honeypot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_honeypot_with_options(request, runtime)

    def update_honeypot_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.available_probe_num):
            query['AvailableProbeNum'] = request.available_probe_num
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.security_group_probe_ip_list):
            query['SecurityGroupProbeIpList'] = request.security_group_probe_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHoneypotNode',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpdateHoneypotNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_honeypot_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_honeypot_node_with_options(request, runtime)

    def update_honeypot_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.honeypot_image_name):
            query['HoneypotImageName'] = request.honeypot_image_name
        if not UtilClient.is_unset(request.honeypot_preset_id):
            query['HoneypotPresetId'] = request.honeypot_preset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.meta):
            query['Meta'] = request.meta
        if not UtilClient.is_unset(request.preset_name):
            query['PresetName'] = request.preset_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHoneypotPreset',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpdateHoneypotPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def update_honeypot_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_honeypot_preset_with_options(request, runtime)

    def update_honeypot_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arp):
            query['Arp'] = request.arp
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.ping):
            query['Ping'] = request.ping
        if not UtilClient.is_unset(request.probe_id):
            query['ProbeId'] = request.probe_id
        if not UtilClient.is_unset(request.service_ip_list):
            query['ServiceIpList'] = request.service_ip_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHoneypotProbe',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpdateHoneypotProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_honeypot_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_honeypot_probe_with_options(request, runtime)

    def update_jenkins_image_registry_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        body = {}
        if not UtilClient.is_unset(request.registry_id):
            body['RegistryId'] = request.registry_id
        if not UtilClient.is_unset(request.registry_name):
            body['RegistryName'] = request.registry_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJenkinsImageRegistryName',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpdateJenkinsImageRegistryNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_jenkins_image_registry_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_jenkins_image_registry_name_with_options(request, runtime)

    def update_jenkins_image_registry_persistence_day_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        body = {}
        if not UtilClient.is_unset(request.persistence_day):
            body['PersistenceDay'] = request.persistence_day
        if not UtilClient.is_unset(request.registry_id):
            body['RegistryId'] = request.registry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJenkinsImageRegistryPersistenceDay',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpdateJenkinsImageRegistryPersistenceDayResponse(),
            self.call_api(params, req, runtime)
        )

    def update_jenkins_image_registry_persistence_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_jenkins_image_registry_persistence_day_with_options(request, runtime)

    def upgrade_backup_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupPolicyVersion',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.UpgradeBackupPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_backup_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_backup_policy_version_with_options(request, runtime)

    def validate_hc_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        if not UtilClient.is_unset(request.risk_ids):
            query['RiskIds'] = request.risk_ids
        if not UtilClient.is_unset(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateHcWarnings',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.ValidateHcWarningsResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_hc_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_hc_warnings_with_options(request, runtime)

    def verify_check_instance_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCheckInstanceResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.VerifyCheckInstanceResultResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_check_instance_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_check_instance_result_with_options(request, runtime)

    def verify_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_ids):
            query['CheckIds'] = request.check_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCheckResult',
            version='2018-12-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_20181203_models.VerifyCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_check_result_with_options(request, runtime)
