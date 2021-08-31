# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class InvokeServiceInstanceOperationAPIRequest(TeaModel):
    def __init__(self, service_instance_id=None, region_id=None, operation_product=None, operation_action=None,
                 operation_version=None, operation_parameters=None):
        self.service_instance_id = service_instance_id  # type: str
        self.region_id = region_id  # type: str
        self.operation_product = operation_product  # type: str
        self.operation_action = operation_action  # type: str
        self.operation_version = operation_version  # type: str
        self.operation_parameters = operation_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeServiceInstanceOperationAPIRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_product is not None:
            result['OperationProduct'] = self.operation_product
        if self.operation_action is not None:
            result['OperationAction'] = self.operation_action
        if self.operation_version is not None:
            result['OperationVersion'] = self.operation_version
        if self.operation_parameters is not None:
            result['OperationParameters'] = self.operation_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationProduct') is not None:
            self.operation_product = m.get('OperationProduct')
        if m.get('OperationAction') is not None:
            self.operation_action = m.get('OperationAction')
        if m.get('OperationVersion') is not None:
            self.operation_version = m.get('OperationVersion')
        if m.get('OperationParameters') is not None:
            self.operation_parameters = m.get('OperationParameters')
        return self


class InvokeServiceInstanceOperationAPIResponseBody(TeaModel):
    def __init__(self, request_id=None, operation_results=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.operation_results = operation_results  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeServiceInstanceOperationAPIResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_results is not None:
            result['OperationResults'] = self.operation_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationResults') is not None:
            self.operation_results = m.get('OperationResults')
        return self


class InvokeServiceInstanceOperationAPIResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InvokeServiceInstanceOperationAPIResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InvokeServiceInstanceOperationAPIResponse, self).to_map()
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
            temp_model = InvokeServiceInstanceOperationAPIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(self, service_instance_id=None, region_id=None):
        self.service_instance_id = service_instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(self, locale=None, image=None, name=None, short_description=None):
        self.locale = locale  # type: str
        self.image = image  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyServiceServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(self, status=None, publish_time=None, version=None, deploy_metadata=None, deploy_type=None,
                 service_id=None, supplier_url=None, service_type=None, supplier_name=None, service_infos=None):
        self.status = status  # type: str
        self.publish_time = publish_time  # type: str
        self.version = version  # type: str
        self.deploy_metadata = deploy_metadata  # type: str
        self.deploy_type = deploy_type  # type: str
        self.service_id = service_id  # type: str
        self.supplier_url = supplier_url  # type: str
        self.service_type = service_type  # type: str
        self.supplier_name = supplier_name  # type: str
        self.service_infos = service_infos  # type: list[GetServiceInstanceResponseBodyServiceServiceInfos]

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        return self


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(self, status=None, template_name=None, update_time=None, request_id=None, service_instance_id=None,
                 create_time=None, user_id=None, service=None, parameters=None, progress=None, status_detail=None,
                 operation_start_time=None, operation_end_time=None, operated_service_instance_id=None, is_operated=None,
                 enable_instance_ops=None, resources=None):
        self.status = status  # type: str
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str
        self.request_id = request_id  # type: str
        self.service_instance_id = service_instance_id  # type: str
        self.create_time = create_time  # type: str
        self.user_id = user_id  # type: long
        self.service = service  # type: GetServiceInstanceResponseBodyService
        self.parameters = parameters  # type: str
        self.progress = progress  # type: long
        self.status_detail = status_detail  # type: str
        self.operation_start_time = operation_start_time  # type: str
        self.operation_end_time = operation_end_time  # type: str
        self.operated_service_instance_id = operated_service_instance_id  # type: str
        self.is_operated = is_operated  # type: bool
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.resources = resources  # type: str

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class GetServiceInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponse, self).to_map()
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
            temp_model = GetServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(self, region_id=None, service_id=None, service_version=None, client_token=None):
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str
        self.service_version = service_version  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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


