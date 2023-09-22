# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('alidns', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_custom_line_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to AddCustomLine.
        

        @param request: AddCustomLineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    def add_custom_line(self, request):
        """
        The operation that you want to perform. Set the value to AddCustomLine.
        

        @param request: AddCustomLineRequest

        @return: AddCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_line_with_options(request, runtime)

    def add_dns_cache_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not UtilClient.is_unset(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not UtilClient.is_unset(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not UtilClient.is_unset(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dns_cache_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dns_cache_domain_with_options(request, runtime)

    def add_dns_gtm_access_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not UtilClient.is_unset(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not UtilClient.is_unset(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not UtilClient.is_unset(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not UtilClient.is_unset(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not UtilClient.is_unset(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not UtilClient.is_unset(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not UtilClient.is_unset(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not UtilClient.is_unset(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not UtilClient.is_unset(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not UtilClient.is_unset(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not UtilClient.is_unset(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dns_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_access_strategy_with_options(request, runtime)

    def add_dns_gtm_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dns_gtm_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_address_pool_with_options(request, runtime)

    def add_dns_gtm_monitor_with_options(self, request, runtime):
        """
        **\
        

        @param request: AddDnsGtmMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddDnsGtmMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDnsGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dns_gtm_monitor(self, request):
        """
        **\
        

        @param request: AddDnsGtmMonitorRequest

        @return: AddDnsGtmMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_dns_gtm_monitor_with_options(request, runtime)

    def add_domain_with_options(self, request, runtime):
        """
        You can check whether a domain name is valid based on the following topic:
        [Domain name validity](https://www.alibabacloud.com/help/zh/doc-detail/67788.htm)
        

        @param request: AddDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_domain(self, request):
        """
        You can check whether a domain name is valid based on the following topic:
        [Domain name validity](https://www.alibabacloud.com/help/zh/doc-detail/67788.htm)
        

        @param request: AddDomainRequest

        @return: AddDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_domain_with_options(request, runtime)

    def add_domain_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainBackup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainBackupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_domain_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_domain_backup_with_options(request, runtime)

    def add_domain_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_domain_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_domain_group_with_options(request, runtime)

    def add_domain_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def add_domain_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_domain_record_with_options(request, runtime)

    def add_gtm_access_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not UtilClient.is_unset(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not UtilClient.is_unset(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_access_strategy_with_options(request, runtime)

    def add_gtm_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.monitor_status):
            query['MonitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gtm_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_address_pool_with_options(request, runtime)

    def add_gtm_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gtm_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_monitor_with_options(request, runtime)

    def add_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.AddGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gtm_recovery_plan_with_options(request, runtime)

    def bind_instance_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.BindInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_instance_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_instance_domains_with_options(request, runtime)

    def change_domain_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ChangeDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_domain_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_domain_group_with_options(request, runtime)

    def change_domain_of_dns_product_with_options(self, request, runtime):
        """
        >  You can call this operation to change the domain name for an Alibaba Cloud DNS instance to which a domain name is bound. You can also call this operation to bind a domain name to an Alibaba Cloud DNS instance to which no domain name is bound. If you need to unbind a domain name from an Alibaba Cloud DNS instance, you can call this operation. In this case, the NewDomain parameter must not be specified.
        

        @param request: ChangeDomainOfDnsProductRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChangeDomainOfDnsProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_domain):
            query['NewDomain'] = request.new_domain
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDomainOfDnsProduct',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ChangeDomainOfDnsProductResponse(),
            self.call_api(params, req, runtime)
        )

    def change_domain_of_dns_product(self, request):
        """
        >  You can call this operation to change the domain name for an Alibaba Cloud DNS instance to which a domain name is bound. You can also call this operation to bind a domain name to an Alibaba Cloud DNS instance to which no domain name is bound. If you need to unbind a domain name from an Alibaba Cloud DNS instance, you can call this operation. In this case, the NewDomain parameter must not be specified.
        

        @param request: ChangeDomainOfDnsProductRequest

        @return: ChangeDomainOfDnsProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_domain_of_dns_product_with_options(request, runtime)

    def copy_gtm_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copy_type):
            query['CopyType'] = request.copy_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyGtmConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CopyGtmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_gtm_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_gtm_config_with_options(request, runtime)

    def create_pdns_app_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreatePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pdns_app_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pdns_app_key_with_options(request, runtime)

    def create_pdns_udp_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.CreatePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pdns_udp_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pdns_udp_ip_segment_with_options(request, runtime)

    def delete_custom_lines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_ids):
            query['LineIds'] = request.line_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_lines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_lines_with_options(request, runtime)

    def delete_dns_cache_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dns_cache_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_cache_domain_with_options(request, runtime)

    def delete_dns_gtm_access_strategy_with_options(self, request, runtime):
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
            action='DeleteDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dns_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_gtm_access_strategy_with_options(request, runtime)

    def delete_dns_gtm_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dns_gtm_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dns_gtm_address_pool_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        """
        Given the unique nature of a HiChina domain name, you are not allowed to delete the HiChina domain name by calling the Alibaba Cloud DNS API.
        *   If the system prompts that a domain name does not exist, it is an unregistered domain name, it does not exist under the account, or its format in the request parameters is incorrect.
        

        @param request: DeleteDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        """
        Given the unique nature of a HiChina domain name, you are not allowed to delete the HiChina domain name by calling the Alibaba Cloud DNS API.
        *   If the system prompts that a domain name does not exist, it is an unregistered domain name, it does not exist under the account, or its format in the request parameters is incorrect.
        

        @param request: DeleteDomainRequest

        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_domain_group_with_options(self, request, runtime):
        """
        >  A domain name group can be deleted only when it contains no domain names. The default group cannot be deleted.
        

        @param request: DeleteDomainGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDomainGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_group(self, request):
        """
        >  A domain name group can be deleted only when it contains no domain names. The default group cannot be deleted.
        

        @param request: DeleteDomainGroupRequest

        @return: DeleteDomainGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_group_with_options(request, runtime)

    def delete_domain_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_record_with_options(request, runtime)

    def delete_gtm_access_strategy_with_options(self, request, runtime):
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
            action='DeleteGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_access_strategy_with_options(request, runtime)

    def delete_gtm_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gtm_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_address_pool_with_options(request, runtime)

    def delete_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gtm_recovery_plan_with_options(request, runtime)

    def delete_sub_domain_records_with_options(self, request, runtime):
        """
        If the DNS records to be deleted contain locked DNS records, locked DNS records will not be deleted.
        

        @param request: DeleteSubDomainRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSubDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DeleteSubDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sub_domain_records(self, request):
        """
        If the DNS records to be deleted contain locked DNS records, locked DNS records will not be deleted.
        

        @param request: DeleteSubDomainRecordsRequest

        @return: DeleteSubDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_domain_records_with_options(request, runtime)

    def describe_batch_result_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_type):
            query['BatchType'] = request.batch_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultCount',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeBatchResultCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_batch_result_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_result_count_with_options(request, runtime)

    def describe_batch_result_detail_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the batch tasks have been executed.
        

        @param request: DescribeBatchResultDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBatchResultDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_type):
            query['BatchType'] = request.batch_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBatchResultDetail',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeBatchResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_batch_result_detail(self, request):
        """
        Before you call this operation, make sure that the batch tasks have been executed.
        

        @param request: DescribeBatchResultDetailRequest

        @return: DescribeBatchResultDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_result_detail_with_options(request, runtime)

    def describe_custom_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_line_with_options(request, runtime)

    def describe_custom_lines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeCustomLinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_lines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_lines_with_options(request, runtime)

    def describe_dnsslbsub_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDNSSLBSubDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDNSSLBSubDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dnsslbsub_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dnsslbsub_domains_with_options(request, runtime)

    def describe_dns_cache_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsCacheDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsCacheDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_cache_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_cache_domains_with_options(request, runtime)

    def describe_dns_gtm_access_strategies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_access_strategies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategies_with_options(request, runtime)

    def describe_dns_gtm_access_strategy_with_options(self, request, runtime):
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
            action='DescribeDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_with_options(request, runtime)

    def describe_dns_gtm_access_strategy_available_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAccessStrategyAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_access_strategy_available_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_access_strategy_available_config_with_options(request, runtime)

    def describe_dns_gtm_addr_attribute_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addrs):
            query['Addrs'] = request.addrs
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddrAttributeInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAddrAttributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_addr_attribute_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_addr_attribute_info_with_options(request, runtime)

    def describe_dns_gtm_address_pool_available_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAddressPoolAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAddressPoolAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_address_pool_available_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_address_pool_available_config_with_options(request, runtime)

    def describe_dns_gtm_available_alert_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmAvailableAlertGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_available_alert_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_available_alert_group_with_options(request, runtime)

    def describe_dns_gtm_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_with_options(request, runtime)

    def describe_dns_gtm_instance_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_instance_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pool_with_options(request, runtime)

    def describe_dns_gtm_instance_address_pools_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_instance_address_pools(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_address_pools_with_options(request, runtime)

    def describe_dns_gtm_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_status_with_options(request, runtime)

    def describe_dns_gtm_instance_system_cname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstanceSystemCnameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_instance_system_cname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instance_system_cname_with_options(request, runtime)

    def describe_dns_gtm_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_instances_with_options(request, runtime)

    def describe_dns_gtm_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_logs_with_options(request, runtime)

    def describe_dns_gtm_monitor_available_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmMonitorAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_monitor_available_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_monitor_available_config_with_options(request, runtime)

    def describe_dns_gtm_monitor_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsGtmMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_gtm_monitor_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_gtm_monitor_config_with_options(request, runtime)

    def describe_dns_product_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_product_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_product_instance_with_options(request, runtime)

    def describe_dns_product_instances_with_options(self, request, runtime):
        """
        The number of the page to return. Pages start from page *1**. Default value: **1**.
        

        @param request: DescribeDnsProductInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDnsProductInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDnsProductInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDnsProductInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dns_product_instances(self, request):
        """
        The number of the page to return. Pages start from page *1**. Default value: **1**.
        

        @param request: DescribeDnsProductInstancesRequest

        @return: DescribeDnsProductInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dns_product_instances_with_options(request, runtime)

    def describe_doh_account_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohAccountStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohAccountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doh_account_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_account_statistics_with_options(request, runtime)

    def describe_doh_domain_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doh_domain_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_domain_statistics_with_options(request, runtime)

    def describe_doh_domain_statistics_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doh_domain_statistics_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_domain_statistics_summary_with_options(request, runtime)

    def describe_doh_sub_domain_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohSubDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doh_sub_domain_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_with_options(request, runtime)

    def describe_doh_sub_domain_statistics_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohSubDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohSubDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doh_sub_domain_statistics_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_sub_domain_statistics_summary_with_options(request, runtime)

    def describe_doh_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDohUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDohUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doh_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doh_user_info_with_options(request, runtime)

    def describe_domain_dnssec_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDnssecInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainDnssecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_dnssec_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_dnssec_info_with_options(request, runtime)

    def describe_domain_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainGroups',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_groups_with_options(request, runtime)

    def describe_domain_info_with_options(self, request, runtime):
        """
        In this example, the domain name is bound to an Alibaba Cloud DNS instance of Enterprise Ultimate Edition. For more information about valid lines, see the return values of the RecordLines parameter.
        

        @param request: DescribeDomainInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDomainInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_info(self, request):
        """
        In this example, the domain name is bound to an Alibaba Cloud DNS instance of Enterprise Ultimate Edition. For more information about valid lines, see the return values of the RecordLines parameter.
        

        @param request: DescribeDomainInfoRequest

        @return: DescribeDomainInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_info_with_options(request, runtime)

    def describe_domain_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_logs_with_options(request, runtime)

    def describe_domain_ns_with_options(self, request, runtime):
        """
        > This operation queries the authoritative servers of a domain name registry to obtain the name servers for a domain name. If the domain name is in an invalid state, such as serverHold or clientHold, an error may be returned.
        

        @param request: DescribeDomainNsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDomainNsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainNsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_ns(self, request):
        """
        > This operation queries the authoritative servers of a domain name registry to obtain the name servers for a domain name. If the domain name is in an invalid state, such as serverHold or clientHold, an error may be returned.
        

        @param request: DescribeDomainNsRequest

        @return: DescribeDomainNsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ns_with_options(request, runtime)

    def describe_domain_record_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecordInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainRecordInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_record_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_record_info_with_options(request, runtime)

    def describe_domain_records_with_options(self, request, runtime):
        """
        You can specify the DomainName, PageNumber, and PageSize parameters to query the DNS records of a domain name.
        *   You can also specify the RRKeyWord, TypeKeyWord, or ValueKeyWord parameter to query the DNS records that contain the specified keyword.
        *   By default, the DNS records are sorted in reverse chronological order based on the time when they were added.
        

        @param request: DescribeDomainRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDomainRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rrkey_word):
            query['RRKeyWord'] = request.rrkey_word
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.type_key_word):
            query['TypeKeyWord'] = request.type_key_word
        if not UtilClient.is_unset(request.value_key_word):
            query['ValueKeyWord'] = request.value_key_word
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_records(self, request):
        """
        You can specify the DomainName, PageNumber, and PageSize parameters to query the DNS records of a domain name.
        *   You can also specify the RRKeyWord, TypeKeyWord, or ValueKeyWord parameter to query the DNS records that contain the specified keyword.
        *   By default, the DNS records are sorted in reverse chronological order based on the time when they were added.
        

        @param request: DescribeDomainRecordsRequest

        @return: DescribeDomainRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_records_with_options(request, runtime)

    def describe_domain_resolve_statistics_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolveStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainResolveStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_resolve_statistics_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolve_statistics_summary_with_options(request, runtime)

    def describe_domain_statistics_with_options(self, request, runtime):
        """
        Real-time data is collected per hour.
        

        @param request: DescribeDomainStatisticsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDomainStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_statistics(self, request):
        """
        Real-time data is collected per hour.
        

        @param request: DescribeDomainStatisticsRequest

        @return: DescribeDomainStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_statistics_with_options(request, runtime)

    def describe_domain_statistics_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_statistics_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_statistics_summary_with_options(request, runtime)

    def describe_domains_with_options(self, request, runtime):
        """
        You can specify the PageNumber and PageSize parameters to query domain names.
        *   You can specify the KeyWord parameter to query domain names that contain the specified keyword.
        *   By default, the domain names in a list are sorted in descending order of the time they were added.
        *   You can specify the GroupId parameter. If you do not specify this parameter, all domain names are queried by default.
        

        @param request: DescribeDomainsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.starmark):
            query['Starmark'] = request.starmark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domains(self, request):
        """
        You can specify the PageNumber and PageSize parameters to query domain names.
        *   You can specify the KeyWord parameter to query domain names that contain the specified keyword.
        *   By default, the domain names in a list are sorted in descending order of the time they were added.
        *   You can specify the GroupId parameter. If you do not specify this parameter, all domain names are queried by default.
        

        @param request: DescribeDomainsRequest

        @return: DescribeDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    def describe_gtm_access_strategies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategies',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_access_strategies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategies_with_options(request, runtime)

    def describe_gtm_access_strategy_with_options(self, request, runtime):
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
            action='DescribeGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategy_with_options(request, runtime)

    def describe_gtm_access_strategy_available_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAccessStrategyAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAccessStrategyAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_access_strategy_available_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_access_strategy_available_config_with_options(request, runtime)

    def describe_gtm_available_alert_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmAvailableAlertGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmAvailableAlertGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_available_alert_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_available_alert_group_with_options(request, runtime)

    def describe_gtm_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstance',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_with_options(request, runtime)

    def describe_gtm_instance_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_instance_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_address_pool_with_options(request, runtime)

    def describe_gtm_instance_address_pools_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceAddressPools',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceAddressPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_instance_address_pools(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_address_pools_with_options(request, runtime)

    def describe_gtm_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_status_with_options(request, runtime)

    def describe_gtm_instance_system_cname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstanceSystemCname',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstanceSystemCnameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_instance_system_cname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instance_system_cname_with_options(request, runtime)

    def describe_gtm_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.need_detail_attributes):
            query['NeedDetailAttributes'] = request.need_detail_attributes
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_instances_with_options(request, runtime)

    def describe_gtm_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_logs_with_options(request, runtime)

    def describe_gtm_monitor_available_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmMonitorAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_monitor_available_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_monitor_available_config_with_options(request, runtime)

    def describe_gtm_monitor_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmMonitorConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_monitor_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_monitor_config_with_options(request, runtime)

    def describe_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plan_with_options(request, runtime)

    def describe_gtm_recovery_plan_available_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlanAvailableConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlanAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_recovery_plan_available_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plan_available_config_with_options(request, runtime)

    def describe_gtm_recovery_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGtmRecoveryPlans',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeGtmRecoveryPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gtm_recovery_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gtm_recovery_plans_with_options(request, runtime)

    def describe_instance_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_domains_with_options(request, runtime)

    def describe_isp_flush_cache_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheInstances',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_isp_flush_cache_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_instances_with_options(request, runtime)

    def describe_isp_flush_cache_remain_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheRemainQuota',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheRemainQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_isp_flush_cache_remain_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_remain_quota_with_options(request, runtime)

    def describe_isp_flush_cache_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheTask',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_isp_flush_cache_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_task_with_options(request, runtime)

    def describe_isp_flush_cache_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIspFlushCacheTasks',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeIspFlushCacheTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_isp_flush_cache_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_isp_flush_cache_tasks_with_options(request, runtime)

    def describe_pdns_account_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAccountSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_account_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_account_summary_with_options(request, runtime)

    def describe_pdns_app_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_app_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_app_key_with_options(request, runtime)

    def describe_pdns_app_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsAppKeys',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsAppKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_app_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_app_keys_with_options(request, runtime)

    def describe_pdns_operate_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsOperateLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsOperateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_operate_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_operate_logs_with_options(request, runtime)

    def describe_pdns_request_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsRequestStatistic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsRequestStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_request_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_request_statistic_with_options(request, runtime)

    def describe_pdns_request_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsRequestStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsRequestStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_request_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_request_statistics_with_options(request, runtime)

    def describe_pdns_threat_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not UtilClient.is_unset(request.threat_type):
            query['ThreatType'] = request.threat_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_threat_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_threat_logs_with_options(request, runtime)

    def describe_pdns_threat_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatStatistic',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_threat_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_threat_statistic_with_options(request, runtime)

    def describe_pdns_threat_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.threat_level):
            query['ThreatLevel'] = request.threat_level
        if not UtilClient.is_unset(request.threat_source_ip):
            query['ThreatSourceIp'] = request.threat_source_ip
        if not UtilClient.is_unset(request.threat_type):
            query['ThreatType'] = request.threat_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsThreatStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsThreatStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_threat_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_threat_statistics_with_options(request, runtime)

    def describe_pdns_udp_ip_segments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsUdpIpSegments',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsUdpIpSegmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_udp_ip_segments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_udp_ip_segments_with_options(request, runtime)

    def describe_pdns_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePdnsUserInfo',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribePdnsUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pdns_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pdns_user_info_with_options(request, runtime)

    def describe_record_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordLogs',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_logs_with_options(request, runtime)

    def describe_record_resolve_statistics_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordResolveStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordResolveStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_resolve_statistics_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_resolve_statistics_summary_with_options(request, runtime)

    def describe_record_statistics_with_options(self, request, runtime):
        """
        Real-time data is collected per hour.
        

        @param request: DescribeRecordStatisticsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRecordStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.rr):
            query['Rr'] = request.rr
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatistics',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_statistics(self, request):
        """
        Real-time data is collected per hour.
        

        @param request: DescribeRecordStatisticsRequest

        @return: DescribeRecordStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_record_statistics_with_options(request, runtime)

    def describe_record_statistics_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_mode):
            query['SearchMode'] = request.search_mode
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordStatisticsSummary',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeRecordStatisticsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_statistics_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_statistics_summary_with_options(request, runtime)

    def describe_sub_domain_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubDomainRecords',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeSubDomainRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sub_domain_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sub_domain_records_with_options(request, runtime)

    def describe_support_lines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportLines',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeSupportLinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_support_lines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_support_lines_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_transfer_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.from_user_id):
            query['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.transfer_type):
            query['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransferDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.DescribeTransferDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_transfer_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_domains_with_options(request, runtime)

    def execute_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ExecuteGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_gtm_recovery_plan_with_options(request, runtime)

    def get_main_domain_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_string):
            query['InputString'] = request.input_string
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMainDomainName',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.GetMainDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    def get_main_domain_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_main_domain_name_with_options(request, runtime)

    def get_txt_record_for_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTxtRecordForVerify',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.GetTxtRecordForVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_txt_record_for_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_txt_record_for_verify_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        Set ResourceId.N or Tag.N that consists of Tag.N.Key and Tag.N.Value in the request to specify the object to be queried.
        *   Tag.N is a resource tag that consists of a key-value pair. If you set only Tag.N.Key, all tag values that are assigned to the specified key are returned. If you set only Tag.N.Value, an error message is returned.
        *   If you set both Tag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        Set ResourceId.N or Tag.N that consists of Tag.N.Key and Tag.N.Value in the request to specify the object to be queried.
        *   Tag.N is a resource tag that consists of a key-value pair. If you set only Tag.N.Key, all tag values that are assigned to the specified key are returned. If you set only Tag.N.Value, an error message is returned.
        *   If you set both Tag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_hichina_domain_dnswith_options(self, request, runtime):
        """
        If the operation succeeds, the name of the DNS server changes to that of an Alibaba Cloud DNS server (ending with hichina.com).
        >  Before you call this operation, make sure that your domain name has been registered with Alibaba Cloud and the DNS server in use is not an Alibaba Cloud DNS server.
        

        @param request: ModifyHichinaDomainDNSRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHichinaDomainDNSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHichinaDomainDNS',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ModifyHichinaDomainDNSResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hichina_domain_dns(self, request):
        """
        If the operation succeeds, the name of the DNS server changes to that of an Alibaba Cloud DNS server (ending with hichina.com).
        >  Before you call this operation, make sure that your domain name has been registered with Alibaba Cloud and the DNS server in use is not an Alibaba Cloud DNS server.
        

        @param request: ModifyHichinaDomainDNSRequest

        @return: ModifyHichinaDomainDNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hichina_domain_dnswith_options(request, runtime)

    def move_domain_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveDomainResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.MoveDomainResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_domain_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_domain_resource_group_with_options(request, runtime)

    def move_gtm_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveGtmResourceGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.MoveGtmResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_gtm_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_gtm_resource_group_with_options(request, runtime)

    def operate_batch_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_record_info):
            query['DomainRecordInfo'] = request.domain_record_info
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBatchDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.OperateBatchDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_batch_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_batch_domain_with_options(request, runtime)

    def pause_pdns_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PausePdnsService',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.PausePdnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_pdns_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pause_pdns_service_with_options(request, runtime)

    def preview_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.PreviewGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def preview_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preview_gtm_recovery_plan_with_options(request, runtime)

    def remove_pdns_app_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePdnsAppKey',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RemovePdnsAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_pdns_app_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_pdns_app_key_with_options(request, runtime)

    def remove_pdns_udp_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RemovePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_pdns_udp_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_pdns_udp_ip_segment_with_options(request, runtime)

    def resume_pdns_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumePdnsService',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ResumePdnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_pdns_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_pdns_service_with_options(request, runtime)

    def retrieve_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetrieveDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RetrieveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def retrieve_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retrieve_domain_with_options(request, runtime)

    def rollback_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.RollbackGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_gtm_recovery_plan_with_options(request, runtime)

    def set_dnsslbstatus_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.open):
            query['Open'] = request.open
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDNSSLBStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDNSSLBStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dnsslbstatus(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dnsslbstatus_with_options(request, runtime)

    def set_dns_gtm_access_mode_with_options(self, request, runtime):
        """
        ***\
        

        @param request: SetDnsGtmAccessModeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDnsGtmAccessModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDnsGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDnsGtmAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dns_gtm_access_mode(self, request):
        """
        ***\
        

        @param request: SetDnsGtmAccessModeRequest

        @return: SetDnsGtmAccessModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dns_gtm_access_mode_with_options(request, runtime)

    def set_dns_gtm_monitor_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDnsGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDnsGtmMonitorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dns_gtm_monitor_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dns_gtm_monitor_status_with_options(request, runtime)

    def set_domain_dnssec_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainDnssecStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDomainDnssecStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_dnssec_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_dnssec_status_with_options(request, runtime)

    def set_domain_record_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainRecordStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetDomainRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_record_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_record_status_with_options(request, runtime)

    def set_gtm_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGtmAccessMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetGtmAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_gtm_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gtm_access_mode_with_options(request, runtime)

    def set_gtm_monitor_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGtmMonitorStatus',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SetGtmMonitorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_gtm_monitor_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gtm_monitor_status_with_options(request, runtime)

    def submit_isp_flush_cache_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIspFlushCacheTask',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SubmitIspFlushCacheTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_isp_flush_cache_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_isp_flush_cache_task_with_options(request, runtime)

    def switch_dns_gtm_instance_strategy_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.strategy_mode):
            query['StrategyMode'] = request.strategy_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDnsGtmInstanceStrategyMode',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.SwitchDnsGtmInstanceStrategyModeResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_dns_gtm_instance_strategy_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dns_gtm_instance_strategy_mode_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def transfer_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.TransferDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_domain_with_options(request, runtime)

    def unbind_instance_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInstanceDomains',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UnbindInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_instance_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_instance_domains_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_app_key_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key_id):
            query['AppKeyId'] = request.app_key_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppKeyState',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateAppKeyStateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_key_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_key_state_with_options(request, runtime)

    def update_custom_line_with_options(self, request, runtime):
        """
        In each CIDR block, the end IP address must be greater than or equal to the start IP address.
        The CIDR blocks that are specified for all custom lines of a domain name cannot intersect.
        

        @param request: UpdateCustomLineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCustomLineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_segment):
            query['IpSegment'] = request.ip_segment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line_id):
            query['LineId'] = request.line_id
        if not UtilClient.is_unset(request.line_name):
            query['LineName'] = request.line_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomLine',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateCustomLineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_line(self, request):
        """
        In each CIDR block, the end IP address must be greater than or equal to the start IP address.
        The CIDR blocks that are specified for all custom lines of a domain name cannot intersect.
        

        @param request: UpdateCustomLineRequest

        @return: UpdateCustomLineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_line_with_options(request, runtime)

    def update_dnsslbweight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDNSSLBWeight',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDNSSLBWeightResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dnsslbweight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dnsslbweight_with_options(request, runtime)

    def update_dns_cache_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_ttl_max):
            query['CacheTtlMax'] = request.cache_ttl_max
        if not UtilClient.is_unset(request.cache_ttl_min):
            query['CacheTtlMin'] = request.cache_ttl_min
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_dns_server):
            query['SourceDnsServer'] = request.source_dns_server
        if not UtilClient.is_unset(request.source_edns):
            query['SourceEdns'] = request.source_edns
        if not UtilClient.is_unset(request.source_protocol):
            query['SourceProtocol'] = request.source_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomain',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsCacheDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dns_cache_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dns_cache_domain_with_options(request, runtime)

    def update_dns_cache_domain_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsCacheDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsCacheDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dns_cache_domain_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dns_cache_domain_remark_with_options(request, runtime)

    def update_dns_gtm_access_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.default_addr_pool):
            query['DefaultAddrPool'] = request.default_addr_pool
        if not UtilClient.is_unset(request.default_addr_pool_type):
            query['DefaultAddrPoolType'] = request.default_addr_pool_type
        if not UtilClient.is_unset(request.default_latency_optimization):
            query['DefaultLatencyOptimization'] = request.default_latency_optimization
        if not UtilClient.is_unset(request.default_lba_strategy):
            query['DefaultLbaStrategy'] = request.default_lba_strategy
        if not UtilClient.is_unset(request.default_max_return_addr_num):
            query['DefaultMaxReturnAddrNum'] = request.default_max_return_addr_num
        if not UtilClient.is_unset(request.default_min_available_addr_num):
            query['DefaultMinAvailableAddrNum'] = request.default_min_available_addr_num
        if not UtilClient.is_unset(request.failover_addr_pool):
            query['FailoverAddrPool'] = request.failover_addr_pool
        if not UtilClient.is_unset(request.failover_addr_pool_type):
            query['FailoverAddrPoolType'] = request.failover_addr_pool_type
        if not UtilClient.is_unset(request.failover_latency_optimization):
            query['FailoverLatencyOptimization'] = request.failover_latency_optimization
        if not UtilClient.is_unset(request.failover_lba_strategy):
            query['FailoverLbaStrategy'] = request.failover_lba_strategy
        if not UtilClient.is_unset(request.failover_max_return_addr_num):
            query['FailoverMaxReturnAddrNum'] = request.failover_max_return_addr_num
        if not UtilClient.is_unset(request.failover_min_available_addr_num):
            query['FailoverMinAvailableAddrNum'] = request.failover_min_available_addr_num
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.strategy_id):
            query['StrategyId'] = request.strategy_id
        if not UtilClient.is_unset(request.strategy_name):
            query['StrategyName'] = request.strategy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dns_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_access_strategy_with_options(request, runtime)

    def update_dns_gtm_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dns_gtm_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_address_pool_with_options(request, runtime)

    def update_dns_gtm_instance_global_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.cname_type):
            query['CnameType'] = request.cname_type
        if not UtilClient.is_unset(request.force_update):
            query['ForceUpdate'] = request.force_update
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.public_cname_mode):
            query['PublicCnameMode'] = request.public_cname_mode
        if not UtilClient.is_unset(request.public_rr):
            query['PublicRr'] = request.public_rr
        if not UtilClient.is_unset(request.public_user_domain_name):
            query['PublicUserDomainName'] = request.public_user_domain_name
        if not UtilClient.is_unset(request.public_zone_name):
            query['PublicZoneName'] = request.public_zone_name
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmInstanceGlobalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dns_gtm_instance_global_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_instance_global_config_with_options(request, runtime)

    def update_dns_gtm_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDnsGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDnsGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dns_gtm_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dns_gtm_monitor_with_options(request, runtime)

    def update_domain_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainGroup',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_domain_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_domain_group_with_options(request, runtime)

    def update_domain_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rr):
            query['RR'] = request.rr
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecord',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def update_domain_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_domain_record_with_options(request, runtime)

    def update_domain_record_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRecordRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRecordRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_domain_record_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_domain_record_remark_with_options(request, runtime)

    def update_domain_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainRemark',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateDomainRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_domain_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_domain_remark_with_options(request, runtime)

    def update_gtm_access_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_lines):
            query['AccessLines'] = request.access_lines
        if not UtilClient.is_unset(request.default_addr_pool_id):
            query['DefaultAddrPoolId'] = request.default_addr_pool_id
        if not UtilClient.is_unset(request.failover_addr_pool_id):
            query['FailoverAddrPoolId'] = request.failover_addr_pool_id
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
            action='UpdateGtmAccessStrategy',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmAccessStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gtm_access_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_access_strategy_with_options(request, runtime)

    def update_gtm_address_pool_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addr):
            query['Addr'] = request.addr
        if not UtilClient.is_unset(request.addr_pool_id):
            query['AddrPoolId'] = request.addr_pool_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.min_available_addr_num):
            query['MinAvailableAddrNum'] = request.min_available_addr_num
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmAddressPool',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gtm_address_pool(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_address_pool_with_options(request, runtime)

    def update_gtm_instance_global_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group):
            query['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.cname_custom_domain_name):
            query['CnameCustomDomainName'] = request.cname_custom_domain_name
        if not UtilClient.is_unset(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lba_strategy):
            query['LbaStrategy'] = request.lba_strategy
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.user_domain_name):
            query['UserDomainName'] = request.user_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmInstanceGlobalConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmInstanceGlobalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gtm_instance_global_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_instance_global_config_with_options(request, runtime)

    def update_gtm_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_city_node):
            query['IspCityNode'] = request.isp_city_node
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.monitor_config_id):
            query['MonitorConfigId'] = request.monitor_config_id
        if not UtilClient.is_unset(request.monitor_extend_info):
            query['MonitorExtendInfo'] = request.monitor_extend_info
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmMonitor',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gtm_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_monitor_with_options(request, runtime)

    def update_gtm_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fault_addr_pool):
            query['FaultAddrPool'] = request.fault_addr_pool
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGtmRecoveryPlan',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateGtmRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gtm_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gtm_recovery_plan_with_options(request, runtime)

    def update_isp_flush_cache_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIspFlushCacheInstanceConfig',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.UpdateIspFlushCacheInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_isp_flush_cache_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_isp_flush_cache_instance_config_with_options(request, runtime)

    def validate_dns_gtm_cname_rr_can_use_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname_mode):
            query['CnameMode'] = request.cname_mode
        if not UtilClient.is_unset(request.cname_rr):
            query['CnameRr'] = request.cname_rr
        if not UtilClient.is_unset(request.cname_type):
            query['CnameType'] = request.cname_type
        if not UtilClient.is_unset(request.cname_zone):
            query['CnameZone'] = request.cname_zone
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateDnsGtmCnameRrCanUse',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidateDnsGtmCnameRrCanUseResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_dns_gtm_cname_rr_can_use(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_dns_gtm_cname_rr_can_use_with_options(request, runtime)

    def validate_pdns_udp_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidatePdnsUdpIpSegment',
            version='2015-01-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alidns_20150109_models.ValidatePdnsUdpIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_pdns_udp_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_pdns_udp_ip_segment_with_options(request, runtime)
