# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ConfigNetStatusRequest(TeaModel):
    def __init__(self, net=None, regions=None, sale_id=None, status=None, sub_nets=None):
        self.net = net  # type: str
        self.regions = regions  # type: list[str]
        self.sale_id = sale_id  # type: str
        self.status = status  # type: str
        self.sub_nets = sub_nets  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigNetStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net is not None:
            result['Net'] = self.net
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_nets is not None:
            result['SubNets'] = self.sub_nets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubNets') is not None:
            self.sub_nets = m.get('SubNets')
        return self


class ConfigNetStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigNetStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigNetStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigNetStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigNetStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfigNetStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(self, name=None, num=None, page=None, sale_id=None, status=None):
        self.name = name  # type: str
        self.num = num  # type: long
        self.page = page  # type: long
        self.sale_id = sale_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceResponseBodyDataInstancesSpec(TeaModel):
    def __init__(self, coverage=None, diversion_type=None, edition=None, idc_numbers=None,
                 initial_installation=None, initial_qty=None, ip_subnet_nums=None, mitigation_analysis=None,
                 mitigation_analysis_capacity=None, mitigation_capacity=None, mitigation_nums=None, normal_bandwidth=None):
        self.coverage = coverage  # type: str
        self.diversion_type = diversion_type  # type: str
        self.edition = edition  # type: str
        self.idc_numbers = idc_numbers  # type: str
        self.initial_installation = initial_installation  # type: str
        self.initial_qty = initial_qty  # type: str
        self.ip_subnet_nums = ip_subnet_nums  # type: str
        self.mitigation_analysis = mitigation_analysis  # type: str
        self.mitigation_analysis_capacity = mitigation_analysis_capacity  # type: str
        self.mitigation_capacity = mitigation_capacity  # type: str
        self.mitigation_nums = mitigation_nums  # type: str
        self.normal_bandwidth = normal_bandwidth  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyDataInstancesSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.diversion_type is not None:
            result['DiversionType'] = self.diversion_type
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.idc_numbers is not None:
            result['IdcNumbers'] = self.idc_numbers
        if self.initial_installation is not None:
            result['InitialInstallation'] = self.initial_installation
        if self.initial_qty is not None:
            result['InitialQty'] = self.initial_qty
        if self.ip_subnet_nums is not None:
            result['IpSubnetNums'] = self.ip_subnet_nums
        if self.mitigation_analysis is not None:
            result['MitigationAnalysis'] = self.mitigation_analysis
        if self.mitigation_analysis_capacity is not None:
            result['MitigationAnalysisCapacity'] = self.mitigation_analysis_capacity
        if self.mitigation_capacity is not None:
            result['MitigationCapacity'] = self.mitigation_capacity
        if self.mitigation_nums is not None:
            result['MitigationNums'] = self.mitigation_nums
        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('DiversionType') is not None:
            self.diversion_type = m.get('DiversionType')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('IdcNumbers') is not None:
            self.idc_numbers = m.get('IdcNumbers')
        if m.get('InitialInstallation') is not None:
            self.initial_installation = m.get('InitialInstallation')
        if m.get('InitialQty') is not None:
            self.initial_qty = m.get('InitialQty')
        if m.get('IpSubnetNums') is not None:
            self.ip_subnet_nums = m.get('IpSubnetNums')
        if m.get('MitigationAnalysis') is not None:
            self.mitigation_analysis = m.get('MitigationAnalysis')
        if m.get('MitigationAnalysisCapacity') is not None:
            self.mitigation_analysis_capacity = m.get('MitigationAnalysisCapacity')
        if m.get('MitigationCapacity') is not None:
            self.mitigation_capacity = m.get('MitigationCapacity')
        if m.get('MitigationNums') is not None:
            self.mitigation_nums = m.get('MitigationNums')
        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')
        return self