class ListServicesRequestFilter(TeaModel):
    def __init__(self, value=None, name=None):
        self.value = value  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, all_versions=None, filter=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.all_versions = all_versions  # type: bool
        self.filter = filter  # type: list[ListServicesRequestFilter]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.all_versions is not None:
            result['AllVersions'] = self.all_versions
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('AllVersions') is not None:
            self.all_versions = m.get('AllVersions')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServicesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListServicesResponseBodyServicesServiceInfos(TeaModel):
    def __init__(self, locale=None, image=None, name=None, short_description=None):
        self.locale = locale  # type: str
        self.image = image  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesResponseBodyServicesServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(self, status=None, default_version=None, publish_time=None, version=None, deploy_type=None,
                 service_id=None, supplier_url=None, service_type=None, supplier_name=None, service_infos=None,
                 commodity_code=None):
        self.status = status  # type: str
        self.default_version = default_version  # type: bool
        self.publish_time = publish_time  # type: str
        self.version = version  # type: str
        self.deploy_type = deploy_type  # type: str
        self.service_id = service_id  # type: str
        self.supplier_url = supplier_url  # type: str
        self.service_type = service_type  # type: str
        self.supplier_name = supplier_name  # type: str
        self.service_infos = service_infos  # type: list[ListServicesResponseBodyServicesServiceInfos]
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServicesResponseBodyServicesServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, total_count=None, max_results=None, services=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str
        self.max_results = max_results  # type: int
        self.services = services  # type: list[ListServicesResponseBodyServices]

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServicesResponse, self).to_map()
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelServiceRegistrationRequest(TeaModel):
    def __init__(self, region_id=None, registration_id=None, client_token=None):
        self.region_id = region_id  # type: str
        self.registration_id = registration_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelServiceRegistrationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CancelServiceRegistrationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelServiceRegistrationResponseBody, self).to_map()
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


class CancelServiceRegistrationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelServiceRegistrationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelServiceRegistrationResponse, self).to_map()
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
            temp_model = CancelServiceRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceRegistrationsRequestFilter(TeaModel):
    def __init__(self, value=None, name=None):
        self.value = value  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceRegistrationsRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListServiceRegistrationsRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, filter=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.filter = filter  # type: list[ListServiceRegistrationsRequestFilter]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceRegistrationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceRegistrationsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListServiceRegistrationsResponseBodyServiceRegistrations(TeaModel):
    def __init__(self, status=None, registration_id=None, finish_time=None, comment=None, service_id=None,
                 submit_time=None):
        self.status = status  # type: str
        self.registration_id = registration_id  # type: str
        self.finish_time = finish_time  # type: str
        self.comment = comment  # type: str
        self.service_id = service_id  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceRegistrationsResponseBodyServiceRegistrations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class ListServiceRegistrationsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, total_count=None, max_results=None,
                 service_registrations=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str
        self.max_results = max_results  # type: int
        self.service_registrations = service_registrations  # type: list[ListServiceRegistrationsResponseBodyServiceRegistrations]

    def validate(self):
        if self.service_registrations:
            for k in self.service_registrations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceRegistrationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceRegistrations'] = []
        if self.service_registrations is not None:
            for k in self.service_registrations:
                result['ServiceRegistrations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.service_registrations = []
        if m.get('ServiceRegistrations') is not None:
            for k in m.get('ServiceRegistrations'):
                temp_model = ListServiceRegistrationsResponseBodyServiceRegistrations()
                self.service_registrations.append(temp_model.from_map(k))
        return self


class ListServiceRegistrationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceRegistrationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceRegistrationsResponse, self).to_map()
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
            temp_model = ListServiceRegistrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupplierInformationRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSupplierInformationRequest, self).to_map()
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


class GetSupplierInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, supplier_name=None, supplier_url=None, supplier_desc=None,
                 operation_ip=None, operation_mfa_present=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.supplier_desc = supplier_desc  # type: str
        self.operation_ip = operation_ip  # type: str
        self.operation_mfa_present = operation_mfa_present  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSupplierInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc
        if self.operation_ip is not None:
            result['OperationIp'] = self.operation_ip
        if self.operation_mfa_present is not None:
            result['OperationMfaPresent'] = self.operation_mfa_present
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')
        if m.get('OperationIp') is not None:
            self.operation_ip = m.get('OperationIp')
        if m.get('OperationMfaPresent') is not None:
            self.operation_mfa_present = m.get('OperationMfaPresent')
        return self


class GetSupplierInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSupplierInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSupplierInformationResponse, self).to_map()
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
            temp_model = GetSupplierInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(self, value=None, name=None):
        self.value = value  # type: list[str]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListServiceInstancesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, filter=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.filter = filter  # type: list[ListServiceInstancesRequestFilter]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(self, locale=None, image=None, name=None, short_description=None):
        self.locale = locale  # type: str
        self.image = image  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(self, status=None, publish_time=None, version=None, deploy_type=None, service_id=None,
                 supplier_url=None, service_type=None, supplier_name=None, service_infos=None):
        self.status = status  # type: str
        self.publish_time = publish_time  # type: str
        self.version = version  # type: str
        self.deploy_type = deploy_type  # type: str
        self.service_id = service_id  # type: str
        self.supplier_url = supplier_url  # type: str
        self.service_type = service_type  # type: str
        self.supplier_name = supplier_name  # type: str
        self.service_infos = service_infos  # type: list[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos]

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(self, status=None, update_time=None, service_instance_id=None, create_time=None, user_id=None,
                 service=None, parameters=None, progress=None, status_detail=None, template_name=None,
                 operated_service_instance_id=None, operation_start_time=None, operation_end_time=None, enable_instance_ops=None):
        self.status = status  # type: str
        self.update_time = update_time  # type: str
        self.service_instance_id = service_instance_id  # type: str
        self.create_time = create_time  # type: str
        self.user_id = user_id  # type: long
        self.service = service  # type: ListServiceInstancesResponseBodyServiceInstancesService
        self.parameters = parameters  # type: str
        self.progress = progress  # type: long
        self.status_detail = status_detail  # type: str
        self.template_name = template_name  # type: str
        self.operated_service_instance_id = operated_service_instance_id  # type: str
        self.operation_start_time = operation_start_time  # type: str
        self.operation_end_time = operation_end_time  # type: str
        self.enable_instance_ops = enable_instance_ops  # type: bool

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, total_count=None, max_results=None, service_instances=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.max_results = max_results  # type: str
        self.service_instances = service_instances  # type: list[ListServiceInstancesResponseBodyServiceInstances]

    def validate(self):
        if self.service_instances:
            for k in self.service_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponse, self).to_map()
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
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterServiceRequest(TeaModel):
    def __init__(self, region_id=None, service_id=None, client_token=None):
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RegisterServiceResponseBody(TeaModel):
    def __init__(self, registration_id=None, request_id=None):
        self.registration_id = registration_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterServiceResponse, self).to_map()
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
            temp_model = RegisterServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestServiceInfo(TeaModel):
    def __init__(self, locale=None, short_description=None, image=None, name=None):
        self.locale = locale  # type: str
        self.short_description = short_description  # type: str
        self.image = image  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequestServiceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, region_id=None, supplier_name=None, supplier_url=None, client_token=None, service_id=None,
                 deploy_type=None, deploy_metadata=None, service_type=None, service_info=None, is_support_operated=None,
                 policy_names=None, duration=None):
        self.region_id = region_id  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.client_token = client_token  # type: str
        self.service_id = service_id  # type: str
        self.deploy_type = deploy_type  # type: str
        self.deploy_metadata = deploy_metadata  # type: str
        self.service_type = service_type  # type: str
        self.service_info = service_info  # type: list[CreateServiceRequestServiceInfo]
        self.is_support_operated = is_support_operated  # type: bool
        self.policy_names = policy_names  # type: str
        self.duration = duration  # type: long

    def validate(self):
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = CreateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, version=None, service_id=None):
        self.status = status  # type: str
        self.request_id = request_id  # type: str
        self.version = version  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
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


class ListPoliciesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, description=None, policy_name=None, policy_type=None, policy_document=None):
        self.description = description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.policy_document = policy_document  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(self, request_id=None, next_token=None, policies=None, max_results=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # NextToken
        self.next_token = next_token  # type: str
        self.policies = policies  # type: list[ListPoliciesResponseBodyPolicies]
        self.max_results = max_results  # type: str

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPoliciesResponse, self).to_map()
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequestServiceInfo(TeaModel):
    def __init__(self, locale=None, short_description=None, image=None, name=None):
        self.locale = locale  # type: str
        self.short_description = short_description  # type: str
        self.image = image  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceRequestServiceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(self, region_id=None, supplier_name=None, supplier_url=None, deploy_type=None,
                 deploy_metadata=None, client_token=None, service_id=None, service_type=None, service_info=None,
                 is_support_operated=None, policy_names=None, duration=None):
        self.region_id = region_id  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.deploy_type = deploy_type  # type: str
        self.deploy_metadata = deploy_metadata  # type: str
        self.client_token = client_token  # type: str
        self.service_id = service_id  # type: str
        self.service_type = service_type  # type: str
        self.service_info = service_info  # type: list[UpdateServiceRequestServiceInfo]
        self.is_support_operated = is_support_operated  # type: bool
        self.policy_names = policy_names  # type: str
        self.duration = duration  # type: long

    def validate(self):
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = UpdateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceResponseBody, self).to_map()
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


class UpdateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceResponse, self).to_map()
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LaunchServiceRequest(TeaModel):
    def __init__(self, region_id=None, service_id=None, service_version=None, client_token=None):
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str
        self.service_version = service_version  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LaunchServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class LaunchServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, service_id=None, version=None, status=None):
        self.request_id = request_id  # type: str
        self.service_id = service_id  # type: str
        self.version = version  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LaunchServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.version is not None:
            result['Version'] = self.version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class LaunchServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: LaunchServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LaunchServiceResponse, self).to_map()
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
            temp_model = LaunchServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawServiceRequest(TeaModel):
    def __init__(self, region_id=None, service_id=None, service_version=None, client_token=None):
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str
        self.service_version = service_version  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WithdrawServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class WithdrawServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WithdrawServiceResponseBody, self).to_map()
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


class WithdrawServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WithdrawServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WithdrawServiceResponse, self).to_map()
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
            temp_model = WithdrawServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSupplierInformationRequest(TeaModel):
    def __init__(self, region_id=None, operation_ip=None, operation_mfa_present=None):
        self.region_id = region_id  # type: str
        self.operation_ip = operation_ip  # type: str
        self.operation_mfa_present = operation_mfa_present  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSupplierInformationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_ip is not None:
            result['OperationIp'] = self.operation_ip
        if self.operation_mfa_present is not None:
            result['OperationMfaPresent'] = self.operation_mfa_present
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationIp') is not None:
            self.operation_ip = m.get('OperationIp')
        if m.get('OperationMfaPresent') is not None:
            self.operation_mfa_present = m.get('OperationMfaPresent')
        return self


class UpdateSupplierInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, supplier_name=None, supplier_url=None, supplier_desc=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.supplier_desc = supplier_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSupplierInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')
        return self


class UpdateSupplierInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSupplierInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSupplierInformationResponse, self).to_map()
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
            temp_model = UpdateSupplierInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(self, region_id=None, service_id=None, service_version=None):
        self.region_id = region_id  # type: str
        self.service_id = service_id  # type: str
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class GetServiceResponseBodyServiceInfos(TeaModel):
    def __init__(self, locale=None, image=None, name=None, short_description=None):
        self.locale = locale  # type: str
        self.image = image  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceResponseBodyServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(self, status=None, deploy_metadata=None, publish_time=None, request_id=None, version=None,
                 deploy_type=None, service_id=None, supplier_url=None, service_type=None, supplier_name=None,
                 service_infos=None, commodity_code=None, is_support_operated=None, policy_names=None, duration=None):
        self.status = status  # type: str
        self.deploy_metadata = deploy_metadata  # type: str
        self.publish_time = publish_time  # type: str
        self.request_id = request_id  # type: str
        self.version = version  # type: str
        self.deploy_type = deploy_type  # type: str
        self.service_id = service_id  # type: str
        self.supplier_url = supplier_url  # type: str
        self.service_type = service_type  # type: str
        self.supplier_name = supplier_name  # type: str
        self.service_infos = service_infos  # type: list[GetServiceResponseBodyServiceInfos]
        self.commodity_code = commodity_code  # type: str
        self.is_support_operated = is_support_operated  # type: bool
        self.policy_names = policy_names  # type: str
        self.duration = duration  # type: long

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceResponseBodyServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class GetServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceResponse, self).to_map()
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


