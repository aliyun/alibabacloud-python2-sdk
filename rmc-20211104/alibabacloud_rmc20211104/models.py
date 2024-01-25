# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ListResourceRelationshipsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, source_region_id=None, source_resource_id=None,
                 source_resource_type=None, target_resource_type=None):
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results  # type: int
        # The token that is used to initiate the next request.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the token to initiate another request and obtain the remaining entries.
        self.next_token = next_token  # type: str
        # The region ID of the resource whose associated resources you want to query.
        self.source_region_id = source_region_id  # type: str
        # The IDs of the resource whose associated resources you want to query.
        # 
        # You can specify a maximum of 10 resource IDs.
        self.source_resource_id = source_resource_id  # type: list[str]
        # The type of the resource whose associated resources you want to query.
        self.source_resource_type = source_resource_type  # type: str
        # The types of the associated resources that you want to query.
        # 
        # You can specify a maximum of 10 resource types.
        self.target_resource_type = target_resource_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceRelationshipsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.source_resource_id is not None:
            result['SourceResourceId'] = self.source_resource_id
        if self.source_resource_type is not None:
            result['SourceResourceType'] = self.source_resource_type
        if self.target_resource_type is not None:
            result['TargetResourceType'] = self.target_resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('SourceResourceId') is not None:
            self.source_resource_id = m.get('SourceResourceId')
        if m.get('SourceResourceType') is not None:
            self.source_resource_type = m.get('SourceResourceType')
        if m.get('TargetResourceType') is not None:
            self.target_resource_type = m.get('TargetResourceType')
        return self


class ListResourceRelationshipsResponseBodyResourceRelationships(TeaModel):
    def __init__(self, account_id=None, source_region_id=None, source_resource_id=None, source_resource_type=None,
                 target_region_id=None, target_resource_id=None, target_resource_type=None):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The region ID of the specified resource.
        self.source_region_id = source_region_id  # type: str
        # The ID of the specified resource.
        self.source_resource_id = source_resource_id  # type: str
        # The type of the specified resource.
        self.source_resource_type = source_resource_type  # type: str
        # The region ID of the associated resource.
        self.target_region_id = target_region_id  # type: str
        # The ID of the associated resource.
        self.target_resource_id = target_resource_id  # type: str
        # The type of the associated resource.
        self.target_resource_type = target_resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceRelationshipsResponseBodyResourceRelationships, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.source_resource_id is not None:
            result['SourceResourceId'] = self.source_resource_id
        if self.source_resource_type is not None:
            result['SourceResourceType'] = self.source_resource_type
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_resource_id is not None:
            result['TargetResourceId'] = self.target_resource_id
        if self.target_resource_type is not None:
            result['TargetResourceType'] = self.target_resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('SourceResourceId') is not None:
            self.source_resource_id = m.get('SourceResourceId')
        if m.get('SourceResourceType') is not None:
            self.source_resource_type = m.get('SourceResourceType')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetResourceId') is not None:
            self.target_resource_id = m.get('TargetResourceId')
        if m.get('TargetResourceType') is not None:
            self.target_resource_type = m.get('TargetResourceType')
        return self


class ListResourceRelationshipsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resource_relationships=None):
        # The maximum number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to initiate the next request.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the associated resources.
        self.resource_relationships = resource_relationships  # type: list[ListResourceRelationshipsResponseBodyResourceRelationships]

    def validate(self):
        if self.resource_relationships:
            for k in self.resource_relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceRelationshipsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceRelationships'] = []
        if self.resource_relationships is not None:
            for k in self.resource_relationships:
                result['ResourceRelationships'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_relationships = []
        if m.get('ResourceRelationships') is not None:
            for k in m.get('ResourceRelationships'):
                temp_model = ListResourceRelationshipsResponseBodyResourceRelationships()
                self.resource_relationships.append(temp_model.from_map(k))
        return self


class ListResourceRelationshipsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceRelationshipsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceRelationshipsResponse, self).to_map()
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
            temp_model = ListResourceRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchResourcesRequestFilter(TeaModel):
    def __init__(self, key=None, match_type=None, value=None):
        # The key of the filter condition. Valid values:
        # 
        # *   ResourceType: resource type
        # *   RegionId: region ID
        # *   ResourceId: resource ID
        # *   ResourceGroupId: resource group ID
        # *   ResourceName: resource name
        self.key = key  # type: str
        # The matching method. Set the value to Equals. This value indicates that resources that match the filter conditions are queried.
        self.match_type = match_type  # type: str
        # The values of the filter condition.
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchResourcesRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchResourcesRequestSortCriterion(TeaModel):
    def __init__(self, key=None, order=None):
        # The attribute based on which the entries are sorted.
        # 
        # The value `CreateTime` indicates the creation time of resources.
        self.key = key  # type: str
        # The order in which the entries are sorted. Valid values:
        # 
        # *   ASC: The entries are sorted in ascending order. This value is the default value.
        # *   DESC: The entries are sorted in descending order.
        self.order = order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchResourcesRequestSortCriterion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class SearchResourcesRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None, resource_group_id=None, sort_criterion=None):
        # The filter conditions.
        self.filter = filter  # type: list[SearchResourcesRequestFilter]
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results  # type: int
        # The token that is used to initiate the next request.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the token to initiate another request and obtain the remaining entries.
        self.next_token = next_token  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The method that is used to sort the entries.
        self.sort_criterion = sort_criterion  # type: SearchResourcesRequestSortCriterion

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        _map = super(SearchResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortCriterion') is not None:
            temp_model = SearchResourcesRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m['SortCriterion'])
        return self


class SearchResourcesResponseBodyFilters(TeaModel):
    def __init__(self, key=None, match_type=None, values=None):
        # The key of the filter condition.
        self.key = key  # type: str
        # The matching method.
        self.match_type = match_type  # type: str
        # The values of the filter condition.
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchResourcesResponseBodyFilters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchResourcesResponseBodyResourcesTags, self).to_map()
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


class SearchResourcesResponseBodyResources(TeaModel):
    def __init__(self, account_id=None, create_time=None, ip_addresses=None, region_id=None, resource_group_id=None,
                 resource_id=None, resource_name=None, resource_type=None, tags=None, zone_id=None):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The time when the resource was created.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.create_time = create_time  # type: str
        # The IP addresses.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses  # type: list[str]
        # The region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The name of the resource.
        self.resource_name = resource_name  # type: str
        # The type of the resource.
        self.resource_type = resource_type  # type: str
        # The tags.
        self.tags = tags  # type: list[SearchResourcesResponseBodyResourcesTags]
        # The zone ID.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchResourcesResponseBody(TeaModel):
    def __init__(self, filters=None, max_results=None, next_token=None, request_id=None, resources=None):
        # The filter conditions.
        self.filters = filters  # type: list[SearchResourcesResponseBodyFilters]
        # The maximum number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used to initiate the next request.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the resources.
        self.resources = resources  # type: list[SearchResourcesResponseBodyResources]

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = SearchResourcesResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = SearchResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class SearchResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchResourcesResponse, self).to_map()
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
            temp_model = SearchResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


