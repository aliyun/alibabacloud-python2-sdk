# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddGrafanaRequest(TeaModel):
    def __init__(self, cluster_id=None, integration=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.integration = integration  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGrafanaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddGrafanaResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGrafanaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGrafanaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddGrafanaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGrafanaResponse, self).to_map()
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
            temp_model = AddGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIntegrationRequest(TeaModel):
    def __init__(self, cluster_id=None, integration=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.integration = integration  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIntegrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddIntegrationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIntegrationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIntegrationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddIntegrationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIntegrationResponse, self).to_map()
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
            temp_model = AddIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyScenarioRequest(TeaModel):
    def __init__(self, app_id=None, config=None, name=None, region_id=None, scenario=None, sign=None, sn_dump=None,
                 sn_force=None, sn_stat=None, sn_transfer=None, update_option=None):
        self.app_id = app_id  # type: str
        self.config = config  # type: dict[str, any]
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.scenario = scenario  # type: str
        self.sign = sign  # type: str
        self.sn_dump = sn_dump  # type: bool
        self.sn_force = sn_force  # type: bool
        self.sn_stat = sn_stat  # type: bool
        self.sn_transfer = sn_transfer  # type: bool
        self.update_option = update_option  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyScenarioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioShrinkRequest(TeaModel):
    def __init__(self, app_id=None, config_shrink=None, name=None, region_id=None, scenario=None, sign=None,
                 sn_dump=None, sn_force=None, sn_stat=None, sn_transfer=None, update_option=None):
        self.app_id = app_id  # type: str
        self.config_shrink = config_shrink  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.scenario = scenario  # type: str
        self.sign = sign  # type: str
        self.sn_dump = sn_dump  # type: bool
        self.sn_force = sn_force  # type: bool
        self.sn_stat = sn_stat  # type: bool
        self.sn_transfer = sn_transfer  # type: bool
        self.update_option = update_option  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyScenarioShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyScenarioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ApplyScenarioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyScenarioResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyScenarioResponse, self).to_map()
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
            temp_model = ApplyScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDataConsistencyRequest(TeaModel):
    def __init__(self, app_type=None, current_timestamp=None, pid=None, proxy_user_id=None, region_id=None):
        self.app_type = app_type  # type: str
        self.current_timestamp = current_timestamp  # type: long
        self.pid = pid  # type: str
        self.proxy_user_id = proxy_user_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDataConsistencyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckDataConsistencyResponseBody(TeaModel):
    def __init__(self, is_data_consistency=None, request_id=None):
        self.is_data_consistency = is_data_consistency  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDataConsistencyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_data_consistency is not None:
            result['IsDataConsistency'] = self.is_data_consistency
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsDataConsistency') is not None:
            self.is_data_consistency = m.get('IsDataConsistency')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDataConsistencyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckDataConsistencyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDataConsistencyResponse, self).to_map()
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
            temp_model = CheckDataConsistencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(self, deletion_task_id=None, region_id=None, role_arn=None, spiregion_id=None, service_name=None):
        self.deletion_task_id = deletion_task_id  # type: str
        self.region_id = region_id  # type: str
        self.role_arn = role_arn  # type: str
        self.spiregion_id = spiregion_id  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(TeaModel):
    def __init__(self, region=None, resources=None):
        self.region = region  # type: str
        self.resources = resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeletingResponseBody(TeaModel):
    def __init__(self, deletable=None, request_id=None, role_usages=None):
        self.deletable = deletable  # type: bool
        self.request_id = request_id  # type: str
        self.role_usages = role_usages  # type: list[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages]

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckServiceLinkedRoleForDeletingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceLinkedRoleForDeletingResponse, self).to_map()
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
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceStatusRequest(TeaModel):
    def __init__(self, region_id=None, svc_code=None):
        self.region_id = region_id  # type: str
        self.svc_code = svc_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.svc_code is not None:
            result['SvcCode'] = self.svc_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SvcCode') is not None:
            self.svc_code = m.get('SvcCode')
        return self


class CheckServiceStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckServiceStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckServiceStatusResponse, self).to_map()
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
            temp_model = CheckServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigAppRequest(TeaModel):
    def __init__(self, app_ids=None, enable=None, region_id=None):
        self.app_ids = app_ids  # type: str
        self.enable = enable  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigAppResponse, self).to_map()
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
            temp_model = ConfigAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactRequest(TeaModel):
    def __init__(self, contact_name=None, ding_robot_webhook_url=None, email=None, phone_num=None, region_id=None,
                 system_noc=None):
        self.contact_name = contact_name  # type: str
        self.ding_robot_webhook_url = ding_robot_webhook_url  # type: str
        self.email = email  # type: str
        self.phone_num = phone_num  # type: str
        self.region_id = region_id  # type: str
        self.system_noc = system_noc  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        return self


class CreateAlertContactResponseBody(TeaModel):
    def __init__(self, contact_id=None, request_id=None):
        self.contact_id = contact_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlertContactResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlertContactResponse, self).to_map()
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
            temp_model = CreateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_name=None, contact_ids=None, region_id=None):
        self.contact_group_name = contact_group_name  # type: str
        self.contact_ids = contact_ids  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAlertContactGroupResponseBody(TeaModel):
    def __init__(self, contact_group_id=None, request_id=None):
        self.contact_group_id = contact_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlertContactGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlertContactGroupResponse, self).to_map()
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
            temp_model = CreateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertTemplateRequest(TeaModel):
    def __init__(self, annotations=None, labels=None, match_expressions=None, message=None, name=None,
                 parent_id=None, region_id=None, rule=None, template_provider=None, type=None):
        self.annotations = annotations  # type: str
        self.labels = labels  # type: str
        self.match_expressions = match_expressions  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str
        self.region_id = region_id  # type: str
        self.rule = rule  # type: str
        self.template_provider = template_provider  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.template_provider is not None:
            result['TemplateProvider'] = self.template_provider
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('TemplateProvider') is not None:
            self.template_provider = m.get('TemplateProvider')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups(TeaModel):
    def __init__(self, label_match_expressions=None):
        self.label_match_expressions = label_match_expressions  # type: list[CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions]

    def validate(self):
        if self.label_match_expressions:
            for k in self.label_match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k in m.get('LabelMatchExpressions'):
                temp_model = CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k))
        return self


class CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid(TeaModel):
    def __init__(self, label_match_expression_groups=None):
        self.label_match_expression_groups = label_match_expression_groups  # type: list[CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups]

    def validate(self):
        if self.label_match_expression_groups:
            for k in self.label_match_expression_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k in m.get('LabelMatchExpressionGroups'):
                temp_model = CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k))
        return self


class CreateAlertTemplateResponseBodyAlertTemplate(TeaModel):
    def __init__(self, alert_provider=None, annotations=None, id=None, label_match_expression_grid=None,
                 labels=None, message=None, name=None, parent_id=None, public=None, rule=None, status=None,
                 template_provider=None, type=None, user_id=None):
        self.alert_provider = alert_provider  # type: str
        self.annotations = annotations  # type: dict[str, any]
        self.id = id  # type: int
        self.label_match_expression_grid = label_match_expression_grid  # type: CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid
        self.labels = labels  # type: dict[str, any]
        self.message = message  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: int
        self.public = public  # type: bool
        self.rule = rule  # type: str
        self.status = status  # type: bool
        self.template_provider = template_provider  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()

    def to_map(self):
        _map = super(CreateAlertTemplateResponseBodyAlertTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_provider is not None:
            result['AlertProvider'] = self.alert_provider
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.id is not None:
            result['Id'] = self.id
        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.public is not None:
            result['Public'] = self.public
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.status is not None:
            result['Status'] = self.status
        if self.template_provider is not None:
            result['TemplateProvider'] = self.template_provider
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertProvider') is not None:
            self.alert_provider = m.get('AlertProvider')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = CreateAlertTemplateResponseBodyAlertTemplateLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m['LabelMatchExpressionGrid'])
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateProvider') is not None:
            self.template_provider = m.get('TemplateProvider')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateAlertTemplateResponseBody(TeaModel):
    def __init__(self, alert_template=None, request_id=None):
        self.alert_template = alert_template  # type: CreateAlertTemplateResponseBodyAlertTemplate
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alert_template:
            self.alert_template.validate()

    def to_map(self):
        _map = super(CreateAlertTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_template is not None:
            result['AlertTemplate'] = self.alert_template.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertTemplate') is not None:
            temp_model = CreateAlertTemplateResponseBodyAlertTemplate()
            self.alert_template = temp_model.from_map(m['AlertTemplate'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlertTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlertTemplateResponse, self).to_map()
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
            temp_model = CreateAlertTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDispatchRuleRequest(TeaModel):
    def __init__(self, dispatch_rule=None, region_id=None):
        self.dispatch_rule = dispatch_rule  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDispatchRuleResponseBody(TeaModel):
    def __init__(self, dispatch_rule_id=None, request_id=None):
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDispatchRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDispatchRuleResponse, self).to_map()
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
            temp_model = CreateDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None, duration=None,
                 expression=None, labels=None, message=None, notify_type=None, region_id=None, type=None):
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: str
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: str
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rule=None, request_id=None):
        self.prometheus_alert_rule = prometheus_alert_rule  # type: CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePrometheusAlertRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = CreatePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRetcodeAppRequest(TeaModel):
    def __init__(self, region_id=None, retcode_app_name=None, retcode_app_type=None):
        self.region_id = region_id  # type: str
        self.retcode_app_name = retcode_app_name  # type: str
        self.retcode_app_type = retcode_app_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRetcodeAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        return self


