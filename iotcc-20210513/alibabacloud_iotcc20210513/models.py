# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DeleteServiceRequest(TeaModel):
    def __init__(self, service_id=None, io_tcloud_connector_id=None, client_token=None, dry_run=None,
                 region_id=None):
        self.service_id = service_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceResponse, self).to_map()
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceEntryRequest(TeaModel):
    def __init__(self, service_id=None, io_tcloud_connector_id=None, service_entry_id=None, client_token=None,
                 dry_run=None, region_id=None):
        self.service_id = service_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_entry_id = service_entry_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteServiceEntryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceEntryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceEntryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceEntryResponse, self).to_map()
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
            temp_model = DeleteServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceEntryAttributeRequest(TeaModel):
    def __init__(self, service_id=None, io_tcloud_connector_id=None, service_entry_id=None,
                 service_entry_name=None, service_entry_description=None, client_token=None, dry_run=None, region_id=None):
        self.service_id = service_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_entry_id = service_entry_id  # type: str
        self.service_entry_name = service_entry_name  # type: str
        self.service_entry_description = service_entry_description  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceEntryAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateServiceEntryAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceEntryAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceEntryAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceEntryAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceEntryAttributeResponse, self).to_map()
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
            temp_model = UpdateServiceEntryAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAttributeRequest(TeaModel):
    def __init__(self, service_id=None, io_tcloud_connector_id=None, service_name=None, service_description=None,
                 client_token=None, dry_run=None, region_id=None):
        self.service_id = service_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_name = service_name  # type: str
        self.service_description = service_description  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateServiceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceAttributeResponse, self).to_map()
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
            temp_model = UpdateServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationRulesRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, authorization_rule_ids=None, destination_type=None,
                 authorization_rule_status=None, authorization_rule_name=None, policy=None, next_token=None, max_results=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.authorization_rule_ids = authorization_rule_ids  # type: list[str]
        self.destination_type = destination_type  # type: list[str]
        self.authorization_rule_status = authorization_rule_status  # type: list[str]
        self.authorization_rule_name = authorization_rule_name  # type: list[str]
        self.policy = policy  # type: list[str]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAuthorizationRulesResponseBodyAuthorizationRules(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, policy=None, authorization_rule_status=None, source_cidrs=None,
                 destination_type=None, destination=None, authorization_rule_name=None, authorization_rule_description=None,
                 authorization_rule_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.policy = policy  # type: str
        self.authorization_rule_status = authorization_rule_status  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]
        self.destination_type = destination_type  # type: str
        self.destination = destination  # type: str
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthorizationRulesResponseBodyAuthorizationRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        return self


class ListAuthorizationRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None,
                 authorization_rules=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.authorization_rules = authorization_rules  # type: list[ListAuthorizationRulesResponseBodyAuthorizationRules]

    def validate(self):
        if self.authorization_rules:
            for k in self.authorization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthorizationRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['AuthorizationRules'] = []
        if self.authorization_rules is not None:
            for k in self.authorization_rules:
                result['AuthorizationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.authorization_rules = []
        if m.get('AuthorizationRules') is not None:
            for k in m.get('AuthorizationRules'):
                temp_model = ListAuthorizationRulesResponseBodyAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k))
        return self


class ListAuthorizationRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAuthorizationRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthorizationRulesResponse, self).to_map()
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
            temp_model = ListAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, service_ids=None, service_names=None, resource_statuses=None,
                 next_token=None, max_results=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_ids = service_ids  # type: list[str]
        self.service_names = service_names  # type: list[str]
        self.resource_statuses = resource_statuses  # type: list[str]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids
        if self.service_names is not None:
            result['ServiceNames'] = self.service_names
        if self.resource_statuses is not None:
            result['ResourceStatuses'] = self.resource_statuses
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')
        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')
        if m.get('ResourceStatuses') is not None:
            self.resource_statuses = m.get('ResourceStatuses')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListServiceResponseBodyServices(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, service_id=None, service_status=None, service_name=None,
                 service_description=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_id = service_id  # type: str
        self.service_status = service_status  # type: str
        self.service_name = service_name  # type: str
        self.service_description = service_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        return self


class ListServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None, services=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.services = services  # type: list[ListServiceResponseBodyServices]

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServiceResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceResponse, self).to_map()
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
            temp_model = ListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateVSwitchWithIoTCloudConnectorRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, vpc_id=None, v_switch_list=None, client_token=None,
                 dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_list = v_switch_list  # type: list[str]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateVSwitchWithIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_list is not None:
            result['VSwitchList'] = self.v_switch_list
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchList') is not None:
            self.v_switch_list = m.get('VSwitchList')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateVSwitchWithIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateVSwitchWithIoTCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateVSwitchWithIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateVSwitchWithIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateVSwitchWithIoTCloudConnectorResponse, self).to_map()
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
            temp_model = AssociateVSwitchWithIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolsRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, connection_pool_ids=None, connection_pool_name=None,
                 connection_pool_status=None, next_token=None, max_results=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.connection_pool_ids = connection_pool_ids  # type: list[str]
        self.connection_pool_name = connection_pool_name  # type: list[str]
        self.connection_pool_status = connection_pool_status  # type: list[str]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.connection_pool_ids is not None:
            result['ConnectionPoolIds'] = self.connection_pool_ids
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ConnectionPoolIds') is not None:
            self.connection_pool_ids = m.get('ConnectionPoolIds')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectionPoolsResponseBodyConnectionPools(TeaModel):
    def __init__(self, connection_pool_id=None, connection_pool_status=None, connection_pool_name=None,
                 connection_pool_description=None, cidrs=None):
        self.connection_pool_id = connection_pool_id  # type: str
        self.connection_pool_status = connection_pool_status  # type: str
        self.connection_pool_name = connection_pool_name  # type: str
        self.connection_pool_description = connection_pool_description  # type: str
        self.cidrs = cidrs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolsResponseBodyConnectionPools, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        return self


class ListConnectionPoolsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None, connection_pools=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.connection_pools = connection_pools  # type: list[ListConnectionPoolsResponseBodyConnectionPools]

    def validate(self):
        if self.connection_pools:
            for k in self.connection_pools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionPoolsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ConnectionPools'] = []
        if self.connection_pools is not None:
            for k in self.connection_pools:
                result['ConnectionPools'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.connection_pools = []
        if m.get('ConnectionPools') is not None:
            for k in m.get('ConnectionPools'):
                temp_model = ListConnectionPoolsResponseBodyConnectionPools()
                self.connection_pools.append(temp_model.from_map(k))
        return self


class ListConnectionPoolsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConnectionPoolsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectionPoolsResponse, self).to_map()
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
            temp_model = ListConnectionPoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionPoolAttributeRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, connection_pool_id=None, count=None, connection_pool_name=None,
                 connection_pool_description=None, cidrs=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.count = count  # type: long
        self.connection_pool_name = connection_pool_name  # type: str
        self.connection_pool_description = connection_pool_description  # type: str
        self.cidrs = cidrs  # type: list[str]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionPoolAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.count is not None:
            result['Count'] = self.count
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateConnectionPoolAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConnectionPoolAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConnectionPoolAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateConnectionPoolAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConnectionPoolAttributeResponse, self).to_map()
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
            temp_model = UpdateConnectionPoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableIoTCloudConnectorAccessLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableIoTCloudConnectorAccessLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableIoTCloudConnectorAccessLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableIoTCloudConnectorAccessLogResponse, self).to_map()
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
            temp_model = DisableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionPoolRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, count=None, connection_pool_name=None,
                 connection_pool_description=None, cidrs=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.count = count  # type: long
        self.connection_pool_name = connection_pool_name  # type: str
        self.connection_pool_description = connection_pool_description  # type: str
        self.cidrs = cidrs  # type: list[str]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.count is not None:
            result['Count'] = self.count
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateConnectionPoolResponseBody(TeaModel):
    def __init__(self, request_id=None, connection_pool_id=None):
        self.request_id = request_id  # type: str
        self.connection_pool_id = connection_pool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConnectionPoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        return self


class CreateConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConnectionPoolResponse, self).to_map()
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
            temp_model = CreateConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, destination_type=None, destination=None, policy=None,
                 source_cidrs=None, authorization_rule_name=None, authorization_rule_description=None, client_token=None,
                 dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.destination_type = destination_type  # type: str
        self.destination = destination  # type: str
        self.policy = policy  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, authorization_rule_id=None):
        self.request_id = request_id  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthorizationRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        return self


class CreateAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuthorizationRuleResponse, self).to_map()
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
            temp_model = CreateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIoTCloudConnectorAttributeRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, io_tcloud_connector_name=None,
                 io_tcloud_connector_description=None, wildcard_domain_enabled=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.wildcard_domain_enabled = wildcard_domain_enabled  # type: bool
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIoTCloudConnectorAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_id=None):
        self.request_id = request_id  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UpdateIoTCloudConnectorAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIoTCloudConnectorAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIoTCloudConnectorAttributeResponse, self).to_map()
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
            temp_model = UpdateIoTCloudConnectorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIoTCloudConnectorResponse, self).to_map()
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
            temp_model = DeleteIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorAvailableZonesRequest(TeaModel):
    def __init__(self, region_id=None, io_tcloud_connector_id=None):
        self.region_id = region_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorAvailableZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        return self


class ListIoTCloudConnectorAvailableZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, io_tcloud_connector_id=None, available_zone_list=None):
        self.request_id = request_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.available_zone_list = available_zone_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorAvailableZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.available_zone_list is not None:
            result['AvailableZoneList'] = self.available_zone_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AvailableZoneList') is not None:
            self.available_zone_list = m.get('AvailableZoneList')
        return self


class ListIoTCloudConnectorAvailableZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIoTCloudConnectorAvailableZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorAvailableZonesResponse, self).to_map()
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
            temp_model = ListIoTCloudConnectorAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIoTCloudConnectorAccessLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(self, request_id=None, access_log_sls_project=None, access_log_sls_log_store=None,
                 access_log_status=None):
        self.request_id = request_id  # type: str
        self.access_log_sls_project = access_log_sls_project  # type: str
        self.access_log_sls_log_store = access_log_sls_log_store  # type: str
        self.access_log_status = access_log_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIoTCloudConnectorAccessLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.access_log_status is not None:
            result['AccessLogStatus'] = self.access_log_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('AccessLogStatus') is not None:
            self.access_log_status = m.get('AccessLogStatus')
        return self


class GetIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIoTCloudConnectorAccessLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIoTCloudConnectorAccessLogResponse, self).to_map()
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
            temp_model = GetIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationRuleRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, authorization_rule_id=None, client_token=None, dry_run=None,
                 region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthorizationRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAuthorizationRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthorizationRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAuthorizationRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAuthorizationRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAuthorizationRuleResponse, self).to_map()
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
            temp_model = DeleteAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionPoolRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, connection_pool_id=None, client_token=None, dry_run=None,
                 region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectionPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConnectionPoolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConnectionPoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConnectionPoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteConnectionPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConnectionPoolResponse, self).to_map()
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
            temp_model = DeleteConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateVSwitchFromIoTCloudConnectorRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateVSwitchFromIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateVSwitchFromIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateVSwitchFromIoTCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DissociateVSwitchFromIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateVSwitchFromIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateVSwitchFromIoTCloudConnectorResponse, self).to_map()
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
            temp_model = DissociateVSwitchFromIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, access_log_sls_project=None, access_log_sls_log_store=None,
                 client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.access_log_sls_project = access_log_sls_project  # type: str
        self.access_log_sls_log_store = access_log_sls_log_store  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableIoTCloudConnectorAccessLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableIoTCloudConnectorAccessLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableIoTCloudConnectorAccessLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableIoTCloudConnectorAccessLogResponse, self).to_map()
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
            temp_model = EnableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceEntriesRequest(TeaModel):
    def __init__(self, service_id=None, io_tcloud_connector_id=None, target=None, target_type=None,
                 service_entry_status=None, service_entry_name=None, next_token=None, max_results=None, region_id=None,
                 service_entry_ids=None):
        self.service_id = service_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.target = target  # type: list[str]
        self.target_type = target_type  # type: list[str]
        self.service_entry_status = service_entry_status  # type: list[str]
        self.service_entry_name = service_entry_name  # type: list[str]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.region_id = region_id  # type: str
        self.service_entry_ids = service_entry_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_ids is not None:
            result['ServiceEntryIds'] = self.service_entry_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryIds') is not None:
            self.service_entry_ids = m.get('ServiceEntryIds')
        return self


