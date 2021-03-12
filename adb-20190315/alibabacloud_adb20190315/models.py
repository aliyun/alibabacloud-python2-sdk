# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class ModifyClusterConnectionStringRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, connection_string_prefix=None, current_connection_string=None, port=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.connection_string_prefix = TeaConverter.to_unicode(connection_string_prefix)  # type: unicode
        self.current_connection_string = TeaConverter.to_unicode(current_connection_string)  # type: unicode
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyClusterConnectionStringResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyClusterConnectionStringResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyClusterConnectionStringResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyClusterConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[unicode]
        self.tag_key = tag_key  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, account_name=None, account_description=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_description = TeaConverter.to_unicode(account_description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAccountDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticDailyPlanRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, elastic_plan_name=None, resource_pool_name=None, elastic_daily_plan_day=None,
                 elastic_daily_plan_status_list=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.elastic_plan_name = TeaConverter.to_unicode(elastic_plan_name)  # type: unicode
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.elastic_daily_plan_day = TeaConverter.to_unicode(elastic_daily_plan_day)  # type: unicode
        self.elastic_daily_plan_status_list = TeaConverter.to_unicode(elastic_daily_plan_status_list)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.elastic_daily_plan_day is not None:
            result['ElasticDailyPlanDay'] = self.elastic_daily_plan_day
        if self.elastic_daily_plan_status_list is not None:
            result['ElasticDailyPlanStatusList'] = self.elastic_daily_plan_status_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('ElasticDailyPlanDay') is not None:
            self.elastic_daily_plan_day = m.get('ElasticDailyPlanDay')
        if m.get('ElasticDailyPlanStatusList') is not None:
            self.elastic_daily_plan_status_list = m.get('ElasticDailyPlanStatusList')
        return self


class DescribeElasticDailyPlanResponseBodyElasticDailyPlanList(TeaModel):
    def __init__(self, status=None, day=None, resource_pool_name=None, start_ts=None, plan_end_ts=None,
                 plan_start_ts=None, elastic_node_num=None, end_ts=None, plan_name=None):
        self.status = status  # type: int
        self.day = TeaConverter.to_unicode(day)  # type: unicode
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.start_ts = TeaConverter.to_unicode(start_ts)  # type: unicode
        self.plan_end_ts = TeaConverter.to_unicode(plan_end_ts)  # type: unicode
        self.plan_start_ts = TeaConverter.to_unicode(plan_start_ts)  # type: unicode
        self.elastic_node_num = elastic_node_num  # type: int
        self.end_ts = TeaConverter.to_unicode(end_ts)  # type: unicode
        self.plan_name = TeaConverter.to_unicode(plan_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.day is not None:
            result['Day'] = self.day
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.plan_end_ts is not None:
            result['PlanEndTs'] = self.plan_end_ts
        if self.plan_start_ts is not None:
            result['PlanStartTs'] = self.plan_start_ts
        if self.elastic_node_num is not None:
            result['ElasticNodeNum'] = self.elastic_node_num
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('PlanEndTs') is not None:
            self.plan_end_ts = m.get('PlanEndTs')
        if m.get('PlanStartTs') is not None:
            self.plan_start_ts = m.get('PlanStartTs')
        if m.get('ElasticNodeNum') is not None:
            self.elastic_node_num = m.get('ElasticNodeNum')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        return self


class DescribeElasticDailyPlanResponseBody(TeaModel):
    def __init__(self, request_id=None, elastic_daily_plan_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.elastic_daily_plan_list = elastic_daily_plan_list  # type: list[DescribeElasticDailyPlanResponseBodyElasticDailyPlanList]

    def validate(self):
        if self.elastic_daily_plan_list:
            for k in self.elastic_daily_plan_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ElasticDailyPlanList'] = []
        if self.elastic_daily_plan_list is not None:
            for k in self.elastic_daily_plan_list:
                result['ElasticDailyPlanList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.elastic_daily_plan_list = []
        if m.get('ElasticDailyPlanList') is not None:
            for k in m.get('ElasticDailyPlanList'):
                temp_model = DescribeElasticDailyPlanResponseBodyElasticDailyPlanList()
                self.elastic_daily_plan_list.append(temp_model.from_map(k))
        return self


class DescribeElasticDailyPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeElasticDailyPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeElasticDailyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoRenewAttributeRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, region_id=None, renewal_status=None, duration=None, period_unit=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.renewal_status = TeaConverter.to_unicode(renewal_status)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.period_unit = TeaConverter.to_unicode(period_unit)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class ModifyAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None, dbcluster_id=None):
        self.task_id = task_id  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DeleteDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPlanRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, process_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        return self


class DescribeSQLPlanResponseBodyStageList(TeaModel):
    def __init__(self, state=None, cputime_avg=None, cputime_max=None, operator_cost=None, scan_time_max=None,
                 input_size_max=None, stage_id=None, scan_size_max=None, cputime_min=None, scan_time_min=None, scan_size_min=None,
                 input_size_min=None, peak_memory=None, scan_time_avg=None, scan_size_avg=None, input_size_avg=None):
        self.state = TeaConverter.to_unicode(state)  # type: unicode
        self.cputime_avg = cputime_avg  # type: long
        self.cputime_max = cputime_max  # type: long
        self.operator_cost = operator_cost  # type: long
        self.scan_time_max = scan_time_max  # type: long
        self.input_size_max = input_size_max  # type: long
        self.stage_id = stage_id  # type: int
        self.scan_size_max = scan_size_max  # type: long
        self.cputime_min = cputime_min  # type: long
        self.scan_time_min = scan_time_min  # type: long
        self.scan_size_min = scan_size_min  # type: long
        self.input_size_min = input_size_min  # type: long
        self.peak_memory = peak_memory  # type: long
        self.scan_time_avg = scan_time_avg  # type: long
        self.scan_size_avg = scan_size_avg  # type: long
        self.input_size_avg = input_size_avg  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.cputime_avg is not None:
            result['CPUTimeAvg'] = self.cputime_avg
        if self.cputime_max is not None:
            result['CPUTimeMax'] = self.cputime_max
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.scan_time_max is not None:
            result['ScanTimeMax'] = self.scan_time_max
        if self.input_size_max is not None:
            result['InputSizeMax'] = self.input_size_max
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.scan_size_max is not None:
            result['ScanSizeMax'] = self.scan_size_max
        if self.cputime_min is not None:
            result['CPUTimeMin'] = self.cputime_min
        if self.scan_time_min is not None:
            result['ScanTimeMin'] = self.scan_time_min
        if self.scan_size_min is not None:
            result['ScanSizeMin'] = self.scan_size_min
        if self.input_size_min is not None:
            result['InputSizeMin'] = self.input_size_min
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.scan_time_avg is not None:
            result['ScanTimeAvg'] = self.scan_time_avg
        if self.scan_size_avg is not None:
            result['ScanSizeAvg'] = self.scan_size_avg
        if self.input_size_avg is not None:
            result['InputSizeAvg'] = self.input_size_avg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CPUTimeAvg') is not None:
            self.cputime_avg = m.get('CPUTimeAvg')
        if m.get('CPUTimeMax') is not None:
            self.cputime_max = m.get('CPUTimeMax')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('ScanTimeMax') is not None:
            self.scan_time_max = m.get('ScanTimeMax')
        if m.get('InputSizeMax') is not None:
            self.input_size_max = m.get('InputSizeMax')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('ScanSizeMax') is not None:
            self.scan_size_max = m.get('ScanSizeMax')
        if m.get('CPUTimeMin') is not None:
            self.cputime_min = m.get('CPUTimeMin')
        if m.get('ScanTimeMin') is not None:
            self.scan_time_min = m.get('ScanTimeMin')
        if m.get('ScanSizeMin') is not None:
            self.scan_size_min = m.get('ScanSizeMin')
        if m.get('InputSizeMin') is not None:
            self.input_size_min = m.get('InputSizeMin')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ScanTimeAvg') is not None:
            self.scan_time_avg = m.get('ScanTimeAvg')
        if m.get('ScanSizeAvg') is not None:
            self.scan_size_avg = m.get('ScanSizeAvg')
        if m.get('InputSizeAvg') is not None:
            self.input_size_avg = m.get('InputSizeAvg')
        return self


class DescribeSQLPlanResponseBodyDetail(TeaModel):
    def __init__(self, sql=None, output_size=None, state=None, output_rows=None, user=None, start_time=None,
                 total_stage=None, queued_time=None, total_time=None, total_task=None, database=None, peak_memory=None,
                 client_ip=None, planning_time=None, cputime=None):
        self.sql = TeaConverter.to_unicode(sql)  # type: unicode
        self.output_size = output_size  # type: long
        self.state = TeaConverter.to_unicode(state)  # type: unicode
        self.output_rows = output_rows  # type: long
        self.user = TeaConverter.to_unicode(user)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.total_stage = total_stage  # type: long
        self.queued_time = queued_time  # type: long
        self.total_time = total_time  # type: long
        self.total_task = total_task  # type: long
        self.database = TeaConverter.to_unicode(database)  # type: unicode
        self.peak_memory = peak_memory  # type: long
        self.client_ip = TeaConverter.to_unicode(client_ip)  # type: unicode
        self.planning_time = planning_time  # type: long
        self.cputime = cputime  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.output_size is not None:
            result['OutputSize'] = self.output_size
        if self.state is not None:
            result['State'] = self.state
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.user is not None:
            result['User'] = self.user
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_stage is not None:
            result['TotalStage'] = self.total_stage
        if self.queued_time is not None:
            result['QueuedTime'] = self.queued_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.total_task is not None:
            result['TotalTask'] = self.total_task
        if self.database is not None:
            result['Database'] = self.database
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.planning_time is not None:
            result['PlanningTime'] = self.planning_time
        if self.cputime is not None:
            result['CPUTime'] = self.cputime
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalStage') is not None:
            self.total_stage = m.get('TotalStage')
        if m.get('QueuedTime') is not None:
            self.queued_time = m.get('QueuedTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('TotalTask') is not None:
            self.total_task = m.get('TotalTask')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('PlanningTime') is not None:
            self.planning_time = m.get('PlanningTime')
        if m.get('CPUTime') is not None:
            self.cputime = m.get('CPUTime')
        return self


class DescribeSQLPlanResponseBody(TeaModel):
    def __init__(self, request_id=None, stage_list=None, origin_info=None, detail=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.stage_list = stage_list  # type: list[DescribeSQLPlanResponseBodyStageList]
        self.origin_info = TeaConverter.to_unicode(origin_info)  # type: unicode
        self.detail = detail  # type: DescribeSQLPlanResponseBodyDetail

    def validate(self):
        if self.stage_list:
            for k in self.stage_list:
                if k:
                    k.validate()
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StageList'] = []
        if self.stage_list is not None:
            for k in self.stage_list:
                result['StageList'].append(k.to_map() if k else None)
        if self.origin_info is not None:
            result['OriginInfo'] = self.origin_info
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stage_list = []
        if m.get('StageList') is not None:
            for k in m.get('StageList'):
                temp_model = DescribeSQLPlanResponseBodyStageList()
                self.stage_list.append(temp_model.from_map(k))
        if m.get('OriginInfo') is not None:
            self.origin_info = m.get('OriginInfo')
        if m.get('Detail') is not None:
            temp_model = DescribeSQLPlanResponseBodyDetail()
            self.detail = temp_model.from_map(m['Detail'])
        return self


class DescribeSQLPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSQLPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSQLPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, account_name=None, account_password=None, account_description=None, account_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode
        self.account_description = TeaConverter.to_unicode(account_description)  # type: unicode
        self.account_type = TeaConverter.to_unicode(account_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None, dbcluster_id=None):
        self.task_id = task_id  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOperatorPermissionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeOperatorPermissionResponseBody(TeaModel):
    def __init__(self, created_time=None, request_id=None, privileges=None, expired_time=None, dbcluster_id=None):
        self.created_time = TeaConverter.to_unicode(created_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.privileges = TeaConverter.to_unicode(privileges)  # type: unicode
        self.expired_time = TeaConverter.to_unicode(expired_time)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.privileges is not None:
            result['Privileges'] = self.privileges
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeOperatorPermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeOperatorPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeOperatorPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProcessListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, show_full=None, running_time=None, user=None, keyword=None, order=None, page_size=None,
                 page_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.show_full = show_full  # type: bool
        self.running_time = running_time  # type: int
        self.user = TeaConverter.to_unicode(user)  # type: unicode
        self.keyword = TeaConverter.to_unicode(keyword)  # type: unicode
        self.order = TeaConverter.to_unicode(order)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.show_full is not None:
            result['ShowFull'] = self.show_full
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.user is not None:
            result['User'] = self.user
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ShowFull') is not None:
            self.show_full = m.get('ShowFull')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeProcessListResponseBodyItemsProcess(TeaModel):
    def __init__(self, start_time=None, time=None, process_id=None, host=None, db=None, command=None, user=None,
                 id=None, info=None):
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.time = time  # type: int
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode
        self.host = TeaConverter.to_unicode(host)  # type: unicode
        self.db = TeaConverter.to_unicode(db)  # type: unicode
        self.command = TeaConverter.to_unicode(command)  # type: unicode
        self.user = TeaConverter.to_unicode(user)  # type: unicode
        self.id = id  # type: int
        self.info = TeaConverter.to_unicode(info)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time is not None:
            result['Time'] = self.time
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.host is not None:
            result['Host'] = self.host
        if self.db is not None:
            result['DB'] = self.db
        if self.command is not None:
            result['Command'] = self.command
        if self.user is not None:
            result['User'] = self.user
        if self.id is not None:
            result['Id'] = self.id
        if self.info is not None:
            result['Info'] = self.info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('DB') is not None:
            self.db = m.get('DB')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        return self


class DescribeProcessListResponseBodyItems(TeaModel):
    def __init__(self, process=None):
        self.process = process  # type: list[DescribeProcessListResponseBodyItemsProcess]

    def validate(self):
        if self.process:
            for k in self.process:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Process'] = []
        if self.process is not None:
            for k in self.process:
                result['Process'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.process = []
        if m.get('Process') is not None:
            for k in m.get('Process'):
                temp_model = DescribeProcessListResponseBodyItemsProcess()
                self.process.append(temp_model.from_map(k))
        return self


class DescribeProcessListResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, items=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.items = items  # type: DescribeProcessListResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeProcessListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeProcessListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeProcessListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeProcessListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTableStatisticsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, page_size=None, page_number=None, order=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.order = TeaConverter.to_unicode(order)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class DescribeTableStatisticsResponseBodyItemsTableStatisticRecords(TeaModel):
    def __init__(self, schema_name=None, table_name=None, row_count=None, data_size=None, index_size=None,
                 primary_key_index_size=None, partition_count=None, cold_data_size=None):
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.row_count = row_count  # type: long
        self.data_size = data_size  # type: long
        self.index_size = index_size  # type: long
        self.primary_key_index_size = primary_key_index_size  # type: long
        self.partition_count = partition_count  # type: long
        self.cold_data_size = cold_data_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.index_size is not None:
            result['IndexSize'] = self.index_size
        if self.primary_key_index_size is not None:
            result['PrimaryKeyIndexSize'] = self.primary_key_index_size
        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count
        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')
        if m.get('PrimaryKeyIndexSize') is not None:
            self.primary_key_index_size = m.get('PrimaryKeyIndexSize')
        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')
        if m.get('ColdDataSize') is not None:
            self.cold_data_size = m.get('ColdDataSize')
        return self


class DescribeTableStatisticsResponseBodyItems(TeaModel):
    def __init__(self, table_statistic_records=None):
        self.table_statistic_records = table_statistic_records  # type: list[DescribeTableStatisticsResponseBodyItemsTableStatisticRecords]

    def validate(self):
        if self.table_statistic_records:
            for k in self.table_statistic_records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TableStatisticRecords'] = []
        if self.table_statistic_records is not None:
            for k in self.table_statistic_records:
                result['TableStatisticRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table_statistic_records = []
        if m.get('TableStatisticRecords') is not None:
            for k in m.get('TableStatisticRecords'):
                temp_model = DescribeTableStatisticsResponseBodyItemsTableStatisticRecords()
                self.table_statistic_records.append(temp_model.from_map(k))
        return self


class DescribeTableStatisticsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, dbcluster_id=None,
                 items=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.items = items  # type: DescribeTableStatisticsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Items') is not None:
            temp_model = DescribeTableStatisticsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeTableStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTableStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeTableStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteElasticPlanRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, elastic_plan_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.elastic_plan_name = TeaConverter.to_unicode(elastic_plan_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        return self


class DeleteElasticPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteElasticPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteElasticPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDBResourcePoolWithUserRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, pool_name=None, pool_user=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode
        self.pool_user = TeaConverter.to_unicode(pool_user)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.pool_user is not None:
            result['PoolUser'] = self.pool_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('PoolUser') is not None:
            self.pool_user = m.get('PoolUser')
        return self


class UnbindDBResourcePoolWithUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindDBResourcePoolWithUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UnbindDBResourcePoolWithUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UnbindDBResourcePoolWithUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPlanTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, process_id=None, stage_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode
        self.stage_id = TeaConverter.to_unicode(stage_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        return self


class DescribeSQLPlanTaskResponseBodyTaskList(TeaModel):
    def __init__(self, scan_cost=None, output_size=None, input_size=None, state=None, operator_cost=None,
                 output_rows=None, scan_size=None, elapsed_time=None, scan_rows=None, peak_memory=None, task_id=None,
                 input_rows=None):
        self.scan_cost = scan_cost  # type: long
        self.output_size = output_size  # type: long
        self.input_size = input_size  # type: long
        self.state = TeaConverter.to_unicode(state)  # type: unicode
        self.operator_cost = operator_cost  # type: long
        self.output_rows = output_rows  # type: long
        self.scan_size = scan_size  # type: long
        self.elapsed_time = elapsed_time  # type: long
        self.scan_rows = scan_rows  # type: long
        self.peak_memory = peak_memory  # type: long
        self.task_id = task_id  # type: int
        self.input_rows = input_rows  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scan_cost is not None:
            result['ScanCost'] = self.scan_cost
        if self.output_size is not None:
            result['OutputSize'] = self.output_size
        if self.input_size is not None:
            result['InputSize'] = self.input_size
        if self.state is not None:
            result['State'] = self.state
        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost
        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScanCost') is not None:
            self.scan_cost = m.get('ScanCost')
        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')
        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')
        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')
        return self


class DescribeSQLPlanTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.task_list = task_list  # type: list[DescribeSQLPlanTaskResponseBodyTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = DescribeSQLPlanTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class DescribeSQLPlanTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSQLPlanTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSQLPlanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, preferred_backup_time=None, preferred_backup_period=None, backup_retention_period=None,
                 enable_backup_log=None, log_backup_retention_period=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.preferred_backup_time = TeaConverter.to_unicode(preferred_backup_time)  # type: unicode
        self.preferred_backup_period = TeaConverter.to_unicode(preferred_backup_period)  # type: unicode
        self.backup_retention_period = TeaConverter.to_unicode(backup_retention_period)  # type: unicode
        self.enable_backup_log = TeaConverter.to_unicode(enable_backup_log)  # type: unicode
        self.log_backup_retention_period = log_backup_retention_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogRecordsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, region_id=None, start_time=None, end_time=None, dbname=None, query_keyword=None,
                 sql_type=None, succeed=None, host_address=None, order_type=None, user=None, page_size=None, page_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.query_keyword = TeaConverter.to_unicode(query_keyword)  # type: unicode
        self.sql_type = TeaConverter.to_unicode(sql_type)  # type: unicode
        self.succeed = TeaConverter.to_unicode(succeed)  # type: unicode
        self.host_address = TeaConverter.to_unicode(host_address)  # type: unicode
        self.order_type = TeaConverter.to_unicode(order_type)  # type: unicode
        self.user = TeaConverter.to_unicode(user)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.user is not None:
            result['User'] = self.user
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeAuditLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, host_address=None, succeed=None, sqltext=None, total_time=None, conn_id=None, dbname=None,
                 sqltype=None, execute_time=None, process_id=None):
        self.host_address = TeaConverter.to_unicode(host_address)  # type: unicode
        self.succeed = TeaConverter.to_unicode(succeed)  # type: unicode
        self.sqltext = TeaConverter.to_unicode(sqltext)  # type: unicode
        self.total_time = TeaConverter.to_unicode(total_time)  # type: unicode
        self.conn_id = TeaConverter.to_unicode(conn_id)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.sqltype = TeaConverter.to_unicode(sqltype)  # type: unicode
        self.execute_time = TeaConverter.to_unicode(execute_time)  # type: unicode
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.conn_id is not None:
            result['ConnId'] = self.conn_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('ConnId') is not None:
            self.conn_id = m.get('ConnId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        return self


class DescribeAuditLogRecordsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, dbcluster_id=None,
                 items=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.items = items  # type: list[DescribeAuditLogRecordsResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeAuditLogRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeAuditLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAuditLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAuditLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBClusterRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, zone_id=None, dbcluster_version=None, dbcluster_category=None, dbcluster_class=None,
                 dbnode_group_count=None, dbnode_storage=None, dbcluster_network_type=None, dbcluster_description=None, pay_type=None,
                 period=None, used_time=None, vpcid=None, v_switch_id=None, client_token=None, executor_count=None,
                 resource_group_id=None, mode=None, storage_resource=None, storage_type=None, compute_resource=None,
                 restore_type=None, source_dbinstance_name=None, backup_set_id=None, restore_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.dbcluster_version = TeaConverter.to_unicode(dbcluster_version)  # type: unicode
        self.dbcluster_category = TeaConverter.to_unicode(dbcluster_category)  # type: unicode
        self.dbcluster_class = TeaConverter.to_unicode(dbcluster_class)  # type: unicode
        self.dbnode_group_count = TeaConverter.to_unicode(dbnode_group_count)  # type: unicode
        self.dbnode_storage = TeaConverter.to_unicode(dbnode_storage)  # type: unicode
        self.dbcluster_network_type = TeaConverter.to_unicode(dbcluster_network_type)  # type: unicode
        self.dbcluster_description = TeaConverter.to_unicode(dbcluster_description)  # type: unicode
        self.pay_type = TeaConverter.to_unicode(pay_type)  # type: unicode
        self.period = TeaConverter.to_unicode(period)  # type: unicode
        self.used_time = TeaConverter.to_unicode(used_time)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.executor_count = TeaConverter.to_unicode(executor_count)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.storage_resource = TeaConverter.to_unicode(storage_resource)  # type: unicode
        self.storage_type = TeaConverter.to_unicode(storage_type)  # type: unicode
        self.compute_resource = TeaConverter.to_unicode(compute_resource)  # type: unicode
        self.restore_type = TeaConverter.to_unicode(restore_type)  # type: unicode
        self.source_dbinstance_name = TeaConverter.to_unicode(source_dbinstance_name)  # type: unicode
        self.backup_set_id = TeaConverter.to_unicode(backup_set_id)  # type: unicode
        self.restore_time = TeaConverter.to_unicode(restore_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version
        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type
        if self.source_dbinstance_name is not None:
            result['SourceDBInstanceName'] = self.source_dbinstance_name
        if self.backup_set_id is not None:
            result['BackupSetID'] = self.backup_set_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')
        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')
        if m.get('SourceDBInstanceName') is not None:
            self.source_dbinstance_name = m.get('SourceDBInstanceName')
        if m.get('BackupSetID') is not None:
            self.backup_set_id = m.get('BackupSetID')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        return self


class CreateDBClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_group_id=None, dbcluster_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterResourceGroupRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, new_resource_group_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.new_resource_group_id = TeaConverter.to_unicode(new_resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        return self


class ModifyDBClusterResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBClusterResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBClusterResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindDBResourcePoolWithUserRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, pool_name=None, pool_user=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode
        self.pool_user = TeaConverter.to_unicode(pool_user)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.pool_user is not None:
            result['PoolUser'] = self.pool_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('PoolUser') is not None:
            self.pool_user = m.get('PoolUser')
        return self


class BindDBResourcePoolWithUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindDBResourcePoolWithUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BindDBResourcePoolWithUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = BindDBResourcePoolWithUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSchemasRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeSchemasResponseBodyItemsSchema(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None):
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeSchemasResponseBodyItems(TeaModel):
    def __init__(self, schema=None):
        self.schema = schema  # type: list[DescribeSchemasResponseBodyItemsSchema]

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeSchemasResponseBodyItemsSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeSchemasResponseBody(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeSchemasResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeSchemasResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSchemasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSchemasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterMaintainTimeRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, maintain_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.maintain_time = TeaConverter.to_unicode(maintain_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        return self


class ModifyDBClusterMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBClusterMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBClusterMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectionCountRecordsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeConnectionCountRecordsResponseBodyAccessIpRecords(TeaModel):
    def __init__(self, access_ip=None, count=None):
        self.access_ip = TeaConverter.to_unicode(access_ip)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeConnectionCountRecordsResponseBodyUserRecords(TeaModel):
    def __init__(self, user=None, count=None):
        self.user = TeaConverter.to_unicode(user)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeConnectionCountRecordsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, dbcluster_id=None, access_ip_records=None,
                 user_records=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.access_ip_records = access_ip_records  # type: list[DescribeConnectionCountRecordsResponseBodyAccessIpRecords]
        self.user_records = user_records  # type: list[DescribeConnectionCountRecordsResponseBodyUserRecords]

    def validate(self):
        if self.access_ip_records:
            for k in self.access_ip_records:
                if k:
                    k.validate()
        if self.user_records:
            for k in self.user_records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['AccessIpRecords'] = []
        if self.access_ip_records is not None:
            for k in self.access_ip_records:
                result['AccessIpRecords'].append(k.to_map() if k else None)
        result['UserRecords'] = []
        if self.user_records is not None:
            for k in self.user_records:
                result['UserRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.access_ip_records = []
        if m.get('AccessIpRecords') is not None:
            for k in m.get('AccessIpRecords'):
                temp_model = DescribeConnectionCountRecordsResponseBodyAccessIpRecords()
                self.access_ip_records.append(temp_model.from_map(k))
        self.user_records = []
        if m.get('UserRecords') is not None:
            for k in m.get('UserRecords'):
                temp_model = DescribeConnectionCountRecordsResponseBodyUserRecords()
                self.user_records.append(temp_model.from_map(k))
        return self


class DescribeConnectionCountRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeConnectionCountRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeConnectionCountRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, backup_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeBackupsResponseBodyItemsBackup(TeaModel):
    def __init__(self, dbcluster_id=None, backup_type=None, backup_start_time=None, backup_size=None,
                 backup_end_time=None, backup_id=None, backup_method=None):
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.backup_type = TeaConverter.to_unicode(backup_type)  # type: unicode
        self.backup_start_time = TeaConverter.to_unicode(backup_start_time)  # type: unicode
        self.backup_size = backup_size  # type: int
        self.backup_end_time = TeaConverter.to_unicode(backup_end_time)  # type: unicode
        self.backup_id = TeaConverter.to_unicode(backup_id)  # type: unicode
        self.backup_method = TeaConverter.to_unicode(backup_method)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        return self


class DescribeBackupsResponseBodyItems(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup  # type: list[DescribeBackupsResponseBodyItemsBackup]

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, items=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.items = items  # type: DescribeBackupsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeBackupsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterDescriptionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, dbcluster_description=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.dbcluster_description = TeaConverter.to_unicode(dbcluster_description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        return self


class ModifyDBClusterDescriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterDescriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBClusterDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBClusterDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColumnsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, schema_name=None, table_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeColumnsResponseBodyItemsColumn(TeaModel):
    def __init__(self, type=None, column_name=None, table_name=None, auto_increment_column=None, dbcluster_id=None,
                 primary_key=None, schema_name=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.column_name = TeaConverter.to_unicode(column_name)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.auto_increment_column = auto_increment_column  # type: bool
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.primary_key = primary_key  # type: bool
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeColumnsResponseBodyItems(TeaModel):
    def __init__(self, column=None):
        self.column = column  # type: list[DescribeColumnsResponseBodyItemsColumn]

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeColumnsResponseBodyItemsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeColumnsResponseBody(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeColumnsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeColumnsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeColumnsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeColumnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeOperatorPermissionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class RevokeOperatorPermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeOperatorPermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RevokeOperatorPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RevokeOperatorPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBResourcePoolRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, pool_name=None, query_type=None, node_num=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode
        self.query_type = TeaConverter.to_unicode(query_type)  # type: unicode
        self.node_num = node_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        return self


class CreateDBResourcePoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBResourcePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateDBResourcePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllAccountsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeAllAccountsResponseBodyAccountList(TeaModel):
    def __init__(self, user=None):
        self.user = TeaConverter.to_unicode(user)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeAllAccountsResponseBody(TeaModel):
    def __init__(self, request_id=None, account_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.account_list = account_list  # type: list[DescribeAllAccountsResponseBodyAccountList]

    def validate(self):
        if self.account_list:
            for k in self.account_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AccountList'] = []
        if self.account_list is not None:
            for k in self.account_list:
                result['AccountList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.account_list = []
        if m.get('AccountList') is not None:
            for k in m.get('AccountList'):
                temp_model = DescribeAllAccountsResponseBodyAccountList()
                self.account_list.append(temp_model.from_map(k))
        return self


class DescribeAllAccountsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAllAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAllAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAuditLogConfigRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, region_id=None, audit_log_status=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.audit_log_status = TeaConverter.to_unicode(audit_log_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        return self


class ModifyAuditLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAuditLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyAuditLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBResourcePoolRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, pool_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        return self


class DeleteDBResourcePoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBResourcePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDBResourcePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class TagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, resource_type=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantOperatorPermissionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, expired_time=None, privileges=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.expired_time = TeaConverter.to_unicode(expired_time)  # type: unicode
        self.privileges = TeaConverter.to_unicode(privileges)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.privileges is not None:
            result['Privileges'] = self.privileges
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')
        return self


class GrantOperatorPermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GrantOperatorPermissionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GrantOperatorPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GrantOperatorPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllDataSourceRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, schema_name=None, table_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeAllDataSourceResponseBodyTablesTable(TeaModel):
    def __init__(self, table_name=None, dbcluster_id=None, schema_name=None):
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeAllDataSourceResponseBodyTables(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[DescribeAllDataSourceResponseBodyTablesTable]

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeAllDataSourceResponseBodyTablesTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBodyColumnsColumn(TeaModel):
    def __init__(self, type=None, column_name=None, table_name=None, auto_increment_column=None, dbcluster_id=None,
                 primary_key=None, schema_name=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.column_name = TeaConverter.to_unicode(column_name)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.auto_increment_column = auto_increment_column  # type: bool
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.primary_key = primary_key  # type: bool
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.auto_increment_column is not None:
            result['AutoIncrementColumn'] = self.auto_increment_column
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('AutoIncrementColumn') is not None:
            self.auto_increment_column = m.get('AutoIncrementColumn')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeAllDataSourceResponseBodyColumns(TeaModel):
    def __init__(self, column=None):
        self.column = column  # type: list[DescribeAllDataSourceResponseBodyColumnsColumn]

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = DescribeAllDataSourceResponseBodyColumnsColumn()
                self.column.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBodySchemasSchema(TeaModel):
    def __init__(self, dbcluster_id=None, schema_name=None):
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeAllDataSourceResponseBodySchemas(TeaModel):
    def __init__(self, schema=None):
        self.schema = schema  # type: list[DescribeAllDataSourceResponseBodySchemasSchema]

    def validate(self):
        if self.schema:
            for k in self.schema:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Schema'] = []
        if self.schema is not None:
            for k in self.schema:
                result['Schema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k in m.get('Schema'):
                temp_model = DescribeAllDataSourceResponseBodySchemasSchema()
                self.schema.append(temp_model.from_map(k))
        return self


class DescribeAllDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None, tables=None, columns=None, schemas=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tables = tables  # type: DescribeAllDataSourceResponseBodyTables
        self.columns = columns  # type: DescribeAllDataSourceResponseBodyColumns
        self.schemas = schemas  # type: DescribeAllDataSourceResponseBodySchemas

    def validate(self):
        if self.tables:
            self.tables.validate()
        if self.columns:
            self.columns.validate()
        if self.schemas:
            self.schemas.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        if self.columns is not None:
            result['Columns'] = self.columns.to_map()
        if self.schemas is not None:
            result['Schemas'] = self.schemas.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            temp_model = DescribeAllDataSourceResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        if m.get('Columns') is not None:
            temp_model = DescribeAllDataSourceResponseBodyColumns()
            self.columns = temp_model.from_map(m['Columns'])
        if m.get('Schemas') is not None:
            temp_model = DescribeAllDataSourceResponseBodySchemas()
            self.schemas = temp_model.from_map(m['Schemas'])
        return self


class DescribeAllDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAllDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAllDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, dbnode_group_count=None, dbnode_storage=None, dbnode_class=None, modify_type=None,
                 executor_count=None, region_id=None, storage_resource=None, compute_resource=None, elastic_ioresource=None,
                 dbcluster_category=None, mode=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.dbnode_group_count = TeaConverter.to_unicode(dbnode_group_count)  # type: unicode
        self.dbnode_storage = TeaConverter.to_unicode(dbnode_storage)  # type: unicode
        self.dbnode_class = TeaConverter.to_unicode(dbnode_class)  # type: unicode
        self.modify_type = TeaConverter.to_unicode(modify_type)  # type: unicode
        self.executor_count = TeaConverter.to_unicode(executor_count)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.storage_resource = TeaConverter.to_unicode(storage_resource)  # type: unicode
        self.compute_resource = TeaConverter.to_unicode(compute_resource)  # type: unicode
        self.elastic_ioresource = elastic_ioresource  # type: int
        self.dbcluster_category = TeaConverter.to_unicode(dbcluster_category)  # type: unicode
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyDBClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, dbcluster_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDBClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablePartitionDiagnoseRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, dbcluster_id=None, page_size=None, page_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeTablePartitionDiagnoseResponseBodyItems(TeaModel):
    def __init__(self, table_name=None, partition_detail=None, schema_name=None, partition_number=None):
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.partition_detail = TeaConverter.to_unicode(partition_detail)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode
        self.partition_number = partition_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.partition_detail is not None:
            result['PartitionDetail'] = self.partition_detail
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.partition_number is not None:
            result['PartitionNumber'] = self.partition_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('PartitionDetail') is not None:
            self.partition_detail = m.get('PartitionDetail')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('PartitionNumber') is not None:
            self.partition_number = m.get('PartitionNumber')
        return self


class DescribeTablePartitionDiagnoseResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, dbcluster_id=None,
                 suggest_max_records_per_partition=None, suggest_min_records_per_partition=None, items=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.suggest_max_records_per_partition = suggest_max_records_per_partition  # type: long
        self.suggest_min_records_per_partition = suggest_min_records_per_partition  # type: long
        self.items = items  # type: list[DescribeTablePartitionDiagnoseResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.suggest_max_records_per_partition is not None:
            result['SuggestMaxRecordsPerPartition'] = self.suggest_max_records_per_partition
        if self.suggest_min_records_per_partition is not None:
            result['SuggestMinRecordsPerPartition'] = self.suggest_min_records_per_partition
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SuggestMaxRecordsPerPartition') is not None:
            self.suggest_max_records_per_partition = m.get('SuggestMaxRecordsPerPartition')
        if m.get('SuggestMinRecordsPerPartition') is not None:
            self.suggest_min_records_per_partition = m.get('SuggestMinRecordsPerPartition')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTablePartitionDiagnoseResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeTablePartitionDiagnoseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTablePartitionDiagnoseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeTablePartitionDiagnoseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBResourcePoolRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, pool_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        return self


class DescribeDBResourcePoolResponseBodyPoolsInfo(TeaModel):
    def __init__(self, query_type=None, update_time=None, pool_name=None, create_time=None, pool_users=None,
                 node_num=None):
        self.query_type = TeaConverter.to_unicode(query_type)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.pool_users = TeaConverter.to_unicode(pool_users)  # type: unicode
        self.node_num = node_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pool_users is not None:
            result['PoolUsers'] = self.pool_users
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PoolUsers') is not None:
            self.pool_users = m.get('PoolUsers')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        return self


class DescribeDBResourcePoolResponseBody(TeaModel):
    def __init__(self, request_id=None, pools_info=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.pools_info = pools_info  # type: list[DescribeDBResourcePoolResponseBodyPoolsInfo]

    def validate(self):
        if self.pools_info:
            for k in self.pools_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PoolsInfo'] = []
        if self.pools_info is not None:
            for k in self.pools_info:
                result['PoolsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.pools_info = []
        if m.get('PoolsInfo') is not None:
            for k in m.get('PoolsInfo'):
                temp_model = DescribeDBResourcePoolResponseBodyPoolsInfo()
                self.pools_info.append(temp_model.from_map(k))
        return self


class DescribeDBResourcePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBResourcePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, resource_type=None, next_token=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_type=None, tag_value=None, resource_id=None, tag_key=None):
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.resource_id = TeaConverter.to_unicode(resource_id)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterPerformanceRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, key=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.key is not None:
            result['Key'] = self.key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformancesSeries(TeaModel):
    def __init__(self, values=None, name=None):
        self.values = values  # type: list[unicode]
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDBClusterPerformanceResponseBodyPerformances(TeaModel):
    def __init__(self, key=None, unit=None, series=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.unit = TeaConverter.to_unicode(unit)  # type: unicode
        self.series = series  # type: list[DescribeDBClusterPerformanceResponseBodyPerformancesSeries]

    def validate(self):
        if self.series:
            for k in self.series:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        result['Series'] = []
        if self.series is not None:
            for k in self.series:
                result['Series'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        self.series = []
        if m.get('Series') is not None:
            for k in m.get('Series'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformancesSeries()
                self.series.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, start_time=None, dbcluster_id=None, performances=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.performances = performances  # type: list[DescribeDBClusterPerformanceResponseBodyPerformances]

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        return self


class DescribeDBClusterPerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBClusterPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBClusterPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticPlanRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, elastic_plan_name=None, resource_pool_name=None, elastic_plan_node_num=None,
                 elastic_plan_time_start=None, elastic_plan_time_end=None, elastic_plan_weekly_repeat=None, elastic_plan_start_day=None,
                 elastic_plan_end_day=None, elastic_plan_enable=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.elastic_plan_name = TeaConverter.to_unicode(elastic_plan_name)  # type: unicode
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.elastic_plan_node_num = elastic_plan_node_num  # type: int
        self.elastic_plan_time_start = TeaConverter.to_unicode(elastic_plan_time_start)  # type: unicode
        self.elastic_plan_time_end = TeaConverter.to_unicode(elastic_plan_time_end)  # type: unicode
        self.elastic_plan_weekly_repeat = TeaConverter.to_unicode(elastic_plan_weekly_repeat)  # type: unicode
        self.elastic_plan_start_day = TeaConverter.to_unicode(elastic_plan_start_day)  # type: unicode
        self.elastic_plan_end_day = TeaConverter.to_unicode(elastic_plan_end_day)  # type: unicode
        self.elastic_plan_enable = elastic_plan_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.elastic_plan_node_num is not None:
            result['ElasticPlanNodeNum'] = self.elastic_plan_node_num
        if self.elastic_plan_time_start is not None:
            result['ElasticPlanTimeStart'] = self.elastic_plan_time_start
        if self.elastic_plan_time_end is not None:
            result['ElasticPlanTimeEnd'] = self.elastic_plan_time_end
        if self.elastic_plan_weekly_repeat is not None:
            result['ElasticPlanWeeklyRepeat'] = self.elastic_plan_weekly_repeat
        if self.elastic_plan_start_day is not None:
            result['ElasticPlanStartDay'] = self.elastic_plan_start_day
        if self.elastic_plan_end_day is not None:
            result['ElasticPlanEndDay'] = self.elastic_plan_end_day
        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('ElasticPlanNodeNum') is not None:
            self.elastic_plan_node_num = m.get('ElasticPlanNodeNum')
        if m.get('ElasticPlanTimeStart') is not None:
            self.elastic_plan_time_start = m.get('ElasticPlanTimeStart')
        if m.get('ElasticPlanTimeEnd') is not None:
            self.elastic_plan_time_end = m.get('ElasticPlanTimeEnd')
        if m.get('ElasticPlanWeeklyRepeat') is not None:
            self.elastic_plan_weekly_repeat = m.get('ElasticPlanWeeklyRepeat')
        if m.get('ElasticPlanStartDay') is not None:
            self.elastic_plan_start_day = m.get('ElasticPlanStartDay')
        if m.get('ElasticPlanEndDay') is not None:
            self.elastic_plan_end_day = m.get('ElasticPlanEndDay')
        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')
        return self


class ModifyElasticPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyElasticPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyElasticPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogBackupPolicyRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, enable_backup_log=None, log_backup_retention_period=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.enable_backup_log = TeaConverter.to_unicode(enable_backup_log)  # type: unicode
        self.log_backup_retention_period = TeaConverter.to_unicode(log_backup_retention_period)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        return self


class ModifyLogBackupPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyLogBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyLogBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyLogBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogTrendRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, start_time=None, end_time=None, dbname=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeriesSeriesItem(TeaModel):
    def __init__(self, values=None, name=None):
        self.values = TeaConverter.to_unicode(values)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeries(TeaModel):
    def __init__(self, series_item=None):
        self.series_item = series_item  # type: list[DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeriesSeriesItem]

    def validate(self):
        if self.series_item:
            for k in self.series_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SeriesItem'] = []
        if self.series_item is not None:
            for k in self.series_item:
                result['SeriesItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.series_item = []
        if m.get('SeriesItem') is not None:
            for k in m.get('SeriesItem'):
                temp_model = DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeriesSeriesItem()
                self.series_item.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItem(TeaModel):
    def __init__(self, key=None, unit=None, series=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.unit = TeaConverter.to_unicode(unit)  # type: unicode
        self.series = series  # type: DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeries

    def validate(self):
        if self.series:
            self.series.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.series is not None:
            result['Series'] = self.series.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Series') is not None:
            temp_model = DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItemSeries()
            self.series = temp_model.from_map(m['Series'])
        return self


class DescribeSlowLogTrendResponseBodyItems(TeaModel):
    def __init__(self, slow_log_trend_item=None):
        self.slow_log_trend_item = slow_log_trend_item  # type: list[DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItem]

    def validate(self):
        if self.slow_log_trend_item:
            for k in self.slow_log_trend_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SlowLogTrendItem'] = []
        if self.slow_log_trend_item is not None:
            for k in self.slow_log_trend_item:
                result['SlowLogTrendItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.slow_log_trend_item = []
        if m.get('SlowLogTrendItem') is not None:
            for k in m.get('SlowLogTrendItem'):
                temp_model = DescribeSlowLogTrendResponseBodyItemsSlowLogTrendItem()
                self.slow_log_trend_item.append(temp_model.from_map(k))
        return self


class DescribeSlowLogTrendResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, start_time=None, dbcluster_id=None, items=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.items = items  # type: DescribeSlowLogTrendResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogTrendResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSlowLogTrendResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSlowLogTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSlowLogTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, region_id=None, zone_id=None, charge_type=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, owner_account=None, accept_language=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.accept_language = TeaConverter.to_unicode(accept_language)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount(TeaModel):
    def __init__(self, step=None, min_count=None, max_count=None):
        self.step = TeaConverter.to_unicode(step)  # type: unicode
        self.min_count = TeaConverter.to_unicode(min_count)  # type: unicode
        self.max_count = TeaConverter.to_unicode(max_count)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList(TeaModel):
    def __init__(self, node_count=None):
        self.node_count = node_count  # type: DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount(TeaModel):
    def __init__(self, step=None, min_count=None, max_count=None):
        self.step = TeaConverter.to_unicode(step)  # type: unicode
        self.min_count = TeaConverter.to_unicode(min_count)  # type: unicode
        self.max_count = TeaConverter.to_unicode(max_count)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList(TeaModel):
    def __init__(self, node_count=None, storage_size=None):
        self.node_count = node_count  # type: DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount
        self.storage_size = storage_size  # type: list[unicode]

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        result = dict()
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount()
            self.node_count = temp_model.from_map(m['NodeCount'])
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList(TeaModel):
    def __init__(self, supported_executor_list=None, instance_class=None, supported_node_count_list=None,
                 tips=None):
        self.supported_executor_list = supported_executor_list  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList]
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode
        self.supported_node_count_list = supported_node_count_list  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList]
        self.tips = TeaConverter.to_unicode(tips)  # type: unicode

    def validate(self):
        if self.supported_executor_list:
            for k in self.supported_executor_list:
                if k:
                    k.validate()
        if self.supported_node_count_list:
            for k in self.supported_node_count_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedExecutorList'] = []
        if self.supported_executor_list is not None:
            for k in self.supported_executor_list:
                result['SupportedExecutorList'].append(k.to_map() if k else None)
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        result['SupportedNodeCountList'] = []
        if self.supported_node_count_list is not None:
            for k in self.supported_node_count_list:
                result['SupportedNodeCountList'].append(k.to_map() if k else None)
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_executor_list = []
        if m.get('SupportedExecutorList') is not None:
            for k in m.get('SupportedExecutorList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList()
                self.supported_executor_list.append(temp_model.from_map(k))
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        self.supported_node_count_list = []
        if m.get('SupportedNodeCountList') is not None:
            for k in m.get('SupportedNodeCountList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList()
                self.supported_node_count_list.append(temp_model.from_map(k))
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource(TeaModel):
    def __init__(self, step=None, min_count=None, max_count=None):
        self.step = TeaConverter.to_unicode(step)  # type: unicode
        self.min_count = TeaConverter.to_unicode(min_count)  # type: unicode
        self.max_count = TeaConverter.to_unicode(max_count)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource(TeaModel):
    def __init__(self, supported_elastic_ioresource=None, supported_storage_resource=None, storage_type=None,
                 supported_compute_resource=None):
        self.supported_elastic_ioresource = supported_elastic_ioresource  # type: DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource
        self.supported_storage_resource = supported_storage_resource  # type: list[unicode]
        self.storage_type = TeaConverter.to_unicode(storage_type)  # type: unicode
        self.supported_compute_resource = supported_compute_resource  # type: list[unicode]

    def validate(self):
        if self.supported_elastic_ioresource:
            self.supported_elastic_ioresource.validate()

    def to_map(self):
        result = dict()
        if self.supported_elastic_ioresource is not None:
            result['SupportedElasticIOResource'] = self.supported_elastic_ioresource.to_map()
        if self.supported_storage_resource is not None:
            result['SupportedStorageResource'] = self.supported_storage_resource
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.supported_compute_resource is not None:
            result['SupportedComputeResource'] = self.supported_compute_resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedElasticIOResource') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource()
            self.supported_elastic_ioresource = temp_model.from_map(m['SupportedElasticIOResource'])
        if m.get('SupportedStorageResource') is not None:
            self.supported_storage_resource = m.get('SupportedStorageResource')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportedComputeResource') is not None:
            self.supported_compute_resource = m.get('SupportedComputeResource')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList(TeaModel):
    def __init__(self, serial=None, supported_instance_class_list=None, supported_flexible_resource=None):
        self.serial = TeaConverter.to_unicode(serial)  # type: unicode
        self.supported_instance_class_list = supported_instance_class_list  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList]
        self.supported_flexible_resource = supported_flexible_resource  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource]

    def validate(self):
        if self.supported_instance_class_list:
            for k in self.supported_instance_class_list:
                if k:
                    k.validate()
        if self.supported_flexible_resource:
            for k in self.supported_flexible_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.serial is not None:
            result['Serial'] = self.serial
        result['SupportedInstanceClassList'] = []
        if self.supported_instance_class_list is not None:
            for k in self.supported_instance_class_list:
                result['SupportedInstanceClassList'].append(k.to_map() if k else None)
        result['SupportedFlexibleResource'] = []
        if self.supported_flexible_resource is not None:
            for k in self.supported_flexible_resource:
                result['SupportedFlexibleResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')
        self.supported_instance_class_list = []
        if m.get('SupportedInstanceClassList') is not None:
            for k in m.get('SupportedInstanceClassList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList()
                self.supported_instance_class_list.append(temp_model.from_map(k))
        self.supported_flexible_resource = []
        if m.get('SupportedFlexibleResource') is not None:
            for k in m.get('SupportedFlexibleResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource()
                self.supported_flexible_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode(TeaModel):
    def __init__(self, supported_serial_list=None, mode=None):
        self.supported_serial_list = supported_serial_list  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList]
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode

    def validate(self):
        if self.supported_serial_list:
            for k in self.supported_serial_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedSerialList'] = []
        if self.supported_serial_list is not None:
            for k in self.supported_serial_list:
                result['SupportedSerialList'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_serial_list = []
        if m.get('SupportedSerialList') is not None:
            for k in m.get('SupportedSerialList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList()
                self.supported_serial_list.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class DescribeAvailableResourceResponseBodyAvailableZoneList(TeaModel):
    def __init__(self, supported_mode=None, zone_id=None):
        self.supported_mode = supported_mode  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode]
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode

    def validate(self):
        if self.supported_mode:
            for k in self.supported_mode:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedMode'] = []
        if self.supported_mode is not None:
            for k in self.supported_mode:
                result['SupportedMode'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supported_mode = []
        if m.get('SupportedMode') is not None:
            for k in m.get('SupportedMode'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode()
                self.supported_mode.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, region_id=None, available_zone_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.available_zone_list = available_zone_list  # type: list[DescribeAvailableResourceResponseBodyAvailableZoneList]

    def validate(self):
        if self.available_zone_list:
            for k in self.available_zone_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['AvailableZoneList'] = []
        if self.available_zone_list is not None:
            for k in self.available_zone_list:
                result['AvailableZoneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.available_zone_list = []
        if m.get('AvailableZoneList') is not None:
            for k in m.get('AvailableZoneList'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZoneList()
                self.available_zone_list.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAvailableResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateElasticPlanRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, elastic_plan_name=None, resource_pool_name=None, elastic_plan_node_num=None,
                 elastic_plan_time_start=None, elastic_plan_time_end=None, elastic_plan_weekly_repeat=None, elastic_plan_start_day=None,
                 elastic_plan_end_day=None, elastic_plan_enable=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.elastic_plan_name = TeaConverter.to_unicode(elastic_plan_name)  # type: unicode
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.elastic_plan_node_num = elastic_plan_node_num  # type: int
        self.elastic_plan_time_start = TeaConverter.to_unicode(elastic_plan_time_start)  # type: unicode
        self.elastic_plan_time_end = TeaConverter.to_unicode(elastic_plan_time_end)  # type: unicode
        self.elastic_plan_weekly_repeat = TeaConverter.to_unicode(elastic_plan_weekly_repeat)  # type: unicode
        self.elastic_plan_start_day = TeaConverter.to_unicode(elastic_plan_start_day)  # type: unicode
        self.elastic_plan_end_day = TeaConverter.to_unicode(elastic_plan_end_day)  # type: unicode
        self.elastic_plan_enable = elastic_plan_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.elastic_plan_node_num is not None:
            result['ElasticPlanNodeNum'] = self.elastic_plan_node_num
        if self.elastic_plan_time_start is not None:
            result['ElasticPlanTimeStart'] = self.elastic_plan_time_start
        if self.elastic_plan_time_end is not None:
            result['ElasticPlanTimeEnd'] = self.elastic_plan_time_end
        if self.elastic_plan_weekly_repeat is not None:
            result['ElasticPlanWeeklyRepeat'] = self.elastic_plan_weekly_repeat
        if self.elastic_plan_start_day is not None:
            result['ElasticPlanStartDay'] = self.elastic_plan_start_day
        if self.elastic_plan_end_day is not None:
            result['ElasticPlanEndDay'] = self.elastic_plan_end_day
        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('ElasticPlanNodeNum') is not None:
            self.elastic_plan_node_num = m.get('ElasticPlanNodeNum')
        if m.get('ElasticPlanTimeStart') is not None:
            self.elastic_plan_time_start = m.get('ElasticPlanTimeStart')
        if m.get('ElasticPlanTimeEnd') is not None:
            self.elastic_plan_time_end = m.get('ElasticPlanTimeEnd')
        if m.get('ElasticPlanWeeklyRepeat') is not None:
            self.elastic_plan_weekly_repeat = m.get('ElasticPlanWeeklyRepeat')
        if m.get('ElasticPlanStartDay') is not None:
            self.elastic_plan_start_day = m.get('ElasticPlanStartDay')
        if m.get('ElasticPlanEndDay') is not None:
            self.elastic_plan_end_day = m.get('ElasticPlanEndDay')
        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')
        return self


class CreateElasticPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateElasticPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateElasticPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterPublicConnectionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ReleaseClusterPublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseClusterPublicConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ReleaseClusterPublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ReleaseClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogConfigRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, region_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAuditLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, audit_log_status=None, dbcluster_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.audit_log_status = TeaConverter.to_unicode(audit_log_status)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeAuditLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAuditLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAuditLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTablesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, schema_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeTablesResponseBodyItemsTable(TeaModel):
    def __init__(self, table_name=None, dbcluster_id=None, schema_name=None):
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class DescribeTablesResponseBodyItems(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[DescribeTablesResponseBodyItemsTable]

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeTablesResponseBodyItemsTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeTablesResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeTablesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterNetInfoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeDBClusterNetInfoResponseBodyItemsAddress(TeaModel):
    def __init__(self, v_switch_id=None, connection_string=None, net_type=None, port=None, vpcid=None,
                 ipaddress=None):
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.connection_string = TeaConverter.to_unicode(connection_string)  # type: unicode
        self.net_type = TeaConverter.to_unicode(net_type)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.ipaddress = TeaConverter.to_unicode(ipaddress)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        return self


class DescribeDBClusterNetInfoResponseBodyItems(TeaModel):
    def __init__(self, address=None):
        self.address = address  # type: list[DescribeDBClusterNetInfoResponseBodyItemsAddress]

    def validate(self):
        if self.address:
            for k in self.address:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Address'] = []
        if self.address is not None:
            for k in self.address:
                result['Address'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k in m.get('Address'):
                temp_model = DescribeDBClusterNetInfoResponseBodyItemsAddress()
                self.address.append(temp_model.from_map(k))
        return self


class DescribeDBClusterNetInfoResponseBody(TeaModel):
    def __init__(self, cluster_network_type=None, request_id=None, items=None):
        self.cluster_network_type = TeaConverter.to_unicode(cluster_network_type)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeDBClusterNetInfoResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterNetInfoResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBClusterNetInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBClusterNetInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBClusterNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInclinedTablesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, table_type=None, order=None, page_size=None, page_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.table_type = TeaConverter.to_unicode(table_type)  # type: unicode
        self.order = TeaConverter.to_unicode(order)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeInclinedTablesResponseBodyItemsTable(TeaModel):
    def __init__(self, type=None, schema=None, size=None, name=None, is_incline=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.schema = TeaConverter.to_unicode(schema)  # type: unicode
        self.size = size  # type: long
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.is_incline = is_incline  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.size is not None:
            result['Size'] = self.size
        if self.name is not None:
            result['Name'] = self.name
        if self.is_incline is not None:
            result['IsIncline'] = self.is_incline
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IsIncline') is not None:
            self.is_incline = m.get('IsIncline')
        return self


class DescribeInclinedTablesResponseBodyItems(TeaModel):
    def __init__(self, table=None):
        self.table = table  # type: list[DescribeInclinedTablesResponseBodyItemsTable]

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = DescribeInclinedTablesResponseBodyItemsTable()
                self.table.append(temp_model.from_map(k))
        return self


class DescribeInclinedTablesResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, items=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.items = items  # type: DescribeInclinedTablesResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeInclinedTablesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeInclinedTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInclinedTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeInclinedTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAttributeRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeDBClusterAttributeResponseBodyItemsDBClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClusterAttributeResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAttributeResponseBodyItemsDBCluster(TeaModel):
    def __init__(self, creation_time=None, enable_spark=None, dts_job_id=None, dbnode_count=None, expired=None,
                 maintain_time=None, pay_type=None, disk_type=None, tags=None, mode=None, port=None, lock_mode=None,
                 engine_version=None, enable_airflow=None, executor_count=None, storage_resource=None, dbcluster_id=None,
                 connection_string=None, rds_instance_id=None, dbcluster_type=None, commodity_code=None, expire_time=None,
                 dbnode_storage=None, dbnode_class=None, lock_reason=None, vpcid=None, compute_resource=None, region_id=None,
                 elastic_ioresource=None, v_switch_id=None, dbversion=None, vpccloud_instance_id=None, dbcluster_status=None,
                 resource_group_id=None, dbcluster_network_type=None, dbcluster_description=None, user_enistatus=None, zone_id=None,
                 category=None, engine=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.enable_spark = enable_spark  # type: bool
        self.dts_job_id = TeaConverter.to_unicode(dts_job_id)  # type: unicode
        self.dbnode_count = dbnode_count  # type: long
        self.expired = TeaConverter.to_unicode(expired)  # type: unicode
        self.maintain_time = TeaConverter.to_unicode(maintain_time)  # type: unicode
        self.pay_type = TeaConverter.to_unicode(pay_type)  # type: unicode
        self.disk_type = TeaConverter.to_unicode(disk_type)  # type: unicode
        self.tags = tags  # type: DescribeDBClusterAttributeResponseBodyItemsDBClusterTags
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.port = port  # type: int
        self.lock_mode = TeaConverter.to_unicode(lock_mode)  # type: unicode
        self.engine_version = TeaConverter.to_unicode(engine_version)  # type: unicode
        self.enable_airflow = enable_airflow  # type: bool
        self.executor_count = TeaConverter.to_unicode(executor_count)  # type: unicode
        self.storage_resource = TeaConverter.to_unicode(storage_resource)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.connection_string = TeaConverter.to_unicode(connection_string)  # type: unicode
        self.rds_instance_id = TeaConverter.to_unicode(rds_instance_id)  # type: unicode
        self.dbcluster_type = TeaConverter.to_unicode(dbcluster_type)  # type: unicode
        self.commodity_code = TeaConverter.to_unicode(commodity_code)  # type: unicode
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.dbnode_storage = dbnode_storage  # type: long
        self.dbnode_class = TeaConverter.to_unicode(dbnode_class)  # type: unicode
        self.lock_reason = TeaConverter.to_unicode(lock_reason)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.compute_resource = TeaConverter.to_unicode(compute_resource)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.elastic_ioresource = elastic_ioresource  # type: int
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.dbversion = TeaConverter.to_unicode(dbversion)  # type: unicode
        self.vpccloud_instance_id = TeaConverter.to_unicode(vpccloud_instance_id)  # type: unicode
        self.dbcluster_status = TeaConverter.to_unicode(dbcluster_status)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.dbcluster_network_type = TeaConverter.to_unicode(dbcluster_network_type)  # type: unicode
        self.dbcluster_description = TeaConverter.to_unicode(dbcluster_description)  # type: unicode
        self.user_enistatus = user_enistatus  # type: bool
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.enable_spark is not None:
            result['EnableSpark'] = self.enable_spark
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.port is not None:
            result['Port'] = self.port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.enable_airflow is not None:
            result['EnableAirflow'] = self.enable_airflow
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.user_enistatus is not None:
            result['UserENIStatus'] = self.user_enistatus
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.category is not None:
            result['Category'] = self.category
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EnableSpark') is not None:
            self.enable_spark = m.get('EnableSpark')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('EnableAirflow') is not None:
            self.enable_airflow = m.get('EnableAirflow')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('UserENIStatus') is not None:
            self.user_enistatus = m.get('UserENIStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeDBClusterAttributeResponseBodyItems(TeaModel):
    def __init__(self, dbcluster=None):
        self.dbcluster = dbcluster  # type: list[DescribeDBClusterAttributeResponseBodyItemsDBCluster]

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClusterAttributeResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeDBClusterAttributeResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBClusterAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBClusterAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClustersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeDBClustersRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, dbcluster_ids=None, dbcluster_description=None, dbcluster_status=None, page_size=None,
                 page_number=None, resource_group_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbcluster_ids = TeaConverter.to_unicode(dbcluster_ids)  # type: unicode
        self.dbcluster_description = TeaConverter.to_unicode(dbcluster_description)  # type: unicode
        self.dbcluster_status = TeaConverter.to_unicode(dbcluster_status)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.tag = tag  # type: list[DescribeDBClustersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeDBClustersResponseBodyItemsDBClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeDBClustersResponseBodyItemsDBClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBClustersResponseBodyItemsDBClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBodyItemsDBCluster(TeaModel):
    def __init__(self, dts_job_id=None, dbnode_count=None, expired=None, create_time=None, pay_type=None,
                 disk_type=None, tags=None, mode=None, port=None, lock_mode=None, storage_resource=None, executor_count=None,
                 dbcluster_id=None, connection_string=None, rds_instance_id=None, dbcluster_type=None, commodity_code=None,
                 expire_time=None, dbnode_storage=None, dbnode_class=None, lock_reason=None, vpcid=None, region_id=None,
                 compute_resource=None, elastic_ioresource=None, v_switch_id=None, dbversion=None, vpccloud_instance_id=None,
                 dbcluster_status=None, resource_group_id=None, dbcluster_network_type=None, dbcluster_description=None,
                 zone_id=None, category=None, engine=None):
        self.dts_job_id = TeaConverter.to_unicode(dts_job_id)  # type: unicode
        self.dbnode_count = dbnode_count  # type: long
        self.expired = TeaConverter.to_unicode(expired)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.pay_type = TeaConverter.to_unicode(pay_type)  # type: unicode
        self.disk_type = TeaConverter.to_unicode(disk_type)  # type: unicode
        self.tags = tags  # type: DescribeDBClustersResponseBodyItemsDBClusterTags
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.lock_mode = TeaConverter.to_unicode(lock_mode)  # type: unicode
        self.storage_resource = TeaConverter.to_unicode(storage_resource)  # type: unicode
        self.executor_count = TeaConverter.to_unicode(executor_count)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.connection_string = TeaConverter.to_unicode(connection_string)  # type: unicode
        self.rds_instance_id = TeaConverter.to_unicode(rds_instance_id)  # type: unicode
        self.dbcluster_type = TeaConverter.to_unicode(dbcluster_type)  # type: unicode
        self.commodity_code = TeaConverter.to_unicode(commodity_code)  # type: unicode
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.dbnode_storage = dbnode_storage  # type: long
        self.dbnode_class = TeaConverter.to_unicode(dbnode_class)  # type: unicode
        self.lock_reason = TeaConverter.to_unicode(lock_reason)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.compute_resource = TeaConverter.to_unicode(compute_resource)  # type: unicode
        self.elastic_ioresource = elastic_ioresource  # type: int
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.dbversion = TeaConverter.to_unicode(dbversion)  # type: unicode
        self.vpccloud_instance_id = TeaConverter.to_unicode(vpccloud_instance_id)  # type: unicode
        self.dbcluster_status = TeaConverter.to_unicode(dbcluster_status)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.dbcluster_network_type = TeaConverter.to_unicode(dbcluster_network_type)  # type: unicode
        self.dbcluster_description = TeaConverter.to_unicode(dbcluster_description)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.engine = TeaConverter.to_unicode(engine)  # type: unicode

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.port is not None:
            result['Port'] = self.port
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource
        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.rds_instance_id is not None:
            result['RdsInstanceId'] = self.rds_instance_id
        if self.dbcluster_type is not None:
            result['DBClusterType'] = self.dbcluster_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource
        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.vpccloud_instance_id is not None:
            result['VPCCloudInstanceId'] = self.vpccloud_instance_id
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.dbcluster_network_type is not None:
            result['DBClusterNetworkType'] = self.dbcluster_network_type
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.category is not None:
            result['Category'] = self.category
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Tags') is not None:
            temp_model = DescribeDBClustersResponseBodyItemsDBClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')
        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('RdsInstanceId') is not None:
            self.rds_instance_id = m.get('RdsInstanceId')
        if m.get('DBClusterType') is not None:
            self.dbcluster_type = m.get('DBClusterType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')
        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('VPCCloudInstanceId') is not None:
            self.vpccloud_instance_id = m.get('VPCCloudInstanceId')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('DBClusterNetworkType') is not None:
            self.dbcluster_network_type = m.get('DBClusterNetworkType')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeDBClustersResponseBodyItems(TeaModel):
    def __init__(self, dbcluster=None):
        self.dbcluster = dbcluster  # type: list[DescribeDBClustersResponseBodyItemsDBCluster]

    def validate(self):
        if self.dbcluster:
            for k in self.dbcluster:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DBCluster'] = []
        if self.dbcluster is not None:
            for k in self.dbcluster:
                result['DBCluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbcluster = []
        if m.get('DBCluster') is not None:
            for k in m.get('DBCluster'):
                temp_model = DescribeDBClustersResponseBodyItemsDBCluster()
                self.dbcluster.append(temp_model.from_map(k))
        return self


class DescribeDBClustersResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, items=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeDBClustersResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeDBClustersResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillProcessRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, process_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        return self


class KillProcessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillProcessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: KillProcessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = KillProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoRenewAttributeRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 region_id=None, dbcluster_ids=None, page_size=None, page_number=None, resource_group_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.dbcluster_ids = TeaConverter.to_unicode(dbcluster_ids)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute(TeaModel):
    def __init__(self, dbcluster_id=None, period_unit=None, duration=None, renewal_status=None,
                 auto_renew_enabled=None, region_id=None):
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.period_unit = TeaConverter.to_unicode(period_unit)  # type: unicode
        self.duration = duration  # type: int
        self.renewal_status = TeaConverter.to_unicode(renewal_status)  # type: unicode
        self.auto_renew_enabled = auto_renew_enabled  # type: bool
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.auto_renew_enabled is not None:
            result['AutoRenewEnabled'] = self.auto_renew_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('AutoRenewEnabled') is not None:
            self.auto_renew_enabled = m.get('AutoRenewEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAutoRenewAttributeResponseBodyItems(TeaModel):
    def __init__(self, auto_renew_attribute=None):
        self.auto_renew_attribute = auto_renew_attribute  # type: list[DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute]

    def validate(self):
        if self.auto_renew_attribute:
            for k in self.auto_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AutoRenewAttribute'] = []
        if self.auto_renew_attribute is not None:
            for k in self.auto_renew_attribute:
                result['AutoRenewAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_renew_attribute = []
        if m.get('AutoRenewAttribute') is not None:
            for k in m.get('AutoRenewAttribute'):
                temp_model = DescribeAutoRenewAttributeResponseBodyItemsAutoRenewAttribute()
                self.auto_renew_attribute.append(temp_model.from_map(k))
        return self


class DescribeAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, total_record_count=None, page_record_count=None, request_id=None, page_number=None,
                 items=None):
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.items = items  # type: DescribeAutoRenewAttributeResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Items') is not None:
            temp_model = DescribeAutoRenewAttributeResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterAccessWhiteListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeDBClusterAccessWhiteListResponseBodyItemsIPArray(TeaModel):
    def __init__(self, dbcluster_iparray_attribute=None, security_iplist=None, dbcluster_iparray_name=None):
        self.dbcluster_iparray_attribute = TeaConverter.to_unicode(dbcluster_iparray_attribute)  # type: unicode
        self.security_iplist = TeaConverter.to_unicode(security_iplist)  # type: unicode
        self.dbcluster_iparray_name = TeaConverter.to_unicode(dbcluster_iparray_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        return self


class DescribeDBClusterAccessWhiteListResponseBodyItems(TeaModel):
    def __init__(self, iparray=None):
        self.iparray = iparray  # type: list[DescribeDBClusterAccessWhiteListResponseBodyItemsIPArray]

    def validate(self):
        if self.iparray:
            for k in self.iparray:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IPArray'] = []
        if self.iparray is not None:
            for k in self.iparray:
                result['IPArray'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.iparray = []
        if m.get('IPArray') is not None:
            for k in m.get('IPArray'):
                temp_model = DescribeDBClusterAccessWhiteListResponseBodyItemsIPArray()
                self.iparray.append(temp_model.from_map(k))
        return self


class DescribeDBClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeDBClusterAccessWhiteListResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeDBClusterAccessWhiteListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeDBClusterAccessWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBClusterAccessWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInfoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskInfoResponseBodyTaskInfo(TeaModel):
    def __init__(self, status=None, finish_time=None, progress=None, begin_time=None, task_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.finish_time = TeaConverter.to_unicode(finish_time)  # type: unicode
        self.progress = TeaConverter.to_unicode(progress)  # type: unicode
        self.begin_time = TeaConverter.to_unicode(begin_time)  # type: unicode
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskInfoResponseBody(TeaModel):
    def __init__(self, task_info=None, request_id=None):
        self.task_info = task_info  # type: DescribeTaskInfoResponseBodyTaskInfo
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskInfo') is not None:
            temp_model = DescribeTaskInfoResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 accept_language=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.accept_language = TeaConverter.to_unicode(accept_language)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(self, local_name=None, zone_id=None, vpc_enabled=None):
        self.local_name = TeaConverter.to_unicode(local_name)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.vpc_enabled = vpc_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeRegionsResponseBodyRegionsRegionZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, zones=None, local_name=None, region_endpoint=None, region_id=None):
        self.zones = zones  # type: DescribeRegionsResponseBodyRegionsRegionZones
        self.local_name = TeaConverter.to_unicode(local_name)  # type: unicode
        self.region_endpoint = TeaConverter.to_unicode(region_endpoint)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBResourcePoolRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, pool_name=None, query_type=None, node_num=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.pool_name = TeaConverter.to_unicode(pool_name)  # type: unicode
        self.query_type = TeaConverter.to_unicode(query_type)  # type: unicode
        self.node_num = node_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        return self


class ModifyDBResourcePoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBResourcePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBResourcePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBResourcePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, account_name=None, account_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_type = TeaConverter.to_unicode(account_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, start_time=None, end_time=None, dbname=None, page_size=None, page_number=None,
                 process_id=None, order=None, range=None, state=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode
        self.order = TeaConverter.to_unicode(order)  # type: unicode
        self.range = TeaConverter.to_unicode(range)  # type: unicode
        self.state = TeaConverter.to_unicode(state)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        if self.order is not None:
            result['Order'] = self.order
        if self.range is not None:
            result['Range'] = self.range
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord(TeaModel):
    def __init__(self, host_address=None, scan_time=None, sqltext=None, output_size=None, peak_memory_usage=None,
                 state=None, wall_time=None, scan_size=None, execution_start_time=None, query_time=None,
                 return_row_counts=None, scan_rows=None, parse_row_counts=None, dbname=None, planning_time=None, queue_time=None,
                 user_name=None, process_id=None):
        self.host_address = TeaConverter.to_unicode(host_address)  # type: unicode
        self.scan_time = scan_time  # type: long
        self.sqltext = TeaConverter.to_unicode(sqltext)  # type: unicode
        self.output_size = TeaConverter.to_unicode(output_size)  # type: unicode
        self.peak_memory_usage = TeaConverter.to_unicode(peak_memory_usage)  # type: unicode
        self.state = TeaConverter.to_unicode(state)  # type: unicode
        self.wall_time = wall_time  # type: long
        self.scan_size = TeaConverter.to_unicode(scan_size)  # type: unicode
        self.execution_start_time = TeaConverter.to_unicode(execution_start_time)  # type: unicode
        self.query_time = query_time  # type: long
        self.return_row_counts = return_row_counts  # type: long
        self.scan_rows = scan_rows  # type: long
        self.parse_row_counts = parse_row_counts  # type: long
        self.dbname = TeaConverter.to_unicode(dbname)  # type: unicode
        self.planning_time = planning_time  # type: long
        self.queue_time = queue_time  # type: long
        self.user_name = TeaConverter.to_unicode(user_name)  # type: unicode
        self.process_id = TeaConverter.to_unicode(process_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.output_size is not None:
            result['OutputSize'] = self.output_size
        if self.peak_memory_usage is not None:
            result['PeakMemoryUsage'] = self.peak_memory_usage
        if self.state is not None:
            result['State'] = self.state
        if self.wall_time is not None:
            result['WallTime'] = self.wall_time
        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.planning_time is not None:
            result['PlanningTime'] = self.planning_time
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.process_id is not None:
            result['ProcessID'] = self.process_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')
        if m.get('PeakMemoryUsage') is not None:
            self.peak_memory_usage = m.get('PeakMemoryUsage')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('WallTime') is not None:
            self.wall_time = m.get('WallTime')
        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('PlanningTime') is not None:
            self.planning_time = m.get('PlanningTime')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')
        return self


class DescribeSlowLogRecordsResponseBodyItems(TeaModel):
    def __init__(self, slow_log_record=None):
        self.slow_log_record = slow_log_record  # type: list[DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord]

    def validate(self):
        if self.slow_log_record:
            for k in self.slow_log_record:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SlowLogRecord'] = []
        if self.slow_log_record is not None:
            for k in self.slow_log_record:
                result['SlowLogRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.slow_log_record = []
        if m.get('SlowLogRecord') is not None:
            for k in m.get('SlowLogRecord'):
                temp_model = DescribeSlowLogRecordsResponseBodyItemsSlowLogRecord()
                self.slow_log_record.append(temp_model.from_map(k))
        return self


class DescribeSlowLogRecordsResponseBody(TeaModel):
    def __init__(self, total_count=None, page_size=None, request_id=None, page_number=None, dbcluster_id=None,
                 items=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.items = items  # type: DescribeSlowLogRecordsResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSlowLogRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterResourcePoolPerformanceRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, key=None, resource_pools=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.resource_pools = TeaConverter.to_unicode(resource_pools)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_pools is not None:
            result['ResourcePools'] = self.resource_pools
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourcePools') is not None:
            self.resource_pools = m.get('ResourcePools')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries(TeaModel):
    def __init__(self, values=None, name=None):
        self.values = values  # type: list[unicode]
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances(TeaModel):
    def __init__(self, resource_pool_name=None, resource_pool_series=None):
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.resource_pool_series = resource_pool_series  # type: list[DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries]

    def validate(self):
        if self.resource_pool_series:
            for k in self.resource_pool_series:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        result['ResourcePoolSeries'] = []
        if self.resource_pool_series is not None:
            for k in self.resource_pool_series:
                result['ResourcePoolSeries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        self.resource_pool_series = []
        if m.get('ResourcePoolSeries') is not None:
            for k in m.get('ResourcePoolSeries'):
                temp_model = DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformancesResourcePoolSeries()
                self.resource_pool_series.append(temp_model.from_map(k))
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances(TeaModel):
    def __init__(self, key=None, unit=None, resource_pool_performances=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.unit = TeaConverter.to_unicode(unit)  # type: unicode
        self.resource_pool_performances = resource_pool_performances  # type: list[DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances]

    def validate(self):
        if self.resource_pool_performances:
            for k in self.resource_pool_performances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.unit is not None:
            result['Unit'] = self.unit
        result['ResourcePoolPerformances'] = []
        if self.resource_pool_performances is not None:
            for k in self.resource_pool_performances:
                result['ResourcePoolPerformances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        self.resource_pool_performances = []
        if m.get('ResourcePoolPerformances') is not None:
            for k in m.get('ResourcePoolPerformances'):
                temp_model = DescribeDBClusterResourcePoolPerformanceResponseBodyPerformancesResourcePoolPerformances()
                self.resource_pool_performances.append(temp_model.from_map(k))
        return self


class DescribeDBClusterResourcePoolPerformanceResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, start_time=None, dbcluster_id=None, performances=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.performances = performances  # type: list[DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances]

    def validate(self):
        if self.performances:
            for k in self.performances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        result['Performances'] = []
        if self.performances is not None:
            for k in self.performances:
                result['Performances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        self.performances = []
        if m.get('Performances') is not None:
            for k in m.get('Performances'):
                temp_model = DescribeDBClusterResourcePoolPerformanceResponseBodyPerformances()
                self.performances.append(temp_model.from_map(k))
        return self


class DescribeDBClusterResourcePoolPerformanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDBClusterResourcePoolPerformanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeDBClusterResourcePoolPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, account_name=None, account_password=None, account_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_password = TeaConverter.to_unicode(account_password)  # type: unicode
        self.account_type = TeaConverter.to_unicode(account_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None, dbcluster_id=None):
        self.task_id = task_id  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ResetAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, account_name=None, account_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode
        self.account_type = TeaConverter.to_unicode(account_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class DescribeAccountsResponseBodyAccountListDBAccount(TeaModel):
    def __init__(self, account_status=None, account_description=None, account_type=None, account_name=None):
        self.account_status = TeaConverter.to_unicode(account_status)  # type: unicode
        self.account_description = TeaConverter.to_unicode(account_description)  # type: unicode
        self.account_type = TeaConverter.to_unicode(account_type)  # type: unicode
        self.account_name = TeaConverter.to_unicode(account_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeAccountsResponseBodyAccountList(TeaModel):
    def __init__(self, dbaccount=None):
        self.dbaccount = dbaccount  # type: list[DescribeAccountsResponseBodyAccountListDBAccount]

    def validate(self):
        if self.dbaccount:
            for k in self.dbaccount:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k in self.dbaccount:
                result['DBAccount'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k in m.get('DBAccount'):
                temp_model = DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(self, request_id=None, account_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.account_list = account_list  # type: DescribeAccountsResponseBodyAccountList

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccountList') is not None:
            temp_model = DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m['AccountList'])
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticPlanRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, elastic_plan_name=None, resource_pool_name=None, elastic_plan_enable=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.elastic_plan_name = TeaConverter.to_unicode(elastic_plan_name)  # type: unicode
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.elastic_plan_enable = elastic_plan_enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.elastic_plan_name is not None:
            result['ElasticPlanName'] = self.elastic_plan_name
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.elastic_plan_enable is not None:
            result['ElasticPlanEnable'] = self.elastic_plan_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ElasticPlanName') is not None:
            self.elastic_plan_name = m.get('ElasticPlanName')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('ElasticPlanEnable') is not None:
            self.elastic_plan_enable = m.get('ElasticPlanEnable')
        return self


class DescribeElasticPlanResponseBodyElasticPlanList(TeaModel):
    def __init__(self, end_time=None, weekly_repeat=None, start_time=None, resource_pool_name=None, start_day=None,
                 elastic_node_num=None, enable=None, end_day=None, plan_name=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.weekly_repeat = TeaConverter.to_unicode(weekly_repeat)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.resource_pool_name = TeaConverter.to_unicode(resource_pool_name)  # type: unicode
        self.start_day = TeaConverter.to_unicode(start_day)  # type: unicode
        self.elastic_node_num = elastic_node_num  # type: int
        self.enable = enable  # type: bool
        self.end_day = TeaConverter.to_unicode(end_day)  # type: unicode
        self.plan_name = TeaConverter.to_unicode(plan_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.weekly_repeat is not None:
            result['WeeklyRepeat'] = self.weekly_repeat
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.resource_pool_name is not None:
            result['ResourcePoolName'] = self.resource_pool_name
        if self.start_day is not None:
            result['StartDay'] = self.start_day
        if self.elastic_node_num is not None:
            result['ElasticNodeNum'] = self.elastic_node_num
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_day is not None:
            result['EndDay'] = self.end_day
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('WeeklyRepeat') is not None:
            self.weekly_repeat = m.get('WeeklyRepeat')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ResourcePoolName') is not None:
            self.resource_pool_name = m.get('ResourcePoolName')
        if m.get('StartDay') is not None:
            self.start_day = m.get('StartDay')
        if m.get('ElasticNodeNum') is not None:
            self.elastic_node_num = m.get('ElasticNodeNum')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndDay') is not None:
            self.end_day = m.get('EndDay')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        return self


class DescribeElasticPlanResponseBody(TeaModel):
    def __init__(self, request_id=None, elastic_plan_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.elastic_plan_list = elastic_plan_list  # type: list[DescribeElasticPlanResponseBodyElasticPlanList]

    def validate(self):
        if self.elastic_plan_list:
            for k in self.elastic_plan_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ElasticPlanList'] = []
        if self.elastic_plan_list is not None:
            for k in self.elastic_plan_list:
                result['ElasticPlanList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.elastic_plan_list = []
        if m.get('ElasticPlanList') is not None:
            for k in m.get('ElasticPlanList'):
                temp_model = DescribeElasticPlanResponseBodyElasticPlanList()
                self.elastic_plan_list.append(temp_model.from_map(k))
        return self


class DescribeElasticPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeElasticPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeElasticPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTableDetailRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, schema_name=None, table_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.schema_name = TeaConverter.to_unicode(schema_name)  # type: unicode
        self.table_name = TeaConverter.to_unicode(table_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeTableDetailResponseBodyItemsShard(TeaModel):
    def __init__(self, size=None, id=None):
        self.size = size  # type: long
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTableDetailResponseBodyItems(TeaModel):
    def __init__(self, shard=None):
        self.shard = shard  # type: list[DescribeTableDetailResponseBodyItemsShard]

    def validate(self):
        if self.shard:
            for k in self.shard:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Shard'] = []
        if self.shard is not None:
            for k in self.shard:
                result['Shard'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.shard = []
        if m.get('Shard') is not None:
            for k in m.get('Shard'):
                temp_model = DescribeTableDetailResponseBodyItemsShard()
                self.shard.append(temp_model.from_map(k))
        return self


class DescribeTableDetailResponseBody(TeaModel):
    def __init__(self, avg_size=None, request_id=None, items=None):
        self.avg_size = avg_size  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.items = items  # type: DescribeTableDetailResponseBodyItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.avg_size is not None:
            result['AvgSize'] = self.avg_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgSize') is not None:
            self.avg_size = m.get('AvgSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Items') is not None:
            temp_model = DescribeTableDetailResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class DescribeTableDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTableDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeTableDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateClusterPublicConnectionRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, connection_string_prefix=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.connection_string_prefix = TeaConverter.to_unicode(connection_string_prefix)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        return self


class AllocateClusterPublicConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateClusterPublicConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AllocateClusterPublicConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AllocateClusterPublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(self, preferred_backup_period=None, log_backup_retention_period=None, request_id=None,
                 preferred_backup_time=None, enable_backup_log=None, backup_retention_period=None):
        self.preferred_backup_period = TeaConverter.to_unicode(preferred_backup_period)  # type: unicode
        self.log_backup_retention_period = log_backup_retention_period  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.preferred_backup_time = TeaConverter.to_unicode(preferred_backup_time)  # type: unicode
        self.enable_backup_log = TeaConverter.to_unicode(enable_backup_log)  # type: unicode
        self.backup_retention_period = backup_retention_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBackupPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterAccessWhiteListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, owner_account=None,
                 dbcluster_id=None, security_ips=None, dbcluster_iparray_name=None, dbcluster_iparray_attribute=None,
                 modify_mode=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode
        self.security_ips = TeaConverter.to_unicode(security_ips)  # type: unicode
        self.dbcluster_iparray_name = TeaConverter.to_unicode(dbcluster_iparray_name)  # type: unicode
        self.dbcluster_iparray_attribute = TeaConverter.to_unicode(dbcluster_iparray_attribute)  # type: unicode
        self.modify_mode = TeaConverter.to_unicode(modify_mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        return self


class ModifyDBClusterAccessWhiteListResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None, dbcluster_id=None):
        self.task_id = task_id  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dbcluster_id = TeaConverter.to_unicode(dbcluster_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        return self


class ModifyDBClusterAccessWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDBClusterAccessWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyDBClusterAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


