# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddMockRuleRequest(TeaModel):
    def __init__(self, name=None, region=None, source=None, provider_app_id=None, provider_app_name=None,
                 extra_json=None, sc_mock_items=None, dubbo_mock_items=None, consumer_app_ids=None, enable=None):
        self.name = name  # type: str
        self.region = region  # type: str
        self.source = source  # type: str
        self.provider_app_id = provider_app_id  # type: str
        self.provider_app_name = provider_app_name  # type: str
        self.extra_json = extra_json  # type: str
        self.sc_mock_items = sc_mock_items  # type: str
        self.dubbo_mock_items = dubbo_mock_items  # type: str
        self.consumer_app_ids = consumer_app_ids  # type: str
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMockRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.sc_mock_items is not None:
            result['ScMockItems'] = self.sc_mock_items
        if self.dubbo_mock_items is not None:
            result['DubboMockItems'] = self.dubbo_mock_items
        if self.consumer_app_ids is not None:
            result['ConsumerAppIds'] = self.consumer_app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('ScMockItems') is not None:
            self.sc_mock_items = m.get('ScMockItems')
        if m.get('DubboMockItems') is not None:
            self.dubbo_mock_items = m.get('DubboMockItems')
        if m.get('ConsumerAppIds') is not None:
            self.consumer_app_ids = m.get('ConsumerAppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class AddMockRuleResponseBodyData(TeaModel):
    def __init__(self, namespace_id=None, sc_mock_item_json=None, consumer_app_name=None, consumer_app_id=None,
                 account_id=None, extra_json=None, source=None, region=None, provider_app_id=None, provider_app_name=None,
                 name=None, id=None, enable=None):
        self.namespace_id = namespace_id  # type: str
        self.sc_mock_item_json = sc_mock_item_json  # type: str
        self.consumer_app_name = consumer_app_name  # type: str
        self.consumer_app_id = consumer_app_id  # type: str
        self.account_id = account_id  # type: str
        self.extra_json = extra_json  # type: str
        self.source = source  # type: str
        self.region = region  # type: str
        self.provider_app_id = provider_app_id  # type: str
        self.provider_app_name = provider_app_name  # type: str
        self.name = name  # type: str
        self.id = id  # type: long
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMockRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.sc_mock_item_json is not None:
            result['ScMockItemJson'] = self.sc_mock_item_json
        if self.consumer_app_name is not None:
            result['ConsumerAppName'] = self.consumer_app_name
        if self.consumer_app_id is not None:
            result['ConsumerAppId'] = self.consumer_app_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.source is not None:
            result['Source'] = self.source
        if self.region is not None:
            result['Region'] = self.region
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ScMockItemJson') is not None:
            self.sc_mock_item_json = m.get('ScMockItemJson')
        if m.get('ConsumerAppName') is not None:
            self.consumer_app_name = m.get('ConsumerAppName')
        if m.get('ConsumerAppId') is not None:
            self.consumer_app_id = m.get('ConsumerAppId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class AddMockRuleResponseBody(TeaModel):
    def __init__(self, http_status_code=None, message=None, request_id=None, data=None, code=None, success=None):
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: AddMockRuleResponseBodyData
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddMockRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AddMockRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMockRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddMockRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddMockRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddMockRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, origin_namespace_id=None, target_namespace_id=None, policy=None, ids=None):
        self.instance_id = instance_id  # type: str
        self.origin_namespace_id = origin_namespace_id  # type: str
        self.target_namespace_id = target_namespace_id  # type: str
        self.policy = policy  # type: str
        self.ids = ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.origin_namespace_id is not None:
            result['OriginNamespaceId'] = self.origin_namespace_id
        if self.target_namespace_id is not None:
            result['TargetNamespaceId'] = self.target_namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginNamespaceId') is not None:
            self.origin_namespace_id = m.get('OriginNamespaceId')
        if m.get('TargetNamespaceId') is not None:
            self.target_namespace_id = m.get('TargetNamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class CloneNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneNacosConfigResponseBodyDataFailData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneNacosConfigResponseBodyDataSkipData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyData(TeaModel):
    def __init__(self, succ_count=None, fail_data=None, skip_count=None, skip_data=None):
        self.succ_count = succ_count  # type: int
        self.fail_data = fail_data  # type: list[CloneNacosConfigResponseBodyDataFailData]
        self.skip_count = skip_count  # type: int
        self.skip_data = skip_data  # type: list[CloneNacosConfigResponseBodyDataSkipData]

    def validate(self):
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CloneNacosConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = CloneNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = CloneNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        return self


class CloneNacosConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: CloneNacosConfigResponseBodyData
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CloneNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = CloneNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloneNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloneNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRuleRequest(TeaModel):
    def __init__(self, instance_id=None, alarm_alias_name=None, alert_way=None, contact_group_ids=None,
                 alarm_item=None, operator=None, aggregates=None, nvalue=None, value=None):
        self.instance_id = instance_id  # type: str
        self.alarm_alias_name = alarm_alias_name  # type: str
        self.alert_way = alert_way  # type: dict[str, any]
        self.contact_group_ids = contact_group_ids  # type: dict[str, any]
        self.alarm_item = alarm_item  # type: str
        self.operator = operator  # type: str
        self.aggregates = aggregates  # type: str
        self.nvalue = nvalue  # type: int
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, alarm_alias_name=None, alert_way_shrink=None,
                 contact_group_ids_shrink=None, alarm_item=None, operator=None, aggregates=None, nvalue=None, value=None):
        self.instance_id = instance_id  # type: str
        self.alarm_alias_name = alarm_alias_name  # type: str
        self.alert_way_shrink = alert_way_shrink  # type: str
        self.contact_group_ids_shrink = contact_group_ids_shrink  # type: str
        self.alarm_item = alarm_item  # type: str
        self.operator = operator  # type: str
        self.aggregates = aggregates  # type: str
        self.nvalue = nvalue  # type: int
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alert_way_shrink is not None:
            result['AlertWay'] = self.alert_way_shrink
        if self.contact_group_ids_shrink is not None:
            result['ContactGroupIds'] = self.contact_group_ids_shrink
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlertWay') is not None:
            self.alert_way_shrink = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids_shrink = m.get('ContactGroupIds')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAlarmRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAlarmRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlarmRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, app_name=None, region=None, source=None, language=None, extra_info=None):
        self.app_name = app_name  # type: str
        self.region = region  # type: str
        self.source = source  # type: str
        self.language = language  # type: str
        self.extra_info = extra_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        if self.language is not None:
            result['Language'] = self.language
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(self, status=None, extra_info=None, app_name=None, update_time=None, license_key=None,
                 create_time=None, app_id=None, user_id=None, source=None, language=None, region_id=None):
        self.status = status  # type: int
        self.extra_info = extra_info  # type: str
        self.app_name = app_name  # type: str
        self.update_time = update_time  # type: long
        self.license_key = license_key  # type: str
        self.create_time = create_time  # type: long
        self.app_id = app_id  # type: str
        self.user_id = user_id  # type: str
        self.source = source  # type: str
        self.language = language  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.source is not None:
            result['Source'] = self.source
        if self.language is not None:
            result['Language'] = self.language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: CreateApplicationResponseBodyData
        self.code = code  # type: int
        self.success = success  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, pub_network_flow=None, pub_slb_specification=None, disk_type=None, vpc_id=None,
                 net_type=None, v_switch_id=None, instance_count=None, cluster_specification=None, cluster_version=None,
                 cluster_type=None, region=None, private_slb_specification=None, connection_type=None, request_pars=None,
                 disk_capacity=None):
        self.pub_network_flow = pub_network_flow  # type: str
        self.pub_slb_specification = pub_slb_specification  # type: str
        self.disk_type = disk_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.net_type = net_type  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.instance_count = instance_count  # type: int
        self.cluster_specification = cluster_specification  # type: str
        self.cluster_version = cluster_version  # type: str
        self.cluster_type = cluster_type  # type: str
        self.region = region  # type: str
        self.private_slb_specification = private_slb_specification  # type: str
        self.connection_type = connection_type  # type: str
        self.request_pars = request_pars  # type: str
        self.disk_capacity = disk_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.pub_slb_specification is not None:
            result['PubSlbSpecification'] = self.pub_slb_specification
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.region is not None:
            result['Region'] = self.region
        if self.private_slb_specification is not None:
            result['PrivateSlbSpecification'] = self.private_slb_specification
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('PubSlbSpecification') is not None:
            self.pub_slb_specification = m.get('PubSlbSpecification')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PrivateSlbSpecification') is not None:
            self.private_slb_specification = m.get('PrivateSlbSpecification')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, instance_id=None, error_code=None, order_id=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.instance_id = instance_id  # type: str
        self.error_code = error_code  # type: str
        self.order_id = order_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEngineNamespaceRequest(TeaModel):
    def __init__(self, cluster_id=None, name=None, desc=None, instance_id=None, service_count=None):
        self.cluster_id = cluster_id  # type: str
        self.name = name  # type: str
        self.desc = desc  # type: str
        self.instance_id = instance_id  # type: str
        self.service_count = service_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEngineNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class CreateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(self, type=None, namespace_show_name=None, quota=None, namespace=None, namespace_desc=None,
                 config_count=None, service_count=None):
        self.type = type  # type: int
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: int
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.config_count = config_count  # type: int
        self.service_count = service_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEngineNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class CreateEngineNamespaceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, cluster_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data = data  # type: CreateEngineNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEngineNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            temp_model = CreateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEngineNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEngineNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEngineNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, data_id=None, group=None, app_name=None, tags=None, desc=None, type=None,
                 content=None, namespace_id=None):
        self.instance_id = instance_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.app_name = app_name  # type: str
        self.tags = tags  # type: str
        self.desc = desc  # type: str
        self.type = type  # type: str
        self.content = content  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        if self.content is not None:
            result['Content'] = self.content
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class CreateNacosConfigResponseBody(TeaModel):
    def __init__(self, http_code=None, request_id=None, message=None, error_code=None, code=None, success=None):
        self.http_code = http_code  # type: str
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.error_code = error_code  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateZnodeRequest(TeaModel):
    def __init__(self, cluster_id=None, path=None, data=None):
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateZnodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateZnodeResponseBodyData(TeaModel):
    def __init__(self, data=None, path=None, dir=None, name=None):
        self.data = data  # type: str
        self.path = path  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateZnodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateZnodeResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: CreateZnodeResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateZnodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateZnodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateZnodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateZnodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRuleRequest(TeaModel):
    def __init__(self, request_pars=None, alarm_rule_id=None):
        self.request_pars = request_pars  # type: str
        self.alarm_rule_id = alarm_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        return self


class DeleteAlarmRuleResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAlarmRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAlarmRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlarmRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEngineNamespaceRequest(TeaModel):
    def __init__(self, id=None, instance_id=None, cluster_id=None):
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEngineNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteEngineNamespaceResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEngineNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEngineNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEngineNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEngineNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, data_id=None, group=None, namespace_id=None):
        self.instance_id = instance_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigResponseBody(TeaModel):
    def __init__(self, http_code=None, request_id=None, message=None, error_code=None, code=None, success=None):
        self.http_code = http_code  # type: str
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.error_code = error_code  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigsRequest(TeaModel):
    def __init__(self, instance_id=None, ids=None, namespace_id=None):
        self.instance_id = instance_id  # type: str
        self.ids = ids  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigsResponseBody(TeaModel):
    def __init__(self, http_code=None, request_id=None, message=None, error_code=None, code=None, success=None):
        self.http_code = http_code  # type: str
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.error_code = error_code  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNacosConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNacosConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosServiceRequest(TeaModel):
    def __init__(self, instance_id=None, service_name=None, group_name=None, namespace_id=None):
        self.instance_id = instance_id  # type: str
        self.service_name = service_name  # type: str
        self.group_name = group_name  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosServiceResponseBody(TeaModel):
    def __init__(self, http_status_code=None, request_id=None, message=None, code=None, success=None, data=None):
        # http状态码
        self.http_status_code = http_status_code  # type: int
        # 请求id
        self.request_id = request_id  # type: str
        # 响应信息
        self.message = message  # type: str
        # 响应码
        self.code = code  # type: int
        # 成功标志
        self.success = success  # type: bool
        # 删除服务的结果
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteNacosServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNacosServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNacosServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZnodeRequest(TeaModel):
    def __init__(self, request_pars=None, cluster_id=None, path=None):
        self.request_pars = request_pars  # type: str
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteZnodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteZnodeResponseBodyData(TeaModel):
    def __init__(self, data=None, path=None, dir=None, name=None):
        self.data = data  # type: str
        self.path = path  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteZnodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteZnodeResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: DeleteZnodeResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteZnodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeleteZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteZnodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteZnodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteZnodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_id=None, ids=None, data_id=None, group=None, app_name=None):
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.ids = ids  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ExportNacosConfigResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportNacosConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportNacosConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: ExportNacosConfigResponseBodyData
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExportNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = ExportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExportNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEngineNamepaceRequest(TeaModel):
    def __init__(self, id=None, instance_id=None, cluster_id=None):
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEngineNamepaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetEngineNamepaceResponseBody(TeaModel):
    def __init__(self, http_code=None, type=None, quota=None, request_id=None, message=None, config_count=None,
                 namespace_show_name=None, error_code=None, success=None, namespace_desc=None, namespace=None):
        self.http_code = http_code  # type: str
        self.type = type  # type: str
        self.quota = quota  # type: str
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.config_count = config_count  # type: str
        self.namespace_show_name = namespace_show_name  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool
        self.namespace_desc = namespace_desc  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEngineNamepaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.type is not None:
            result['Type'] = self.type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetEngineNamepaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEngineNamepaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEngineNamepaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEngineNamepaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportFileUrlRequest(TeaModel):
    def __init__(self, content_type=None, instance_id=None, namespace_id=None):
        self.content_type = content_type  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImportFileUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetImportFileUrlResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImportFileUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImportFileUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: GetImportFileUrlResponseBodyData
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImportFileUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = GetImportFileUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImportFileUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImportFileUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImportFileUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, data_id=None, group=None, namespace_id=None):
        self.instance_id = instance_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetNacosConfigResponseBodyConfiguration(TeaModel):
    def __init__(self, type=None, app_name=None, tags=None, md_5=None, data_id=None, content=None, group=None,
                 desc=None):
        self.type = type  # type: str
        self.app_name = app_name  # type: str
        self.tags = tags  # type: str
        self.md_5 = md_5  # type: str
        self.data_id = data_id  # type: str
        self.content = content  # type: str
        self.group = group  # type: str
        self.desc = desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosConfigResponseBodyConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.content is not None:
            result['Content'] = self.content
        if self.group is not None:
            result['Group'] = self.group
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class GetNacosConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, configuration=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.configuration = configuration  # type: GetNacosConfigResponseBodyConfiguration
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super(GetNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Configuration') is not None:
            temp_model = GetNacosConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosHistoryConfigRequest(TeaModel):
    def __init__(self, instance_id=None, data_id=None, group=None, namespace_id=None, nid=None):
        self.instance_id = instance_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.namespace_id = namespace_id  # type: str
        self.nid = nid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosHistoryConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nid is not None:
            result['Nid'] = self.nid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Nid') is not None:
            self.nid = m.get('Nid')
        return self


class GetNacosHistoryConfigResponseBodyConfiguration(TeaModel):
    def __init__(self, app_name=None, md_5=None, data_id=None, content=None, group=None, op_type=None):
        self.app_name = app_name  # type: str
        self.md_5 = md_5  # type: str
        self.data_id = data_id  # type: str
        self.content = content  # type: str
        self.group = group  # type: str
        self.op_type = op_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosHistoryConfigResponseBodyConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.content is not None:
            result['Content'] = self.content
        if self.group is not None:
            result['Group'] = self.group
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class GetNacosHistoryConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, configuration=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.configuration = configuration  # type: GetNacosHistoryConfigResponseBodyConfiguration
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super(GetNacosHistoryConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Configuration') is not None:
            temp_model = GetNacosHistoryConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosHistoryConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNacosHistoryConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNacosHistoryConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNacosHistoryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOverviewRequest(TeaModel):
    def __init__(self, period=None, region=None):
        self.period = period  # type: int
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetOverviewResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: int
        self.success = success  # type: str
        self.http_status_code = http_status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOverviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, namespace_id=None, policy=None, file_url=None):
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.policy = policy  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ImportNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNacosConfigResponseBodyDataFailData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNacosConfigResponseBodyDataSkipData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyData(TeaModel):
    def __init__(self, succ_count=None, fail_data=None, skip_count=None, skip_data=None):
        self.succ_count = succ_count  # type: int
        self.fail_data = fail_data  # type: list[ImportNacosConfigResponseBodyDataFailData]
        self.skip_count = skip_count  # type: int
        self.skip_data = skip_data  # type: list[ImportNacosConfigResponseBodyDataSkipData]

    def validate(self):
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportNacosConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = ImportNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = ImportNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        return self


class ImportNacosConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: ImportNacosConfigResponseBodyData
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImportNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = ImportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmContactGroupsRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmContactGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlarmContactGroupsResponseBodyData(TeaModel):
    def __init__(self, contact_group_name=None, contact_group_id=None):
        self.contact_group_name = contact_group_name  # type: str
        self.contact_group_id = contact_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmContactGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        return self


class ListAlarmContactGroupsResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListAlarmContactGroupsResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmContactGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmContactGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmContactGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmContactGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmContactGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmContactGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, alarm_mse_type=None, start_time=None,
                 end_time=None, alarm_name=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.alarm_mse_type = alarm_mse_type  # type: str
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.alarm_name = alarm_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        return self


class ListAlarmHistoriesResponseBodyData(TeaModel):
    def __init__(self, alarm_time=None, alarm_email=None, alarm_ding_ding=None, alarm_phone=None, alarm_name=None,
                 alarm_content=None):
        self.alarm_time = alarm_time  # type: str
        self.alarm_email = alarm_email  # type: str
        self.alarm_ding_ding = alarm_ding_ding  # type: str
        self.alarm_phone = alarm_phone  # type: str
        self.alarm_name = alarm_name  # type: str
        self.alarm_content = alarm_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmHistoriesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_email is not None:
            result['AlarmEmail'] = self.alarm_email
        if self.alarm_ding_ding is not None:
            result['AlarmDingDing'] = self.alarm_ding_ding
        if self.alarm_phone is not None:
            result['AlarmPhone'] = self.alarm_phone
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmEmail') is not None:
            self.alarm_email = m.get('AlarmEmail')
        if m.get('AlarmDingDing') is not None:
            self.alarm_ding_ding = m.get('AlarmDingDing')
        if m.get('AlarmPhone') is not None:
            self.alarm_phone = m.get('AlarmPhone')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListAlarmHistoriesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmHistoriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmItemsRequest(TeaModel):
    def __init__(self, request_pars=None):
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmItemsResponseBodyData(TeaModel):
    def __init__(self, alarm_desc=None, cluster_type=None, alarm_code=None):
        self.alarm_desc = alarm_desc  # type: str
        self.cluster_type = cluster_type  # type: str
        self.alarm_code = alarm_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmItemsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_desc is not None:
            result['AlarmDesc'] = self.alarm_desc
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.alarm_code is not None:
            result['AlarmCode'] = self.alarm_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmDesc') is not None:
            self.alarm_desc = m.get('AlarmDesc')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('AlarmCode') is not None:
            self.alarm_code = m.get('AlarmCode')
        return self


class ListAlarmItemsResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListAlarmItemsResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmItemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmRulesRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, alarm_mse_type=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.alarm_mse_type = alarm_mse_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        return self


class ListAlarmRulesResponseBodyData(TeaModel):
    def __init__(self, alarm_status=None, alarm_rule_id=None, create_time=None, alarm_rule_detail=None,
                 alarm_name=None):
        self.alarm_status = alarm_status  # type: str
        self.alarm_rule_id = alarm_rule_id  # type: str
        self.create_time = create_time  # type: str
        self.alarm_rule_detail = alarm_rule_detail  # type: str
        self.alarm_name = alarm_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.alarm_rule_detail is not None:
            result['AlarmRuleDetail'] = self.alarm_rule_detail
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AlarmRuleDetail') is not None:
            self.alarm_rule_detail = m.get('AlarmRuleDetail')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        return self


class ListAlarmRulesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListAlarmRulesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAlarmRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsInstancesRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, cluster_id=None, service_name=None,
                 group_name=None, namespace_id=None, cluster_name=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.cluster_id = cluster_id  # type: str
        self.service_name = service_name  # type: str
        self.group_name = group_name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.cluster_name = cluster_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ListAnsInstancesResponseBodyData(TeaModel):
    def __init__(self, default_key=None, ephemeral=None, marked=None, ip=None, instance_id=None, port=None,
                 last_beat=None, ok_count=None, weight=None, instance_heart_beat_interval=None, ip_delete_timeout=None,
                 app=None, fail_count=None, healthy=None, enabled=None, datum_key=None, cluster_name=None,
                 instance_heart_beat_time_out=None, service_name=None, metadata=None):
        self.default_key = default_key  # type: str
        self.ephemeral = ephemeral  # type: bool
        self.marked = marked  # type: bool
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.port = port  # type: int
        self.last_beat = last_beat  # type: long
        self.ok_count = ok_count  # type: int
        self.weight = weight  # type: int
        self.instance_heart_beat_interval = instance_heart_beat_interval  # type: int
        self.ip_delete_timeout = ip_delete_timeout  # type: int
        self.app = app  # type: str
        self.fail_count = fail_count  # type: int
        self.healthy = healthy  # type: bool
        self.enabled = enabled  # type: bool
        self.datum_key = datum_key  # type: str
        self.cluster_name = cluster_name  # type: str
        self.instance_heart_beat_time_out = instance_heart_beat_time_out  # type: int
        self.service_name = service_name  # type: str
        self.metadata = metadata  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_key is not None:
            result['DefaultKey'] = self.default_key
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.marked is not None:
            result['Marked'] = self.marked
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.last_beat is not None:
            result['LastBeat'] = self.last_beat
        if self.ok_count is not None:
            result['OkCount'] = self.ok_count
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.instance_heart_beat_interval is not None:
            result['InstanceHeartBeatInterval'] = self.instance_heart_beat_interval
        if self.ip_delete_timeout is not None:
            result['IpDeleteTimeout'] = self.ip_delete_timeout
        if self.app is not None:
            result['App'] = self.app
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.healthy is not None:
            result['Healthy'] = self.healthy
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.datum_key is not None:
            result['DatumKey'] = self.datum_key
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_heart_beat_time_out is not None:
            result['InstanceHeartBeatTimeOut'] = self.instance_heart_beat_time_out
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultKey') is not None:
            self.default_key = m.get('DefaultKey')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('Marked') is not None:
            self.marked = m.get('Marked')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LastBeat') is not None:
            self.last_beat = m.get('LastBeat')
        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('InstanceHeartBeatInterval') is not None:
            self.instance_heart_beat_interval = m.get('InstanceHeartBeatInterval')
        if m.get('IpDeleteTimeout') is not None:
            self.ip_delete_timeout = m.get('IpDeleteTimeout')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('Healthy') is not None:
            self.healthy = m.get('Healthy')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('DatumKey') is not None:
            self.datum_key = m.get('DatumKey')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceHeartBeatTimeOut') is not None:
            self.instance_heart_beat_time_out = m.get('InstanceHeartBeatTimeOut')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListAnsInstancesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListAnsInstancesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnsInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServiceClustersRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, cluster_id=None, service_name=None,
                 group_name=None, namespace_id=None, cluster_name=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.cluster_id = cluster_id  # type: str
        self.service_name = service_name  # type: str
        self.group_name = group_name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.cluster_name = cluster_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServiceClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ListAnsServiceClustersResponseBodyDataClusters(TeaModel):
    def __init__(self, default_check_port=None, health_checker_type=None, use_ipport_4check=None,
                 service_name=None, name=None, default_port=None, metadata=None):
        self.default_check_port = default_check_port  # type: int
        self.health_checker_type = health_checker_type  # type: str
        self.use_ipport_4check = use_ipport_4check  # type: bool
        self.service_name = service_name  # type: str
        self.name = name  # type: str
        self.default_port = default_port  # type: int
        self.metadata = metadata  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServiceClustersResponseBodyDataClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_check_port is not None:
            result['DefaultCheckPort'] = self.default_check_port
        if self.health_checker_type is not None:
            result['HealthCheckerType'] = self.health_checker_type
        if self.use_ipport_4check is not None:
            result['UseIPPort4Check'] = self.use_ipport_4check
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.name is not None:
            result['Name'] = self.name
        if self.default_port is not None:
            result['DefaultPort'] = self.default_port
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultCheckPort') is not None:
            self.default_check_port = m.get('DefaultCheckPort')
        if m.get('HealthCheckerType') is not None:
            self.health_checker_type = m.get('HealthCheckerType')
        if m.get('UseIPPort4Check') is not None:
            self.use_ipport_4check = m.get('UseIPPort4Check')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DefaultPort') is not None:
            self.default_port = m.get('DefaultPort')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListAnsServiceClustersResponseBodyData(TeaModel):
    def __init__(self, protect_threshold=None, group_name=None, clusters=None, name=None, selector_type=None,
                 metadata=None):
        self.protect_threshold = protect_threshold  # type: float
        self.group_name = group_name  # type: str
        self.clusters = clusters  # type: list[ListAnsServiceClustersResponseBodyDataClusters]
        self.name = name  # type: str
        self.selector_type = selector_type  # type: str
        self.metadata = metadata  # type: dict[str, any]

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnsServiceClustersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.selector_type is not None:
            result['SelectorType'] = self.selector_type
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListAnsServiceClustersResponseBodyDataClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectorType') is not None:
            self.selector_type = m.get('SelectorType')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListAnsServiceClustersResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: ListAnsServiceClustersResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAnsServiceClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListAnsServiceClustersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsServiceClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnsServiceClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnsServiceClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsServiceClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServicesRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, cluster_id=None, service_name=None,
                 group_name=None, has_ip_count=None, instance_id=None, namespace_id=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.cluster_id = cluster_id  # type: str
        self.service_name = service_name  # type: str
        self.group_name = group_name  # type: str
        self.has_ip_count = has_ip_count  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_ip_count is not None:
            result['HasIpCount'] = self.has_ip_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasIpCount') is not None:
            self.has_ip_count = m.get('HasIpCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListAnsServicesResponseBodyData(TeaModel):
    def __init__(self, healthy_instance_count=None, group_name=None, ip_count=None, name=None, cluster_count=None):
        self.healthy_instance_count = healthy_instance_count  # type: int
        self.group_name = group_name  # type: str
        self.ip_count = ip_count  # type: int
        self.name = name  # type: str
        self.cluster_count = cluster_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.healthy_instance_count is not None:
            result['HealthyInstanceCount'] = self.healthy_instance_count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.name is not None:
            result['Name'] = self.name
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HealthyInstanceCount') is not None:
            self.healthy_instance_count = m.get('HealthyInstanceCount')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')
        return self


class ListAnsServicesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListAnsServicesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnsServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnsServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnsServicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAnsServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterConnectionTypesResponseBodyData(TeaModel):
    def __init__(self, show_name=None):
        self.show_name = show_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterConnectionTypesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterConnectionTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: list[ListClusterConnectionTypesResponseBodyData]
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterConnectionTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterConnectionTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterConnectionTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterConnectionTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterConnectionTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterConnectionTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, cluster_alias_name=None, region_id=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(self, end_date=None, intranet_domain=None, internet_domain=None, create_time=None,
                 charge_type=None, intranet_address=None, instance_id=None, internet_address=None, cluster_alias_name=None,
                 cluster_type=None, init_status=None, app_version=None):
        self.end_date = end_date  # type: str
        self.intranet_domain = intranet_domain  # type: str
        self.internet_domain = internet_domain  # type: str
        self.create_time = create_time  # type: str
        self.charge_type = charge_type  # type: str
        self.intranet_address = intranet_address  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_address = internet_address  # type: str
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.init_status = init_status  # type: str
        self.app_version = app_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListClustersResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTypesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypesRequest, self).to_map()
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


class ListClusterTypesResponseBodyData(TeaModel):
    def __init__(self, show_name=None):
        self.show_name = show_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: list[ListClusterTypesResponseBodyData]
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterVersionsRequest(TeaModel):
    def __init__(self, cluster_type=None):
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterVersionsResponseBodyData(TeaModel):
    def __init__(self, show_name=None, cluster_type=None, code=None):
        self.show_name = show_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListClusterVersionsResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: list[ListClusterVersionsResponseBodyData]
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEngineNamespacesRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEngineNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListEngineNamespacesResponseBodyData(TeaModel):
    def __init__(self, type=None, namespace_show_name=None, quota=None, namespace=None, namespace_desc=None,
                 config_count=None, service_count=None):
        self.type = type  # type: int
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: int
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.config_count = config_count  # type: int
        self.service_count = service_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEngineNamespacesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class ListEngineNamespacesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListEngineNamespacesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEngineNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEngineNamespacesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEngineNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEngineNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEngineNamespacesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEngineNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaInstancesRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, cluster_id=None, service_name=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.cluster_id = cluster_id  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListEurekaInstancesResponseBodyData(TeaModel):
    def __init__(self, status=None, last_dirty_timestamp=None, ip_addr=None, home_page_url=None, host_name=None,
                 instance_id=None, port=None, secure_port=None, app=None, duration_in_secs=None, last_updated_timestamp=None,
                 renewal_interval_in_secs=None, vip_address=None, metadata=None):
        self.status = status  # type: str
        self.last_dirty_timestamp = last_dirty_timestamp  # type: long
        self.ip_addr = ip_addr  # type: str
        self.home_page_url = home_page_url  # type: str
        self.host_name = host_name  # type: str
        self.instance_id = instance_id  # type: str
        self.port = port  # type: int
        self.secure_port = secure_port  # type: int
        self.app = app  # type: str
        self.duration_in_secs = duration_in_secs  # type: int
        self.last_updated_timestamp = last_updated_timestamp  # type: long
        self.renewal_interval_in_secs = renewal_interval_in_secs  # type: int
        self.vip_address = vip_address  # type: str
        self.metadata = metadata  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.last_dirty_timestamp is not None:
            result['LastDirtyTimestamp'] = self.last_dirty_timestamp
        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr
        if self.home_page_url is not None:
            result['HomePageUrl'] = self.home_page_url
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.secure_port is not None:
            result['SecurePort'] = self.secure_port
        if self.app is not None:
            result['App'] = self.app
        if self.duration_in_secs is not None:
            result['DurationInSecs'] = self.duration_in_secs
        if self.last_updated_timestamp is not None:
            result['LastUpdatedTimestamp'] = self.last_updated_timestamp
        if self.renewal_interval_in_secs is not None:
            result['RenewalIntervalInSecs'] = self.renewal_interval_in_secs
        if self.vip_address is not None:
            result['VipAddress'] = self.vip_address
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LastDirtyTimestamp') is not None:
            self.last_dirty_timestamp = m.get('LastDirtyTimestamp')
        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')
        if m.get('HomePageUrl') is not None:
            self.home_page_url = m.get('HomePageUrl')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SecurePort') is not None:
            self.secure_port = m.get('SecurePort')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('DurationInSecs') is not None:
            self.duration_in_secs = m.get('DurationInSecs')
        if m.get('LastUpdatedTimestamp') is not None:
            self.last_updated_timestamp = m.get('LastUpdatedTimestamp')
        if m.get('RenewalIntervalInSecs') is not None:
            self.renewal_interval_in_secs = m.get('RenewalIntervalInSecs')
        if m.get('VipAddress') is not None:
            self.vip_address = m.get('VipAddress')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class ListEurekaInstancesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListEurekaInstancesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEurekaInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEurekaInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEurekaInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEurekaInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEurekaInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaServicesRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, cluster_id=None, region_id=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEurekaServicesResponseBodyData(TeaModel):
    def __init__(self, instances_id=None, name=None, up_status=None):
        self.instances_id = instances_id  # type: list[str]
        self.name = name  # type: str
        self.up_status = up_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances_id is not None:
            result['InstancesId'] = self.instances_id
        if self.name is not None:
            result['Name'] = self.name
        if self.up_status is not None:
            result['UpStatus'] = self.up_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstancesId') is not None:
            self.instances_id = m.get('InstancesId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpStatus') is not None:
            self.up_status = m.get('UpStatus')
        return self


class ListEurekaServicesResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, data=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.data = data  # type: list[ListEurekaServicesResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEurekaServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEurekaServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEurekaServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEurekaServicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEurekaServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByConfigRequest(TeaModel):
    def __init__(self, request_pars=None, instance_id=None, data_id=None, group=None, namespace_id=None):
        self.request_pars = request_pars  # type: str
        self.instance_id = instance_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListListenersByConfigResponseBodyListeners(TeaModel):
    def __init__(self, ip=None, md_5=None):
        self.ip = ip  # type: str
        self.md_5 = md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByConfigResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListListenersByConfigResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, listeners=None, request_id=None, message=None,
                 page_size=None, page_number=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.listeners = listeners  # type: list[ListListenersByConfigResponseBodyListeners]
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersByConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByConfigResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListListenersByConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListListenersByConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersByConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListListenersByConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByIpRequest(TeaModel):
    def __init__(self, request_pars=None, instance_id=None, ip=None, namespace_id=None):
        self.request_pars = request_pars  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListListenersByIpResponseBodyListeners(TeaModel):
    def __init__(self, md_5=None, data_id=None, group=None):
        self.md_5 = md_5  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByIpResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ListListenersByIpResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, listeners=None, request_id=None, message=None,
                 page_size=None, page_number=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.listeners = listeners  # type: list[ListListenersByIpResponseBodyListeners]
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersByIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByIpResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListListenersByIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListListenersByIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersByIpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListListenersByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosConfigsRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, instance_id=None, region_id=None,
                 data_id=None, group=None, app_name=None, tags=None, namespace_id=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.app_name = app_name  # type: str
        self.tags = tags  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNacosConfigsResponseBodyConfigurations(TeaModel):
    def __init__(self, app_name=None, data_id=None, id=None, group=None):
        self.app_name = app_name  # type: str
        self.data_id = data_id  # type: str
        self.id = id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosConfigsResponseBodyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.id is not None:
            result['Id'] = self.id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ListNacosConfigsResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, error_code=None, configurations=None, code=None, success=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.error_code = error_code  # type: str
        self.configurations = configurations  # type: list[ListNacosConfigsResponseBodyConfigurations]
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNacosConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['Configurations'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.configurations = []
        if m.get('Configurations') is not None:
            for k in m.get('Configurations'):
                temp_model = ListNacosConfigsResponseBodyConfigurations()
                self.configurations.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNacosConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNacosConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNacosConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosHistoryConfigsRequest(TeaModel):
    def __init__(self, request_pars=None, page_num=None, page_size=None, instance_id=None, region_id=None,
                 data_id=None, group=None, namespace_id=None):
        self.request_pars = request_pars  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosHistoryConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNacosHistoryConfigsResponseBodyHistoryItems(TeaModel):
    def __init__(self, app_name=None, data_id=None, group=None, last_modified_time=None, id=None, op_type=None):
        self.app_name = app_name  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.last_modified_time = last_modified_time  # type: long
        self.id = id  # type: long
        self.op_type = op_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosHistoryConfigsResponseBodyHistoryItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.id is not None:
            result['Id'] = self.id
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class ListNacosHistoryConfigsResponseBody(TeaModel):
    def __init__(self, http_code=None, total_count=None, request_id=None, message=None, page_size=None,
                 page_number=None, error_code=None, success=None, history_items=None):
        self.http_code = http_code  # type: str
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.error_code = error_code  # type: str
        self.success = success  # type: bool
        self.history_items = history_items  # type: list[ListNacosHistoryConfigsResponseBodyHistoryItems]

    def validate(self):
        if self.history_items:
            for k in self.history_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNacosHistoryConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        result['HistoryItems'] = []
        if self.history_items is not None:
            for k in self.history_items:
                result['HistoryItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k in m.get('HistoryItems'):
                temp_model = ListNacosHistoryConfigsResponseBodyHistoryItems()
                self.history_items.append(temp_model.from_map(k))
        return self


class ListNacosHistoryConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNacosHistoryConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNacosHistoryConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNacosHistoryConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZnodeChildrenRequest(TeaModel):
    def __init__(self, path=None, cluster_id=None):
        self.path = path  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZnodeChildrenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListZnodeChildrenResponseBodyData(TeaModel):
    def __init__(self, data=None, path=None, dir=None, name=None):
        self.data = data  # type: str
        self.path = path  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZnodeChildrenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListZnodeChildrenResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[ListZnodeChildrenResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListZnodeChildrenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListZnodeChildrenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZnodeChildrenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListZnodeChildrenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListZnodeChildrenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListZnodeChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBusinessLocationsResponseBodyData(TeaModel):
    def __init__(self, ordering=None, type=None, district_en_name=None, show_name=None, district_cn_name=None,
                 en_name=None, district_id=None, district_show_name=None, description=None, en_description=None,
                 cn_name=None, name=None, district_ordering=None):
        self.ordering = ordering  # type: int
        self.type = type  # type: str
        self.district_en_name = district_en_name  # type: str
        self.show_name = show_name  # type: str
        self.district_cn_name = district_cn_name  # type: str
        self.en_name = en_name  # type: str
        self.district_id = district_id  # type: str
        self.district_show_name = district_show_name  # type: str
        self.description = description  # type: str
        self.en_description = en_description  # type: str
        self.cn_name = cn_name  # type: str
        self.name = name  # type: str
        self.district_ordering = district_ordering  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBusinessLocationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ordering is not None:
            result['Ordering'] = self.ordering
        if self.type is not None:
            result['Type'] = self.type
        if self.district_en_name is not None:
            result['DistrictEnName'] = self.district_en_name
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.district_cn_name is not None:
            result['DistrictCnName'] = self.district_cn_name
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_show_name is not None:
            result['DistrictShowName'] = self.district_show_name
        if self.description is not None:
            result['Description'] = self.description
        if self.en_description is not None:
            result['EnDescription'] = self.en_description
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.name is not None:
            result['Name'] = self.name
        if self.district_ordering is not None:
            result['DistrictOrdering'] = self.district_ordering
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ordering') is not None:
            self.ordering = m.get('Ordering')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DistrictEnName') is not None:
            self.district_en_name = m.get('DistrictEnName')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('DistrictCnName') is not None:
            self.district_cn_name = m.get('DistrictCnName')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictShowName') is not None:
            self.district_show_name = m.get('DistrictShowName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnDescription') is not None:
            self.en_description = m.get('EnDescription')
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DistrictOrdering') is not None:
            self.district_ordering = m.get('DistrictOrdering')
        return self


class QueryBusinessLocationsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[QueryBusinessLocationsResponseBodyData]
        self.error_code = error_code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBusinessLocationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryBusinessLocationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBusinessLocationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryBusinessLocationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBusinessLocationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBusinessLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDetailRequest(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryClusterDetailResponseBodyDataInstanceModels(TeaModel):
    def __init__(self, pod_name=None, single_tunnel_vip=None, internet_ip=None, ip=None, role=None,
                 health_status=None):
        self.pod_name = pod_name  # type: str
        self.single_tunnel_vip = single_tunnel_vip  # type: str
        self.internet_ip = internet_ip  # type: str
        self.ip = ip  # type: str
        self.role = role  # type: str
        self.health_status = health_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyDataInstanceModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.single_tunnel_vip is not None:
            result['SingleTunnelVip'] = self.single_tunnel_vip
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.role is not None:
            result['Role'] = self.role
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('SingleTunnelVip') is not None:
            self.single_tunnel_vip = m.get('SingleTunnelVip')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        return self


class QueryClusterDetailResponseBodyData(TeaModel):
    def __init__(self, vpc_id=None, create_time=None, intranet_address=None, disk_type=None, pub_network_flow=None,
                 disk_capacity=None, memory_capacity=None, cluster_alias_name=None, instance_count=None, intranet_port=None,
                 instance_models=None, intranet_domain=None, internet_domain=None, pay_info=None, internet_address=None,
                 instance_id=None, acl_entry_list=None, health_status=None, init_cost_time=None, region_id=None, acl_id=None,
                 cpu=None, cluster_type=None, cluster_name=None, init_status=None, internet_port=None, app_version=None,
                 net_type=None, cluster_version=None, cluster_specification=None, v_switch_id=None, connection_type=None):
        self.vpc_id = vpc_id  # type: str
        self.create_time = create_time  # type: str
        self.intranet_address = intranet_address  # type: str
        self.disk_type = disk_type  # type: str
        self.pub_network_flow = pub_network_flow  # type: str
        self.disk_capacity = disk_capacity  # type: long
        self.memory_capacity = memory_capacity  # type: long
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.instance_count = instance_count  # type: int
        self.intranet_port = intranet_port  # type: str
        self.instance_models = instance_models  # type: list[QueryClusterDetailResponseBodyDataInstanceModels]
        self.intranet_domain = intranet_domain  # type: str
        self.internet_domain = internet_domain  # type: str
        self.pay_info = pay_info  # type: str
        self.internet_address = internet_address  # type: str
        self.instance_id = instance_id  # type: str
        self.acl_entry_list = acl_entry_list  # type: str
        self.health_status = health_status  # type: str
        self.init_cost_time = init_cost_time  # type: long
        self.region_id = region_id  # type: str
        self.acl_id = acl_id  # type: str
        self.cpu = cpu  # type: int
        self.cluster_type = cluster_type  # type: str
        self.cluster_name = cluster_name  # type: str
        self.init_status = init_status  # type: str
        self.internet_port = internet_port  # type: str
        self.app_version = app_version  # type: str
        self.net_type = net_type  # type: str
        self.cluster_version = cluster_version  # type: str
        self.cluster_specification = cluster_specification  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.connection_type = connection_type  # type: str

    def validate(self):
        if self.instance_models:
            for k in self.instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port
        result['InstanceModels'] = []
        if self.instance_models is not None:
            for k in self.instance_models:
                result['InstanceModels'].append(k.to_map() if k else None)
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.pay_info is not None:
            result['PayInfo'] = self.pay_info
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.init_cost_time is not None:
            result['InitCostTime'] = self.init_cost_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')
        self.instance_models = []
        if m.get('InstanceModels') is not None:
            for k in m.get('InstanceModels'):
                temp_model = QueryClusterDetailResponseBodyDataInstanceModels()
                self.instance_models.append(temp_model.from_map(k))
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('PayInfo') is not None:
            self.pay_info = m.get('PayInfo')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InitCostTime') is not None:
            self.init_cost_time = m.get('InitCostTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        return self


class QueryClusterDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryClusterDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDiskSpecificationRequest(TeaModel):
    def __init__(self, cluster_type=None):
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class QueryClusterDiskSpecificationResponseBodyData(TeaModel):
    def __init__(self, step=None, max=None, min=None):
        self.step = step  # type: int
        self.max = max  # type: int
        self.min = min  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        return self


class QueryClusterDiskSpecificationResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None,
                 dynamic_message=None, code=None, success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: QueryClusterDiskSpecificationResponseBodyData
        self.error_code = error_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = QueryClusterDiskSpecificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDiskSpecificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryClusterDiskSpecificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterDiskSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterSpecificationResponseBodyData(TeaModel):
    def __init__(self, cluster_specification_name=None, disk_capacity=None, memory_capacity=None,
                 instance_count=None, max_tps=None, max_con=None, cpu_capacity=None):
        self.cluster_specification_name = cluster_specification_name  # type: str
        self.disk_capacity = disk_capacity  # type: str
        self.memory_capacity = memory_capacity  # type: str
        self.instance_count = instance_count  # type: str
        self.max_tps = max_tps  # type: str
        self.max_con = max_con  # type: str
        self.cpu_capacity = cpu_capacity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterSpecificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_specification_name is not None:
            result['ClusterSpecificationName'] = self.cluster_specification_name
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.max_con is not None:
            result['MaxCon'] = self.max_con
        if self.cpu_capacity is not None:
            result['CpuCapacity'] = self.cpu_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterSpecificationName') is not None:
            self.cluster_specification_name = m.get('ClusterSpecificationName')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('MaxCon') is not None:
            self.max_con = m.get('MaxCon')
        if m.get('CpuCapacity') is not None:
            self.cpu_capacity = m.get('CpuCapacity')
        return self


class QueryClusterSpecificationResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, http_status_code=None, data=None, error_code=None, code=None,
                 success=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.data = data  # type: list[QueryClusterSpecificationResponseBodyData]
        self.error_code = error_code  # type: str
        self.code = code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryClusterSpecificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryClusterSpecificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterSpecificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryClusterSpecificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryClusterSpecificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryClusterSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConfigRequest(TeaModel):
    def __init__(self, request_pars=None, cluster_id=None, config_type=None, instance_id=None):
        self.request_pars = request_pars  # type: str
        self.cluster_id = cluster_id  # type: str
        self.config_type = config_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryConfigResponseBodyData(TeaModel):
    def __init__(self, max_client_cnxns=None, config_auth_supported=None, init_limit=None, mcpenabled=None,
                 open_super_acl=None, restart_flag=None, jvm_flags_custom=None, autopurge_purge_interval=None,
                 autopurge_snap_retain_count=None, sync_limit=None, config_auth_enabled=None, cluster_name=None, mcpsupported=None,
                 jute_maxbuffer=None, tick_time=None, pass_word=None, user_name=None):
        self.max_client_cnxns = max_client_cnxns  # type: str
        self.config_auth_supported = config_auth_supported  # type: bool
        self.init_limit = init_limit  # type: str
        self.mcpenabled = mcpenabled  # type: bool
        self.open_super_acl = open_super_acl  # type: bool
        self.restart_flag = restart_flag  # type: bool
        self.jvm_flags_custom = jvm_flags_custom  # type: str
        self.autopurge_purge_interval = autopurge_purge_interval  # type: str
        self.autopurge_snap_retain_count = autopurge_snap_retain_count  # type: str
        self.sync_limit = sync_limit  # type: str
        self.config_auth_enabled = config_auth_enabled  # type: bool
        self.cluster_name = cluster_name  # type: str
        self.mcpsupported = mcpsupported  # type: bool
        self.jute_maxbuffer = jute_maxbuffer  # type: str
        self.tick_time = tick_time  # type: str
        self.pass_word = pass_word  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.config_auth_supported is not None:
            result['ConfigAuthSupported'] = self.config_auth_supported
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.restart_flag is not None:
            result['RestartFlag'] = self.restart_flag
        if self.jvm_flags_custom is not None:
            result['JvmFlagsCustom'] = self.jvm_flags_custom
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.mcpsupported is not None:
            result['MCPSupported'] = self.mcpsupported
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('ConfigAuthSupported') is not None:
            self.config_auth_supported = m.get('ConfigAuthSupported')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('RestartFlag') is not None:
            self.restart_flag = m.get('RestartFlag')
        if m.get('JvmFlagsCustom') is not None:
            self.jvm_flags_custom = m.get('JvmFlagsCustom')
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MCPSupported') is not None:
            self.mcpsupported = m.get('MCPSupported')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryConfigResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorRequest(TeaModel):
    def __init__(self, request_pars=None, monitor_type=None, start_time=None, end_time=None, step=None,
                 instance_id=None):
        self.request_pars = request_pars  # type: str
        self.monitor_type = monitor_type  # type: str
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.step = step  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.step is not None:
            result['Step'] = self.step
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryMonitorResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonitorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryZnodeDetailRequest(TeaModel):
    def __init__(self, request_pars=None, cluster_id=None, path=None):
        self.request_pars = request_pars  # type: str
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryZnodeDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class QueryZnodeDetailResponseBodyData(TeaModel):
    def __init__(self, data=None, path=None, dir=None, name=None):
        self.data = data  # type: str
        self.path = path  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryZnodeDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryZnodeDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryZnodeDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryZnodeDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryZnodeDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryZnodeDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryZnodeDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryZnodeDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryZnodeDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartClusterRequest(TeaModel):
    def __init__(self, request_pars=None, instance_id=None, cluster_id=None):
        self.request_pars = request_pars  # type: str
        self.instance_id = instance_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class RestartClusterResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryClusterRequest(TeaModel):
    def __init__(self, request_pars=None, instance_id=None):
        self.request_pars = request_pars  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RetryClusterResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RetryClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScalingClusterRequest(TeaModel):
    def __init__(self, instance_count=None, cpu=None, memory_capacity=None, cluster_specification=None,
                 instance_id=None):
        self.instance_count = instance_count  # type: int
        self.cpu = cpu  # type: int
        self.memory_capacity = memory_capacity  # type: long
        self.cluster_specification = cluster_specification  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ScalingClusterResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScalingClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ScalingClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScalingClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ScalingClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclRequest(TeaModel):
    def __init__(self, acl_entry_list=None, instance_id=None):
        self.acl_entry_list = acl_entry_list  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAclResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAclResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(self, request_pars=None, cluster_alias_name=None, instance_id=None):
        self.request_pars = request_pars  # type: str
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRequest(TeaModel):
    def __init__(self, request_pars=None, cluster_id=None, config_type=None, tick_time=None, init_limit=None,
                 sync_limit=None, max_client_cnxns=None, open_super_acl=None, user_name=None, pass_word=None,
                 jute_maxbuffer=None, autopurge_purge_interval=None, autopurge_snap_retain_count=None, config_auth_enabled=None,
                 mcpenabled=None, instance_id=None):
        self.request_pars = request_pars  # type: str
        self.cluster_id = cluster_id  # type: str
        self.config_type = config_type  # type: str
        self.tick_time = tick_time  # type: str
        self.init_limit = init_limit  # type: str
        self.sync_limit = sync_limit  # type: str
        self.max_client_cnxns = max_client_cnxns  # type: str
        self.open_super_acl = open_super_acl  # type: str
        self.user_name = user_name  # type: str
        self.pass_word = pass_word  # type: str
        self.jute_maxbuffer = jute_maxbuffer  # type: str
        self.autopurge_purge_interval = autopurge_purge_interval  # type: str
        self.autopurge_snap_retain_count = autopurge_snap_retain_count  # type: str
        self.config_auth_enabled = config_auth_enabled  # type: bool
        self.mcpenabled = mcpenabled  # type: bool
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateConfigResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEngineNamespaceRequest(TeaModel):
    def __init__(self, name=None, desc=None, service_count=None, id=None, cluster_id=None, instance_id=None):
        self.name = name  # type: str
        self.desc = desc  # type: str
        self.service_count = service_count  # type: int
        self.id = id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEngineNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        if self.id is not None:
            result['Id'] = self.id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(self, type=None, namespace_show_name=None, quota=None, namespace=None, namespace_desc=None,
                 config_count=None):
        self.type = type  # type: int
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: int
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.config_count = config_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEngineNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        return self


class UpdateEngineNamespaceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: UpdateEngineNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateEngineNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = UpdateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEngineNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEngineNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEngineNamespaceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosConfigRequest(TeaModel):
    def __init__(self, instance_id=None, data_id=None, group=None, app_name=None, tags=None, desc=None, type=None,
                 content=None, namespace_id=None, md_5=None, beta_ips=None):
        self.instance_id = instance_id  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.app_name = app_name  # type: str
        self.tags = tags  # type: str
        self.desc = desc  # type: str
        self.type = type  # type: str
        self.content = content  # type: str
        self.namespace_id = namespace_id  # type: str
        self.md_5 = md_5  # type: str
        self.beta_ips = beta_ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        if self.content is not None:
            result['Content'] = self.content
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        return self


class UpdateNacosConfigResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNacosConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, service_name=None, group_name=None, namespace_id=None, cluster_name=None,
                 ip=None, port=None, ephemeral=None, weight=None, enabled=None, metadata=None):
        # 实例id
        self.instance_id = instance_id  # type: str
        # 服务名
        self.service_name = service_name  # type: str
        # 分组名
        self.group_name = group_name  # type: str
        # 命名空间id
        self.namespace_id = namespace_id  # type: str
        # Nacos集群名
        self.cluster_name = cluster_name  # type: str
        # Nacos实例ip
        self.ip = ip  # type: str
        # Nacos实例端口
        self.port = port  # type: int
        # 临时节点标志
        self.ephemeral = ephemeral  # type: bool
        # 权重
        self.weight = weight  # type: str
        # 服务禁用标志
        self.enabled = enabled  # type: bool
        # 节点元数据
        self.metadata = metadata  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        return self


class UpdateNacosInstanceResponseBody(TeaModel):
    def __init__(self, http_status_code=None, request_id=None, message=None, code=None, success=None, data=None):
        # http状态码
        self.http_status_code = http_status_code  # type: int
        # 请求id
        self.request_id = request_id  # type: str
        # 响应信息
        self.message = message  # type: str
        # 响应码
        self.code = code  # type: int
        # 成功标志
        self.success = success  # type: bool
        # 修改结果
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateNacosInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateNacosInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNacosInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNacosInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZnodeRequest(TeaModel):
    def __init__(self, request_pars=None, cluster_id=None, path=None, data=None):
        self.request_pars = request_pars  # type: str
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateZnodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateZnodeResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, error_code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateZnodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateZnodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateZnodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateZnodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(self, request_pars=None, instance_id=None, upgrade_version=None):
        self.request_pars = request_pars  # type: str
        self.instance_id = instance_id  # type: str
        self.upgrade_version = upgrade_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')
        return self


class UpgradeClusterResponseBody(TeaModel):
    def __init__(self, http_code=None, message=None, request_id=None, error_code=None, success=None):
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