class CreateRetcodeAppResponseBodyRetcodeAppDataBean(TeaModel):
    def __init__(self, app_id=None, pid=None):
        self.app_id = app_id  # type: long
        self.pid = pid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRetcodeAppResponseBodyRetcodeAppDataBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class CreateRetcodeAppResponseBody(TeaModel):
    def __init__(self, request_id=None, retcode_app_data_bean=None):
        self.request_id = request_id  # type: str
        self.retcode_app_data_bean = retcode_app_data_bean  # type: CreateRetcodeAppResponseBodyRetcodeAppDataBean

    def validate(self):
        if self.retcode_app_data_bean:
            self.retcode_app_data_bean.validate()

    def to_map(self):
        _map = super(CreateRetcodeAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retcode_app_data_bean is not None:
            result['RetcodeAppDataBean'] = self.retcode_app_data_bean.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetcodeAppDataBean') is not None:
            temp_model = CreateRetcodeAppResponseBodyRetcodeAppDataBean()
            self.retcode_app_data_bean = temp_model.from_map(m['RetcodeAppDataBean'])
        return self


class CreateRetcodeAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRetcodeAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRetcodeAppResponse, self).to_map()
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
            temp_model = CreateRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWehookRequest(TeaModel):
    def __init__(self, body=None, contact_name=None, http_headers=None, http_params=None, method=None,
                 region_id=None, url=None):
        self.body = body  # type: str
        self.contact_name = contact_name  # type: str
        self.http_headers = http_headers  # type: str
        self.http_params = http_params  # type: str
        self.method = method  # type: str
        self.region_id = region_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWehookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.method is not None:
            result['Method'] = self.method
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateWehookResponseBody(TeaModel):
    def __init__(self, contact_id=None, request_id=None):
        self.contact_id = contact_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWehookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWehookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWehookResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWehookResponse, self).to_map()
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
            temp_model = CreateWehookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactRequest(TeaModel):
    def __init__(self, contact_id=None, region_id=None):
        self.contact_id = contact_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertContactResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertContactResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertContactResponse, self).to_map()
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
            temp_model = DeleteAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_id=None, region_id=None):
        self.contact_group_id = contact_group_id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertContactGroupResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertContactGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertContactGroupResponse, self).to_map()
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
            temp_model = DeleteAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertRulesRequest(TeaModel):
    def __init__(self, alert_ids=None, region_id=None):
        self.alert_ids = alert_ids  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertRulesResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertRulesResponse, self).to_map()
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
            temp_model = DeleteAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertTemplateRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlertTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAlertTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAlertTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlertTemplateResponse, self).to_map()
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
            temp_model = DeleteAlertTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDispatchRuleRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDispatchRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDispatchRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDispatchRuleResponse, self).to_map()
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
            temp_model = DeleteDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGrafanaResourceRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, user_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGrafanaResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteGrafanaResourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGrafanaResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGrafanaResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGrafanaResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGrafanaResourceResponse, self).to_map()
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
            temp_model = DeleteGrafanaResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None):
        self.alert_id = alert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DeletePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePrometheusAlertRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = DeletePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRetcodeAppRequest(TeaModel):
    def __init__(self, app_id=None, region_id=None):
        self.app_id = app_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRetcodeAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteRetcodeAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRetcodeAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRetcodeAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRetcodeAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRetcodeAppResponse, self).to_map()
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
            temp_model = DeleteRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScenarioRequest(TeaModel):
    def __init__(self, region_id=None, scenario_id=None):
        self.region_id = region_id  # type: str
        self.scenario_id = scenario_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScenarioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        return self


class DeleteScenarioResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScenarioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteScenarioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteScenarioResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScenarioResponse, self).to_map()
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
            temp_model = DeleteScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTraceAppRequest(TeaModel):
    def __init__(self, app_id=None, pid=None, region_id=None, type=None):
        self.app_id = app_id  # type: str
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTraceAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteTraceAppResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTraceAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTraceAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTraceAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTraceAppResponse, self).to_map()
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
            temp_model = DeleteTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDispatchRuleRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleGroupRules(TeaModel):
    def __init__(self, group_id=None, group_interval=None, group_wait_time=None, grouping_fields=None):
        self.group_id = group_id  # type: long
        self.group_interval = group_interval  # type: long
        self.group_wait_time = group_wait_time  # type: long
        self.grouping_fields = grouping_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleGroupRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait_time is not None:
            result['GroupWaitTime'] = self.group_wait_time
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWaitTime') is not None:
            self.group_wait_time = m.get('GroupWaitTime')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups(TeaModel):
    def __init__(self, label_match_expressions=None):
        self.label_match_expressions = label_match_expressions  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions]

    def validate(self):
        if self.label_match_expressions:
            for k in self.label_match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k in m.get('LabelMatchExpressions'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid(TeaModel):
    def __init__(self, label_match_expression_groups=None):
        self.label_match_expression_groups = label_match_expression_groups  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups]

    def validate(self):
        if self.label_match_expression_groups:
            for k in self.label_match_expression_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k in m.get('LabelMatchExpressionGroups'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects(TeaModel):
    def __init__(self, name=None, notify_object_id=None, notify_type=None):
        self.name = name  # type: str
        self.notify_object_id = notify_object_id  # type: str
        self.notify_type = notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules(TeaModel):
    def __init__(self, notify_channels=None, notify_objects=None):
        self.notify_channels = notify_channels  # type: list[str]
        self.notify_objects = notify_objects  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects]

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRule(TeaModel):
    def __init__(self, group_rules=None, label_match_expression_grid=None, name=None, notify_rules=None,
                 rule_id=None, state=None):
        self.group_rules = group_rules  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleGroupRules]
        self.label_match_expression_grid = label_match_expression_grid  # type: DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid
        self.name = name  # type: str
        self.notify_rules = notify_rules  # type: list[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules]
        self.rule_id = rule_id  # type: long
        self.state = state  # type: str

    def validate(self):
        if self.group_rules:
            for k in self.group_rules:
                if k:
                    k.validate()
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()
        if self.notify_rules:
            for k in self.notify_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBodyDispatchRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GroupRules'] = []
        if self.group_rules is not None:
            for k in self.group_rules:
                result['GroupRules'].append(k.to_map() if k else None)
        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['NotifyRules'] = []
        if self.notify_rules is not None:
            for k in self.notify_rules:
                result['NotifyRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.group_rules = []
        if m.get('GroupRules') is not None:
            for k in m.get('GroupRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleGroupRules()
                self.group_rules.append(temp_model.from_map(k))
        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m['LabelMatchExpressionGrid'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.notify_rules = []
        if m.get('NotifyRules') is not None:
            for k in m.get('NotifyRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules()
                self.notify_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeDispatchRuleResponseBody(TeaModel):
    def __init__(self, dispatch_rule=None, request_id=None):
        self.dispatch_rule = dispatch_rule  # type: DescribeDispatchRuleResponseBodyDispatchRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dispatch_rule:
            self.dispatch_rule.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRule()
            self.dispatch_rule = temp_model.from_map(m['DispatchRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDispatchRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDispatchRuleResponse, self).to_map()
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
            temp_model = DescribeDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None):
        self.alert_id = alert_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rule=None, request_id=None):
        self.prometheus_alert_rule = prometheus_alert_rule  # type: DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePrometheusAlertRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = DescribePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceLicenseKeyRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTraceLicenseKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTraceLicenseKeyResponseBody(TeaModel):
    def __init__(self, license_key=None, request_id=None):
        self.license_key = license_key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTraceLicenseKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTraceLicenseKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTraceLicenseKeyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTraceLicenseKeyResponse, self).to_map()
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
            temp_model = DescribeTraceLicenseKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceLocationRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTraceLocationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTraceLocationResponseBodyRegionConfigs(TeaModel):
    def __init__(self, region_no=None, url=None):
        self.region_no = region_no  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTraceLocationResponseBodyRegionConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeTraceLocationResponseBody(TeaModel):
    def __init__(self, region_configs=None, request_id=None):
        self.region_configs = region_configs  # type: list[DescribeTraceLocationResponseBodyRegionConfigs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.region_configs:
            for k in self.region_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTraceLocationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionConfigs'] = []
        if self.region_configs is not None:
            for k in self.region_configs:
                result['RegionConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_configs = []
        if m.get('RegionConfigs') is not None:
            for k in m.get('RegionConfigs'):
                temp_model = DescribeTraceLocationResponseBodyRegionConfigs()
                self.region_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTraceLocationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTraceLocationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTraceLocationResponse, self).to_map()
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
            temp_model = DescribeTraceLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAlertTemplateRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAlertTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableAlertTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAlertTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableAlertTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableAlertTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAlertTemplateResponse, self).to_map()
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
            temp_model = DisableAlertTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAlertTemplateRequest(TeaModel):
    def __init__(self, id=None, region_id=None):
        self.id = id  # type: long
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAlertTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableAlertTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableAlertTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableAlertTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableAlertTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableAlertTemplateResponse, self).to_map()
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
            temp_model = EnableAlertTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportPrometheusRulesRequest(TeaModel):
    def __init__(self, cluster_id=None, name=None, name_space=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.name = name  # type: str
        self.name_space = name_space  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportPrometheusRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ExportPrometheusRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportPrometheusRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportPrometheusRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportPrometheusRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportPrometheusRulesResponse, self).to_map()
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
            temp_model = ExportPrometheusRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentDownloadUrlRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAgentDownloadUrlResponseBody(TeaModel):
    def __init__(self, arms_agent_download_url=None, request_id=None):
        self.arms_agent_download_url = arms_agent_download_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arms_agent_download_url is not None:
            result['ArmsAgentDownloadUrl'] = self.arms_agent_download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArmsAgentDownloadUrl') is not None:
            self.arms_agent_download_url = m.get('ArmsAgentDownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAgentDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAgentDownloadUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentDownloadUrlResponse, self).to_map()
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
            temp_model = GetAgentDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppApiByPageRequest(TeaModel):
    def __init__(self, current_page=None, end_time=None, interval_mills=None, pid=None, page_size=None,
                 region_id=None, start_time=None):
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.interval_mills = interval_mills  # type: int
        self.pid = pid  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppApiByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval_mills is not None:
            result['IntervalMills'] = self.interval_mills
        if self.pid is not None:
            result['PId'] = self.pid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntervalMills') is not None:
            self.interval_mills = m.get('IntervalMills')
        if m.get('PId') is not None:
            self.pid = m.get('PId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAppApiByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page=None, page_size=None, total=None):
        self.items = items  # type: list[dict[str, any]]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppApiByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAppApiByPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetAppApiByPageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAppApiByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAppApiByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAppApiByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppApiByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppApiByPageResponse, self).to_map()
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
            temp_model = GetAppApiByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsistencySnapshotRequest(TeaModel):
    def __init__(self, app_type=None, current_timestamp=None, pid=None, proxy_user_id=None, region_id=None):
        self.app_type = app_type  # type: str
        self.current_timestamp = current_timestamp  # type: long
        self.pid = pid  # type: str
        self.proxy_user_id = proxy_user_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsistencySnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetConsistencySnapshotResponseBody(TeaModel):
    def __init__(self, consistency_result_json_str=None, request_id=None):
        self.consistency_result_json_str = consistency_result_json_str  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConsistencySnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistency_result_json_str is not None:
            result['ConsistencyResultJsonStr'] = self.consistency_result_json_str
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsistencyResultJsonStr') is not None:
            self.consistency_result_json_str = m.get('ConsistencyResultJsonStr')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConsistencySnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConsistencySnapshotResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConsistencySnapshotResponse, self).to_map()
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
            temp_model = GetConsistencySnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntegrationTokenRequest(TeaModel):
    def __init__(self, product_type=None, region_id=None):
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntegrationTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIntegrationTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        self.request_id = request_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntegrationTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetIntegrationTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIntegrationTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIntegrationTokenResponse, self).to_map()
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
            temp_model = GetIntegrationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultipleTraceRequest(TeaModel):
    def __init__(self, region_id=None, trace_ids=None):
        self.region_id = region_id  # type: str
        self.trace_ids = trace_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultipleTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_ids is not None:
            result['TraceIDs'] = self.trace_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceIDs') is not None:
            self.trace_ids = m.get('TraceIDs')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList(TeaModel):
    def __init__(self, tag_entry_list=None, timestamp=None):
        self.tag_entry_list = tag_entry_list  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList]
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpans(TeaModel):
    def __init__(self, duration=None, have_stack=None, log_event_list=None, operation_name=None,
                 parent_span_id=None, result_code=None, rpc_id=None, rpc_type=None, service_ip=None, service_name=None,
                 span_id=None, tag_entry_list=None, timestamp=None, trace_id=None):
        self.duration = duration  # type: long
        self.have_stack = have_stack  # type: bool
        self.log_event_list = log_event_list  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList]
        self.operation_name = operation_name  # type: str
        self.parent_span_id = parent_span_id  # type: str
        self.result_code = result_code  # type: str
        self.rpc_id = rpc_id  # type: str
        self.rpc_type = rpc_type  # type: int
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.span_id = span_id  # type: str
        self.tag_entry_list = tag_entry_list  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList]
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfosSpans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfos(TeaModel):
    def __init__(self, spans=None, trace_id=None):
        self.spans = spans  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfosSpans]
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBodyMultiCallChainInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpans()
                self.spans.append(temp_model.from_map(k))
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBody(TeaModel):
    def __init__(self, multi_call_chain_infos=None, request_id=None):
        self.multi_call_chain_infos = multi_call_chain_infos  # type: list[GetMultipleTraceResponseBodyMultiCallChainInfos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.multi_call_chain_infos:
            for k in self.multi_call_chain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MultiCallChainInfos'] = []
        if self.multi_call_chain_infos is not None:
            for k in self.multi_call_chain_infos:
                result['MultiCallChainInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.multi_call_chain_infos = []
        if m.get('MultiCallChainInfos') is not None:
            for k in m.get('MultiCallChainInfos'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfos()
                self.multi_call_chain_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMultipleTraceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMultipleTraceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMultipleTraceResponse, self).to_map()
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
            temp_model = GetMultipleTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrometheusApiTokenRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrometheusApiTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPrometheusApiTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        self.request_id = request_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPrometheusApiTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetPrometheusApiTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPrometheusApiTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPrometheusApiTokenResponse, self).to_map()
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
            temp_model = GetPrometheusApiTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRetcodeShareUrlRequest(TeaModel):
    def __init__(self, pid=None):
        self.pid = pid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRetcodeShareUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetRetcodeShareUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, url=None):
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRetcodeShareUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetRetcodeShareUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRetcodeShareUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRetcodeShareUrlResponse, self).to_map()
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
            temp_model = GetRetcodeShareUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackRequest(TeaModel):
    def __init__(self, end_time=None, pid=None, region_id=None, rpc_id=None, start_time=None, trace_id=None):
        self.end_time = end_time  # type: long
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.rpc_id = rpc_id  # type: str
        self.start_time = start_time  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rpc_id is not None:
            result['RpcID'] = self.rpc_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RpcID') is not None:
            self.rpc_id = m.get('RpcID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetStackResponseBodyStackInfoExtInfo(TeaModel):
    def __init__(self, info=None, type=None):
        self.info = info  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStackResponseBodyStackInfoExtInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetStackResponseBodyStackInfo(TeaModel):
    def __init__(self, api=None, duration=None, exception=None, ext_info=None, line=None, rpc_id=None,
                 service_name=None, start_time=None):
        self.api = api  # type: str
        self.duration = duration  # type: long
        self.exception = exception  # type: str
        self.ext_info = ext_info  # type: GetStackResponseBodyStackInfoExtInfo
        self.line = line  # type: str
        self.rpc_id = rpc_id  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        _map = super(GetStackResponseBodyStackInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()
        if self.line is not None:
            result['Line'] = self.line
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('ExtInfo') is not None:
            temp_model = GetStackResponseBodyStackInfoExtInfo()
            self.ext_info = temp_model.from_map(m['ExtInfo'])
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetStackResponseBody(TeaModel):
    def __init__(self, request_id=None, stack_info=None):
        self.request_id = request_id  # type: str
        self.stack_info = stack_info  # type: list[GetStackResponseBodyStackInfo]

    def validate(self):
        if self.stack_info:
            for k in self.stack_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetStackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackInfo'] = []
        if self.stack_info is not None:
            for k in self.stack_info:
                result['StackInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_info = []
        if m.get('StackInfo') is not None:
            for k in m.get('StackInfo'):
                temp_model = GetStackResponseBodyStackInfo()
                self.stack_info.append(temp_model.from_map(k))
        return self


class GetStackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStackResponse, self).to_map()
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
            temp_model = GetStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(self, region_id=None, trace_id=None):
        self.region_id = region_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodySpansLogEventListTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodySpansLogEventListTagEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTraceResponseBodySpansLogEventList(TeaModel):
    def __init__(self, tag_entry_list=None, timestamp=None):
        self.tag_entry_list = tag_entry_list  # type: list[GetTraceResponseBodySpansLogEventListTagEntryList]
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansLogEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpansTagEntryList(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodySpansTagEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTraceResponseBodySpans(TeaModel):
    def __init__(self, duration=None, have_stack=None, log_event_list=None, operation_name=None,
                 parent_span_id=None, result_code=None, rpc_id=None, rpc_type=None, service_ip=None, service_name=None,
                 span_id=None, tag_entry_list=None, timestamp=None, trace_id=None):
        self.duration = duration  # type: long
        self.have_stack = have_stack  # type: bool
        self.log_event_list = log_event_list  # type: list[GetTraceResponseBodySpansLogEventList]
        self.operation_name = operation_name  # type: str
        self.parent_span_id = parent_span_id  # type: str
        self.result_code = result_code  # type: str
        self.rpc_id = rpc_id  # type: str
        self.rpc_type = rpc_type  # type: int
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.span_id = span_id  # type: str
        self.tag_entry_list = tag_entry_list  # type: list[GetTraceResponseBodySpansTagEntryList]
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetTraceResponseBodySpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(self, request_id=None, spans=None):
        self.request_id = request_id  # type: str
        self.spans = spans  # type: list[GetTraceResponseBodySpans]

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetTraceResponseBodySpans()
                self.spans.append(temp_model.from_map(k))
        return self


class GetTraceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTraceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTraceResponse, self).to_map()
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
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceAppRequest(TeaModel):
    def __init__(self, pid=None, region_id=None):
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceAppResponseBodyTraceApp(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceAppResponseBodyTraceApp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetTraceAppResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_app=None):
        self.request_id = request_id  # type: str
        self.trace_app = trace_app  # type: GetTraceAppResponseBodyTraceApp

    def validate(self):
        if self.trace_app:
            self.trace_app.validate()

    def to_map(self):
        _map = super(GetTraceAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_app is not None:
            result['TraceApp'] = self.trace_app.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceApp') is not None:
            temp_model = GetTraceAppResponseBodyTraceApp()
            self.trace_app = temp_model.from_map(m['TraceApp'])
        return self


class GetTraceAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTraceAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTraceAppResponse, self).to_map()
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
            temp_model = GetTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportAppAlertRulesRequest(TeaModel):
    def __init__(self, contact_group_ids=None, is_auto_start=None, pids=None, region_id=None,
                 templage_alert_config=None, template_alert_id=None):
        self.contact_group_ids = contact_group_ids  # type: str
        self.is_auto_start = is_auto_start  # type: bool
        self.pids = pids  # type: str
        self.region_id = region_id  # type: str
        self.templage_alert_config = templage_alert_config  # type: str
        self.template_alert_id = template_alert_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportAppAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        if self.template_alert_id is not None:
            result['TemplateAlertId'] = self.template_alert_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        if m.get('TemplateAlertId') is not None:
            self.template_alert_id = m.get('TemplateAlertId')
        return self


class ImportAppAlertRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportAppAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportAppAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportAppAlertRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportAppAlertRulesResponse, self).to_map()
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
            temp_model = ImportAppAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportCustomAlertRulesRequest(TeaModel):
    def __init__(self, contact_group_ids=None, is_auto_start=None, region_id=None, templage_alert_config=None,
                 template_alert_config=None):
        self.contact_group_ids = contact_group_ids  # type: str
        self.is_auto_start = is_auto_start  # type: bool
        self.region_id = region_id  # type: str
        self.templage_alert_config = templage_alert_config  # type: str
        self.template_alert_config = template_alert_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportCustomAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        if self.template_alert_config is not None:
            result['TemplateAlertConfig'] = self.template_alert_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        if m.get('TemplateAlertConfig') is not None:
            self.template_alert_config = m.get('TemplateAlertConfig')
        return self


class ImportCustomAlertRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportCustomAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportCustomAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportCustomAlertRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportCustomAlertRulesResponse, self).to_map()
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
            temp_model = ImportCustomAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportPrometheusRulesRequest(TeaModel):
    def __init__(self, cluster_id=None, content=None, name=None, name_space=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.content = content  # type: str
        self.name = name  # type: str
        self.name_space = name_space  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportPrometheusRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ImportPrometheusRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportPrometheusRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportPrometheusRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportPrometheusRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportPrometheusRulesResponse, self).to_map()
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
            temp_model = ImportPrometheusRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListActivatedAlertsRequest(TeaModel):
    def __init__(self, current_page=None, filter=None, page_size=None, region_id=None):
        self.current_page = current_page  # type: int
        self.filter = filter  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListActivatedAlertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListActivatedAlertsResponseBodyPageAlertsDispatchRules(TeaModel):
    def __init__(self, rule_id=None, rule_name=None):
        self.rule_id = rule_id  # type: int
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBodyPageAlertsDispatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListActivatedAlertsResponseBodyPageAlerts(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, alert_type=None, count=None, create_time=None,
                 dispatch_rules=None, ends_at=None, expand_fields=None, integration_name=None, integration_type=None,
                 involved_object_kind=None, involved_object_name=None, message=None, severity=None, starts_at=None, status=None):
        self.alert_id = alert_id  # type: str
        self.alert_name = alert_name  # type: str
        self.alert_type = alert_type  # type: str
        self.count = count  # type: int
        self.create_time = create_time  # type: long
        self.dispatch_rules = dispatch_rules  # type: list[ListActivatedAlertsResponseBodyPageAlertsDispatchRules]
        self.ends_at = ends_at  # type: long
        self.expand_fields = expand_fields  # type: dict[str, any]
        self.integration_name = integration_name  # type: str
        self.integration_type = integration_type  # type: str
        self.involved_object_kind = involved_object_kind  # type: str
        self.involved_object_name = involved_object_name  # type: str
        self.message = message  # type: str
        self.severity = severity  # type: str
        self.starts_at = starts_at  # type: long
        self.status = status  # type: str

    def validate(self):
        if self.dispatch_rules:
            for k in self.dispatch_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBodyPageAlerts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k in self.dispatch_rules:
                result['DispatchRules'].append(k.to_map() if k else None)
        if self.ends_at is not None:
            result['EndsAt'] = self.ends_at
        if self.expand_fields is not None:
            result['ExpandFields'] = self.expand_fields
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.involved_object_kind is not None:
            result['InvolvedObjectKind'] = self.involved_object_kind
        if self.involved_object_name is not None:
            result['InvolvedObjectName'] = self.involved_object_name
        if self.message is not None:
            result['Message'] = self.message
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.starts_at is not None:
            result['StartsAt'] = self.starts_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k in m.get('DispatchRules'):
                temp_model = ListActivatedAlertsResponseBodyPageAlertsDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k))
        if m.get('EndsAt') is not None:
            self.ends_at = m.get('EndsAt')
        if m.get('ExpandFields') is not None:
            self.expand_fields = m.get('ExpandFields')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('InvolvedObjectKind') is not None:
            self.involved_object_kind = m.get('InvolvedObjectKind')
        if m.get('InvolvedObjectName') is not None:
            self.involved_object_name = m.get('InvolvedObjectName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartsAt') is not None:
            self.starts_at = m.get('StartsAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListActivatedAlertsResponseBodyPage(TeaModel):
    def __init__(self, alerts=None, page=None, page_size=None, total=None):
        self.alerts = alerts  # type: list[ListActivatedAlertsResponseBodyPageAlerts]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.alerts:
            for k in self.alerts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBodyPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alerts'] = []
        if self.alerts is not None:
            for k in self.alerts:
                result['Alerts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alerts = []
        if m.get('Alerts') is not None:
            for k in m.get('Alerts'):
                temp_model = ListActivatedAlertsResponseBodyPageAlerts()
                self.alerts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListActivatedAlertsResponseBody(TeaModel):
    def __init__(self, page=None, request_id=None):
        self.page = page  # type: ListActivatedAlertsResponseBodyPage
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListActivatedAlertsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListActivatedAlertsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListActivatedAlertsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListActivatedAlertsResponse, self).to_map()
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
            temp_model = ListActivatedAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertTemplatesRequest(TeaModel):
    def __init__(self, alert_provider=None, labels=None, name=None, region_id=None, status=None,
                 template_provider=None, type=None):
        self.alert_provider = alert_provider  # type: str
        self.labels = labels  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: bool
        self.template_provider = template_provider  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_provider is not None:
            result['AlertProvider'] = self.alert_provider
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_provider is not None:
            result['TemplateProvider'] = self.template_provider
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertProvider') is not None:
            self.alert_provider = m.get('AlertProvider')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateProvider') is not None:
            self.template_provider = m.get('TemplateProvider')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(TeaModel):
    def __init__(self, key=None, operator=None, value=None):
        self.key = key  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroups(TeaModel):
    def __init__(self, label_match_expressions=None):
        self.label_match_expressions = label_match_expressions  # type: list[ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions]

    def validate(self):
        if self.label_match_expressions:
            for k in self.label_match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k in m.get('LabelMatchExpressions'):
                temp_model = ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k))
        return self


class ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGrid(TeaModel):
    def __init__(self, label_match_expression_groups=None):
        self.label_match_expression_groups = label_match_expression_groups  # type: list[ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroups]

    def validate(self):
        if self.label_match_expression_groups:
            for k in self.label_match_expression_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGrid, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k in m.get('LabelMatchExpressionGroups'):
                temp_model = ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k))
        return self


class ListAlertTemplatesResponseBodyAlertTemplates(TeaModel):
    def __init__(self, alert_provider=None, annotations=None, id=None, label_match_expression_grid=None,
                 labels=None, message=None, name=None, parent_id=None, public=None, rule=None, status=None,
                 template_provider=None, type=None, user_id=None):
        self.alert_provider = alert_provider  # type: str
        self.annotations = annotations  # type: dict[str, any]
        self.id = id  # type: int
        self.label_match_expression_grid = label_match_expression_grid  # type: ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGrid
        self.labels = labels  # type: dict[str, any]
        self.message = message  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: int
        self.public = public  # type: bool
        self.rule = rule  # type: str
        self.status = status  # type: bool
        self.template_provider = template_provider  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()

    def to_map(self):
        _map = super(ListAlertTemplatesResponseBodyAlertTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_provider is not None:
            result['AlertProvider'] = self.alert_provider
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.id is not None:
            result['Id'] = self.id
        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.public is not None:
            result['Public'] = self.public
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.status is not None:
            result['Status'] = self.status
        if self.template_provider is not None:
            result['TemplateProvider'] = self.template_provider
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertProvider') is not None:
            self.alert_provider = m.get('AlertProvider')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = ListAlertTemplatesResponseBodyAlertTemplatesLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m['LabelMatchExpressionGrid'])
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Public') is not None:
            self.public = m.get('Public')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateProvider') is not None:
            self.template_provider = m.get('TemplateProvider')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAlertTemplatesResponseBody(TeaModel):
    def __init__(self, alert_templates=None, request_id=None):
        self.alert_templates = alert_templates  # type: list[ListAlertTemplatesResponseBodyAlertTemplates]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alert_templates:
            for k in self.alert_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertTemplates'] = []
        if self.alert_templates is not None:
            for k in self.alert_templates:
                result['AlertTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_templates = []
        if m.get('AlertTemplates') is not None:
            for k in m.get('AlertTemplates'):
                temp_model = ListAlertTemplatesResponseBodyAlertTemplates()
                self.alert_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlertTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAlertTemplatesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlertTemplatesResponse, self).to_map()
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
            temp_model = ListAlertTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterFromGrafanaRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterFromGrafanaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClusterFromGrafanaResponseBodyPromClusterList(TeaModel):
    def __init__(self, agent_status=None, cluster_id=None, cluster_name=None, cluster_type=None, controller_id=None,
                 create_time=None, extra=None, id=None, install_time=None, is_controller_installed=None,
                 last_heart_beat_time=None, node_num=None, options=None, plugins_json_array=None, region_id=None, state_json=None,
                 update_time=None, user_id=None):
        self.agent_status = agent_status  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.controller_id = controller_id  # type: str
        self.create_time = create_time  # type: long
        self.extra = extra  # type: str
        self.id = id  # type: long
        self.install_time = install_time  # type: long
        self.is_controller_installed = is_controller_installed  # type: bool
        self.last_heart_beat_time = last_heart_beat_time  # type: long
        self.node_num = node_num  # type: int
        self.options = options  # type: str
        self.plugins_json_array = plugins_json_array  # type: str
        self.region_id = region_id  # type: str
        self.state_json = state_json  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterFromGrafanaResponseBodyPromClusterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.id is not None:
            result['Id'] = self.id
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.options is not None:
            result['Options'] = self.options
        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state_json is not None:
            result['StateJson'] = self.state_json
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListClusterFromGrafanaResponseBody(TeaModel):
    def __init__(self, prom_cluster_list=None, request_id=None):
        self.prom_cluster_list = prom_cluster_list  # type: list[ListClusterFromGrafanaResponseBodyPromClusterList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prom_cluster_list:
            for k in self.prom_cluster_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterFromGrafanaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k in self.prom_cluster_list:
                result['PromClusterList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k in m.get('PromClusterList'):
                temp_model = ListClusterFromGrafanaResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterFromGrafanaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterFromGrafanaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterFromGrafanaResponse, self).to_map()
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
            temp_model = ListClusterFromGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardsRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, product=None, recreate_switch=None, region_id=None,
                 title=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.product = product  # type: str
        self.recreate_switch = recreate_switch  # type: bool
        self.region_id = region_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.product is not None:
            result['Product'] = self.product
        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListDashboardsResponseBodyDashboardVos(TeaModel):
    def __init__(self, dashboard_type=None, exporter=None, id=None, is_arms_exporter=None, kind=None, name=None,
                 need_update=None, tags=None, time=None, title=None, type=None, uid=None, url=None, version=None):
        self.dashboard_type = dashboard_type  # type: str
        self.exporter = exporter  # type: str
        self.id = id  # type: str
        self.is_arms_exporter = is_arms_exporter  # type: bool
        self.kind = kind  # type: str
        self.name = name  # type: str
        self.need_update = need_update  # type: bool
        self.tags = tags  # type: list[str]
        self.time = time  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.uid = uid  # type: str
        self.url = url  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDashboardsResponseBodyDashboardVos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type
        if self.exporter is not None:
            result['Exporter'] = self.exporter
        if self.id is not None:
            result['Id'] = self.id
        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.time is not None:
            result['Time'] = self.time
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')
        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDashboardsResponseBody(TeaModel):
    def __init__(self, dashboard_vos=None, request_id=None):
        self.dashboard_vos = dashboard_vos  # type: list[ListDashboardsResponseBodyDashboardVos]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dashboard_vos:
            for k in self.dashboard_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDashboardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DashboardVos'] = []
        if self.dashboard_vos is not None:
            for k in self.dashboard_vos:
                result['DashboardVos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dashboard_vos = []
        if m.get('DashboardVos') is not None:
            for k in m.get('DashboardVos'):
                temp_model = ListDashboardsResponseBodyDashboardVos()
                self.dashboard_vos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDashboardsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDashboardsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDashboardsResponse, self).to_map()
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
            temp_model = ListDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDispatchRuleRequest(TeaModel):
    def __init__(self, name=None, region_id=None, system=None):
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.system = system  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system is not None:
            result['System'] = self.system
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('System') is not None:
            self.system = m.get('System')
        return self


