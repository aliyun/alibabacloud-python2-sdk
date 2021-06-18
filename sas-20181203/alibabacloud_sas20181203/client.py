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
            'ap-southeast-3': 'tds.ap-southeast-3.aliyuncs.com',
            'ap-northeast-1': 'tds.aliyuncs.com',
            'ap-northeast-2-pop': 'tds.aliyuncs.com',
            'ap-south-1': 'tds.aliyuncs.com',
            'ap-southeast-1': 'tds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'tds.aliyuncs.com',
            'ap-southeast-5': 'tds.aliyuncs.com',
            'cn-beijing': 'tds.aliyuncs.com',
            'cn-beijing-finance-1': 'tds.aliyuncs.com',
            'cn-beijing-finance-pop': 'tds.aliyuncs.com',
            'cn-beijing-gov-1': 'tds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'tds.aliyuncs.com',
            'cn-chengdu': 'tds.aliyuncs.com',
            'cn-edge-1': 'tds.aliyuncs.com',
            'cn-fujian': 'tds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'tds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'tds.aliyuncs.com',
            'cn-hangzhou-finance': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'tds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'tds.aliyuncs.com',
            'cn-hangzhou-test-306': 'tds.aliyuncs.com',
            'cn-hongkong': 'tds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'tds.aliyuncs.com',
            'cn-huhehaote': 'tds.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'tds.aliyuncs.com',
            'cn-north-2-gov-1': 'tds.aliyuncs.com',
            'cn-qingdao': 'tds.aliyuncs.com',
            'cn-qingdao-nebula': 'tds.aliyuncs.com',
            'cn-shanghai': 'tds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'tds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'tds.aliyuncs.com',
            'cn-shanghai-finance-1': 'tds.aliyuncs.com',
            'cn-shanghai-inner': 'tds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'tds.aliyuncs.com',
            'cn-shenzhen': 'tds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'tds.aliyuncs.com',
            'cn-shenzhen-inner': 'tds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'tds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'tds.aliyuncs.com',
            'cn-wuhan': 'tds.aliyuncs.com',
            'cn-wulanchabu': 'tds.aliyuncs.com',
            'cn-yushanfang': 'tds.aliyuncs.com',
            'cn-zhangbei': 'tds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'tds.aliyuncs.com',
            'cn-zhangjiakou': 'tds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'tds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'tds.aliyuncs.com',
            'eu-central-1': 'tds.aliyuncs.com',
            'eu-west-1': 'tds.aliyuncs.com',
            'eu-west-1-oxs': 'tds.aliyuncs.com',
            'me-east-1': 'tds.aliyuncs.com',
            'rus-west-1-pop': 'tds.aliyuncs.com',
            'us-east-1': 'tds.aliyuncs.com',
            'us-west-1': 'tds.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_vpc_honey_pot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.AddVpcHoneyPotResponse(),
            self.do_rpcrequest('AddVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vpc_honey_pot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vpc_honey_pot_with_options(request, runtime)

    def check_quara_file_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckQuaraFileIdResponse(),
            self.do_rpcrequest('CheckQuaraFileId', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_quara_file_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_quara_file_id_with_options(request, runtime)

    def check_security_event_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CheckSecurityEventIdResponse(),
            self.do_rpcrequest('CheckSecurityEventId', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_security_event_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_security_event_id_with_options(request, runtime)

    def create_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAntiBruteForceRuleResponse(),
            self.do_rpcrequest('CreateAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_anti_brute_force_rule_with_options(request, runtime)

    def create_asset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateAssetResponse(),
            self.do_rpcrequest('CreateAsset', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_asset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_asset_with_options(request, runtime)

    def create_backup_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.CreateBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateBackupPolicyResponse(),
            self.do_rpcrequest('CreateBackupPolicy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    def create_or_update_asset_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateOrUpdateAssetGroupResponse(),
            self.do_rpcrequest('CreateOrUpdateAssetGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_or_update_asset_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_asset_group_with_options(request, runtime)

    def create_restore_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateRestoreJobResponse(),
            self.do_rpcrequest('CreateRestoreJob', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_restore_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_restore_job_with_options(request, runtime)

    def create_sas_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateSasOrderResponse(),
            self.do_rpcrequest('CreateSasOrder', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sas_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sas_order_with_options(request, runtime)

    def create_service_linked_role_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(self):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(runtime)

    def create_similar_security_events_query_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.CreateSimilarSecurityEventsQueryTaskResponse(),
            self.do_rpcrequest('CreateSimilarSecurityEventsQueryTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_similar_security_events_query_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_similar_security_events_query_task_with_options(request, runtime)

    def delete_asset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteAssetResponse(),
            self.do_rpcrequest('DeleteAsset', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_asset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_asset_with_options(request, runtime)

    def delete_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyResponse(),
            self.do_rpcrequest('DeleteBackupPolicy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_with_options(request, runtime)

    def delete_backup_policy_machine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteBackupPolicyMachineResponse(),
            self.do_rpcrequest('DeleteBackupPolicyMachine', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup_policy_machine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_machine_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteGroupResponse(),
            self.do_rpcrequest('DeleteGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_login_base_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteLoginBaseConfigResponse(),
            self.do_rpcrequest('DeleteLoginBaseConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_login_base_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_login_base_config_with_options(request, runtime)

    def delete_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteStrategyResponse(),
            self.do_rpcrequest('DeleteStrategy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_strategy_with_options(request, runtime)

    def delete_tag_with_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteTagWithUuidResponse(),
            self.do_rpcrequest('DeleteTagWithUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tag_with_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_uuid_with_options(request, runtime)

    def delete_vpc_honey_pot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DeleteVpcHoneyPotResponse(),
            self.do_rpcrequest('DeleteVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc_honey_pot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_honey_pot_with_options(request, runtime)

    def describe_accesskey_leak_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAccesskeyLeakListResponse(),
            self.do_rpcrequest('DescribeAccesskeyLeakList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accesskey_leak_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accesskey_leak_list_with_options(request, runtime)

    def describe_affected_malicious_file_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAffectedMaliciousFileImagesResponse(),
            self.do_rpcrequest('DescribeAffectedMaliciousFileImages', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_affected_malicious_file_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_affected_malicious_file_images_with_options(request, runtime)

    def describe_alarm_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventDetailResponse(),
            self.do_rpcrequest('DescribeAlarmEventDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarm_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_detail_with_options(request, runtime)

    def describe_alarm_event_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventListResponse(),
            self.do_rpcrequest('DescribeAlarmEventList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarm_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_list_with_options(request, runtime)

    def describe_alarm_event_stack_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAlarmEventStackInfoResponse(),
            self.do_rpcrequest('DescribeAlarmEventStackInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarm_event_stack_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_stack_info_with_options(request, runtime)

    def describe_all_entity_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllEntityResponse(),
            self.do_rpcrequest('DescribeAllEntity', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_entity(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_entity_with_options(runtime)

    def describe_all_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllGroupsResponse(),
            self.do_rpcrequest('DescribeAllGroups', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_groups_with_options(request, runtime)

    def describe_all_regions_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAllRegionsStatisticsResponse(),
            self.do_rpcrequest('DescribeAllRegionsStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_regions_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_regions_statistics_with_options(request, runtime)

    def describe_anti_brute_force_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAntiBruteForceRulesResponse(),
            self.do_rpcrequest('DescribeAntiBruteForceRules', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_anti_brute_force_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_anti_brute_force_rules_with_options(request, runtime)

    def describe_asset_detail_by_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidResponse(),
            self.do_rpcrequest('DescribeAssetDetailByUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_asset_detail_by_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_detail_by_uuid_with_options(request, runtime)

    def describe_asset_detail_by_uuids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeAssetDetailByUuidsResponse(),
            self.do_rpcrequest('DescribeAssetDetailByUuids', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_asset_detail_by_uuids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_detail_by_uuids_with_options(request, runtime)

    def describe_auto_del_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeAutoDelConfigResponse(),
            self.do_rpcrequest('DescribeAutoDelConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_del_config(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_del_config_with_options(runtime)

    def describe_backup_clients_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupClientsResponse(),
            self.do_rpcrequest('DescribeBackupClients', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_clients(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_clients_with_options(request, runtime)

    def describe_backup_dirs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupDirsResponse(),
            self.do_rpcrequest('DescribeBackupDirs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_dirs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dirs_with_options(request, runtime)

    def describe_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupFilesResponse(),
            self.do_rpcrequest('DescribeBackupFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_files_with_options(request, runtime)

    def describe_backup_machine_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupMachineStatusResponse(),
            self.do_rpcrequest('DescribeBackupMachineStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_machine_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_machine_status_with_options(request, runtime)

    def describe_backup_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupPoliciesResponse(),
            self.do_rpcrequest('DescribeBackupPolicies', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policies_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_backup_restore_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBackupRestoreCountResponse(),
            self.do_rpcrequest('DescribeBackupRestoreCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_restore_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_restore_count_with_options(request, runtime)

    def describe_brute_force_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeBruteForceSummaryResponse(),
            self.do_rpcrequest('DescribeBruteForceSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_brute_force_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_brute_force_summary_with_options(request, runtime)

    def describe_check_ecs_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckEcsWarningsResponse(),
            self.do_rpcrequest('DescribeCheckEcsWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_ecs_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_ecs_warnings_with_options(request, runtime)

    def describe_check_warning_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningDetailResponse(),
            self.do_rpcrequest('DescribeCheckWarningDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_warning_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_detail_with_options(request, runtime)

    def describe_check_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningsResponse(),
            self.do_rpcrequest('DescribeCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warnings_with_options(request, runtime)

    def describe_check_warning_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCheckWarningSummaryResponse(),
            self.do_rpcrequest('DescribeCheckWarningSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_warning_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_summary_with_options(request, runtime)

    def describe_cloud_center_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudCenterInstancesResponse(),
            self.do_rpcrequest('DescribeCloudCenterInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_center_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_center_instances_with_options(request, runtime)

    def describe_cloud_product_field_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeCloudProductFieldStatisticsResponse(),
            self.do_rpcrequest('DescribeCloudProductFieldStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_product_field_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_product_field_statistics_with_options(runtime)

    def describe_concern_necessity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeConcernNecessityResponse(),
            self.do_rpcrequest('DescribeConcernNecessity', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_concern_necessity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_concern_necessity_with_options(request, runtime)

    def describe_container_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeContainerStatisticsResponse(),
            self.do_rpcrequest('DescribeContainerStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_container_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_statistics_with_options(request, runtime)

    def describe_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeCriteriaResponse(),
            self.do_rpcrequest('DescribeCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_criteria_with_options(request, runtime)

    def describe_dialog_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDialogMessagesResponse(),
            self.do_rpcrequest('DescribeDialogMessages', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dialog_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_messages_with_options(request, runtime)

    def describe_ding_talk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDingTalkResponse(),
            self.do_rpcrequest('DescribeDingTalk', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ding_talk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ding_talk_with_options(request, runtime)

    def describe_domain_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainCountResponse(),
            self.do_rpcrequest('DescribeDomainCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_count_with_options(request, runtime)

    def describe_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainDetailResponse(),
            self.do_rpcrequest('DescribeDomainDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    def describe_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeDomainListResponse(),
            self.do_rpcrequest('DescribeDomainList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_list_with_options(request, runtime)

    def describe_emg_vul_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeEmgVulItemResponse(),
            self.do_rpcrequest('DescribeEmgVulItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_emg_vul_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_emg_vul_item_with_options(request, runtime)

    def describe_exclude_system_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExcludeSystemPathResponse(),
            self.do_rpcrequest('DescribeExcludeSystemPath', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exclude_system_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exclude_system_path_with_options(request, runtime)

    def describe_export_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExportInfoResponse(),
            self.do_rpcrequest('DescribeExportInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_export_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_export_info_with_options(request, runtime)

    def describe_exposed_instance_criteria_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceCriteriaResponse(),
            self.do_rpcrequest('DescribeExposedInstanceCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exposed_instance_criteria(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_criteria_with_options(request, runtime)

    def describe_exposed_instance_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceDetailResponse(),
            self.do_rpcrequest('DescribeExposedInstanceDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exposed_instance_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_detail_with_options(request, runtime)

    def describe_exposed_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedInstanceListResponse(),
            self.do_rpcrequest('DescribeExposedInstanceList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exposed_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_instance_list_with_options(request, runtime)

    def describe_exposed_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsResponse(),
            self.do_rpcrequest('DescribeExposedStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exposed_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_with_options(runtime)

    def describe_exposed_statistics_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeExposedStatisticsDetailResponse(),
            self.do_rpcrequest('DescribeExposedStatisticsDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_exposed_statistics_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exposed_statistics_detail_with_options(request, runtime)

    def describe_field_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeFieldStatisticsResponse(),
            self.do_rpcrequest('DescribeFieldStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_field_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_field_statistics_with_options(request, runtime)

    def describe_front_vul_patch_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeFrontVulPatchListResponse(),
            self.do_rpcrequest('DescribeFrontVulPatchList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_front_vul_patch_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    def describe_graph_4investigation_online_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGraph4InvestigationOnlineResponse(),
            self.do_rpcrequest('DescribeGraph4InvestigationOnline', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_graph_4investigation_online(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_graph_4investigation_online_with_options(request, runtime)

    def describe_grouped_container_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedContainerInstancesResponse(),
            self.do_rpcrequest('DescribeGroupedContainerInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_container_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_container_instances_with_options(request, runtime)

    def describe_grouped_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedInstancesResponse(),
            self.do_rpcrequest('DescribeGroupedInstances', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_instances_with_options(request, runtime)

    def describe_grouped_malicious_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedMaliciousFilesResponse(),
            self.do_rpcrequest('DescribeGroupedMaliciousFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_malicious_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_malicious_files_with_options(request, runtime)

    def describe_grouped_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedTagsResponse(),
            self.do_rpcrequest('DescribeGroupedTags', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_tags_with_options(request, runtime)

    def describe_grouped_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeGroupedVulResponse(),
            self.do_rpcrequest('DescribeGroupedVul', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    def describe_honey_pot_auth_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotAuthResponse(),
            self.do_rpcrequest('DescribeHoneyPotAuth', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_honey_pot_auth(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_auth_with_options(runtime)

    def describe_honey_pot_susp_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeHoneyPotSuspStatisticsResponse(),
            self.do_rpcrequest('DescribeHoneyPotSuspStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_honey_pot_susp_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_honey_pot_susp_statistics_with_options(request, runtime)

    def describe_image_grouped_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageGroupedVulListResponse(),
            self.do_rpcrequest('DescribeImageGroupedVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_grouped_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_grouped_vul_list_with_options(request, runtime)

    def describe_image_scan_auth_count_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageScanAuthCountResponse(),
            self.do_rpcrequest('DescribeImageScanAuthCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_scan_auth_count(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_scan_auth_count_with_options(runtime)

    def describe_image_statistics_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageStatisticsResponse(),
            self.do_rpcrequest('DescribeImageStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_statistics(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_statistics_with_options(runtime)

    def describe_image_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeImageVulListResponse(),
            self.do_rpcrequest('DescribeImageVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_vul_list_with_options(request, runtime)

    def describe_install_captcha_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstallCaptchaResponse(),
            self.do_rpcrequest('DescribeInstallCaptcha', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_install_captcha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_install_captcha_with_options(request, runtime)

    def describe_instance_anti_brute_force_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceAntiBruteForceRulesResponse(),
            self.do_rpcrequest('DescribeInstanceAntiBruteForceRules', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_anti_brute_force_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_anti_brute_force_rules_with_options(request, runtime)

    def describe_instance_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeInstanceStatisticsResponse(),
            self.do_rpcrequest('DescribeInstanceStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    def describe_ip_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeIpInfoResponse(),
            self.do_rpcrequest('DescribeIpInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_info_with_options(request, runtime)

    def describe_logstore_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeLogstoreStorageResponse(),
            self.do_rpcrequest('DescribeLogstoreStorage', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_logstore_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_logstore_storage_with_options(request, runtime)

    def describe_module_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeModuleConfigResponse(),
            self.do_rpcrequest('DescribeModuleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_module_config(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_module_config_with_options(runtime)

    def describe_notice_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeNoticeConfigResponse(),
            self.do_rpcrequest('DescribeNoticeConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_notice_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notice_config_with_options(request, runtime)

    def describe_property_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCountResponse(),
            self.do_rpcrequest('DescribePropertyCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_count_with_options(request, runtime)

    def describe_property_cron_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyCronDetailResponse(),
            self.do_rpcrequest('DescribePropertyCronDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_cron_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_cron_detail_with_options(request, runtime)

    def describe_property_port_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortDetailResponse(),
            self.do_rpcrequest('DescribePropertyPortDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_port_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_port_detail_with_options(request, runtime)

    def describe_property_port_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyPortItemResponse(),
            self.do_rpcrequest('DescribePropertyPortItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_port_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_port_item_with_options(request, runtime)

    def describe_property_proc_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcDetailResponse(),
            self.do_rpcrequest('DescribePropertyProcDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_proc_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_proc_detail_with_options(request, runtime)

    def describe_property_proc_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyProcItemResponse(),
            self.do_rpcrequest('DescribePropertyProcItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_proc_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_proc_item_with_options(request, runtime)

    def describe_property_sca_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyScaDetailResponse(),
            self.do_rpcrequest('DescribePropertyScaDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_sca_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_sca_detail_with_options(request, runtime)

    def describe_property_software_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareDetailResponse(),
            self.do_rpcrequest('DescribePropertySoftwareDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_software_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_software_detail_with_options(request, runtime)

    def describe_property_software_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertySoftwareItemResponse(),
            self.do_rpcrequest('DescribePropertySoftwareItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_software_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_software_item_with_options(request, runtime)

    def describe_property_usage_newest_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUsageNewestResponse(),
            self.do_rpcrequest('DescribePropertyUsageNewest', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_usage_newest(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_usage_newest_with_options(request, runtime)

    def describe_property_user_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserDetailResponse(),
            self.do_rpcrequest('DescribePropertyUserDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_user_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_user_detail_with_options(request, runtime)

    def describe_property_user_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribePropertyUserItemResponse(),
            self.do_rpcrequest('DescribePropertyUserItem', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_property_user_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_property_user_item_with_options(request, runtime)

    def describe_quara_file_download_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeQuaraFileDownloadInfoResponse(),
            self.do_rpcrequest('DescribeQuaraFileDownloadInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_quara_file_download_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_quara_file_download_info_with_options(request, runtime)

    def describe_restore_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRestoreJobsResponse(),
            self.do_rpcrequest('DescribeRestoreJobs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_restore_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_jobs_with_options(request, runtime)

    def describe_risk_check_item_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckItemResultResponse(),
            self.do_rpcrequest('DescribeRiskCheckItemResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_check_item_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_item_result_with_options(request, runtime)

    def describe_risk_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckResultResponse(),
            self.do_rpcrequest('DescribeRiskCheckResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_result_with_options(request, runtime)

    def describe_risk_check_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskCheckSummaryResponse(),
            self.do_rpcrequest('DescribeRiskCheckSummary', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_check_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_check_summary_with_options(request, runtime)

    def describe_risk_item_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskItemTypeResponse(),
            self.do_rpcrequest('DescribeRiskItemType', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_item_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_item_type_with_options(request, runtime)

    def describe_risk_list_check_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeRiskListCheckResultResponse(),
            self.do_rpcrequest('DescribeRiskListCheckResult', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_list_check_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_list_check_result_with_options(request, runtime)

    def describe_sas_asset_statistics_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSasAssetStatisticsColumnResponse(),
            self.do_rpcrequest('DescribeSasAssetStatisticsColumn', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sas_asset_statistics_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sas_asset_statistics_column_with_options(request, runtime)

    def describe_scan_task_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeScanTaskProgressResponse(),
            self.do_rpcrequest('DescribeScanTaskProgress', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scan_task_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    def describe_search_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSearchConditionResponse(),
            self.do_rpcrequest('DescribeSearchCondition', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_search_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_search_condition_with_options(request, runtime)

    def describe_secure_suggestion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecureSuggestionResponse(),
            self.do_rpcrequest('DescribeSecureSuggestion', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_secure_suggestion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_secure_suggestion_with_options(request, runtime)

    def describe_security_check_schedule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityCheckScheduleConfigResponse(),
            self.do_rpcrequest('DescribeSecurityCheckScheduleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_check_schedule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_check_schedule_config_with_options(request, runtime)

    def describe_security_event_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationsResponse(),
            self.do_rpcrequest('DescribeSecurityEventOperations', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_event_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    def describe_security_event_operation_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityEventOperationStatusResponse(),
            self.do_rpcrequest('DescribeSecurityEventOperationStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_event_operation_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    def describe_security_stat_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSecurityStatInfoResponse(),
            self.do_rpcrequest('DescribeSecurityStatInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_stat_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_stat_info_with_options(request, runtime)

    def describe_service_linked_role_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeServiceLinkedRoleStatusResponse(),
            self.do_rpcrequest('DescribeServiceLinkedRoleStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service_linked_role_status(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_linked_role_status_with_options(runtime)

    def describe_similar_event_scenarios_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarEventScenariosResponse(),
            self.do_rpcrequest('DescribeSimilarEventScenarios', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_similar_event_scenarios(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_similar_event_scenarios_with_options(request, runtime)

    def describe_similar_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSimilarSecurityEventsResponse(),
            self.do_rpcrequest('DescribeSimilarSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_similar_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_similar_security_events_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSnapshotsResponse(),
            self.do_rpcrequest('DescribeSnapshots', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyResponse(),
            self.do_rpcrequest('DescribeStrategy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_with_options(request, runtime)

    def describe_strategy_exec_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyExecDetailResponse(),
            self.do_rpcrequest('DescribeStrategyExecDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_strategy_exec_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_exec_detail_with_options(request, runtime)

    def describe_strategy_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyProcessResponse(),
            self.do_rpcrequest('DescribeStrategyProcess', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_strategy_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_process_with_options(request, runtime)

    def describe_strategy_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeStrategyTargetResponse(),
            self.do_rpcrequest('DescribeStrategyTarget', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_strategy_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_target_with_options(request, runtime)

    def describe_summary_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSummaryInfoResponse(),
            self.do_rpcrequest('DescribeSummaryInfo', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_summary_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_summary_info_with_options(request, runtime)

    def describe_support_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSupportRegionResponse(),
            self.do_rpcrequest('DescribeSupportRegion', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_support_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_support_region_with_options(request, runtime)

    def describe_susp_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventDetailResponse(),
            self.do_rpcrequest('DescribeSuspEventDetail', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_detail_with_options(request, runtime)

    def describe_susp_event_quara_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventQuaraFilesResponse(),
            self.do_rpcrequest('DescribeSuspEventQuaraFiles', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_event_quara_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    def describe_susp_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeSuspEventsResponse(),
            self.do_rpcrequest('DescribeSuspEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    def describe_user_backup_machines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBackupMachinesResponse(),
            self.do_rpcrequest('DescribeUserBackupMachines', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_backup_machines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_backup_machines_with_options(request, runtime)

    def describe_user_baseline_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserBaselineAuthorizationResponse(),
            self.do_rpcrequest('DescribeUserBaselineAuthorization', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_baseline_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_baseline_authorization_with_options(request, runtime)

    def describe_user_layout_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUserLayoutAuthorizationResponse(),
            self.do_rpcrequest('DescribeUserLayoutAuthorization', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_layout_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_layout_authorization_with_options(request, runtime)

    def describe_uuids_by_vul_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeUuidsByVulNamesResponse(),
            self.do_rpcrequest('DescribeUuidsByVulNames', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_uuids_by_vul_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uuids_by_vul_names_with_options(request, runtime)

    def describe_version_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVersionConfigResponse(),
            self.do_rpcrequest('DescribeVersionConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_version_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_version_config_with_options(request, runtime)

    def describe_vol_dingding_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVolDingdingMessageResponse(),
            self.do_rpcrequest('DescribeVolDingdingMessage', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vol_dingding_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vol_dingding_message_with_options(request, runtime)

    def describe_vpc_honey_pot_criteria_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotCriteriaResponse(),
            self.do_rpcrequest('DescribeVpcHoneyPotCriteria', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_honey_pot_criteria(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_criteria_with_options(runtime)

    def describe_vpc_honey_pot_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcHoneyPotListResponse(),
            self.do_rpcrequest('DescribeVpcHoneyPotList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_honey_pot_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_honey_pot_list_with_options(request, runtime)

    def describe_vpc_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            sas_20181203_models.DescribeVpcListResponse(),
            self.do_rpcrequest('DescribeVpcList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_list(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_list_with_options(runtime)

    def describe_vul_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulDetailsResponse(),
            self.do_rpcrequest('DescribeVulDetails', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    def describe_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulListResponse(),
            self.do_rpcrequest('DescribeVulList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    def describe_vul_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeVulWhitelistResponse(),
            self.do_rpcrequest('DescribeVulWhitelist', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_whitelist_with_options(request, runtime)

    def describe_warning_machines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWarningMachinesResponse(),
            self.do_rpcrequest('DescribeWarningMachines', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_warning_machines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_warning_machines_with_options(request, runtime)

    def describe_web_lock_bind_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockBindListResponse(),
            self.do_rpcrequest('DescribeWebLockBindList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_lock_bind_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_bind_list_with_options(request, runtime)

    def describe_web_lock_config_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.DescribeWebLockConfigListResponse(),
            self.do_rpcrequest('DescribeWebLockConfigList', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_lock_config_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_lock_config_list_with_options(request, runtime)

    def exec_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ExecStrategyResponse(),
            self.do_rpcrequest('ExecStrategy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def exec_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exec_strategy_with_options(request, runtime)

    def export_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ExportRecordResponse(),
            self.do_rpcrequest('ExportRecord', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_record_with_options(request, runtime)

    def fix_check_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.FixCheckWarningsResponse(),
            self.do_rpcrequest('FixCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fix_check_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fix_check_warnings_with_options(request, runtime)

    def get_backup_storage_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetBackupStorageCountResponse(),
            self.do_rpcrequest('GetBackupStorageCount', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_backup_storage_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_backup_storage_count_with_options(request, runtime)

    def get_inc_iocs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetIncIOCsResponse(),
            self.do_rpcrequest('GetIncIOCs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_inc_iocs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_inc_iocs_with_options(request, runtime)

    def get_iocs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetIOCsResponse(),
            self.do_rpcrequest('GetIOCs', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_iocs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_iocs_with_options(request, runtime)

    def get_local_install_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetLocalInstallScriptResponse(),
            self.do_rpcrequest('GetLocalInstallScript', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_local_install_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_local_install_script_with_options(request, runtime)

    def get_local_uninstall_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetLocalUninstallScriptResponse(),
            self.do_rpcrequest('GetLocalUninstallScript', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_local_uninstall_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_local_uninstall_script_with_options(request, runtime)

    def get_suspicious_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetSuspiciousStatisticsResponse(),
            self.do_rpcrequest('GetSuspiciousStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_suspicious_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_suspicious_statistics_with_options(request, runtime)

    def get_vul_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.GetVulStatisticsResponse(),
            self.do_rpcrequest('GetVulStatistics', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_vul_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vul_statistics_with_options(request, runtime)

    def handle_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSecurityEventsResponse(),
            self.do_rpcrequest('HandleSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def handle_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    def handle_similar_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.HandleSimilarSecurityEventsResponse(),
            self.do_rpcrequest('HandleSimilarSecurityEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def handle_similar_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_similar_security_events_with_options(request, runtime)

    def ignore_hc_check_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.IgnoreHcCheckWarningsResponse(),
            self.do_rpcrequest('IgnoreHcCheckWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ignore_hc_check_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ignore_hc_check_warnings_with_options(request, runtime)

    def install_backup_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.InstallBackupClientResponse(),
            self.do_rpcrequest('InstallBackupClient', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_backup_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_backup_client_with_options(request, runtime)

    def modify_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAntiBruteForceRuleResponse(),
            self.do_rpcrequest('ModifyAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_anti_brute_force_rule_with_options(request, runtime)

    def modify_asset_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyAssetGroupResponse(),
            self.do_rpcrequest('ModifyAssetGroup', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_asset_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_asset_group_with_options(request, runtime)

    def modify_backup_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = sas_20181203_models.ModifyBackupPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy):
            request.policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy, 'Policy', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_backup_policy_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyBackupPolicyStatusResponse(),
            self.do_rpcrequest('ModifyBackupPolicyStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_status_with_options(request, runtime)

    def modify_create_vul_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyCreateVulWhitelistResponse(),
            self.do_rpcrequest('ModifyCreateVulWhitelist', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_create_vul_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_create_vul_whitelist_with_options(request, runtime)

    def modify_emg_vul_submit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyEmgVulSubmitResponse(),
            self.do_rpcrequest('ModifyEmgVulSubmit', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_emg_vul_submit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_emg_vul_submit_with_options(request, runtime)

    def modify_group_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyGroupPropertyResponse(),
            self.do_rpcrequest('ModifyGroupProperty', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_group_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_group_property_with_options(request, runtime)

    def modify_instance_anti_brute_force_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyInstanceAntiBruteForceRuleResponse(),
            self.do_rpcrequest('ModifyInstanceAntiBruteForceRule', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_anti_brute_force_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_anti_brute_force_rule_with_options(request, runtime)

    def modify_login_base_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginBaseConfigResponse(),
            self.do_rpcrequest('ModifyLoginBaseConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_login_base_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_login_base_config_with_options(request, runtime)

    def modify_login_switch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyLoginSwitchConfigResponse(),
            self.do_rpcrequest('ModifyLoginSwitchConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_login_switch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_login_switch_config_with_options(request, runtime)

    def modify_notice_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyNoticeConfigResponse(),
            self.do_rpcrequest('ModifyNoticeConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_notice_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_notice_config_with_options(request, runtime)

    def modify_open_log_shipper_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOpenLogShipperResponse(),
            self.do_rpcrequest('ModifyOpenLogShipper', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_open_log_shipper(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_open_log_shipper_with_options(request, runtime)

    def modify_operate_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyOperateVulResponse(),
            self.do_rpcrequest('ModifyOperateVul', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_operate_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    def modify_push_all_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyPushAllTaskResponse(),
            self.do_rpcrequest('ModifyPushAllTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_push_all_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_push_all_task_with_options(request, runtime)

    def modify_risk_check_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskCheckStatusResponse(),
            self.do_rpcrequest('ModifyRiskCheckStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_risk_check_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_risk_check_status_with_options(request, runtime)

    def modify_risk_single_result_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyRiskSingleResultStatusResponse(),
            self.do_rpcrequest('ModifyRiskSingleResultStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_risk_single_result_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_risk_single_result_status_with_options(request, runtime)

    def modify_security_check_schedule_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifySecurityCheckScheduleConfigResponse(),
            self.do_rpcrequest('ModifySecurityCheckScheduleConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_check_schedule_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_check_schedule_config_with_options(request, runtime)

    def modify_start_vul_scan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStartVulScanResponse(),
            self.do_rpcrequest('ModifyStartVulScan', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_start_vul_scan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_start_vul_scan_with_options(request, runtime)

    def modify_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStrategyResponse(),
            self.do_rpcrequest('ModifyStrategy', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_strategy_with_options(request, runtime)

    def modify_strategy_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyStrategyTargetResponse(),
            self.do_rpcrequest('ModifyStrategyTarget', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_strategy_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_strategy_target_with_options(request, runtime)

    def modify_tag_with_uuid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyTagWithUuidResponse(),
            self.do_rpcrequest('ModifyTagWithUuid', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_tag_with_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_with_uuid_with_options(request, runtime)

    def modify_vpc_honey_pot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVpcHoneyPotResponse(),
            self.do_rpcrequest('ModifyVpcHoneyPot', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_honey_pot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_honey_pot_with_options(request, runtime)

    def modify_vul_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyVulTargetConfigResponse(),
            self.do_rpcrequest('ModifyVulTargetConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vul_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vul_target_config_with_options(request, runtime)

    def modify_web_lock_create_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockCreateConfigResponse(),
            self.do_rpcrequest('ModifyWebLockCreateConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_create_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_create_config_with_options(request, runtime)

    def modify_web_lock_delete_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockDeleteConfigResponse(),
            self.do_rpcrequest('ModifyWebLockDeleteConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_delete_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_delete_config_with_options(request, runtime)

    def modify_web_lock_start_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStartResponse(),
            self.do_rpcrequest('ModifyWebLockStart', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_start(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_start_with_options(request, runtime)

    def modify_web_lock_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockStatusResponse(),
            self.do_rpcrequest('ModifyWebLockStatus', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_status_with_options(request, runtime)

    def modify_web_lock_unbind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockUnbindResponse(),
            self.do_rpcrequest('ModifyWebLockUnbind', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_unbind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_unbind_with_options(request, runtime)

    def modify_web_lock_update_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ModifyWebLockUpdateConfigResponse(),
            self.do_rpcrequest('ModifyWebLockUpdateConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_lock_update_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_lock_update_config_with_options(request, runtime)

    def operate_suspicious_target_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateSuspiciousTargetConfigResponse(),
            self.do_rpcrequest('OperateSuspiciousTargetConfig', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_suspicious_target_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_suspicious_target_config_with_options(request, runtime)

    def operate_vuls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.OperateVulsResponse(),
            self.do_rpcrequest('OperateVuls', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_vuls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    def operation_susp_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.OperationSuspEventsResponse(),
            self.do_rpcrequest('OperationSuspEvents', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operation_susp_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operation_susp_events_with_options(request, runtime)

    def pause_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.PauseClientResponse(),
            self.do_rpcrequest('PauseClient', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pause_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pause_client_with_options(request, runtime)

    def refresh_container_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.RefreshContainerAssetsResponse(),
            self.do_rpcrequest('RefreshContainerAssets', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_container_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_container_assets_with_options(request, runtime)

    def rollback_susp_event_quara_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.RollbackSuspEventQuaraFileResponse(),
            self.do_rpcrequest('RollbackSuspEventQuaraFile', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_susp_event_quara_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    def sas_install_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.SasInstallCodeResponse(),
            self.do_rpcrequest('SasInstallCode', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sas_install_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sas_install_code_with_options(request, runtime)

    def start_baseline_security_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.StartBaselineSecurityCheckResponse(),
            self.do_rpcrequest('StartBaselineSecurityCheck', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_baseline_security_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_baseline_security_check_with_options(request, runtime)

    def start_image_vul_scan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.StartImageVulScanResponse(),
            self.do_rpcrequest('StartImageVulScan', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_image_vul_scan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_image_vul_scan_with_options(request, runtime)

    def start_virus_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.StartVirusScanTaskResponse(),
            self.do_rpcrequest('StartVirusScanTask', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_virus_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    def unbind_aegis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.UnbindAegisResponse(),
            self.do_rpcrequest('UnbindAegis', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_aegis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_aegis_with_options(request, runtime)

    def uninstall_backup_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.UninstallBackupClientResponse(),
            self.do_rpcrequest('UninstallBackupClient', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def uninstall_backup_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_backup_client_with_options(request, runtime)

    def validate_hc_warnings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sas_20181203_models.ValidateHcWarningsResponse(),
            self.do_rpcrequest('ValidateHcWarnings', '2018-12-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_hc_warnings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_hc_warnings_with_options(request, runtime)