class ListInstanceResponseBodyDataInstances(TeaModel):
    def __init__(self, comment=None, gmt_create=None, gmt_expire=None, gmt_modify=None, instance_id=None,
                 message=None, name=None, sale_id=None, spec=None, status=None, user_id=None):
        self.comment = comment  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_expire = gmt_expire  # type: str
        self.gmt_modify = gmt_modify  # type: str
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.sale_id = sale_id  # type: str
        self.spec = spec  # type: ListInstanceResponseBodyDataInstancesSpec
        self.status = status  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBodyDataInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Spec') is not None:
            temp_model = ListInstanceResponseBodyDataInstancesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListInstanceResponseBodyData(TeaModel):
    def __init__(self, instances=None, num=None, page=None, total=None):
        self.instances = instances  # type: list[ListInstanceResponseBodyDataInstances]
        self.num = num  # type: long
        self.page = page  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: long
        self.data = data  # type: list[ListInstanceResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNetListRequest(TeaModel):
    def __init__(self, main_net=None, mode=None, net=None, num=None, page=None, sale_id=None):
        self.main_net = main_net  # type: str
        self.mode = mode  # type: str
        self.net = net  # type: str
        self.num = num  # type: long
        self.page = page  # type: long
        self.sale_id = sale_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNetListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_net is not None:
            result['MainNet'] = self.main_net
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.net is not None:
            result['Net'] = self.net
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MainNet') is not None:
            self.main_net = m.get('MainNet')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh(TeaModel):
    def __init__(self, mbps=None, pps=None):
        # Mbps。
        self.mbps = mbps  # type: int
        # Pps。
        self.pps = pps  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy(TeaModel):
    def __init__(self, policy_name=None):
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh(TeaModel):
    def __init__(self, thresh_mbps=None):
        self.thresh_mbps = thresh_mbps  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.thresh_mbps is not None:
            result['ThreshMbps'] = self.thresh_mbps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ThreshMbps') is not None:
            self.thresh_mbps = m.get('ThreshMbps')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefense(TeaModel):
    def __init__(self, clean_th=None, dj_policy=None, hole_th=None):
        self.clean_th = clean_th  # type: QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh
        self.dj_policy = dj_policy  # type: QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy
        self.hole_th = hole_th  # type: QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh

    def validate(self):
        if self.clean_th:
            self.clean_th.validate()
        if self.dj_policy:
            self.dj_policy.validate()
        if self.hole_th:
            self.hole_th.validate()

    def to_map(self):
        _map = super(QueryNetListResponseBodyDataNetsDDoSDefense, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clean_th is not None:
            result['CleanTh'] = self.clean_th.to_map()
        if self.dj_policy is not None:
            result['DjPolicy'] = self.dj_policy.to_map()
        if self.hole_th is not None:
            result['HoleTh'] = self.hole_th.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CleanTh') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh()
            self.clean_th = temp_model.from_map(m['CleanTh'])
        if m.get('DjPolicy') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy()
            self.dj_policy = temp_model.from_map(m['DjPolicy'])
        if m.get('HoleTh') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh()
            self.hole_th = temp_model.from_map(m['HoleTh'])
        return self


class QueryNetListResponseBodyDataNetsDeclared(TeaModel):
    def __init__(self, declared=None, region=None):
        self.declared = declared  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNetListResponseBodyDataNetsDeclared, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.declared is not None:
            result['Declared'] = self.declared
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Declared') is not None:
            self.declared = m.get('Declared')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryNetListResponseBodyDataNets(TeaModel):
    def __init__(self, ddo_sdefense=None, declared=None, declared_state=None, fwd_effect=None, gmt_create=None,
                 gmt_modify=None, mode=None, net=None, net_extend=None, net_main=None, net_type=None, sale_id=None,
                 upstream_type=None, user_id=None):
        self.ddo_sdefense = ddo_sdefense  # type: QueryNetListResponseBodyDataNetsDDoSDefense
        self.declared = declared  # type: list[QueryNetListResponseBodyDataNetsDeclared]
        self.declared_state = declared_state  # type: int
        self.fwd_effect = fwd_effect  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modify = gmt_modify  # type: str
        self.mode = mode  # type: str
        self.net = net  # type: str
        self.net_extend = net_extend  # type: long
        self.net_main = net_main  # type: str
        self.net_type = net_type  # type: str
        self.sale_id = sale_id  # type: str
        self.upstream_type = upstream_type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.ddo_sdefense:
            self.ddo_sdefense.validate()
        if self.declared:
            for k in self.declared:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryNetListResponseBodyDataNets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddo_sdefense is not None:
            result['DDoSDefense'] = self.ddo_sdefense.to_map()
        result['Declared'] = []
        if self.declared is not None:
            for k in self.declared:
                result['Declared'].append(k.to_map() if k else None)
        if self.declared_state is not None:
            result['DeclaredState'] = self.declared_state
        if self.fwd_effect is not None:
            result['FwdEffect'] = self.fwd_effect
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.net is not None:
            result['Net'] = self.net
        if self.net_extend is not None:
            result['NetExtend'] = self.net_extend
        if self.net_main is not None:
            result['NetMain'] = self.net_main
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DDoSDefense') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefense()
            self.ddo_sdefense = temp_model.from_map(m['DDoSDefense'])
        self.declared = []
        if m.get('Declared') is not None:
            for k in m.get('Declared'):
                temp_model = QueryNetListResponseBodyDataNetsDeclared()
                self.declared.append(temp_model.from_map(k))
        if m.get('DeclaredState') is not None:
            self.declared_state = m.get('DeclaredState')
        if m.get('FwdEffect') is not None:
            self.fwd_effect = m.get('FwdEffect')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('NetExtend') is not None:
            self.net_extend = m.get('NetExtend')
        if m.get('NetMain') is not None:
            self.net_main = m.get('NetMain')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryNetListResponseBodyData(TeaModel):
    def __init__(self, nets=None, num=None, page=None, total=None):
        self.nets = nets  # type: list[QueryNetListResponseBodyDataNets]
        self.num = num  # type: long
        self.page = page  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.nets:
            for k in self.nets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryNetListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nets'] = []
        if self.nets is not None:
            for k in self.nets:
                result['Nets'].append(k.to_map() if k else None)
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.nets = []
        if m.get('Nets') is not None:
            for k in m.get('Nets'):
                temp_model = QueryNetListResponseBodyDataNets()
                self.nets.append(temp_model.from_map(k))
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryNetListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: long
        self.data = data  # type: list[QueryNetListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryNetListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryNetListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryNetListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryNetListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryNetListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryNetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