class ListDispatchRuleResponseBodyDispatchRules(TeaModel):
    def __init__(self, name=None, rule_id=None, state=None):
        self.name = name  # type: str
        self.rule_id = rule_id  # type: long
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDispatchRuleResponseBodyDispatchRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListDispatchRuleResponseBody(TeaModel):
    def __init__(self, dispatch_rules=None, request_id=None):
        self.dispatch_rules = dispatch_rules  # type: list[ListDispatchRuleResponseBodyDispatchRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dispatch_rules:
            for k in self.dispatch_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k in self.dispatch_rules:
                result['DispatchRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k in m.get('DispatchRules'):
                temp_model = ListDispatchRuleResponseBodyDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDispatchRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDispatchRuleResponse, self).to_map()
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
            temp_model = ListDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPromClustersRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPromClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPromClustersResponseBodyPromClusterList(TeaModel):
    def __init__(self, agent_status=None, cluster_id=None, cluster_name=None, cluster_type=None, controller_id=None,
                 create_time=None, extra=None, id=None, install_time=None, is_controller_installed=None,
                 last_heart_beat_time=None, node_num=None, options=None, plugins_json_array=None, region_id=None, state_json=None,
                 update_time=None, user_id=None):
        self.agent_status = agent_status  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.controller_id = controller_id  # type: str
        self.create_time = create_time  # type: long
        self.extra = extra  # type: str
        self.id = id  # type: long
        self.install_time = install_time  # type: long
        self.is_controller_installed = is_controller_installed  # type: bool
        self.last_heart_beat_time = last_heart_beat_time  # type: long
        self.node_num = node_num  # type: int
        self.options = options  # type: str
        self.plugins_json_array = plugins_json_array  # type: str
        self.region_id = region_id  # type: str
        self.state_json = state_json  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPromClustersResponseBodyPromClusterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.id is not None:
            result['Id'] = self.id
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.options is not None:
            result['Options'] = self.options
        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state_json is not None:
            result['StateJson'] = self.state_json
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListPromClustersResponseBody(TeaModel):
    def __init__(self, prom_cluster_list=None, request_id=None):
        self.prom_cluster_list = prom_cluster_list  # type: list[ListPromClustersResponseBodyPromClusterList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prom_cluster_list:
            for k in self.prom_cluster_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPromClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k in self.prom_cluster_list:
                result['PromClusterList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k in m.get('PromClusterList'):
                temp_model = ListPromClustersResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPromClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPromClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPromClustersResponse, self).to_map()
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
            temp_model = ListPromClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusAlertRulesRequest(TeaModel):
    def __init__(self, cluster_id=None, match_expressions=None, name=None, region_id=None, status=None, type=None):
        self.cluster_id = cluster_id  # type: str
        self.match_expressions = match_expressions  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRules(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBodyPrometheusAlertRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPrometheusAlertRulesResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rules=None, request_id=None):
        self.prometheus_alert_rules = prometheus_alert_rules  # type: list[ListPrometheusAlertRulesResponseBodyPrometheusAlertRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rules:
            for k in self.prometheus_alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrometheusAlertRules'] = []
        if self.prometheus_alert_rules is not None:
            for k in self.prometheus_alert_rules:
                result['PrometheusAlertRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prometheus_alert_rules = []
        if m.get('PrometheusAlertRules') is not None:
            for k in m.get('PrometheusAlertRules'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRules()
                self.prometheus_alert_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrometheusAlertRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertRulesResponse, self).to_map()
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
            temp_model = ListPrometheusAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusAlertTemplatesRequest(TeaModel):
    def __init__(self, cluster_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates(TeaModel):
    def __init__(self, alert_name=None, annotations=None, description=None, duration=None, expression=None,
                 labels=None, type=None, version=None):
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations]
        self.description = description  # type: str
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels]
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPrometheusAlertTemplatesResponseBody(TeaModel):
    def __init__(self, prometheus_alert_templates=None, request_id=None):
        self.prometheus_alert_templates = prometheus_alert_templates  # type: list[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_templates:
            for k in self.prometheus_alert_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrometheusAlertTemplates'] = []
        if self.prometheus_alert_templates is not None:
            for k in self.prometheus_alert_templates:
                result['PrometheusAlertTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prometheus_alert_templates = []
        if m.get('PrometheusAlertTemplates') is not None:
            for k in m.get('PrometheusAlertTemplates'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates()
                self.prometheus_alert_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusAlertTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPrometheusAlertTemplatesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPrometheusAlertTemplatesResponse, self).to_map()
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
            temp_model = ListPrometheusAlertTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRetcodeAppsRequest(TeaModel):
    def __init__(self, region_id=None, security_token=None):
        self.region_id = region_id  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRetcodeAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListRetcodeAppsResponseBodyRetcodeApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, pid=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.pid = pid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRetcodeAppsResponseBodyRetcodeApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class ListRetcodeAppsResponseBody(TeaModel):
    def __init__(self, request_id=None, retcode_apps=None):
        self.request_id = request_id  # type: str
        self.retcode_apps = retcode_apps  # type: list[ListRetcodeAppsResponseBodyRetcodeApps]

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRetcodeAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = ListRetcodeAppsResponseBodyRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        return self


class ListRetcodeAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRetcodeAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRetcodeAppsResponse, self).to_map()
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
            temp_model = ListRetcodeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenarioRequest(TeaModel):
    def __init__(self, app_id=None, name=None, region_id=None, scenario=None, sign=None):
        self.app_id = app_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.scenario = scenario  # type: str
        self.sign = sign  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScenarioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class ListScenarioResponseBodyArmsScenarios(TeaModel):
    def __init__(self, app_id=None, create_time=None, extensions=None, id=None, name=None, region_id=None, sign=None,
                 update_time=None, user_id=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: str
        self.extensions = extensions  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.sign = sign  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScenarioResponseBodyArmsScenarios, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListScenarioResponseBody(TeaModel):
    def __init__(self, arms_scenarios=None, request_id=None):
        self.arms_scenarios = arms_scenarios  # type: list[ListScenarioResponseBodyArmsScenarios]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.arms_scenarios:
            for k in self.arms_scenarios:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListScenarioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ArmsScenarios'] = []
        if self.arms_scenarios is not None:
            for k in self.arms_scenarios:
                result['ArmsScenarios'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.arms_scenarios = []
        if m.get('ArmsScenarios') is not None:
            for k in m.get('ArmsScenarios'):
                temp_model = ListScenarioResponseBodyArmsScenarios()
                self.arms_scenarios.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListScenarioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListScenarioResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListScenarioResponse, self).to_map()
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
            temp_model = ListScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerlessTopNAppsRequest(TeaModel):
    def __init__(self, end_time=None, limit=None, order_by=None, region_id=None, start_time=None):
        self.end_time = end_time  # type: long
        self.limit = limit  # type: int
        self.order_by = order_by  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerlessTopNAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListServerlessTopNAppsResponseBodyData(TeaModel):
    def __init__(self, count=None, error=None, name=None, pid=None, region=None, rt=None):
        self.count = count  # type: int
        self.error = error  # type: int
        self.name = name  # type: str
        self.pid = pid  # type: str
        self.region = region  # type: str
        self.rt = rt  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerlessTopNAppsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.error is not None:
            result['Error'] = self.error
        if self.name is not None:
            result['Name'] = self.name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region is not None:
            result['Region'] = self.region
        if self.rt is not None:
            result['Rt'] = self.rt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        return self


class ListServerlessTopNAppsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListServerlessTopNAppsResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServerlessTopNAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListServerlessTopNAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListServerlessTopNAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServerlessTopNAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServerlessTopNAppsResponse, self).to_map()
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
            temp_model = ListServerlessTopNAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTraceAppsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTraceAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListTraceAppsResponseBodyTraceApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTraceAppsResponseBodyTraceApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListTraceAppsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, trace_apps=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_apps = trace_apps  # type: list[ListTraceAppsResponseBodyTraceApps]

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTraceAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = ListTraceAppsResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class ListTraceAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTraceAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTraceAppsResponse, self).to_map()
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
            temp_model = ListTraceAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsDefaultSLRRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsDefaultSLRRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenArmsDefaultSLRResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsDefaultSLRResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenArmsDefaultSLRResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenArmsDefaultSLRResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenArmsDefaultSLRResponse, self).to_map()
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
            temp_model = OpenArmsDefaultSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsServiceRequest(TeaModel):
    def __init__(self, owner_id=None, type=None):
        self.owner_id = owner_id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenArmsServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenArmsServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenArmsServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenArmsServiceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenArmsServiceResponse, self).to_map()
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
            temp_model = OpenArmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenVClusterRequest(TeaModel):
    def __init__(self, cluster_type=None, length=None, product=None, recreate_switch=None, region_id=None):
        self.cluster_type = cluster_type  # type: str
        self.length = length  # type: int
        self.product = product  # type: str
        self.recreate_switch = recreate_switch  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenVClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.length is not None:
            result['Length'] = self.length
        if self.product is not None:
            result['Product'] = self.product
        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenVClusterResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenVClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenVClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenVClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenVClusterResponse, self).to_map()
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
            temp_model = OpenVClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenXtraceDefaultSLRRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenXtraceDefaultSLRRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenXtraceDefaultSLRResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenXtraceDefaultSLRResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenXtraceDefaultSLRResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenXtraceDefaultSLRResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenXtraceDefaultSLRResponse, self).to_map()
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
            temp_model = OpenXtraceDefaultSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetRequestDimensions(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetRequestDimensions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequestOptionalDims(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetRequestOptionalDims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequestRequiredDims(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetRequestRequiredDims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequest(TeaModel):
    def __init__(self, dataset_id=None, date_str=None, dimensions=None, hungry_mode=None, interval_in_sec=None,
                 is_drill_down=None, limit=None, max_time=None, measures=None, min_time=None, optional_dims=None,
                 order_by_key=None, proxy_user_id=None, reduce_tail=None, required_dims=None):
        self.dataset_id = dataset_id  # type: long
        self.date_str = date_str  # type: str
        self.dimensions = dimensions  # type: list[QueryDatasetRequestDimensions]
        self.hungry_mode = hungry_mode  # type: bool
        self.interval_in_sec = interval_in_sec  # type: int
        self.is_drill_down = is_drill_down  # type: bool
        self.limit = limit  # type: int
        self.max_time = max_time  # type: long
        self.measures = measures  # type: list[str]
        self.min_time = min_time  # type: long
        self.optional_dims = optional_dims  # type: list[QueryDatasetRequestOptionalDims]
        self.order_by_key = order_by_key  # type: str
        self.proxy_user_id = proxy_user_id  # type: str
        self.reduce_tail = reduce_tail  # type: bool
        self.required_dims = required_dims  # type: list[QueryDatasetRequestRequiredDims]

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.optional_dims:
            for k in self.optional_dims:
                if k:
                    k.validate()
        if self.required_dims:
            for k in self.required_dims:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.date_str is not None:
            result['DateStr'] = self.date_str
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.hungry_mode is not None:
            result['HungryMode'] = self.hungry_mode
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.is_drill_down is not None:
            result['IsDrillDown'] = self.is_drill_down
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        result['OptionalDims'] = []
        if self.optional_dims is not None:
            for k in self.optional_dims:
                result['OptionalDims'].append(k.to_map() if k else None)
        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail
        result['RequiredDims'] = []
        if self.required_dims is not None:
            for k in self.required_dims:
                result['RequiredDims'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = QueryDatasetRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('HungryMode') is not None:
            self.hungry_mode = m.get('HungryMode')
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('IsDrillDown') is not None:
            self.is_drill_down = m.get('IsDrillDown')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        self.optional_dims = []
        if m.get('OptionalDims') is not None:
            for k in m.get('OptionalDims'):
                temp_model = QueryDatasetRequestOptionalDims()
                self.optional_dims.append(temp_model.from_map(k))
        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')
        self.required_dims = []
        if m.get('RequiredDims') is not None:
            for k in m.get('RequiredDims'):
                temp_model = QueryDatasetRequestRequiredDims()
                self.required_dims.append(temp_model.from_map(k))
        return self


class QueryDatasetResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDatasetResponse, self).to_map()
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
            temp_model = QueryDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryMetricRequest(TeaModel):
    def __init__(self, consistency_data_key=None, consistency_query_strategy=None, dimensions=None, end_time=None,
                 filters=None, interval_in_sec=None, limit=None, measures=None, metric=None, order=None, order_by=None,
                 proxy_user_id=None, start_time=None):
        self.consistency_data_key = consistency_data_key  # type: str
        self.consistency_query_strategy = consistency_query_strategy  # type: str
        self.dimensions = dimensions  # type: list[str]
        self.end_time = end_time  # type: long
        self.filters = filters  # type: list[QueryMetricRequestFilters]
        self.interval_in_sec = interval_in_sec  # type: int
        self.limit = limit  # type: int
        self.measures = measures  # type: list[str]
        self.metric = metric  # type: str
        self.order = order  # type: str
        self.order_by = order_by  # type: str
        self.proxy_user_id = proxy_user_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistency_data_key is not None:
            result['ConsistencyDataKey'] = self.consistency_data_key
        if self.consistency_query_strategy is not None:
            result['ConsistencyQueryStrategy'] = self.consistency_query_strategy
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsistencyDataKey') is not None:
            self.consistency_data_key = m.get('ConsistencyDataKey')
        if m.get('ConsistencyQueryStrategy') is not None:
            self.consistency_query_strategy = m.get('ConsistencyQueryStrategy')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMetricResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMetricResponse, self).to_map()
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
            temp_model = QueryMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricByPageRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricByPageRequestFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryMetricByPageRequest(TeaModel):
    def __init__(self, current_page=None, custom_filters=None, dimensions=None, end_time=None, filters=None,
                 interval_in_sec=None, measures=None, metric=None, order=None, order_by=None, page_size=None, start_time=None):
        self.current_page = current_page  # type: int
        self.custom_filters = custom_filters  # type: list[str]
        self.dimensions = dimensions  # type: list[str]
        self.end_time = end_time  # type: long
        self.filters = filters  # type: list[QueryMetricByPageRequestFilters]
        self.interval_in_sec = interval_in_sec  # type: int
        self.measures = measures  # type: list[str]
        self.metric = metric  # type: str
        self.order = order  # type: str
        self.order_by = order_by  # type: str
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMetricByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricByPageRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricByPageResponseBodyData(TeaModel):
    def __init__(self, items=None, page=None, page_size=None, total=None):
        self.items = items  # type: list[dict[str, any]]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricByPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMetricByPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryMetricByPageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMetricByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryMetricByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMetricByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMetricByPageResponse, self).to_map()
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
            temp_model = QueryMetricByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTraceAppConfigRequestSettings(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTraceAppConfigRequestSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SaveTraceAppConfigRequest(TeaModel):
    def __init__(self, pid=None, settings=None):
        self.pid = pid  # type: str
        self.settings = settings  # type: list[SaveTraceAppConfigRequestSettings]

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveTraceAppConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = SaveTraceAppConfigRequestSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class SaveTraceAppConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTraceAppConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveTraceAppConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTraceAppConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTraceAppConfigResponse, self).to_map()
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
            temp_model = SaveTraceAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactRequest(TeaModel):
    def __init__(self, contact_ids=None, contact_name=None, current_page=None, email=None, page_size=None,
                 phone=None, region_id=None):
        self.contact_ids = contact_ids  # type: str
        self.contact_name = contact_name  # type: str
        self.current_page = current_page  # type: str
        self.email = email  # type: str
        self.page_size = page_size  # type: str
        self.phone = phone  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.email is not None:
            result['Email'] = self.email
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchAlertContactResponseBodyPageBeanContacts(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, create_time=None, ding_robot=None, email=None, phone=None,
                 system_noc=None, update_time=None, user_id=None, webhook=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.create_time = create_time  # type: long
        self.ding_robot = ding_robot  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.system_noc = system_noc  # type: bool
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str
        self.webhook = webhook  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactResponseBodyPageBeanContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class SearchAlertContactResponseBodyPageBean(TeaModel):
    def __init__(self, contacts=None, page_number=None, page_size=None, total_count=None):
        self.contacts = contacts  # type: list[SearchAlertContactResponseBodyPageBeanContacts]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertContactResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactResponseBodyPageBeanContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertContactResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchAlertContactResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertContactResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertContactResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertContactResponse, self).to_map()
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
            temp_model = SearchAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_ids=None, contact_group_name=None, contact_id=None, contact_name=None,
                 is_detail=None, region_id=None):
        self.contact_group_ids = contact_group_ids  # type: str
        self.contact_group_name = contact_group_name  # type: str
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.is_detail = is_detail  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchAlertContactGroupResponseBodyContactGroupsContacts(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, create_time=None, ding_robot=None, email=None, phone=None,
                 system_noc=None, update_time=None, user_id=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.create_time = create_time  # type: long
        self.ding_robot = ding_robot  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.system_noc = system_noc  # type: bool
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertContactGroupResponseBodyContactGroupsContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBodyContactGroups(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contacts=None, create_time=None,
                 update_time=None, user_id=None):
        self.contact_group_id = contact_group_id  # type: long
        self.contact_group_name = contact_group_name  # type: str
        self.contacts = contacts  # type: list[SearchAlertContactGroupResponseBodyContactGroupsContacts]
        self.create_time = create_time  # type: long
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertContactGroupResponseBodyContactGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBody(TeaModel):
    def __init__(self, contact_groups=None, request_id=None):
        self.contact_groups = contact_groups  # type: list[SearchAlertContactGroupResponseBodyContactGroups]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contact_groups:
            for k in self.contact_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactGroups'] = []
        if self.contact_groups is not None:
            for k in self.contact_groups:
                result['ContactGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contact_groups = []
        if m.get('ContactGroups') is not None:
            for k in m.get('ContactGroups'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroups()
                self.contact_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertContactGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertContactGroupResponse, self).to_map()
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
            temp_model = SearchAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertHistoriesRequest(TeaModel):
    def __init__(self, alert_id=None, alert_type=None, current_page=None, end_time=None, page_size=None,
                 region_id=None, start_time=None):
        self.alert_id = alert_id  # type: long
        self.alert_type = alert_type  # type: int
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertHistoriesResponseBodyPageBeanAlarmHistories(TeaModel):
    def __init__(self, alarm_content=None, alarm_response_code=None, alarm_sources=None, alarm_time=None,
                 alarm_type=None, emails=None, id=None, phones=None, strategy_id=None, target=None, user_id=None):
        self.alarm_content = alarm_content  # type: str
        self.alarm_response_code = alarm_response_code  # type: int
        self.alarm_sources = alarm_sources  # type: str
        self.alarm_time = alarm_time  # type: long
        self.alarm_type = alarm_type  # type: int
        self.emails = emails  # type: str
        self.id = id  # type: long
        self.phones = phones  # type: str
        self.strategy_id = strategy_id  # type: str
        self.target = target  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertHistoriesResponseBodyPageBeanAlarmHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.alarm_response_code is not None:
            result['AlarmResponseCode'] = self.alarm_response_code
        if self.alarm_sources is not None:
            result['AlarmSources'] = self.alarm_sources
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.id is not None:
            result['Id'] = self.id
        if self.phones is not None:
            result['Phones'] = self.phones
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.target is not None:
            result['Target'] = self.target
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('AlarmResponseCode') is not None:
            self.alarm_response_code = m.get('AlarmResponseCode')
        if m.get('AlarmSources') is not None:
            self.alarm_sources = m.get('AlarmSources')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phones') is not None:
            self.phones = m.get('Phones')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertHistoriesResponseBodyPageBean(TeaModel):
    def __init__(self, alarm_histories=None, page_number=None, page_size=None, total_count=None):
        self.alarm_histories = alarm_histories  # type: list[SearchAlertHistoriesResponseBodyPageBeanAlarmHistories]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertHistoriesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = SearchAlertHistoriesResponseBodyPageBeanAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertHistoriesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchAlertHistoriesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchAlertHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertHistoriesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertHistoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertHistoriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertHistoriesResponse, self).to_map()
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
            temp_model = SearchAlertHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertRulesRequest(TeaModel):
    def __init__(self, app_type=None, current_page=None, page_size=None, pid=None, region_id=None, title=None,
                 type=None):
        self.app_type = app_type  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.title = title  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext(TeaModel):
    def __init__(self, alarm_content_sub_title=None, alarm_content_template=None, content=None, sub_title=None):
        self.alarm_content_sub_title = alarm_content_sub_title  # type: str
        self.alarm_content_template = alarm_content_template  # type: str
        self.content = content  # type: str
        self.sub_title = sub_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content_sub_title is not None:
            result['AlarmContentSubTitle'] = self.alarm_content_sub_title
        if self.alarm_content_template is not None:
            result['AlarmContentTemplate'] = self.alarm_content_template
        if self.content is not None:
            result['Content'] = self.content
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContentSubTitle') is not None:
            self.alarm_content_sub_title = m.get('AlarmContentSubTitle')
        if m.get('AlarmContentTemplate') is not None:
            self.alarm_content_template = m.get('AlarmContentTemplate')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules(TeaModel):
    def __init__(self, aggregates=None, alias=None, measure=None, nvalue=None, operator=None, value=None):
        self.aggregates = aggregates  # type: str
        self.alias = alias  # type: str
        self.measure = measure  # type: str
        self.nvalue = nvalue  # type: int
        self.operator = operator  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.measure is not None:
            result['Measure'] = self.measure
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Measure') is not None:
            self.measure = m.get('Measure')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule(TeaModel):
    def __init__(self, operator=None, rules=None):
        self.operator = operator  # type: str
        self.rules = rules  # type: list[SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator is not None:
            result['Operator'] = self.operator
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules()
                self.rules.append(temp_model.from_map(k))
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam(TeaModel):
    def __init__(self, app_group_id=None, app_id=None, dimensions=None, pid=None, type=None):
        self.app_group_id = app_group_id  # type: str
        self.app_id = app_id  # type: str
        self.dimensions = dimensions  # type: list[SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions]
        self.pid = pid  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesNotice(TeaModel):
    def __init__(self, end_time=None, notice_end_time=None, notice_start_time=None, start_time=None):
        self.end_time = end_time  # type: long
        self.notice_end_time = notice_end_time  # type: long
        self.notice_start_time = notice_start_time  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRulesNotice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.notice_end_time is not None:
            result['NoticeEndTime'] = self.notice_end_time
        if self.notice_start_time is not None:
            result['NoticeStartTime'] = self.notice_start_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NoticeEndTime') is not None:
            self.notice_end_time = m.get('NoticeEndTime')
        if m.get('NoticeStartTime') is not None:
            self.notice_start_time = m.get('NoticeStartTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRules(TeaModel):
    def __init__(self, alarm_context=None, alert_level=None, alert_rule=None, alert_title=None, alert_type=None,
                 alert_version=None, alert_way=None, alert_ways=None, config=None, contact_group_id_list=None,
                 contact_group_ids=None, create_time=None, id=None, metric_param=None, notice=None, region_id=None, status=None,
                 task_id=None, task_status=None, title=None, update_time=None, user_id=None):
        self.alarm_context = alarm_context  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext
        self.alert_level = alert_level  # type: str
        self.alert_rule = alert_rule  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule
        self.alert_title = alert_title  # type: str
        self.alert_type = alert_type  # type: int
        self.alert_version = alert_version  # type: int
        self.alert_way = alert_way  # type: list[str]
        self.alert_ways = alert_ways  # type: list[str]
        self.config = config  # type: str
        self.contact_group_id_list = contact_group_id_list  # type: str
        self.contact_group_ids = contact_group_ids  # type: str
        self.create_time = create_time  # type: long
        self.id = id  # type: long
        self.metric_param = metric_param  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam
        self.notice = notice  # type: SearchAlertRulesResponseBodyPageBeanAlertRulesNotice
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: long
        self.task_status = task_status  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.alarm_context:
            self.alarm_context.validate()
        if self.alert_rule:
            self.alert_rule.validate()
        if self.metric_param:
            self.metric_param.validate()
        if self.notice:
            self.notice.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBeanAlertRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_context is not None:
            result['AlarmContext'] = self.alarm_context.to_map()
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_version is not None:
            result['AlertVersion'] = self.alert_version
        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way
        if self.alert_ways is not None:
            result['AlertWays'] = self.alert_ways
        if self.config is not None:
            result['Config'] = self.config
        if self.contact_group_id_list is not None:
            result['ContactGroupIdList'] = self.contact_group_id_list
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param.to_map()
        if self.notice is not None:
            result['Notice'] = self.notice.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContext') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext()
            self.alarm_context = temp_model.from_map(m['AlarmContext'])
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertRule') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule()
            self.alert_rule = temp_model.from_map(m['AlertRule'])
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertVersion') is not None:
            self.alert_version = m.get('AlertVersion')
        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')
        if m.get('AlertWays') is not None:
            self.alert_ways = m.get('AlertWays')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ContactGroupIdList') is not None:
            self.contact_group_id_list = m.get('ContactGroupIdList')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetricParam') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam()
            self.metric_param = temp_model.from_map(m['MetricParam'])
        if m.get('Notice') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesNotice()
            self.notice = temp_model.from_map(m['Notice'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertRulesResponseBodyPageBean(TeaModel):
    def __init__(self, alert_rules=None, page_number=None, page_size=None, total_count=None):
        self.alert_rules = alert_rules  # type: list[SearchAlertRulesResponseBodyPageBeanAlertRules]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.alert_rules:
            for k in self.alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k in self.alert_rules:
                result['AlertRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k in m.get('AlertRules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertRulesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchAlertRulesResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAlertRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAlertRulesResponse, self).to_map()
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
            temp_model = SearchAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEventsRequest(TeaModel):
    def __init__(self, alert_id=None, alert_type=None, app_type=None, current_page=None, end_time=None,
                 is_trigger=None, page_size=None, pid=None, region_id=None, start_time=None):
        self.alert_id = alert_id  # type: long
        self.alert_type = alert_type  # type: int
        self.app_type = app_type  # type: str
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.is_trigger = is_trigger  # type: int
        self.page_size = page_size  # type: int
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchEventsResponseBodyPageBeanEvent(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, alert_rule=None, alert_type=None, event_level=None,
                 event_time=None, id=None, links=None, message=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.alert_rule = alert_rule  # type: str
        self.alert_type = alert_type  # type: int
        self.event_level = event_level  # type: str
        self.event_time = event_time  # type: long
        self.id = id  # type: long
        self.links = links  # type: list[str]
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEventsResponseBodyPageBeanEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.id is not None:
            result['Id'] = self.id
        if self.links is not None:
            result['Links'] = self.links
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SearchEventsResponseBodyPageBean(TeaModel):
    def __init__(self, event=None, page_number=None, page_size=None, total_count=None):
        self.event = event  # type: list[SearchEventsResponseBodyPageBeanEvent]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.event:
            for k in self.event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchEventsResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Event'] = []
        if self.event is not None:
            for k in self.event:
                result['Event'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k in m.get('Event'):
                temp_model = SearchEventsResponseBodyPageBeanEvent()
                self.event.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchEventsResponseBody(TeaModel):
    def __init__(self, is_trigger=None, page_bean=None, request_id=None):
        self.is_trigger = is_trigger  # type: int
        self.page_bean = page_bean  # type: SearchEventsResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('PageBean') is not None:
            temp_model = SearchEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchEventsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchEventsResponse, self).to_map()
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
            temp_model = SearchEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRetcodeAppByPageRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, retcode_app_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.retcode_app_name = retcode_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRetcodeAppByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        return self


class SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, pid=None, region_id=None, type=None,
                 update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchRetcodeAppByPageResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, retcode_apps=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.retcode_apps = retcode_apps  # type: list[SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchRetcodeAppByPageResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchRetcodeAppByPageResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchRetcodeAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchRetcodeAppByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchRetcodeAppByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchRetcodeAppByPageResponse, self).to_map()
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
            temp_model = SearchRetcodeAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByNameRequest(TeaModel):
    def __init__(self, region_id=None, trace_app_name=None):
        self.region_id = region_id  # type: str
        self.trace_app_name = trace_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        return self


class SearchTraceAppByNameResponseBodyTraceApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByNameResponseBodyTraceApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchTraceAppByNameResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_apps=None):
        self.request_id = request_id  # type: str
        self.trace_apps = trace_apps  # type: list[SearchTraceAppByNameResponseBodyTraceApps]

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTraceAppByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByNameResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTraceAppByNameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTraceAppByNameResponse, self).to_map()
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
            temp_model = SearchTraceAppByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByPageRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, trace_app_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.trace_app_name = trace_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        return self


class SearchTraceAppByPageResponseBodyPageBeanTraceApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, labels=None, pid=None, region_id=None, show=None,
                 type=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.labels = labels  # type: list[str]
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.show = show  # type: bool
        self.type = type  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTraceAppByPageResponseBodyPageBeanTraceApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchTraceAppByPageResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, trace_apps=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.trace_apps = trace_apps  # type: list[SearchTraceAppByPageResponseBodyPageBeanTraceApps]

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTraceAppByPageResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByPageResponseBodyPageBeanTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByPageResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchTraceAppByPageResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchTraceAppByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTraceAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTraceAppByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTraceAppByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTraceAppByPageResponse, self).to_map()
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
            temp_model = SearchTraceAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequestExclusionFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesRequestExclusionFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchTracesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchTracesRequest(TeaModel):
    def __init__(self, end_time=None, exclusion_filters=None, min_duration=None, operation_name=None,
                 region_id=None, reverse=None, service_ip=None, service_name=None, start_time=None, tag=None):
        self.end_time = end_time  # type: long
        self.exclusion_filters = exclusion_filters  # type: list[SearchTracesRequestExclusionFilters]
        self.min_duration = min_duration  # type: long
        self.operation_name = operation_name  # type: str
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long
        self.tag = tag  # type: list[SearchTracesRequestTag]

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = SearchTracesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyTraceInfos(TeaModel):
    def __init__(self, duration=None, operation_name=None, service_ip=None, service_name=None, timestamp=None,
                 trace_id=None):
        self.duration = duration  # type: long
        self.operation_name = operation_name  # type: str
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesResponseBodyTraceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_infos=None):
        self.request_id = request_id  # type: str
        self.trace_infos = trace_infos  # type: list[SearchTracesResponseBodyTraceInfos]

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesResponseBodyTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTracesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTracesResponse, self).to_map()
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
            temp_model = SearchTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesByPageRequestExclusionFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesByPageRequestExclusionFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchTracesByPageRequest(TeaModel):
    def __init__(self, end_time=None, exclusion_filters=None, min_duration=None, operation_name=None,
                 page_number=None, page_size=None, region_id=None, reverse=None, service_ip=None, service_name=None,
                 start_time=None):
        self.end_time = end_time  # type: long
        self.exclusion_filters = exclusion_filters  # type: list[SearchTracesByPageRequestExclusionFilters]
        self.min_duration = min_duration  # type: long
        self.operation_name = operation_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesByPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesByPageRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchTracesByPageResponseBodyPageBeanTraceInfos(TeaModel):
    def __init__(self, duration=None, operation_name=None, service_ip=None, service_name=None, timestamp=None,
                 trace_id=None):
        self.duration = duration  # type: long
        self.operation_name = operation_name  # type: str
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesByPageResponseBodyPageBeanTraceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesByPageResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None, trace_infos=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.trace_infos = trace_infos  # type: list[SearchTracesByPageResponseBodyPageBeanTraceInfos]

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesByPageResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesByPageResponseBodyPageBeanTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesByPageResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        self.page_bean = page_bean  # type: SearchTracesByPageResponseBodyPageBean
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchTracesByPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTracesByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTracesByPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTracesByPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTracesByPageResponse, self).to_map()
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
            temp_model = SearchTracesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomIncidentsRequest(TeaModel):
    def __init__(self, incidents=None, product_type=None, region_id=None):
        self.incidents = incidents  # type: str
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomIncidentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incidents is not None:
            result['Incidents'] = self.incidents
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Incidents') is not None:
            self.incidents = m.get('Incidents')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SendCustomIncidentsResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCustomIncidentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendCustomIncidentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCustomIncidentsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCustomIncidentsResponse, self).to_map()
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
            temp_model = SendCustomIncidentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMseIncidentRequest(TeaModel):
    def __init__(self, incidents=None, region_id=None):
        self.incidents = incidents  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMseIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incidents is not None:
            result['Incidents'] = self.incidents
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Incidents') is not None:
            self.incidents = m.get('Incidents')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SendMseIncidentResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMseIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMseIncidentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendMseIncidentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMseIncidentResponse, self).to_map()
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
            temp_model = SendMseIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRetcodeShareStatusRequest(TeaModel):
    def __init__(self, pid=None, status=None):
        self.pid = pid  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRetcodeShareStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetRetcodeShareStatusResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRetcodeShareStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetRetcodeShareStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetRetcodeShareStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetRetcodeShareStatusResponse, self).to_map()
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
            temp_model = SetRetcodeShareStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlertRequest(TeaModel):
    def __init__(self, alert_id=None, region_id=None):
        self.alert_id = alert_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartAlertResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAlertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartAlertResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartAlertResponse, self).to_map()
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
            temp_model = StartAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAlertRequest(TeaModel):
    def __init__(self, alert_id=None, region_id=None):
        self.alert_id = alert_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopAlertResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAlertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopAlertResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAlertResponse, self).to_map()
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
            temp_model = StopAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactRequest(TeaModel):
    def __init__(self, contact_id=None, contact_name=None, ding_robot_webhook_url=None, email=None, phone_num=None,
                 region_id=None, system_noc=None):
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.ding_robot_webhook_url = ding_robot_webhook_url  # type: str
        self.email = email  # type: str
        self.phone_num = phone_num  # type: str
        self.region_id = region_id  # type: str
        self.system_noc = system_noc  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        return self


class UpdateAlertContactResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertContactResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertContactResponse, self).to_map()
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
            temp_model = UpdateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactGroupRequest(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None, contact_ids=None, region_id=None):
        self.contact_group_id = contact_group_id  # type: long
        self.contact_group_name = contact_group_name  # type: str
        self.contact_ids = contact_ids  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAlertContactGroupResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertContactGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertContactGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertContactGroupResponse, self).to_map()
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
            temp_model = UpdateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None, contact_group_ids=None, is_auto_start=None, region_id=None,
                 templage_alert_config=None):
        self.alert_id = alert_id  # type: long
        self.contact_group_ids = contact_group_ids  # type: str
        self.is_auto_start = is_auto_start  # type: bool
        self.region_id = region_id  # type: str
        self.templage_alert_config = templage_alert_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        return self


class UpdateAlertRuleResponseBody(TeaModel):
    def __init__(self, alert_id=None, data=None, request_id=None):
        self.alert_id = alert_id  # type: long
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertRuleResponse, self).to_map()
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
            temp_model = UpdateAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertTemplateRequest(TeaModel):
    def __init__(self, annotations=None, id=None, labels=None, match_expressions=None, message=None, name=None,
                 region_id=None, rule=None, status=None, type=None):
        self.annotations = annotations  # type: str
        self.id = id  # type: long
        self.labels = labels  # type: str
        self.match_expressions = match_expressions  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.rule = rule  # type: str
        self.status = status  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.id is not None:
            result['Id'] = self.id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateAlertTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAlertTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertTemplateResponse, self).to_map()
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
            temp_model = UpdateAlertTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDispatchRuleRequest(TeaModel):
    def __init__(self, dispatch_rule=None, region_id=None):
        self.dispatch_rule = dispatch_rule  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDispatchRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateDispatchRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDispatchRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDispatchRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDispatchRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDispatchRuleResponse, self).to_map()
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
            temp_model = UpdateDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrometheusAlertRuleRequest(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, region_id=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: str
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: str
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(self, alert_id=None, alert_name=None, annotations=None, cluster_id=None, dispatch_rule_id=None,
                 duration=None, expression=None, labels=None, message=None, notify_type=None, status=None, type=None):
        self.alert_id = alert_id  # type: long
        self.alert_name = alert_name  # type: str
        self.annotations = annotations  # type: list[UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations]
        self.cluster_id = cluster_id  # type: str
        self.dispatch_rule_id = dispatch_rule_id  # type: long
        self.duration = duration  # type: str
        self.expression = expression  # type: str
        self.labels = labels  # type: list[UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels]
        self.message = message  # type: str
        self.notify_type = notify_type  # type: str
        self.status = status  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(self, prometheus_alert_rule=None, request_id=None):
        self.prometheus_alert_rule = prometheus_alert_rule  # type: UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePrometheusAlertRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePrometheusAlertRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePrometheusAlertRuleResponse, self).to_map()
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
            temp_model = UpdatePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebhookRequest(TeaModel):
    def __init__(self, body=None, contact_id=None, contact_name=None, http_headers=None, http_params=None,
                 method=None, region_id=None, url=None):
        self.body = body  # type: str
        self.contact_id = contact_id  # type: long
        self.contact_name = contact_name  # type: str
        self.http_headers = http_headers  # type: str
        self.http_params = http_params  # type: str
        self.method = method  # type: str
        self.region_id = region_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.method is not None:
            result['Method'] = self.method
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateWebhookResponseBody(TeaModel):
    def __init__(self, is_success=None, request_id=None):
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebhookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWebhookResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWebhookResponse, self).to_map()
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
            temp_model = UpdateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