class ListServiceEntriesResponseBodyServiceEntries(TeaModel):
    def __init__(self, service_id=None, service_entry_status=None, target=None, target_type=None,
                 service_entry_name=None, service_entry_description=None, service_entry_id=None):
        self.service_id = service_id  # type: str
        self.service_entry_status = service_entry_status  # type: str
        self.target = target  # type: str
        self.target_type = target_type  # type: str
        self.service_entry_name = service_entry_name  # type: str
        self.service_entry_description = service_entry_description  # type: str
        self.service_entry_id = service_entry_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceEntriesResponseBodyServiceEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        return self


class ListServiceEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, next_token=None, max_results=None, service_entries=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.service_entries = service_entries  # type: list[ListServiceEntriesResponseBodyServiceEntries]

    def validate(self):
        if self.service_entries:
            for k in self.service_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceEntries'] = []
        if self.service_entries is not None:
            for k in self.service_entries:
                result['ServiceEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.service_entries = []
        if m.get('ServiceEntries') is not None:
            for k in m.get('ServiceEntries'):
                temp_model = ListServiceEntriesResponseBodyServiceEntries()
                self.service_entries.append(temp_model.from_map(k))
        return self


class ListServiceEntriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceEntriesResponse, self).to_map()
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
            temp_model = ListServiceEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, service_name=None, service_description=None, client_token=None,
                 dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.service_name = service_name  # type: str
        self.service_description = service_description  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, service_id=None):
        self.request_id = request_id  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceResponse, self).to_map()
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorsRequest(TeaModel):
    def __init__(self, io_tcloud_connector_status=None, io_tcloud_connector_ids=None,
                 io_tcloud_connector_name=None, isps=None, vpc_ids=None, apns=None, next_token=None, max_results=None, region_id=None):
        self.io_tcloud_connector_status = io_tcloud_connector_status  # type: list[str]
        self.io_tcloud_connector_ids = io_tcloud_connector_ids  # type: list[str]
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: list[str]
        self.isps = isps  # type: list[str]
        self.vpc_ids = vpc_ids  # type: list[str]
        self.apns = apns  # type: list[str]
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.io_tcloud_connector_ids is not None:
            result['IoTCloudConnectorIds'] = self.io_tcloud_connector_ids
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.isps is not None:
            result['Isps'] = self.isps
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.apns is not None:
            result['Apns'] = self.apns
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('IoTCloudConnectorIds') is not None:
            self.io_tcloud_connector_ids = m.get('IoTCloudConnectorIds')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('Isps') is not None:
            self.isps = m.get('Isps')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Apns') is not None:
            self.apns = m.get('Apns')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIoTCloudConnectorsResponseBodyIoTCloudConnectors(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, io_tcloud_connector_status=None, isp=None,
                 io_tcloud_connector_business_status=None, apn=None, rate_limit=None, vpc_id=None, v_switch_ids=None, io_tcloud_connector_name=None,
                 io_tcloud_connector_description=None, wildcard_domain_enabled=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.io_tcloud_connector_status = io_tcloud_connector_status  # type: str
        self.isp = isp  # type: str
        self.io_tcloud_connector_business_status = io_tcloud_connector_business_status  # type: str
        self.apn = apn  # type: str
        self.rate_limit = rate_limit  # type: long
        self.vpc_id = vpc_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.wildcard_domain_enabled = wildcard_domain_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorsResponseBodyIoTCloudConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.io_tcloud_connector_business_status is not None:
            result['IoTCloudConnectorBusinessStatus'] = self.io_tcloud_connector_business_status
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('IoTCloudConnectorBusinessStatus') is not None:
            self.io_tcloud_connector_business_status = m.get('IoTCloudConnectorBusinessStatus')
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('RateLimit') is not None:
            self.rate_limit = m.get('RateLimit')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class ListIoTCloudConnectorsResponseBody(TeaModel):
    def __init__(self, total_count=None, next_token=None, max_results=None, request_id=None,
                 io_tcloud_connectors=None):
        self.total_count = total_count  # type: int
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.request_id = request_id  # type: str
        self.io_tcloud_connectors = io_tcloud_connectors  # type: list[ListIoTCloudConnectorsResponseBodyIoTCloudConnectors]

    def validate(self):
        if self.io_tcloud_connectors:
            for k in self.io_tcloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['IoTCloudConnectors'] = []
        if self.io_tcloud_connectors is not None:
            for k in self.io_tcloud_connectors:
                result['IoTCloudConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.io_tcloud_connectors = []
        if m.get('IoTCloudConnectors') is not None:
            for k in m.get('IoTCloudConnectors'):
                temp_model = ListIoTCloudConnectorsResponseBodyIoTCloudConnectors()
                self.io_tcloud_connectors.append(temp_model.from_map(k))
        return self


class ListIoTCloudConnectorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIoTCloudConnectorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorsResponse, self).to_map()
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
            temp_model = ListIoTCloudConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorRequest(TeaModel):
    def __init__(self, isp=None, apn=None, io_tcloud_connector_name=None, io_tcloud_connector_description=None,
                 wildcard_domain_enabled=None, client_token=None, dry_run=None, region_id=None):
        self.isp = isp  # type: str
        self.apn = apn  # type: str
        self.io_tcloud_connector_name = io_tcloud_connector_name  # type: str
        self.io_tcloud_connector_description = io_tcloud_connector_description  # type: str
        self.wildcard_domain_enabled = wildcard_domain_enabled  # type: bool
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.apn is not None:
            result['APN'] = self.apn
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIoTCloudConnectorResponseBody(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, request_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIoTCloudConnectorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIoTCloudConnectorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIoTCloudConnectorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIoTCloudConnectorResponse, self).to_map()
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
            temp_model = CreateIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleAttributeRequest(TeaModel):
    def __init__(self, io_tcloud_connector_id=None, authorization_rule_id=None, destination_type=None,
                 destination=None, policy=None, source_cidrs=None, authorization_rule_name=None,
                 authorization_rule_description=None, client_token=None, dry_run=None, region_id=None):
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.authorization_rule_id = authorization_rule_id  # type: str
        self.destination_type = destination_type  # type: str
        self.destination = destination  # type: str
        self.policy = policy  # type: str
        self.source_cidrs = source_cidrs  # type: list[str]
        self.authorization_rule_name = authorization_rule_name  # type: str
        self.authorization_rule_description = authorization_rule_description  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationRuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAuthorizationRuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuthorizationRuleAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuthorizationRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAuthorizationRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuthorizationRuleAttributeResponse, self).to_map()
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
            temp_model = UpdateAuthorizationRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceEntryRequest(TeaModel):
    def __init__(self, service_id=None, io_tcloud_connector_id=None, target=None, target_type=None,
                 service_entry_name=None, service_entry_description=None, client_token=None, dry_run=None, region_id=None):
        self.service_id = service_id  # type: str
        self.io_tcloud_connector_id = io_tcloud_connector_id  # type: str
        self.target = target  # type: str
        self.target_type = target_type  # type: str
        self.service_entry_name = service_entry_name  # type: str
        self.service_entry_description = service_entry_description  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceEntryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceEntryResponseBody(TeaModel):
    def __init__(self, request_id=None, service_entry_id=None):
        self.request_id = request_id  # type: str
        self.service_entry_id = service_entry_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceEntryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        return self


class CreateServiceEntryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceEntryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceEntryResponse, self).to_map()
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
            temp_model = CreateServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


