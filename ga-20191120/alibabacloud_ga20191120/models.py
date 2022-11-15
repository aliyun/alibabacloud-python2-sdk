# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddEntriesToAclRequestAclEntries(TeaModel):
    def __init__(self, entry=None, entry_description=None):
        self.entry = entry  # type: str
        self.entry_description = entry_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEntriesToAclRequestAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class AddEntriesToAclRequest(TeaModel):
    def __init__(self, acl_entries=None, acl_id=None, client_token=None, dry_run=None, region_id=None):
        self.acl_entries = acl_entries  # type: list[AddEntriesToAclRequestAclEntries]
        self.acl_id = acl_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddEntriesToAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = AddEntriesToAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddEntriesToAclResponseBody(TeaModel):
    def __init__(self, acl_id=None, request_id=None):
        self.acl_id = acl_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEntriesToAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddEntriesToAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddEntriesToAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEntriesToAclResponse, self).to_map()
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
            temp_model = AddEntriesToAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAclsWithListenerRequest(TeaModel):
    def __init__(self, acl_ids=None, acl_type=None, client_token=None, dry_run=None, listener_id=None,
                 region_id=None):
        self.acl_ids = acl_ids  # type: list[str]
        self.acl_type = acl_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAclsWithListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateAclsWithListenerResponseBody(TeaModel):
    def __init__(self, acl_ids=None, listener_id=None, request_id=None):
        self.acl_ids = acl_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAclsWithListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAclsWithListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateAclsWithListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateAclsWithListenerResponse, self).to_map()
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
            temp_model = AssociateAclsWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAdditionalCertificatesWithListenerRequestCertificates(TeaModel):
    def __init__(self, domain=None, id=None):
        self.domain = domain  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerRequestCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AssociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(self, accelerator_id=None, certificates=None, client_token=None, listener_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.certificates = certificates  # type: list[AssociateAdditionalCertificatesWithListenerRequestCertificates]
        self.client_token = client_token  # type: str
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = AssociateAdditionalCertificatesWithListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(self, listener_id=None, request_id=None):
        self.listener_id = listener_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateAdditionalCertificatesWithListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerResponse, self).to_map()
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
            temp_model = AssociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDdosToAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, ddos_id=None, ddos_region_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.ddos_id = ddos_id  # type: str
        self.ddos_region_id = ddos_region_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDdosToAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachDdosToAcceleratorResponseBody(TeaModel):
    def __init__(self, ddos_id=None, ga_id=None, request_id=None):
        self.ddos_id = ddos_id  # type: str
        self.ga_id = ga_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDdosToAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.ga_id is not None:
            result['GaId'] = self.ga_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('GaId') is not None:
            self.ga_id = m.get('GaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachDdosToAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachDdosToAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachDdosToAcceleratorResponse, self).to_map()
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
            temp_model = AttachDdosToAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLogStoreToEndpointGroupRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, endpoint_group_ids=None, listener_id=None,
                 region_id=None, sls_log_store_name=None, sls_project_name=None, sls_region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str
        self.sls_log_store_name = sls_log_store_name  # type: str
        self.sls_project_name = sls_project_name  # type: str
        self.sls_region_id = sls_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachLogStoreToEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')
        return self


class AttachLogStoreToEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachLogStoreToEndpointGroupResponseBody, self).to_map()
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


class AttachLogStoreToEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachLogStoreToEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachLogStoreToEndpointGroupResponse, self).to_map()
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
            temp_model = AttachLogStoreToEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandwidthPackageAddAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth_package_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageAddAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BandwidthPackageAddAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerators=None, bandwidth_package_id=None, request_id=None):
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageAddAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BandwidthPackageAddAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BandwidthPackageAddAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BandwidthPackageAddAcceleratorResponse, self).to_map()
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
            temp_model = BandwidthPackageAddAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandwidthPackageRemoveAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth_package_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageRemoveAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BandwidthPackageRemoveAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerators=None, bandwidth_package_id=None, request_id=None):
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BandwidthPackageRemoveAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BandwidthPackageRemoveAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BandwidthPackageRemoveAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BandwidthPackageRemoveAcceleratorResponse, self).to_map()
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
            temp_model = BandwidthPackageRemoveAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, client_token=None, new_resource_group_id=None, region_id=None, resource_id=None,
                 resource_type=None):
        self.client_token = client_token  # type: str
        self.new_resource_group_id = new_resource_group_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigEndpointProbeRequest(TeaModel):
    def __init__(self, client_token=None, enable=None, endpoint=None, endpoint_group_id=None, endpoint_type=None,
                 probe_port=None, probe_protocol=None, region_id=None):
        self.client_token = client_token  # type: str
        self.enable = enable  # type: str
        self.endpoint = endpoint  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.probe_port = probe_port  # type: str
        self.probe_protocol = probe_protocol  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigEndpointProbeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigEndpointProbeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigEndpointProbeResponseBody, self).to_map()
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


class ConfigEndpointProbeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigEndpointProbeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigEndpointProbeResponse, self).to_map()
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
            temp_model = ConfigEndpointProbeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAcceleratorRequestIpSetConfig(TeaModel):
    def __init__(self, access_mode=None):
        self.access_mode = access_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAcceleratorRequestIpSetConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class CreateAcceleratorRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_duration=None, auto_use_coupon=None,
                 bandwidth_billing_type=None, client_token=None, duration=None, ip_set_config=None, name=None, pricing_cycle=None,
                 region_id=None, resource_group_id=None, spec=None):
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_use_coupon = auto_use_coupon  # type: str
        self.bandwidth_billing_type = bandwidth_billing_type  # type: str
        self.client_token = client_token  # type: str
        self.duration = duration  # type: int
        self.ip_set_config = ip_set_config  # type: CreateAcceleratorRequestIpSetConfig
        self.name = name  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.spec = spec  # type: str

    def validate(self):
        if self.ip_set_config:
            self.ip_set_config.validate()

    def to_map(self):
        _map = super(CreateAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IpSetConfig') is not None:
            temp_model = CreateAcceleratorRequestIpSetConfig()
            self.ip_set_config = temp_model.from_map(m['IpSetConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class CreateAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, order_id=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAcceleratorResponse, self).to_map()
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
            temp_model = CreateAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclRequestAclEntries(TeaModel):
    def __init__(self, entry=None, entry_description=None):
        self.entry = entry  # type: str
        self.entry_description = entry_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAclRequestAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class CreateAclRequest(TeaModel):
    def __init__(self, acl_entries=None, acl_name=None, address_ipversion=None, client_token=None, dry_run=None,
                 region_id=None, resource_group_id=None):
        self.acl_entries = acl_entries  # type: list[CreateAclRequestAclEntries]
        self.acl_name = acl_name  # type: str
        self.address_ipversion = address_ipversion  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = CreateAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateAclResponseBody(TeaModel):
    def __init__(self, acl_id=None, request_id=None):
        self.acl_id = acl_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAclResponse, self).to_map()
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
            temp_model = CreateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationMonitorRequest(TeaModel):
    def __init__(self, accelerator_id=None, address=None, client_token=None, detect_enable=None,
                 detect_threshold=None, detect_times=None, listener_id=None, options_json=None, region_id=None, silence_time=None,
                 task_name=None):
        self.accelerator_id = accelerator_id  # type: str
        self.address = address  # type: str
        self.client_token = client_token  # type: str
        self.detect_enable = detect_enable  # type: bool
        self.detect_threshold = detect_threshold  # type: int
        self.detect_times = detect_times  # type: int
        self.listener_id = listener_id  # type: str
        self.options_json = options_json  # type: str
        self.region_id = region_id  # type: str
        self.silence_time = silence_time  # type: int
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateApplicationMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationMonitorResponse, self).to_map()
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
            temp_model = CreateApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBandwidthPackageRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_duration=None, auto_use_coupon=None,
                 bandwidth=None, bandwidth_type=None, billing_type=None, cbn_geographic_region_id_a=None,
                 cbn_geographic_region_id_b=None, charge_type=None, client_token=None, duration=None, pricing_cycle=None, ratio=None,
                 region_id=None, resource_group_id=None, type=None):
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_use_coupon = auto_use_coupon  # type: str
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.billing_type = billing_type  # type: str
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str
        self.charge_type = charge_type  # type: str
        self.client_token = client_token  # type: str
        self.duration = duration  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.ratio = ratio  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateBandwidthPackageResponseBody(TeaModel):
    def __init__(self, bandwidth_package_id=None, order_id=None, request_id=None):
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBandwidthPackageResponse, self).to_map()
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
            temp_model = CreateBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBasicAcceleratorRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_duration=None, auto_use_coupon=None,
                 bandwidth_billing_type=None, client_token=None, duration=None, pricing_cycle=None, region_id=None, resource_group_id=None):
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.auto_use_coupon = auto_use_coupon  # type: str
        self.bandwidth_billing_type = bandwidth_billing_type  # type: str
        self.client_token = client_token  # type: str
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBasicAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateBasicAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, order_id=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBasicAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBasicAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBasicAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBasicAcceleratorResponse, self).to_map()
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
            temp_model = CreateBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBasicEndpointGroupRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, description=None, endpoint_address=None,
                 endpoint_group_region=None, endpoint_sub_address=None, endpoint_type=None, name=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.endpoint_address = endpoint_address  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_sub_address = endpoint_sub_address  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBasicEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBasicEndpointGroupResponseBody(TeaModel):
    def __init__(self, endpoint_group_id=None, request_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBasicEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBasicEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBasicEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBasicEndpointGroupResponse, self).to_map()
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
            temp_model = CreateBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBasicIpSetRequest(TeaModel):
    def __init__(self, accelerate_region_id=None, accelerator_id=None, bandwidth=None, client_token=None,
                 isp_type=None, region_id=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth = bandwidth  # type: long
        self.client_token = client_token  # type: str
        self.isp_type = isp_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBasicIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBasicIpSetResponseBody(TeaModel):
    def __init__(self, ip_set_id=None, request_id=None):
        self.ip_set_id = ip_set_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBasicIpSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBasicIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBasicIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBasicIpSetResponse, self).to_map()
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
            temp_model = CreateBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations(TeaModel):
    def __init__(self, from_port=None, protocols=None, to_port=None):
        self.from_port = from_port  # type: int
        self.protocols = protocols  # type: list[str]
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(self, client_token=None, destination_configurations=None, dry_run=None, endpoint_group_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.destination_configurations = destination_configurations  # type: list[CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations]
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupDestinationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(self, destination_ids=None, request_id=None):
        self.destination_ids = destination_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupDestinationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_ids is not None:
            result['DestinationIds'] = self.destination_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationIds') is not None:
            self.destination_ids = m.get('DestinationIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomRoutingEndpointGroupDestinationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupDestinationsResponse, self).to_map()
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
            temp_model = CreateCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations(TeaModel):
    def __init__(self, from_port=None, protocols=None, to_port=None):
        self.from_port = from_port  # type: int
        self.protocols = protocols  # type: list[str]
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(self, address=None, port_ranges=None):
        self.address = address  # type: str
        self.port_ranges = port_ranges  # type: list[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, endpoint=None, policy_configurations=None, traffic_to_endpoint_policy=None, type=None):
        self.endpoint = endpoint  # type: str
        self.policy_configurations = policy_configurations  # type: list[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations]
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(self, description=None, destination_configurations=None, endpoint_configurations=None,
                 endpoint_group_region=None, name=None):
        self.description = description  # type: str
        self.destination_configurations = destination_configurations  # type: list[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations]
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateCustomRoutingEndpointGroupsRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, endpoint_group_configurations=None,
                 listener_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_configurations = endpoint_group_configurations  # type: list[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointGroupsResponseBody(TeaModel):
    def __init__(self, endpoint_group_ids=None, request_id=None):
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomRoutingEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointGroupsResponse, self).to_map()
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
            temp_model = CreateCustomRoutingEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations(TeaModel):
    def __init__(self, address=None, port_ranges=None):
        self.address = address  # type: str
        self.port_ranges = port_ranges  # type: list[CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_id=None, policy_configurations=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.policy_configurations = policy_configurations  # type: list[CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations]
        self.region_id = region_id  # type: str

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointTrafficPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(self, policy_ids=None, request_id=None):
        self.policy_ids = policy_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointTrafficPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomRoutingEndpointTrafficPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointTrafficPoliciesResponse, self).to_map()
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
            temp_model = CreateCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(self, address=None, port_ranges=None):
        self.address = address  # type: str
        self.port_ranges = port_ranges  # type: list[CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateCustomRoutingEndpointsRequestEndpointConfigurations(TeaModel):
    def __init__(self, endpoint=None, policy_configurations=None, traffic_to_endpoint_policy=None, type=None):
        self.endpoint = endpoint  # type: str
        self.policy_configurations = policy_configurations  # type: list[CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations]
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointsRequestEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCustomRoutingEndpointsRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_configurations=None, endpoint_group_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateCustomRoutingEndpointsRequestEndpointConfigurations]
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateCustomRoutingEndpointsRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(self, endpoint_ids=None, request_id=None):
        self.endpoint_ids = endpoint_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomRoutingEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomRoutingEndpointsResponse, self).to_map()
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
            temp_model = CreateCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointGroupRequestEndpointConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation=None, endpoint=None, type=None, weight=None):
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.endpoint = endpoint  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupRequestEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateEndpointGroupRequestPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: int
        self.listener_port = listener_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupRequestPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class CreateEndpointGroupRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, description=None, endpoint_configurations=None,
                 endpoint_group_region=None, endpoint_group_type=None, endpoint_request_protocol=None, health_check_enabled=None,
                 health_check_interval_seconds=None, health_check_path=None, health_check_port=None, health_check_protocol=None,
                 listener_id=None, name=None, port_overrides=None, region_id=None, threshold_count=None,
                 traffic_percentage=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateEndpointGroupRequestEndpointConfigurations]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.port_overrides = port_overrides  # type: list[CreateEndpointGroupRequestPortOverrides]
        self.region_id = region_id  # type: str
        self.threshold_count = threshold_count  # type: int
        self.traffic_percentage = traffic_percentage  # type: int

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class CreateEndpointGroupResponseBody(TeaModel):
    def __init__(self, endpoint_group_id=None, request_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupResponse, self).to_map()
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
            temp_model = CreateEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, endpoint=None, type=None, weight=None):
        self.endpoint = endpoint  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: long
        self.listener_port = listener_port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation_proxy_protocol=None, enable_client_ippreservation_toa=None,
                 endpoint_configurations=None, endpoint_group_description=None, endpoint_group_name=None, endpoint_group_region=None,
                 endpoint_group_type=None, endpoint_request_protocol=None, health_check_enabled=None,
                 health_check_interval_seconds=None, health_check_path=None, health_check_port=None, health_check_protocol=None,
                 port_overrides=None, threshold_count=None, traffic_percentage=None):
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol  # type: bool
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa  # type: bool
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_group_description = endpoint_group_description  # type: str
        self.endpoint_group_name = endpoint_group_name  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: long
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: long
        self.health_check_protocol = health_check_protocol  # type: str
        self.port_overrides = port_overrides  # type: list[CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides]
        self.threshold_count = threshold_count  # type: long
        self.traffic_percentage = traffic_percentage  # type: long

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupsRequestEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class CreateEndpointGroupsRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, endpoint_group_configurations=None,
                 listener_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_configurations = endpoint_group_configurations  # type: list[CreateEndpointGroupsRequestEndpointGroupConfigurations]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEndpointGroupsResponseBody(TeaModel):
    def __init__(self, endpoint_group_ids=None, request_id=None):
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEndpointGroupsResponse, self).to_map()
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
            temp_model = CreateEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(self, endpoint_group_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(self, server_group_tuples=None):
        self.server_group_tuples = server_group_tuples  # type: list[CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples]

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActions(TeaModel):
    def __init__(self, forward_group_config=None, order=None, rule_action_type=None, rule_action_value=None):
        self.forward_group_config = forward_group_config  # type: CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig
        self.order = order  # type: int
        self.rule_action_type = rule_action_type  # type: str
        self.rule_action_value = rule_action_value  # type: str

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditions(TeaModel):
    def __init__(self, host_config=None, path_config=None, rule_condition_type=None, rule_condition_value=None):
        self.host_config = host_config  # type: CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig
        self.path_config = path_config  # type: CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig
        self.rule_condition_type = rule_condition_type  # type: str
        self.rule_condition_value = rule_condition_value  # type: str

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRulesRuleConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('PathConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')
        return self


class CreateForwardingRulesRequestForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_name=None, priority=None, rule_actions=None, rule_conditions=None,
                 rule_direction=None):
        self.forwarding_rule_name = forwarding_rule_name  # type: str
        self.priority = priority  # type: int
        self.rule_actions = rule_actions  # type: list[CreateForwardingRulesRequestForwardingRulesRuleActions]
        self.rule_conditions = rule_conditions  # type: list[CreateForwardingRulesRequestForwardingRulesRuleConditions]
        self.rule_direction = rule_direction  # type: str

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequestForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_direction is not None:
            result['RuleDirection'] = self.rule_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')
        return self


class CreateForwardingRulesRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, forwarding_rules=None, listener_id=None,
                 region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.forwarding_rules = forwarding_rules  # type: list[CreateForwardingRulesRequestForwardingRules]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = CreateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class CreateForwardingRulesResponseBody(TeaModel):
    def __init__(self, forwarding_rules=None, request_id=None):
        self.forwarding_rules = forwarding_rules  # type: list[CreateForwardingRulesResponseBodyForwardingRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = CreateForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateForwardingRulesResponse, self).to_map()
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
            temp_model = CreateForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpSetsRequestAccelerateRegion(TeaModel):
    def __init__(self, accelerate_region_id=None, bandwidth=None, ip_version=None, isp_type=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.ip_version = ip_version  # type: str
        self.isp_type = isp_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIpSetsRequestAccelerateRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        return self


class CreateIpSetsRequest(TeaModel):
    def __init__(self, accelerate_region=None, accelerator_id=None, client_token=None, region_id=None):
        self.accelerate_region = accelerate_region  # type: list[CreateIpSetsRequestAccelerateRegion]
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.accelerate_region:
            for k in self.accelerate_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccelerateRegion'] = []
        if self.accelerate_region is not None:
            for k in self.accelerate_region:
                result['AccelerateRegion'].append(k.to_map() if k else None)
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accelerate_region = []
        if m.get('AccelerateRegion') is not None:
            for k in m.get('AccelerateRegion'):
                temp_model = CreateIpSetsRequestAccelerateRegion()
                self.accelerate_region.append(temp_model.from_map(k))
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIpSetsResponseBodyIpSets(TeaModel):
    def __init__(self, accelerate_region_id=None, bandwidth=None, ip_set_id=None, isp_type=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.ip_set_id = ip_set_id  # type: str
        self.isp_type = isp_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIpSetsResponseBodyIpSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        return self


class CreateIpSetsResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, ip_sets=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.ip_sets = ip_sets  # type: list[CreateIpSetsResponseBodyIpSets]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateIpSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = CreateIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpSetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIpSetsResponse, self).to_map()
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
            temp_model = CreateIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListenerRequestCertificates(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations(TeaModel):
    def __init__(self, from_port=None, protocols=None, to_port=None):
        self.from_port = from_port  # type: int
        self.protocols = protocols  # type: list[str]
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(self, address=None, port_ranges=None):
        self.address = address  # type: str
        self.port_ranges = port_ranges  # type: list[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, endpoint=None, policy_configurations=None, traffic_to_endpoint_policy=None, type=None):
        self.endpoint = endpoint  # type: str
        self.policy_configurations = policy_configurations  # type: list[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations]
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurations(TeaModel):
    def __init__(self, description=None, destination_configurations=None, endpoint_configurations=None,
                 endpoint_group_region=None, name=None):
        self.description = description  # type: str
        self.destination_configurations = destination_configurations  # type: list[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations]
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerRequestCustomRoutingEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, endpoint=None, type=None, weight=None):
        self.endpoint = endpoint  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateListenerRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: long
        self.listener_port = listener_port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestEndpointGroupConfigurationsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class CreateListenerRequestEndpointGroupConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation_proxy_protocol=None, enable_client_ippreservation_toa=None,
                 endpoint_configurations=None, endpoint_group_description=None, endpoint_group_name=None, endpoint_group_region=None,
                 endpoint_group_type=None, endpoint_request_protocol=None, health_check_enabled=None,
                 health_check_interval_seconds=None, health_check_path=None, health_check_port=None, health_check_protocol=None,
                 port_overrides=None, threshold_count=None, traffic_percentage=None):
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol  # type: bool
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa  # type: bool
        self.endpoint_configurations = endpoint_configurations  # type: list[CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_group_description = endpoint_group_description  # type: str
        self.endpoint_group_name = endpoint_group_name  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: long
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: long
        self.health_check_protocol = health_check_protocol  # type: str
        self.port_overrides = port_overrides  # type: list[CreateListenerRequestEndpointGroupConfigurationsPortOverrides]
        self.threshold_count = threshold_count  # type: long
        self.traffic_percentage = traffic_percentage  # type: long

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerRequestEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateListenerRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class CreateListenerRequestPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestXForwardedForConfig(TeaModel):
    def __init__(self, xforwarded_for_ga_ap_enabled=None, xforwarded_for_ga_id_enabled=None,
                 xforwarded_for_port_enabled=None, xforwarded_for_proto_enabled=None, xreal_ip_enabled=None):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled  # type: bool
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled  # type: bool
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled  # type: bool
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled  # type: bool
        self.xreal_ip_enabled = xreal_ip_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestXForwardedForConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class CreateListenerRequest(TeaModel):
    def __init__(self, accelerator_id=None, certificates=None, client_affinity=None, client_token=None,
                 custom_routing_endpoint_group_configurations=None, description=None, endpoint_group_configurations=None, name=None, port_ranges=None,
                 protocol=None, proxy_protocol=None, region_id=None, security_policy_id=None, type=None,
                 xforwarded_for_config=None):
        self.accelerator_id = accelerator_id  # type: str
        self.certificates = certificates  # type: list[CreateListenerRequestCertificates]
        self.client_affinity = client_affinity  # type: str
        self.client_token = client_token  # type: str
        self.custom_routing_endpoint_group_configurations = custom_routing_endpoint_group_configurations  # type: list[CreateListenerRequestCustomRoutingEndpointGroupConfigurations]
        self.description = description  # type: str
        self.endpoint_group_configurations = endpoint_group_configurations  # type: list[CreateListenerRequestEndpointGroupConfigurations]
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[CreateListenerRequestPortRanges]
        self.protocol = protocol  # type: str
        self.proxy_protocol = proxy_protocol  # type: bool
        self.region_id = region_id  # type: str
        self.security_policy_id = security_policy_id  # type: str
        self.type = type  # type: str
        self.xforwarded_for_config = xforwarded_for_config  # type: CreateListenerRequestXForwardedForConfig

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.custom_routing_endpoint_group_configurations:
            for k in self.custom_routing_endpoint_group_configurations:
                if k:
                    k.validate()
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super(CreateListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['CustomRoutingEndpointGroupConfigurations'] = []
        if self.custom_routing_endpoint_group_configurations is not None:
            for k in self.custom_routing_endpoint_group_configurations:
                result['CustomRoutingEndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.type is not None:
            result['Type'] = self.type
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = CreateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.custom_routing_endpoint_group_configurations = []
        if m.get('CustomRoutingEndpointGroupConfigurations') is not None:
            for k in m.get('CustomRoutingEndpointGroupConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurations()
                self.custom_routing_endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateListenerRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XForwardedForConfig') is not None:
            temp_model = CreateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class CreateListenerResponseBody(TeaModel):
    def __init__(self, listener_id=None, request_id=None):
        self.listener_id = listener_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateListenerResponse, self).to_map()
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
            temp_model = CreateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpareIpsRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, region_id=None, spare_ips=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str
        self.spare_ips = spare_ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpareIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spare_ips is not None:
            result['SpareIps'] = self.spare_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpareIps') is not None:
            self.spare_ips = m.get('SpareIps')
        return self


class CreateSpareIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSpareIpsResponseBody, self).to_map()
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


class CreateSpareIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSpareIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSpareIpsResponse, self).to_map()
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
            temp_model = CreateSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAcceleratorResponse, self).to_map()
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
            temp_model = DeleteAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclRequest(TeaModel):
    def __init__(self, acl_id=None, client_token=None, dry_run=None, region_id=None):
        self.acl_id = acl_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAclResponseBody(TeaModel):
    def __init__(self, acl_id=None, request_id=None):
        self.acl_id = acl_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAclResponse, self).to_map()
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
            temp_model = DeleteAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationMonitorRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteApplicationMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationMonitorResponseBody, self).to_map()
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


class DeleteApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationMonitorResponse, self).to_map()
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
            temp_model = DeleteApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBandwidthPackageRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, client_token=None, region_id=None):
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBandwidthPackageResponseBody(TeaModel):
    def __init__(self, bandwidth_package_id=None, request_id=None):
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBandwidthPackageResponse, self).to_map()
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
            temp_model = DeleteBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBasicAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBasicAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBasicAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBasicAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBasicAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBasicAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBasicAcceleratorResponse, self).to_map()
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
            temp_model = DeleteBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBasicEndpointGroupRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_group_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBasicEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class DeleteBasicEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBasicEndpointGroupResponseBody, self).to_map()
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


class DeleteBasicEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBasicEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBasicEndpointGroupResponse, self).to_map()
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
            temp_model = DeleteBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBasicIpSetRequest(TeaModel):
    def __init__(self, client_token=None, ip_set_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBasicIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBasicIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBasicIpSetResponseBody, self).to_map()
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


class DeleteBasicIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBasicIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBasicIpSetResponse, self).to_map()
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
            temp_model = DeleteBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(self, client_token=None, destination_ids=None, dry_run=None, endpoint_group_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.destination_ids = destination_ids  # type: list[str]
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointGroupDestinationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_ids is not None:
            result['DestinationIds'] = self.destination_ids
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationIds') is not None:
            self.destination_ids = m.get('DestinationIds')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointGroupDestinationsResponseBody, self).to_map()
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


class DeleteCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomRoutingEndpointGroupDestinationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointGroupDestinationsResponse, self).to_map()
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
            temp_model = DeleteCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointGroupsRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, endpoint_group_ids=None,
                 region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointGroupsResponseBody, self).to_map()
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


class DeleteCustomRoutingEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomRoutingEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointGroupsResponse, self).to_map()
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
            temp_model = DeleteCustomRoutingEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_id=None, policy_ids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.policy_ids = policy_ids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointTrafficPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointTrafficPoliciesResponseBody, self).to_map()
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


class DeleteCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomRoutingEndpointTrafficPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointTrafficPoliciesResponse, self).to_map()
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
            temp_model = DeleteCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointsRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_group_id=None, endpoint_ids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_ids = endpoint_ids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointsResponseBody, self).to_map()
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


class DeleteCustomRoutingEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomRoutingEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomRoutingEndpointsResponse, self).to_map()
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
            temp_model = DeleteCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointGroupRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, endpoint_group_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class DeleteEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupResponseBody, self).to_map()
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


class DeleteEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEndpointGroupResponse, self).to_map()
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
            temp_model = DeleteEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointGroupsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_group_ids=None, region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteEndpointGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointGroupsResponseBody, self).to_map()
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


class DeleteEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEndpointGroupsResponse, self).to_map()
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
            temp_model = DeleteEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteForwardingRulesRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, forwarding_rule_ids=None, listener_id=None,
                 region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class DeleteForwardingRulesResponseBody(TeaModel):
    def __init__(self, forwarding_rules=None, request_id=None):
        self.forwarding_rules = forwarding_rules  # type: list[DeleteForwardingRulesResponseBodyForwardingRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = DeleteForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteForwardingRulesResponse, self).to_map()
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
            temp_model = DeleteForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpSetRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, ip_set_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetResponseBody, self).to_map()
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


class DeleteIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpSetResponse, self).to_map()
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
            temp_model = DeleteIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpSetsRequest(TeaModel):
    def __init__(self, ip_set_ids=None, region_id=None):
        self.ip_set_ids = ip_set_ids  # type: list[str]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_ids is not None:
            result['IpSetIds'] = self.ip_set_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpSetIds') is not None:
            self.ip_set_ids = m.get('IpSetIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpSetsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpSetsResponseBody, self).to_map()
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


class DeleteIpSetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpSetsResponse, self).to_map()
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
            temp_model = DeleteIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListenerRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, listener_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DeleteListenerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteListenerResponseBody, self).to_map()
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


class DeleteListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteListenerResponse, self).to_map()
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
            temp_model = DeleteListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpareIpsRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, region_id=None, spare_ips=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str
        self.spare_ips = spare_ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpareIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spare_ips is not None:
            result['SpareIps'] = self.spare_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpareIps') is not None:
            self.spare_ips = m.get('SpareIps')
        return self


class DeleteSpareIpsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpareIpsResponseBody, self).to_map()
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


class DeleteSpareIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSpareIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSpareIpsResponse, self).to_map()
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
            temp_model = DeleteSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAcceleratorResponseBodyBasicBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_type=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBodyBasicBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAcceleratorResponseBodyIpSetConfig(TeaModel):
    def __init__(self, access_mode=None):
        self.access_mode = access_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBodyIpSetConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class DescribeAcceleratorResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBodyTags, self).to_map()
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


class DescribeAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth_billing_type=None, basic_bandwidth_package=None, cen_id=None,
                 create_time=None, cross_domain_bandwidth_package=None, cross_private_state=None, ddos_id=None,
                 description=None, dns_name=None, expired_time=None, instance_charge_type=None, ip_set_config=None, name=None,
                 region_id=None, request_id=None, resource_group_id=None, second_dns_name=None, spec=None, state=None,
                 tags=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth_billing_type = bandwidth_billing_type  # type: str
        self.basic_bandwidth_package = basic_bandwidth_package  # type: DescribeAcceleratorResponseBodyBasicBandwidthPackage
        self.cen_id = cen_id  # type: str
        self.create_time = create_time  # type: long
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package  # type: DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage
        self.cross_private_state = cross_private_state  # type: str
        self.ddos_id = ddos_id  # type: str
        self.description = description  # type: str
        self.dns_name = dns_name  # type: str
        self.expired_time = expired_time  # type: long
        self.instance_charge_type = instance_charge_type  # type: str
        self.ip_set_config = ip_set_config  # type: DescribeAcceleratorResponseBodyIpSetConfig
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.second_dns_name = second_dns_name  # type: str
        self.spec = spec  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[DescribeAcceleratorResponseBodyTags]

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.ip_set_config:
            self.ip_set_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.cross_private_state is not None:
            result['CrossPrivateState'] = self.cross_private_state
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = DescribeAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('CrossPrivateState') is not None:
            self.cross_private_state = m.get('CrossPrivateState')
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('IpSetConfig') is not None:
            temp_model = DescribeAcceleratorResponseBodyIpSetConfig()
            self.ip_set_config = temp_model.from_map(m['IpSetConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeAcceleratorResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAcceleratorResponse, self).to_map()
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
            temp_model = DescribeAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAcceleratorAutoRenewAttributeRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorAutoRenewAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAcceleratorAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, auto_renew=None, auto_renew_duration=None, renewal_status=None,
                 request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.renewal_status = renewal_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAcceleratorAutoRenewAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAcceleratorAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAcceleratorAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAcceleratorAutoRenewAttributeResponse, self).to_map()
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
            temp_model = DescribeAcceleratorAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationMonitorRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeApplicationMonitorResponseBodyIspCityList(TeaModel):
    def __init__(self, city=None, city_name=None, isp=None, isp_name=None):
        self.city = city  # type: str
        self.city_name = city_name  # type: str
        self.isp = isp  # type: str
        self.isp_name = isp_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationMonitorResponseBodyIspCityList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class DescribeApplicationMonitorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, address=None, detect_enable=None, detect_threshold=None,
                 detect_times=None, isp_city_list=None, listener_id=None, options_json=None, region_id=None, request_id=None,
                 silence_time=None, task_id=None, task_name=None):
        self.accelerator_id = accelerator_id  # type: str
        self.address = address  # type: str
        self.detect_enable = detect_enable  # type: bool
        self.detect_threshold = detect_threshold  # type: int
        self.detect_times = detect_times  # type: int
        self.isp_city_list = isp_city_list  # type: list[DescribeApplicationMonitorResponseBodyIspCityList]
        self.listener_id = listener_id  # type: str
        self.options_json = options_json  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.silence_time = silence_time  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        if self.isp_city_list:
            for k in self.isp_city_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        result['IspCityList'] = []
        if self.isp_city_list is not None:
            for k in self.isp_city_list:
                result['IspCityList'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        self.isp_city_list = []
        if m.get('IspCityList') is not None:
            for k in m.get('IspCityList'):
                temp_model = DescribeApplicationMonitorResponseBodyIspCityList()
                self.isp_city_list.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationMonitorResponse, self).to_map()
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
            temp_model = DescribeApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwidthPackageRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, region_id=None):
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBandwidthPackageResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBandwidthPackageResponseBodyTags, self).to_map()
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


class DescribeBandwidthPackageResponseBody(TeaModel):
    def __init__(self, accelerators=None, bandwidth=None, bandwidth_package_id=None, bandwidth_type=None,
                 billing_type=None, cbn_geographic_region_id_a=None, cbn_geographic_region_id_b=None, charge_type=None,
                 create_time=None, description=None, expired_time=None, name=None, ratio=None, region_id=None, request_id=None,
                 resource_group_id=None, state=None, tags=None, type=None):
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.billing_type = billing_type  # type: str
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str
        self.charge_type = charge_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.name = name  # type: str
        self.ratio = ratio  # type: int
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[DescribeBandwidthPackageResponseBodyTags]
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeBandwidthPackageResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBandwidthPackageResponse, self).to_map()
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
            temp_model = DescribeBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwidthPackageAutoRenewAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBandwidthPackageAutoRenewAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBandwidthPackageAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, instance_id=None, renewal_status=None,
                 request_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.instance_id = instance_id  # type: str
        self.renewal_status = renewal_status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBandwidthPackageAutoRenewAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBandwidthPackageAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBandwidthPackageAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBandwidthPackageAutoRenewAttributeResponse, self).to_map()
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
            temp_model = DescribeBandwidthPackageAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndPointTrafficPolicyRequest(TeaModel):
    def __init__(self, policy_id=None, region_id=None):
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndPointTrafficPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeCustomRoutingEndPointTrafficPolicyResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, address=None, endpoint=None, endpoint_group_id=None, endpoint_id=None,
                 listener_id=None, policy_id=None, port_ranges=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.address = address  # type: str
        self.endpoint = endpoint  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.policy_id = policy_id  # type: str
        self.port_ranges = port_ranges  # type: list[DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCustomRoutingEndPointTrafficPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCustomRoutingEndPointTrafficPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomRoutingEndPointTrafficPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomRoutingEndPointTrafficPolicyResponse, self).to_map()
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
            temp_model = DescribeCustomRoutingEndPointTrafficPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndpointRequest(TeaModel):
    def __init__(self, endpoint_id=None, region_id=None):
        self.endpoint_id = endpoint_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndpointResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, endpoint=None, endpoint_group_id=None, endpoint_id=None,
                 listener_id=None, request_id=None, traffic_to_endpoint_policy=None, type=None):
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint = endpoint  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.request_id = request_id  # type: str
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCustomRoutingEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomRoutingEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointResponse, self).to_map()
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
            temp_model = DescribeCustomRoutingEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndpointGroupRequest(TeaModel):
    def __init__(self, endpoint_group_id=None, region_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndpointGroupResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, access_log_switch=None, description=None, enable_access_log=None,
                 endpoint_group_id=None, endpoint_group_ip_list=None, endpoint_group_region=None,
                 endpoint_group_unconfirmed_ip_list=None, listener_id=None, name=None, request_id=None, sls_log_store_name=None, sls_project_name=None,
                 sls_region=None, state=None):
        self.accelerator_id = accelerator_id  # type: str
        self.access_log_switch = access_log_switch  # type: str
        self.description = description  # type: str
        self.enable_access_log = enable_access_log  # type: bool
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_ip_list = endpoint_group_ip_list  # type: list[str]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.sls_log_store_name = sls_log_store_name  # type: str
        self.sls_project_name = sls_project_name  # type: str
        self.sls_region = sls_region  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeCustomRoutingEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomRoutingEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointGroupResponse, self).to_map()
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
            temp_model = DescribeCustomRoutingEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(self, destination_id=None, region_id=None):
        self.destination_id = destination_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointGroupDestinationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, destination_id=None, endpoint_group_id=None, from_port=None,
                 listener_id=None, protocols=None, request_id=None, to_port=None):
        self.accelerator_id = accelerator_id  # type: str
        self.destination_id = destination_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.from_port = from_port  # type: int
        self.listener_id = listener_id  # type: str
        self.protocols = protocols  # type: list[str]
        self.request_id = request_id  # type: str
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointGroupDestinationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomRoutingEndpointGroupDestinationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomRoutingEndpointGroupDestinationsResponse, self).to_map()
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
            temp_model = DescribeCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointGroupRequest(TeaModel):
    def __init__(self, endpoint_group_id=None, region_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEndpointGroupResponseBodyEndpointConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation=None, endpoint=None, probe_port=None, probe_protocol=None,
                 type=None, weight=None):
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.endpoint = endpoint  # type: str
        self.probe_port = probe_port  # type: int
        self.probe_protocol = probe_protocol  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointGroupResponseBodyEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeEndpointGroupResponseBodyPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: int
        self.listener_port = listener_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointGroupResponseBodyPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class DescribeEndpointGroupResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, access_log_switch=None, description=None, enable_access_log=None,
                 endpoint_configurations=None, endpoint_group_id=None, endpoint_group_ip_list=None, endpoint_group_region=None,
                 endpoint_group_type=None, endpoint_group_unconfirmed_ip_list=None, endpoint_request_protocol=None,
                 forwarding_rule_ids=None, health_check_enabled=None, health_check_interval_seconds=None, health_check_path=None,
                 health_check_port=None, health_check_protocol=None, listener_id=None, name=None, port_overrides=None,
                 request_id=None, sls_log_store_name=None, sls_project_name=None, sls_region=None, state=None,
                 threshold_count=None, total_count=None, traffic_percentage=None):
        self.accelerator_id = accelerator_id  # type: str
        self.access_log_switch = access_log_switch  # type: str
        self.description = description  # type: str
        self.enable_access_log = enable_access_log  # type: bool
        self.endpoint_configurations = endpoint_configurations  # type: list[DescribeEndpointGroupResponseBodyEndpointConfigurations]
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_ip_list = endpoint_group_ip_list  # type: list[str]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list  # type: list[str]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.port_overrides = port_overrides  # type: list[DescribeEndpointGroupResponseBodyPortOverrides]
        self.request_id = request_id  # type: str
        self.sls_log_store_name = sls_log_store_name  # type: str
        self.sls_project_name = sls_project_name  # type: str
        self.sls_region = sls_region  # type: str
        self.state = state  # type: str
        self.threshold_count = threshold_count  # type: int
        self.total_count = total_count  # type: int
        self.traffic_percentage = traffic_percentage  # type: int

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region
        if self.state is not None:
            result['State'] = self.state
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = DescribeEndpointGroupResponseBodyEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = DescribeEndpointGroupResponseBodyPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class DescribeEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndpointGroupResponse, self).to_map()
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
            temp_model = DescribeEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpSetRequest(TeaModel):
    def __init__(self, ip_set_id=None, region_id=None):
        self.ip_set_id = ip_set_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeIpSetResponseBody(TeaModel):
    def __init__(self, accelerate_region_id=None, accelerator_id=None, bandwidth=None, ip_address_list=None,
                 ip_set_id=None, ip_version=None, isp_type=None, request_id=None, state=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.ip_address_list = ip_address_list  # type: list[str]
        self.ip_set_id = ip_set_id  # type: str
        self.ip_version = ip_version  # type: str
        self.isp_type = isp_type  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpSetResponse, self).to_map()
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
            temp_model = DescribeIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeListenerRequest(TeaModel):
    def __init__(self, listener_id=None, region_id=None):
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeListenerResponseBodyBackendPorts(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: str
        self.to_port = to_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyBackendPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeListenerResponseBodyCertificates(TeaModel):
    def __init__(self, id=None, type=None):
        self.id = id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeListenerResponseBodyPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeListenerResponseBodyRelatedAcls(TeaModel):
    def __init__(self, acl_id=None, status=None):
        self.acl_id = acl_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyRelatedAcls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeListenerResponseBodyXForwardedForConfig(TeaModel):
    def __init__(self, xforwarded_for_ga_ap_enabled=None, xforwarded_for_ga_id_enabled=None,
                 xforwarded_for_port_enabled=None, xforwarded_for_proto_enabled=None, xreal_ip_enabled=None):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled  # type: bool
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled  # type: bool
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled  # type: bool
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled  # type: bool
        self.xreal_ip_enabled = xreal_ip_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeListenerResponseBodyXForwardedForConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class DescribeListenerResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, acl_type=None, backend_ports=None, certificates=None,
                 client_affinity=None, create_time=None, description=None, listener_id=None, name=None, port_ranges=None,
                 protocol=None, proxy_protocol=None, related_acls=None, request_id=None, security_policy_id=None, state=None,
                 type=None, xforwarded_for_config=None):
        self.accelerator_id = accelerator_id  # type: str
        self.acl_type = acl_type  # type: str
        self.backend_ports = backend_ports  # type: list[DescribeListenerResponseBodyBackendPorts]
        self.certificates = certificates  # type: list[DescribeListenerResponseBodyCertificates]
        self.client_affinity = client_affinity  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[DescribeListenerResponseBodyPortRanges]
        self.protocol = protocol  # type: str
        self.proxy_protocol = proxy_protocol  # type: bool
        self.related_acls = related_acls  # type: list[DescribeListenerResponseBodyRelatedAcls]
        self.request_id = request_id  # type: str
        self.security_policy_id = security_policy_id  # type: str
        self.state = state  # type: str
        self.type = type  # type: str
        self.xforwarded_for_config = xforwarded_for_config  # type: DescribeListenerResponseBodyXForwardedForConfig

    def validate(self):
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.related_acls:
            for k in self.related_acls:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super(DescribeListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        result['RelatedAcls'] = []
        if self.related_acls is not None:
            for k in self.related_acls:
                result['RelatedAcls'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = DescribeListenerResponseBodyBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = DescribeListenerResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = DescribeListenerResponseBodyPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        self.related_acls = []
        if m.get('RelatedAcls') is not None:
            for k in m.get('RelatedAcls'):
                temp_model = DescribeListenerResponseBodyRelatedAcls()
                self.related_acls.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XForwardedForConfig') is not None:
            temp_model = DescribeListenerResponseBodyXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class DescribeListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeListenerResponse, self).to_map()
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
            temp_model = DescribeListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDdosFromAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDdosFromAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachDdosFromAcceleratorResponseBody(TeaModel):
    def __init__(self, ddos_id=None, request_id=None):
        self.ddos_id = ddos_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDdosFromAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachDdosFromAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachDdosFromAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachDdosFromAcceleratorResponse, self).to_map()
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
            temp_model = DetachDdosFromAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLogStoreFromEndpointGroupRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, endpoint_group_ids=None, listener_id=None,
                 region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachLogStoreFromEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachLogStoreFromEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachLogStoreFromEndpointGroupResponseBody, self).to_map()
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


class DetachLogStoreFromEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachLogStoreFromEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachLogStoreFromEndpointGroupResponse, self).to_map()
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
            temp_model = DetachLogStoreFromEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectApplicationMonitorRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetectApplicationMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectApplicationMonitorResponseBody, self).to_map()
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


class DetectApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectApplicationMonitorResponse, self).to_map()
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
            temp_model = DetectApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationMonitorRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DisableApplicationMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationMonitorResponseBody, self).to_map()
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


class DisableApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationMonitorResponse, self).to_map()
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
            temp_model = DisableApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAclsFromListenerRequest(TeaModel):
    def __init__(self, acl_ids=None, client_token=None, dry_run=None, listener_id=None, region_id=None):
        self.acl_ids = acl_ids  # type: list[str]
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAclsFromListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateAclsFromListenerResponseBody(TeaModel):
    def __init__(self, acl_ids=None, listener_id=None, request_id=None):
        self.acl_ids = acl_ids  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAclsFromListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DissociateAclsFromListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DissociateAclsFromListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateAclsFromListenerResponse, self).to_map()
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
            temp_model = DissociateAclsFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAdditionalCertificatesFromListenerRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, domains=None, listener_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.domains = domains  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAdditionalCertificatesFromListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateAdditionalCertificatesFromListenerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateAdditionalCertificatesFromListenerResponseBody, self).to_map()
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


class DissociateAdditionalCertificatesFromListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DissociateAdditionalCertificatesFromListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateAdditionalCertificatesFromListenerResponse, self).to_map()
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
            temp_model = DissociateAdditionalCertificatesFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationMonitorRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class EnableApplicationMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationMonitorResponseBody, self).to_map()
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


class EnableApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationMonitorResponse, self).to_map()
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
            temp_model = EnableApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAclRequest(TeaModel):
    def __init__(self, acl_id=None, region_id=None):
        self.acl_id = acl_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAclResponseBodyAclEntries(TeaModel):
    def __init__(self, entry=None, entry_description=None):
        self.entry = entry  # type: str
        self.entry_description = entry_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclResponseBodyAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class GetAclResponseBodyRelatedListeners(TeaModel):
    def __init__(self, accelerator_id=None, acl_type=None, listener_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.acl_type = acl_type  # type: str
        self.listener_id = listener_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclResponseBodyRelatedListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class GetAclResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAclResponseBodyTags, self).to_map()
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


class GetAclResponseBody(TeaModel):
    def __init__(self, acl_entries=None, acl_id=None, acl_name=None, acl_status=None, address_ipversion=None,
                 related_listeners=None, request_id=None, resource_group_id=None, tags=None):
        self.acl_entries = acl_entries  # type: list[GetAclResponseBodyAclEntries]
        self.acl_id = acl_id  # type: str
        self.acl_name = acl_name  # type: str
        self.acl_status = acl_status  # type: str
        self.address_ipversion = address_ipversion  # type: str
        self.related_listeners = related_listeners  # type: list[GetAclResponseBodyRelatedListeners]
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tags = tags  # type: list[GetAclResponseBodyTags]

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = GetAclResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = GetAclResponseBodyRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetAclResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAclResponse, self).to_map()
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
            temp_model = GetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBasicAcceleratorResponseBodyBasicBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_type=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicAcceleratorResponseBodyBasicBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBasicAcceleratorResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicAcceleratorResponseBodyTags, self).to_map()
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


class GetBasicAcceleratorResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth_billing_type=None, basic_bandwidth_package=None,
                 basic_endpoint_group_id=None, basic_ip_set_id=None, cen_id=None, create_time=None, cross_domain_bandwidth_package=None,
                 cross_private_state=None, description=None, expired_time=None, instance_charge_type=None, name=None, region_id=None,
                 request_id=None, resource_group_id=None, state=None, tags=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth_billing_type = bandwidth_billing_type  # type: str
        self.basic_bandwidth_package = basic_bandwidth_package  # type: GetBasicAcceleratorResponseBodyBasicBandwidthPackage
        self.basic_endpoint_group_id = basic_endpoint_group_id  # type: str
        self.basic_ip_set_id = basic_ip_set_id  # type: str
        self.cen_id = cen_id  # type: str
        self.create_time = create_time  # type: long
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package  # type: GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage
        self.cross_private_state = cross_private_state  # type: str
        self.description = description  # type: str
        self.expired_time = expired_time  # type: long
        self.instance_charge_type = instance_charge_type  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[GetBasicAcceleratorResponseBodyTags]

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetBasicAcceleratorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.basic_endpoint_group_id is not None:
            result['BasicEndpointGroupId'] = self.basic_endpoint_group_id
        if self.basic_ip_set_id is not None:
            result['BasicIpSetId'] = self.basic_ip_set_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.cross_private_state is not None:
            result['CrossPrivateState'] = self.cross_private_state
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = GetBasicAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('BasicEndpointGroupId') is not None:
            self.basic_endpoint_group_id = m.get('BasicEndpointGroupId')
        if m.get('BasicIpSetId') is not None:
            self.basic_ip_set_id = m.get('BasicIpSetId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('CrossPrivateState') is not None:
            self.cross_private_state = m.get('CrossPrivateState')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetBasicAcceleratorResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetBasicAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBasicAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBasicAcceleratorResponse, self).to_map()
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
            temp_model = GetBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicEndpointGroupRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_group_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBasicEndpointGroupResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, description=None, endpoint_address=None, endpoint_group_id=None,
                 endpoint_group_region=None, endpoint_sub_address=None, endpoint_type=None, name=None, request_id=None, state=None):
        self.accelerator_id = accelerator_id  # type: str
        self.description = description  # type: str
        self.endpoint_address = endpoint_address  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_sub_address = endpoint_sub_address  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicEndpointGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetBasicEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBasicEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBasicEndpointGroupResponse, self).to_map()
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
            temp_model = GetBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicIpSetRequest(TeaModel):
    def __init__(self, client_token=None, ip_set_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBasicIpSetResponseBody(TeaModel):
    def __init__(self, accelerate_region_id=None, accelerator_id=None, bandwidth=None, ip_address=None,
                 ip_set_id=None, ip_version=None, isp_type=None, request_id=None, state=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth = bandwidth  # type: long
        self.ip_address = ip_address  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.ip_version = ip_version  # type: str
        self.isp_type = isp_type  # type: str
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBasicIpSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetBasicIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBasicIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBasicIpSetResponse, self).to_map()
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
            temp_model = GetBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHealthStatusRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, listener_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHealthStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHealthStatusResponseBodyEndpointGroupsEndpoints(TeaModel):
    def __init__(self, address=None, endpoint_id=None, health_detail=None, health_status=None, port=None, type=None):
        self.address = address  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.health_detail = health_detail  # type: str
        self.health_status = health_status  # type: str
        self.port = port  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHealthStatusResponseBodyEndpointGroupsEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.health_detail is not None:
            result['HealthDetail'] = self.health_detail
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('HealthDetail') is not None:
            self.health_detail = m.get('HealthDetail')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHealthStatusResponseBodyEndpointGroups(TeaModel):
    def __init__(self, endpoint_group_id=None, endpoint_group_type=None, endpoints=None, forwarding_rule_ids=None,
                 health_status=None):
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoints = endpoints  # type: list[GetHealthStatusResponseBodyEndpointGroupsEndpoints]
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.health_status = health_status  # type: str

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHealthStatusResponseBodyEndpointGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = GetHealthStatusResponseBodyEndpointGroupsEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        return self


class GetHealthStatusResponseBody(TeaModel):
    def __init__(self, endpoint_groups=None, health_status=None, listener_id=None, request_id=None):
        self.endpoint_groups = endpoint_groups  # type: list[GetHealthStatusResponseBodyEndpointGroups]
        self.health_status = health_status  # type: str
        self.listener_id = listener_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHealthStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = GetHealthStatusResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHealthStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHealthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHealthStatusResponse, self).to_map()
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
            temp_model = GetHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpareIpRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, region_id=None, spare_ip=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str
        self.spare_ip = spare_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpareIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')
        return self


class GetSpareIpResponseBody(TeaModel):
    def __init__(self, request_id=None, state=None):
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpareIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetSpareIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSpareIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSpareIpResponse, self).to_map()
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
            temp_model = GetSpareIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccelerateAreasRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccelerateAreasRequest, self).to_map()
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


class ListAccelerateAreasResponseBodyAreasRegionList(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccelerateAreasResponseBodyAreasRegionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccelerateAreasResponseBodyAreas(TeaModel):
    def __init__(self, area_id=None, local_name=None, region_list=None):
        self.area_id = area_id  # type: str
        self.local_name = local_name  # type: str
        self.region_list = region_list  # type: list[ListAccelerateAreasResponseBodyAreasRegionList]

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccelerateAreasResponseBodyAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = ListAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class ListAccelerateAreasResponseBody(TeaModel):
    def __init__(self, areas=None, request_id=None):
        self.areas = areas  # type: list[ListAccelerateAreasResponseBodyAreas]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccelerateAreasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = ListAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccelerateAreasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccelerateAreasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccelerateAreasResponse, self).to_map()
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
            temp_model = ListAccelerateAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAcceleratorsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsRequestTag, self).to_map()
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


class ListAcceleratorsRequest(TeaModel):
    def __init__(self, accelerator_id=None, page_number=None, page_size=None, region_id=None,
                 resource_group_id=None, state=None, tag=None):
        self.accelerator_id = accelerator_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tag = tag  # type: list[ListAcceleratorsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAcceleratorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAcceleratorsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_type=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAcceleratorsResponseBodyAcceleratorsIpSetConfig(TeaModel):
    def __init__(self, access_mode=None):
        self.access_mode = access_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAcceleratorsIpSetConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class ListAcceleratorsResponseBodyAcceleratorsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAcceleratorsTags, self).to_map()
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


class ListAcceleratorsResponseBodyAccelerators(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth=None, bandwidth_billing_type=None,
                 basic_bandwidth_package=None, cen_id=None, create_time=None, cross_domain_bandwidth_package=None, ddos_id=None,
                 description=None, dns_name=None, expired_time=None, instance_charge_type=None, ip_set_config=None, name=None,
                 region_id=None, resource_group_id=None, second_dns_name=None, spec=None, state=None, tags=None, type=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_billing_type = bandwidth_billing_type  # type: str
        self.basic_bandwidth_package = basic_bandwidth_package  # type: ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage
        self.cen_id = cen_id  # type: str
        self.create_time = create_time  # type: long
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package  # type: ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage
        self.ddos_id = ddos_id  # type: str
        self.description = description  # type: str
        self.dns_name = dns_name  # type: str
        self.expired_time = expired_time  # type: long
        self.instance_charge_type = instance_charge_type  # type: str
        self.ip_set_config = ip_set_config  # type: ListAcceleratorsResponseBodyAcceleratorsIpSetConfig
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.second_dns_name = second_dns_name  # type: str
        self.spec = spec  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[ListAcceleratorsResponseBodyAcceleratorsTags]
        self.type = type  # type: str

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.ip_set_config:
            self.ip_set_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAcceleratorsResponseBodyAccelerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('IpSetConfig') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsIpSetConfig()
            self.ip_set_config = temp_model.from_map(m['IpSetConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAcceleratorsResponseBodyAcceleratorsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAcceleratorsResponseBody(TeaModel):
    def __init__(self, accelerators=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.accelerators = accelerators  # type: list[ListAcceleratorsResponseBodyAccelerators]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.accelerators:
            for k in self.accelerators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAcceleratorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accelerators'] = []
        if self.accelerators is not None:
            for k in self.accelerators:
                result['Accelerators'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accelerators = []
        if m.get('Accelerators') is not None:
            for k in m.get('Accelerators'):
                temp_model = ListAcceleratorsResponseBodyAccelerators()
                self.accelerators.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAcceleratorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAcceleratorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAcceleratorsResponse, self).to_map()
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
            temp_model = ListAcceleratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAclsRequestTag, self).to_map()
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


class ListAclsRequest(TeaModel):
    def __init__(self, acl_ids=None, acl_name=None, client_token=None, max_results=None, next_token=None,
                 region_id=None, resource_group_id=None, tag=None):
        self.acl_ids = acl_ids  # type: list[str]
        self.acl_name = acl_name  # type: str
        self.client_token = client_token  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[ListAclsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAclsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAclsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAclsResponseBodyAclsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAclsResponseBodyAclsTags, self).to_map()
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


class ListAclsResponseBodyAcls(TeaModel):
    def __init__(self, acl_id=None, acl_name=None, acl_status=None, address_ipversion=None, resource_group_id=None,
                 tags=None):
        self.acl_id = acl_id  # type: str
        self.acl_name = acl_name  # type: str
        self.acl_status = acl_status  # type: str
        self.address_ipversion = address_ipversion  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tags = tags  # type: list[ListAclsResponseBodyAclsTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAclsResponseBodyAcls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAclsResponseBodyAclsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAclsResponseBody(TeaModel):
    def __init__(self, acls=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.acls = acls  # type: list[ListAclsResponseBodyAcls]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAclsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = ListAclsResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAclsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAclsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAclsResponse, self).to_map()
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
            temp_model = ListAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationMonitorRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, search_value=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.search_value = search_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class ListApplicationMonitorResponseBodyApplicationMonitors(TeaModel):
    def __init__(self, accelerator_id=None, address=None, detect_enable=None, detect_threshold=None,
                 detect_times=None, listener_id=None, options_json=None, silence_time=None, state=None, task_id=None,
                 task_name=None):
        self.accelerator_id = accelerator_id  # type: str
        self.address = address  # type: str
        self.detect_enable = detect_enable  # type: bool
        self.detect_threshold = detect_threshold  # type: int
        self.detect_times = detect_times  # type: int
        self.listener_id = listener_id  # type: str
        self.options_json = options_json  # type: str
        self.silence_time = silence_time  # type: int
        self.state = state  # type: str
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationMonitorResponseBodyApplicationMonitors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.state is not None:
            result['State'] = self.state
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListApplicationMonitorResponseBody(TeaModel):
    def __init__(self, application_monitors=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.application_monitors = application_monitors  # type: list[ListApplicationMonitorResponseBodyApplicationMonitors]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.application_monitors:
            for k in self.application_monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationMonitors'] = []
        if self.application_monitors is not None:
            for k in self.application_monitors:
                result['ApplicationMonitors'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_monitors = []
        if m.get('ApplicationMonitors') is not None:
            for k in m.get('ApplicationMonitors'):
                temp_model = ListApplicationMonitorResponseBodyApplicationMonitors()
                self.application_monitors.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationMonitorResponse, self).to_map()
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
            temp_model = ListApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationMonitorDetectResultRequest(TeaModel):
    def __init__(self, begin_time=None, end_time=None, page_number=None, page_size=None, region_id=None,
                 task_id=None):
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationMonitorDetectResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList(TeaModel):
    def __init__(self, accelerator_id=None, content=None, detail=None, detect_time=None, diag_status=None,
                 listener_id=None, port=None, protocol=None, status_code=None, task_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.content = content  # type: str
        self.detail = detail  # type: str
        self.detect_time = detect_time  # type: str
        self.diag_status = diag_status  # type: str
        self.listener_id = listener_id  # type: str
        self.port = port  # type: str
        self.protocol = protocol  # type: str
        self.status_code = status_code  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.content is not None:
            result['Content'] = self.content
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.detect_time is not None:
            result['DetectTime'] = self.detect_time
        if self.diag_status is not None:
            result['DiagStatus'] = self.diag_status
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DetectTime') is not None:
            self.detect_time = m.get('DetectTime')
        if m.get('DiagStatus') is not None:
            self.diag_status = m.get('DiagStatus')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListApplicationMonitorDetectResultResponseBody(TeaModel):
    def __init__(self, application_monitor_detect_result_list=None, page_number=None, page_size=None,
                 request_id=None, total_count=None):
        self.application_monitor_detect_result_list = application_monitor_detect_result_list  # type: list[ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.application_monitor_detect_result_list:
            for k in self.application_monitor_detect_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationMonitorDetectResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationMonitorDetectResultList'] = []
        if self.application_monitor_detect_result_list is not None:
            for k in self.application_monitor_detect_result_list:
                result['ApplicationMonitorDetectResultList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_monitor_detect_result_list = []
        if m.get('ApplicationMonitorDetectResultList') is not None:
            for k in m.get('ApplicationMonitorDetectResultList'):
                temp_model = ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList()
                self.application_monitor_detect_result_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationMonitorDetectResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationMonitorDetectResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationMonitorDetectResultResponse, self).to_map()
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
            temp_model = ListApplicationMonitorDetectResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableAccelerateAreasRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableAccelerateAreasResponseBodyAreasRegionList(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponseBodyAreasRegionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableAccelerateAreasResponseBodyAreas(TeaModel):
    def __init__(self, area_id=None, local_name=None, region_list=None):
        self.area_id = area_id  # type: str
        self.local_name = local_name  # type: str
        self.region_list = region_list  # type: list[ListAvailableAccelerateAreasResponseBodyAreasRegionList]

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponseBodyAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = ListAvailableAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class ListAvailableAccelerateAreasResponseBody(TeaModel):
    def __init__(self, areas=None, request_id=None):
        self.areas = areas  # type: list[ListAvailableAccelerateAreasResponseBodyAreas]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = ListAvailableAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAvailableAccelerateAreasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAvailableAccelerateAreasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableAccelerateAreasResponse, self).to_map()
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
            temp_model = ListAvailableAccelerateAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableBusiRegionsRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableBusiRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableBusiRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, pop=None, region_id=None):
        self.local_name = local_name  # type: str
        self.pop = pop  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableBusiRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.pop is not None:
            result['Pop'] = self.pop
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('Pop') is not None:
            self.pop = m.get('Pop')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableBusiRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[ListAvailableBusiRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableBusiRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListAvailableBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAvailableBusiRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAvailableBusiRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableBusiRegionsResponse, self).to_map()
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
            temp_model = ListAvailableBusiRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBandwidthPackagesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthPackagesRequestTag, self).to_map()
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


class ListBandwidthPackagesRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, page_number=None, page_size=None, region_id=None,
                 resource_group_id=None, state=None, tag=None, type=None):
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tag = tag  # type: list[ListBandwidthPackagesRequestTag]
        self.type = type  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListBandwidthPackagesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBandwidthPackagesResponseBodyBandwidthPackagesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthPackagesResponseBodyBandwidthPackagesTags, self).to_map()
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


class ListBandwidthPackagesResponseBodyBandwidthPackages(TeaModel):
    def __init__(self, accelerators=None, bandwidth=None, bandwidth_package_id=None, bandwidth_type=None,
                 billing_type=None, cbn_geographic_region_id_a=None, cbn_geographic_region_id_b=None, charge_type=None,
                 create_time=None, description=None, expired_time=None, name=None, ratio=None, region_id=None,
                 resource_group_id=None, state=None, tags=None, type=None):
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.billing_type = billing_type  # type: str
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a  # type: str
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b  # type: str
        self.charge_type = charge_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.name = name  # type: str
        self.ratio = ratio  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[ListBandwidthPackagesResponseBodyBandwidthPackagesTags]
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthPackagesResponseBodyBandwidthPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListBandwidthPackagesResponseBodyBandwidthPackagesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBandwidthPackagesResponseBody(TeaModel):
    def __init__(self, bandwidth_packages=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.bandwidth_packages = bandwidth_packages  # type: list[ListBandwidthPackagesResponseBodyBandwidthPackages]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListBandwidthPackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBandwidthPackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBandwidthPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBandwidthPackagesResponse, self).to_map()
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
            temp_model = ListBandwidthPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBandwidthackagesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBandwidthackagesResponseBodyBandwidthPackagesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBandwidthackagesResponseBodyBandwidthPackagesTags, self).to_map()
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


class ListBandwidthackagesResponseBodyBandwidthPackages(TeaModel):
    def __init__(self, accelerators=None, bandwidth=None, bandwidth_package_id=None, charge_type=None,
                 create_time=None, description=None, expired_time=None, name=None, region_id=None, resource_group_id=None,
                 state=None, tags=None):
        self.accelerators = accelerators  # type: list[str]
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.charge_type = charge_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[ListBandwidthackagesResponseBodyBandwidthPackagesTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthackagesResponseBodyBandwidthPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListBandwidthackagesResponseBodyBandwidthPackagesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListBandwidthackagesResponseBody(TeaModel):
    def __init__(self, bandwidth_packages=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.bandwidth_packages = bandwidth_packages  # type: list[ListBandwidthackagesResponseBodyBandwidthPackages]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBandwidthackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListBandwidthackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBandwidthackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBandwidthackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBandwidthackagesResponse, self).to_map()
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
            temp_model = ListBandwidthackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBasicAcceleratorsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBasicAcceleratorsRequestTag, self).to_map()
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


class ListBasicAcceleratorsRequest(TeaModel):
    def __init__(self, accelerator_id=None, page_number=None, page_size=None, region_id=None,
                 resource_group_id=None, state=None, tag=None):
        self.accelerator_id = accelerator_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tag = tag  # type: list[ListBasicAcceleratorsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBasicAcceleratorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListBasicAcceleratorsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, bandwidth_type=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage(TeaModel):
    def __init__(self, bandwidth=None, instance_id=None):
        self.bandwidth = bandwidth  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListBasicAcceleratorsResponseBodyAcceleratorsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBasicAcceleratorsResponseBodyAcceleratorsTags, self).to_map()
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


class ListBasicAcceleratorsResponseBodyAccelerators(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth_billing_type=None, basic_bandwidth_package=None,
                 basic_endpoint_group_id=None, basic_ip_set_id=None, create_time=None, cross_domain_bandwidth_package=None,
                 description=None, expired_time=None, instance_charge_type=None, name=None, region_id=None,
                 resource_group_id=None, state=None, tags=None, type=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth_billing_type = bandwidth_billing_type  # type: str
        self.basic_bandwidth_package = basic_bandwidth_package  # type: ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage
        self.basic_endpoint_group_id = basic_endpoint_group_id  # type: str
        self.basic_ip_set_id = basic_ip_set_id  # type: str
        self.create_time = create_time  # type: long
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package  # type: ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage
        self.description = description  # type: str
        self.expired_time = expired_time  # type: long
        self.instance_charge_type = instance_charge_type  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.tags = tags  # type: list[ListBasicAcceleratorsResponseBodyAcceleratorsTags]
        self.type = type  # type: str

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBasicAcceleratorsResponseBodyAccelerators, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.basic_endpoint_group_id is not None:
            result['BasicEndpointGroupId'] = self.basic_endpoint_group_id
        if self.basic_ip_set_id is not None:
            result['BasicIpSetId'] = self.basic_ip_set_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('BasicEndpointGroupId') is not None:
            self.basic_endpoint_group_id = m.get('BasicEndpointGroupId')
        if m.get('BasicIpSetId') is not None:
            self.basic_ip_set_id = m.get('BasicIpSetId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListBasicAcceleratorsResponseBodyAcceleratorsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBasicAcceleratorsResponseBody(TeaModel):
    def __init__(self, accelerators=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.accelerators = accelerators  # type: list[ListBasicAcceleratorsResponseBodyAccelerators]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.accelerators:
            for k in self.accelerators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBasicAcceleratorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accelerators'] = []
        if self.accelerators is not None:
            for k in self.accelerators:
                result['Accelerators'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accelerators = []
        if m.get('Accelerators') is not None:
            for k in m.get('Accelerators'):
                temp_model = ListBasicAcceleratorsResponseBodyAccelerators()
                self.accelerators.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBasicAcceleratorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBasicAcceleratorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBasicAcceleratorsResponse, self).to_map()
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
            temp_model = ListBasicAcceleratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBusiRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBusiRegionsRequest, self).to_map()
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


class ListBusiRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBusiRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBusiRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[ListBusiRegionsResponseBodyRegions]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBusiRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBusiRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBusiRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBusiRegionsResponse, self).to_map()
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
            temp_model = ListBusiRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(self, accelerator_id=None, endpoint_group_id=None, from_port=None, listener_id=None,
                 page_number=None, page_size=None, protocols=None, region_id=None, to_port=None):
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.from_port = from_port  # type: int
        self.listener_id = listener_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.protocols = protocols  # type: list[str]
        self.region_id = region_id  # type: str
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupDestinationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations(TeaModel):
    def __init__(self, accelerator_id=None, destination_id=None, endpoint_group_id=None, from_port=None,
                 listener_id=None, protocols=None, to_port=None):
        self.accelerator_id = accelerator_id  # type: str
        self.destination_id = destination_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.from_port = from_port  # type: int
        self.listener_id = listener_id  # type: str
        self.protocols = protocols  # type: list[str]
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(self, destinations=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.destinations = destinations  # type: list[ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.destinations:
            for k in self.destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupDestinationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Destinations'] = []
        if self.destinations is not None:
            for k in self.destinations:
                result['Destinations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.destinations = []
        if m.get('Destinations') is not None:
            for k in m.get('Destinations'):
                temp_model = ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations()
                self.destinations.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomRoutingEndpointGroupDestinationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupDestinationsResponse, self).to_map()
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
            temp_model = ListCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointGroupsRequest(TeaModel):
    def __init__(self, accelerator_id=None, endpoint_group_id=None, listener_id=None, page_number=None,
                 page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.listener_id = listener_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups(TeaModel):
    def __init__(self, accelerator_id=None, description=None, endpoint_group_id=None, endpoint_group_ip_list=None,
                 endpoint_group_region=None, endpoint_group_unconfirmed_ip_list=None, listener_id=None, name=None, state=None):
        self.accelerator_id = accelerator_id  # type: str
        self.description = description  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_ip_list = endpoint_group_ip_list  # type: list[str]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list  # type: list[str]
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListCustomRoutingEndpointGroupsResponseBody(TeaModel):
    def __init__(self, endpoint_groups=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.endpoint_groups = endpoint_groups  # type: list[ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomRoutingEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointGroupsResponse, self).to_map()
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
            temp_model = ListCustomRoutingEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(self, accelerator_id=None, address=None, endpoint_group_id=None, endpoint_id=None,
                 listener_id=None, page_number=None, page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.address = address  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointTrafficPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, accelerator_id=None, address=None, endpoint_group_id=None, endpoint_id=None,
                 listener_id=None, policy_id=None, port_ranges=None):
        self.accelerator_id = accelerator_id  # type: str
        self.address = address  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.policy_id = policy_id  # type: str
        self.port_ranges = port_ranges  # type: list[ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, policies=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policies = policies  # type: list[ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointTrafficPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomRoutingEndpointTrafficPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointTrafficPoliciesResponse, self).to_map()
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
            temp_model = ListCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointsRequest(TeaModel):
    def __init__(self, accelerator_id=None, endpoint_group_id=None, listener_id=None, page_number=None,
                 page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.listener_id = listener_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(self, accelerator_id=None, endpoint=None, endpoint_group_id=None, endpoint_id=None,
                 listener_id=None, traffic_to_endpoint_policy=None, type=None):
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint = endpoint  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingEndpointsResponseBodyEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(self, endpoints=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.endpoints = endpoints  # type: list[ListCustomRoutingEndpointsResponseBodyEndpoints]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListCustomRoutingEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomRoutingEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomRoutingEndpointsResponse, self).to_map()
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
            temp_model = ListCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingPortMappingsRequest(TeaModel):
    def __init__(self, accelerator_id=None, endpoint_group_id=None, listener_id=None, page_number=None,
                 page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.listener_id = listener_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress(TeaModel):
    def __init__(self, ip_address=None, port=None):
        self.ip_address = ip_address  # type: str
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ListCustomRoutingPortMappingsResponseBodyPortMappings(TeaModel):
    def __init__(self, accelerator_id=None, accelerator_port=None, destination_socket_address=None,
                 destination_traffic_state=None, endpoint_group_id=None, endpoint_group_region=None, endpoint_id=None, listener_id=None,
                 protocols=None, vswitch=None):
        self.accelerator_id = accelerator_id  # type: str
        self.accelerator_port = accelerator_port  # type: int
        self.destination_socket_address = destination_socket_address  # type: ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress
        self.destination_traffic_state = destination_traffic_state  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.protocols = protocols  # type: list[str]
        self.vswitch = vswitch  # type: str

    def validate(self):
        if self.destination_socket_address:
            self.destination_socket_address.validate()

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsResponseBodyPortMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.accelerator_port is not None:
            result['AcceleratorPort'] = self.accelerator_port
        if self.destination_socket_address is not None:
            result['DestinationSocketAddress'] = self.destination_socket_address.to_map()
        if self.destination_traffic_state is not None:
            result['DestinationTrafficState'] = self.destination_traffic_state
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AcceleratorPort') is not None:
            self.accelerator_port = m.get('AcceleratorPort')
        if m.get('DestinationSocketAddress') is not None:
            temp_model = ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress()
            self.destination_socket_address = temp_model.from_map(m['DestinationSocketAddress'])
        if m.get('DestinationTrafficState') is not None:
            self.destination_traffic_state = m.get('DestinationTrafficState')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class ListCustomRoutingPortMappingsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, port_mappings=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.port_mappings = port_mappings  # type: list[ListCustomRoutingPortMappingsResponseBodyPortMappings]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = ListCustomRoutingPortMappingsResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingPortMappingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomRoutingPortMappingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsResponse, self).to_map()
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
            temp_model = ListCustomRoutingPortMappingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingPortMappingsByDestinationRequest(TeaModel):
    def __init__(self, destination_address=None, endpoint_id=None, page_number=None, page_size=None, region_id=None):
        self.destination_address = destination_address  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsByDestinationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_address is not None:
            result['DestinationAddress'] = self.destination_address
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationAddress') is not None:
            self.destination_address = m.get('DestinationAddress')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress(TeaModel):
    def __init__(self, ip_address=None, port=None):
        self.ip_address = ip_address  # type: str
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings(TeaModel):
    def __init__(self, accelerator_id=None, accelerator_port=None, destination_socket_address=None,
                 destination_traffic_state=None, endpoint_group_id=None, endpoint_group_region=None, endpoint_id=None, listener_id=None,
                 protocols=None, vswitch=None):
        self.accelerator_id = accelerator_id  # type: str
        self.accelerator_port = accelerator_port  # type: int
        self.destination_socket_address = destination_socket_address  # type: ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress
        self.destination_traffic_state = destination_traffic_state  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.listener_id = listener_id  # type: str
        self.protocols = protocols  # type: list[str]
        self.vswitch = vswitch  # type: str

    def validate(self):
        if self.destination_socket_address:
            self.destination_socket_address.validate()

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.accelerator_port is not None:
            result['AcceleratorPort'] = self.accelerator_port
        if self.destination_socket_address is not None:
            result['DestinationSocketAddress'] = self.destination_socket_address.to_map()
        if self.destination_traffic_state is not None:
            result['DestinationTrafficState'] = self.destination_traffic_state
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AcceleratorPort') is not None:
            self.accelerator_port = m.get('AcceleratorPort')
        if m.get('DestinationSocketAddress') is not None:
            temp_model = ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress()
            self.destination_socket_address = temp_model.from_map(m['DestinationSocketAddress'])
        if m.get('DestinationTrafficState') is not None:
            self.destination_traffic_state = m.get('DestinationTrafficState')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class ListCustomRoutingPortMappingsByDestinationResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, port_mappings=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.port_mappings = port_mappings  # type: list[ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsByDestinationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingPortMappingsByDestinationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomRoutingPortMappingsByDestinationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomRoutingPortMappingsByDestinationResponse, self).to_map()
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
            temp_model = ListCustomRoutingPortMappingsByDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointGroupsRequest(TeaModel):
    def __init__(self, accelerator_id=None, access_log_switch=None, endpoint_group_id=None,
                 endpoint_group_type=None, listener_id=None, page_number=None, page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.access_log_switch = access_log_switch  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.listener_id = listener_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation=None, endpoint=None, endpoint_id=None, probe_port=None,
                 probe_protocol=None, type=None, weight=None):
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.endpoint = endpoint  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.probe_port = probe_port  # type: int
        self.probe_protocol = probe_protocol  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: int
        self.listener_port = listener_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class ListEndpointGroupsResponseBodyEndpointGroups(TeaModel):
    def __init__(self, accelerator_id=None, description=None, endpoint_configurations=None, endpoint_group_id=None,
                 endpoint_group_ip_list=None, endpoint_group_region=None, endpoint_group_type=None,
                 endpoint_group_unconfirmed_ip_list=None, endpoint_request_protocol=None, forwarding_rule_ids=None, health_check_enabled=None,
                 health_check_interval_seconds=None, health_check_path=None, health_check_port=None, health_check_protocol=None,
                 listener_id=None, name=None, port_overrides=None, state=None, threshold_count=None, traffic_percentage=None):
        self.accelerator_id = accelerator_id  # type: str
        self.description = description  # type: str
        self.endpoint_configurations = endpoint_configurations  # type: list[ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations]
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_ip_list = endpoint_group_ip_list  # type: list[str]
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_group_type = endpoint_group_type  # type: str
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list  # type: list[str]
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.forwarding_rule_ids = forwarding_rule_ids  # type: list[str]
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.port_overrides = port_overrides  # type: list[ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides]
        self.state = state  # type: str
        self.threshold_count = threshold_count  # type: int
        self.traffic_percentage = traffic_percentage  # type: int

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBodyEndpointGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.state is not None:
            result['State'] = self.state
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class ListEndpointGroupsResponseBody(TeaModel):
    def __init__(self, endpoint_groups=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.endpoint_groups = endpoint_groups  # type: list[ListEndpointGroupsResponseBodyEndpointGroups]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEndpointGroupsResponse, self).to_map()
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
            temp_model = ListEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListForwardingRulesRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, forwarding_rule_id=None, listener_id=None,
                 max_results=None, next_token=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.forwarding_rule_id = forwarding_rule_id  # type: str
        self.listener_id = listener_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(self, endpoint_group_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(self, server_group_tuples=None):
        self.server_group_tuples = server_group_tuples  # type: list[ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples]

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActions(TeaModel):
    def __init__(self, forward_group_config=None, order=None, rule_action_type=None, rule_action_value=None):
        self.forward_group_config = forward_group_config  # type: ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig
        self.order = order  # type: int
        self.rule_action_type = rule_action_type  # type: str
        self.rule_action_value = rule_action_value  # type: str

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditions(TeaModel):
    def __init__(self, host_config=None, path_config=None, rule_condition_type=None, rule_condition_value=None):
        self.host_config = host_config  # type: ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig
        self.path_config = path_config  # type: ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig
        self.rule_condition_type = rule_condition_type  # type: str
        self.rule_condition_value = rule_condition_value  # type: str

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRulesRuleConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('PathConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')
        return self


class ListForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_direction=None, forwarding_rule_id=None, forwarding_rule_name=None,
                 forwarding_rule_status=None, listener_id=None, priority=None, rule_actions=None, rule_conditions=None):
        self.forwarding_rule_direction = forwarding_rule_direction  # type: str
        self.forwarding_rule_id = forwarding_rule_id  # type: str
        self.forwarding_rule_name = forwarding_rule_name  # type: str
        self.forwarding_rule_status = forwarding_rule_status  # type: str
        self.listener_id = listener_id  # type: str
        self.priority = priority  # type: int
        self.rule_actions = rule_actions  # type: list[ListForwardingRulesResponseBodyForwardingRulesRuleActions]
        self.rule_conditions = rule_conditions  # type: list[ListForwardingRulesResponseBodyForwardingRulesRuleConditions]

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_direction is not None:
            result['ForwardingRuleDirection'] = self.forwarding_rule_direction
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.forwarding_rule_status is not None:
            result['ForwardingRuleStatus'] = self.forwarding_rule_status
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleDirection') is not None:
            self.forwarding_rule_direction = m.get('ForwardingRuleDirection')
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('ForwardingRuleStatus') is not None:
            self.forwarding_rule_status = m.get('ForwardingRuleStatus')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        return self


class ListForwardingRulesResponseBody(TeaModel):
    def __init__(self, forwarding_rules=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.forwarding_rules = forwarding_rules  # type: list[ListForwardingRulesResponseBodyForwardingRules]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = ListForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListForwardingRulesResponse, self).to_map()
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
            temp_model = ListForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpSetsRequest(TeaModel):
    def __init__(self, accelerator_id=None, page_number=None, page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIpSetsResponseBodyIpSets(TeaModel):
    def __init__(self, accelerate_region_id=None, bandwidth=None, ip_address_list=None, ip_set_id=None,
                 ip_version=None, isp_type=None, state=None):
        self.accelerate_region_id = accelerate_region_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.ip_address_list = ip_address_list  # type: list[str]
        self.ip_set_id = ip_set_id  # type: str
        self.ip_version = ip_version  # type: str
        self.isp_type = isp_type  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpSetsResponseBodyIpSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListIpSetsResponseBody(TeaModel):
    def __init__(self, ip_sets=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.ip_sets = ip_sets  # type: list[ListIpSetsResponseBodyIpSets]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIpSetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = ListIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpSetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIpSetsResponse, self).to_map()
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
            temp_model = ListIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenerCertificatesRequest(TeaModel):
    def __init__(self, accelerator_id=None, listener_id=None, max_results=None, next_token=None, region_id=None,
                 role=None):
        self.accelerator_id = accelerator_id  # type: str
        self.listener_id = listener_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.role = role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenerCertificatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListListenerCertificatesResponseBodyCertificates(TeaModel):
    def __init__(self, certificate_id=None, domain=None, is_default=None, state=None):
        self.certificate_id = certificate_id  # type: str
        self.domain = domain  # type: str
        self.is_default = is_default  # type: bool
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenerCertificatesResponseBodyCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListListenerCertificatesResponseBody(TeaModel):
    def __init__(self, certificates=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.certificates = certificates  # type: list[ListListenerCertificatesResponseBodyCertificates]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenerCertificatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenerCertificatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListListenerCertificatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenerCertificatesResponse, self).to_map()
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
            temp_model = ListListenerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersRequest(TeaModel):
    def __init__(self, accelerator_id=None, page_number=None, page_size=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListListenersResponseBodyListenersBackendPorts(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: str
        self.to_port = to_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersBackendPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListListenersResponseBodyListenersCertificates(TeaModel):
    def __init__(self, id=None, type=None):
        self.id = id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListListenersResponseBodyListenersPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListListenersResponseBodyListenersXForwardedForConfig(TeaModel):
    def __init__(self, xforwarded_for_ga_ap_enabled=None, xforwarded_for_ga_id_enabled=None,
                 xforwarded_for_port_enabled=None, xforwarded_for_proto_enabled=None, xreal_ip_enabled=None):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled  # type: bool
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled  # type: bool
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled  # type: bool
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled  # type: bool
        self.xreal_ip_enabled = xreal_ip_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersXForwardedForConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class ListListenersResponseBodyListeners(TeaModel):
    def __init__(self, accelerator_id=None, backend_ports=None, certificates=None, client_affinity=None,
                 create_time=None, description=None, listener_id=None, name=None, port_ranges=None, protocol=None,
                 proxy_protocol=None, security_policy_id=None, state=None, type=None, xforwarded_for_config=None):
        self.accelerator_id = accelerator_id  # type: str
        self.backend_ports = backend_ports  # type: list[ListListenersResponseBodyListenersBackendPorts]
        self.certificates = certificates  # type: list[ListListenersResponseBodyListenersCertificates]
        self.client_affinity = client_affinity  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[ListListenersResponseBodyListenersPortRanges]
        self.protocol = protocol  # type: str
        self.proxy_protocol = proxy_protocol  # type: bool
        self.security_policy_id = security_policy_id  # type: str
        self.state = state  # type: str
        self.type = type  # type: str
        self.xforwarded_for_config = xforwarded_for_config  # type: ListListenersResponseBodyListenersXForwardedForConfig

    def validate(self):
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super(ListListenersResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = ListListenersResponseBodyListenersBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenersResponseBodyListenersCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListListenersResponseBodyListenersPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XForwardedForConfig') is not None:
            temp_model = ListListenersResponseBodyListenersXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class ListListenersResponseBody(TeaModel):
    def __init__(self, listeners=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.listeners = listeners  # type: list[ListListenersResponseBodyListeners]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListListenersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersResponse, self).to_map()
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
            temp_model = ListListenersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpareIpsRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, dry_run=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpareIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSpareIpsResponseBodySpareIps(TeaModel):
    def __init__(self, spare_ip=None, state=None):
        self.spare_ip = spare_ip  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpareIpsResponseBodySpareIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListSpareIpsResponseBody(TeaModel):
    def __init__(self, request_id=None, spare_ips=None):
        self.request_id = request_id  # type: str
        self.spare_ips = spare_ips  # type: list[ListSpareIpsResponseBodySpareIps]

    def validate(self):
        if self.spare_ips:
            for k in self.spare_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSpareIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpareIps'] = []
        if self.spare_ips is not None:
            for k in self.spare_ips:
                result['SpareIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spare_ips = []
        if m.get('SpareIps') is not None:
            for k in m.get('SpareIps'):
                temp_model = ListSpareIpsResponseBodySpareIps()
                self.spare_ips.append(temp_model.from_map(k))
        return self


class ListSpareIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSpareIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSpareIpsResponse, self).to_map()
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
            temp_model = ListSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemSecurityPoliciesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemSecurityPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSystemSecurityPoliciesResponseBodySecurityPolicies(TeaModel):
    def __init__(self, ciphers=None, security_policy_id=None, tls_versions=None):
        self.ciphers = ciphers  # type: list[str]
        self.security_policy_id = security_policy_id  # type: str
        self.tls_versions = tls_versions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemSecurityPoliciesResponseBodySecurityPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')
        return self


class ListSystemSecurityPoliciesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, security_policies=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.security_policies = security_policies  # type: list[ListSystemSecurityPoliciesResponseBodySecurityPolicies]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSystemSecurityPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSystemSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSystemSecurityPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSystemSecurityPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSystemSecurityPoliciesResponse, self).to_map()
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
            temp_model = ListSystemSecurityPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntriesFromAclRequestAclEntries(TeaModel):
    def __init__(self, entry=None):
        self.entry = entry  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntriesFromAclRequestAclEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class RemoveEntriesFromAclRequest(TeaModel):
    def __init__(self, acl_entries=None, acl_id=None, client_token=None, dry_run=None, region_id=None):
        self.acl_entries = acl_entries  # type: list[RemoveEntriesFromAclRequestAclEntries]
        self.acl_id = acl_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveEntriesFromAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = RemoveEntriesFromAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveEntriesFromAclResponseBody(TeaModel):
    def __init__(self, acl_id=None, request_id=None):
        self.acl_id = acl_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveEntriesFromAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveEntriesFromAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveEntriesFromAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveEntriesFromAclResponse, self).to_map()
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
            temp_model = RemoveEntriesFromAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceBandwidthPackageRequest(TeaModel):
    def __init__(self, accelerator_id=None, bandwidth_package_id=None, region_id=None,
                 target_bandwidth_package_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.region_id = region_id  # type: str
        self.target_bandwidth_package_id = target_bandwidth_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_bandwidth_package_id is not None:
            result['TargetBandwidthPackageId'] = self.target_bandwidth_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetBandwidthPackageId') is not None:
            self.target_bandwidth_package_id = m.get('TargetBandwidthPackageId')
        return self


class ReplaceBandwidthPackageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceBandwidthPackageResponseBody, self).to_map()
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


class ReplaceBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReplaceBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplaceBandwidthPackageResponse, self).to_map()
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
            temp_model = ReplaceBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, auto_pay=None, auto_use_coupon=None, client_token=None,
                 description=None, name=None, region_id=None, spec=None):
        self.accelerator_id = accelerator_id  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_use_coupon = auto_use_coupon  # type: bool
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorResponseBody, self).to_map()
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


class UpdateAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAcceleratorResponse, self).to_map()
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
            temp_model = UpdateAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorAutoRenewAttributeRequest(TeaModel):
    def __init__(self, accelerator_id=None, auto_renew=None, auto_renew_duration=None, client_token=None, name=None,
                 region_id=None, renewal_status=None):
        self.accelerator_id = accelerator_id  # type: str
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.client_token = client_token  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.renewal_status = renewal_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorAutoRenewAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class UpdateAcceleratorAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, accelerator_id=None, request_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorAutoRenewAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAcceleratorAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAcceleratorAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAcceleratorAutoRenewAttributeResponse, self).to_map()
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
            temp_model = UpdateAcceleratorAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorConfirmRequest(TeaModel):
    def __init__(self, accelerator_id=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorConfirmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAcceleratorConfirmResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAcceleratorConfirmResponseBody, self).to_map()
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


class UpdateAcceleratorConfirmResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAcceleratorConfirmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAcceleratorConfirmResponse, self).to_map()
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
            temp_model = UpdateAcceleratorConfirmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclAttributeRequest(TeaModel):
    def __init__(self, acl_id=None, acl_name=None, client_token=None, dry_run=None, region_id=None):
        self.acl_id = acl_id  # type: str
        self.acl_name = acl_name  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAclAttributeResponseBody(TeaModel):
    def __init__(self, acl_id=None, request_id=None):
        self.acl_id = acl_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAclAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAclAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAclAttributeResponse, self).to_map()
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
            temp_model = UpdateAclAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationMonitorRequest(TeaModel):
    def __init__(self, address=None, client_token=None, detect_enable=None, detect_threshold=None,
                 detect_times=None, listener_id=None, options_json=None, region_id=None, silence_time=None, task_id=None,
                 task_name=None):
        self.address = address  # type: str
        self.client_token = client_token  # type: str
        self.detect_enable = detect_enable  # type: bool
        self.detect_threshold = detect_threshold  # type: int
        self.detect_times = detect_times  # type: int
        self.listener_id = listener_id  # type: str
        self.options_json = options_json  # type: str
        self.region_id = region_id  # type: str
        self.silence_time = silence_time  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateApplicationMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationMonitorResponseBody, self).to_map()
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


class UpdateApplicationMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationMonitorResponse, self).to_map()
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
            temp_model = UpdateApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBandwidthPackagaAutoRenewAttributeRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_duration=None, client_token=None, instance_id=None, name=None,
                 region_id=None, renewal_status=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_duration = auto_renew_duration  # type: int
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.renewal_status = renewal_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBandwidthPackagaAutoRenewAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class UpdateBandwidthPackagaAutoRenewAttributeResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBandwidthPackagaAutoRenewAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBandwidthPackagaAutoRenewAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBandwidthPackagaAutoRenewAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBandwidthPackagaAutoRenewAttributeResponse, self).to_map()
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
            temp_model = UpdateBandwidthPackagaAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBandwidthPackageRequest(TeaModel):
    def __init__(self, auto_pay=None, auto_use_coupon=None, bandwidth=None, bandwidth_package_id=None,
                 bandwidth_type=None, description=None, name=None, region_id=None):
        self.auto_pay = auto_pay  # type: bool
        self.auto_use_coupon = auto_use_coupon  # type: bool
        self.bandwidth = bandwidth  # type: int
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBandwidthPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBandwidthPackageResponseBody(TeaModel):
    def __init__(self, bandwidth_package=None, description=None, name=None, request_id=None):
        self.bandwidth_package = bandwidth_package  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBandwidthPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBandwidthPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBandwidthPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBandwidthPackageResponse, self).to_map()
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
            temp_model = UpdateBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicAcceleratorRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, description=None, name=None, region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicAcceleratorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBasicAcceleratorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicAcceleratorResponseBody, self).to_map()
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


class UpdateBasicAcceleratorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBasicAcceleratorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBasicAcceleratorResponse, self).to_map()
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
            temp_model = UpdateBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicEndpointGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, endpoint_address=None, endpoint_group_id=None,
                 endpoint_sub_address=None, endpoint_type=None, name=None, region_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.endpoint_address = endpoint_address  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_sub_address = endpoint_sub_address  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBasicEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicEndpointGroupResponseBody, self).to_map()
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


class UpdateBasicEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBasicEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBasicEndpointGroupResponse, self).to_map()
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
            temp_model = UpdateBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicIpSetRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, ip_set_id=None, region_id=None):
        self.bandwidth = bandwidth  # type: int
        self.client_token = client_token  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBasicIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBasicIpSetResponseBody, self).to_map()
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


class UpdateBasicIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBasicIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBasicIpSetResponse, self).to_map()
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
            temp_model = UpdateBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointGroupAttributeRequest(TeaModel):
    def __init__(self, client_token=None, description=None, endpoint_group_id=None, name=None, region_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointGroupAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupAttributeResponseBody, self).to_map()
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


class UpdateCustomRoutingEndpointGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomRoutingEndpointGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupAttributeResponse, self).to_map()
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
            temp_model = UpdateCustomRoutingEndpointGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations(TeaModel):
    def __init__(self, destination_id=None, from_port=None, protocols=None, to_port=None):
        self.destination_id = destination_id  # type: str
        self.from_port = from_port  # type: int
        self.protocols = protocols  # type: list[str]
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(self, client_token=None, destination_configurations=None, dry_run=None, endpoint_group_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.destination_configurations = destination_configurations  # type: list[UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations]
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupDestinationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupDestinationsResponseBody, self).to_map()
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


class UpdateCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomRoutingEndpointGroupDestinationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointGroupDestinationsResponse, self).to_map()
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
            temp_model = UpdateCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations(TeaModel):
    def __init__(self, address=None, policy_id=None, port_ranges=None):
        self.address = address  # type: str
        self.policy_id = policy_id  # type: str
        self.port_ranges = port_ranges  # type: list[UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_id=None, policy_configurations=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.policy_configurations = policy_configurations  # type: list[UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations]
        self.region_id = region_id  # type: str

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointTrafficPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(self, policy_ids=None, request_id=None):
        self.policy_ids = policy_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointTrafficPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomRoutingEndpointTrafficPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointTrafficPoliciesResponse, self).to_map()
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
            temp_model = UpdateCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: str
        self.to_port = to_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(self, address=None, port_ranges=None):
        self.address = address  # type: str
        self.port_ranges = port_ranges  # type: list[UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges]

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class UpdateCustomRoutingEndpointsRequestEndpointConfigurations(TeaModel):
    def __init__(self, endpoint_id=None, policy_configurations=None, traffic_to_endpoint_policy=None):
        self.endpoint_id = endpoint_id  # type: str
        self.policy_configurations = policy_configurations  # type: list[UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations]
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy  # type: str

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointsRequestEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        return self


class UpdateCustomRoutingEndpointsRequest(TeaModel):
    def __init__(self, client_token=None, endpoint_configurations=None, endpoint_group_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.endpoint_configurations = endpoint_configurations  # type: list[UpdateCustomRoutingEndpointsRequestEndpointConfigurations]
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateCustomRoutingEndpointsRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(self, endpoint_ids=None, request_id=None):
        self.endpoint_ids = endpoint_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomRoutingEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomRoutingEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomRoutingEndpointsResponse, self).to_map()
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
            temp_model = UpdateCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupRequestEndpointConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation=None, endpoint=None, type=None, weight=None):
        self.enable_client_ippreservation = enable_client_ippreservation  # type: bool
        self.endpoint = endpoint  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupRequestEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateEndpointGroupRequestPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: int
        self.listener_port = listener_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupRequestPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class UpdateEndpointGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, endpoint_configurations=None, endpoint_group_id=None,
                 endpoint_group_region=None, endpoint_request_protocol=None, health_check_enabled=None,
                 health_check_interval_seconds=None, health_check_path=None, health_check_port=None, health_check_protocol=None, name=None,
                 port_overrides=None, region_id=None, threshold_count=None, traffic_percentage=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.endpoint_configurations = endpoint_configurations  # type: list[UpdateEndpointGroupRequestEndpointConfigurations]
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_region = endpoint_group_region  # type: str
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: int
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: int
        self.health_check_protocol = health_check_protocol  # type: str
        self.name = name  # type: str
        self.port_overrides = port_overrides  # type: list[UpdateEndpointGroupRequestPortOverrides]
        self.region_id = region_id  # type: str
        self.threshold_count = threshold_count  # type: int
        self.traffic_percentage = traffic_percentage  # type: int

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = UpdateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class UpdateEndpointGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupResponseBody, self).to_map()
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


class UpdateEndpointGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEndpointGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupResponse, self).to_map()
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
            temp_model = UpdateEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupAttributeRequest(TeaModel):
    def __init__(self, client_token=None, description=None, endpoint_group_id=None, name=None, region_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEndpointGroupAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupAttributeResponseBody, self).to_map()
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


class UpdateEndpointGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEndpointGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupAttributeResponse, self).to_map()
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
            temp_model = UpdateEndpointGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(self, endpoint=None, type=None, weight=None):
        self.endpoint = endpoint  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(self, endpoint_port=None, listener_port=None):
        self.endpoint_port = endpoint_port  # type: long
        self.listener_port = listener_port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(self, enable_client_ippreservation_proxy_protocol=None, enable_client_ippreservation_toa=None,
                 endpoint_configurations=None, endpoint_group_description=None, endpoint_group_id=None, endpoint_group_name=None,
                 endpoint_request_protocol=None, health_check_enabled=None, health_check_interval_seconds=None, health_check_path=None,
                 health_check_port=None, health_check_protocol=None, port_overrides=None, threshold_count=None,
                 traffic_percentage=None):
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol  # type: bool
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa  # type: bool
        self.endpoint_configurations = endpoint_configurations  # type: list[UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations]
        self.endpoint_group_description = endpoint_group_description  # type: str
        self.endpoint_group_id = endpoint_group_id  # type: str
        self.endpoint_group_name = endpoint_group_name  # type: str
        self.endpoint_request_protocol = endpoint_request_protocol  # type: str
        self.health_check_enabled = health_check_enabled  # type: bool
        self.health_check_interval_seconds = health_check_interval_seconds  # type: long
        self.health_check_path = health_check_path  # type: str
        self.health_check_port = health_check_port  # type: long
        self.health_check_protocol = health_check_protocol  # type: str
        self.port_overrides = port_overrides  # type: list[UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides]
        self.threshold_count = threshold_count  # type: long
        self.traffic_percentage = traffic_percentage  # type: long

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequestEndpointGroupConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class UpdateEndpointGroupsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_group_configurations=None, listener_id=None,
                 region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.endpoint_group_configurations = endpoint_group_configurations  # type: list[UpdateEndpointGroupsRequestEndpointGroupConfigurations]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEndpointGroupsResponseBody(TeaModel):
    def __init__(self, endpoint_group_ids=None, request_id=None):
        self.endpoint_group_ids = endpoint_group_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEndpointGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateEndpointGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEndpointGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEndpointGroupsResponse, self).to_map()
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
            temp_model = UpdateEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(self, endpoint_group_id=None):
        self.endpoint_group_id = endpoint_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(self, server_group_tuples=None):
        self.server_group_tuples = server_group_tuples  # type: list[UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples]

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActions(TeaModel):
    def __init__(self, forward_group_config=None, order=None, rule_action_type=None, rule_action_value=None):
        self.forward_group_config = forward_group_config  # type: UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig
        self.order = order  # type: int
        self.rule_action_type = rule_action_type  # type: str
        self.rule_action_value = rule_action_value  # type: str

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditions(TeaModel):
    def __init__(self, host_config=None, path_config=None, rule_condition_type=None, rule_condition_value=None):
        self.host_config = host_config  # type: UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig
        self.path_config = path_config  # type: UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig
        self.rule_condition_type = rule_condition_type  # type: str
        self.rule_condition_value = rule_condition_value  # type: str

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRulesRuleConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('PathConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')
        return self


class UpdateForwardingRulesRequestForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None, forwarding_rule_name=None, priority=None, rule_actions=None,
                 rule_conditions=None, rule_direction=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str
        self.forwarding_rule_name = forwarding_rule_name  # type: str
        self.priority = priority  # type: int
        self.rule_actions = rule_actions  # type: list[UpdateForwardingRulesRequestForwardingRulesRuleActions]
        self.rule_conditions = rule_conditions  # type: list[UpdateForwardingRulesRequestForwardingRulesRuleConditions]
        self.rule_direction = rule_direction  # type: str

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequestForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_direction is not None:
            result['RuleDirection'] = self.rule_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')
        return self


class UpdateForwardingRulesRequest(TeaModel):
    def __init__(self, accelerator_id=None, client_token=None, forwarding_rules=None, listener_id=None,
                 region_id=None):
        self.accelerator_id = accelerator_id  # type: str
        self.client_token = client_token  # type: str
        self.forwarding_rules = forwarding_rules  # type: list[UpdateForwardingRulesRequestForwardingRules]
        self.listener_id = listener_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = UpdateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(self, forwarding_rule_id=None):
        self.forwarding_rule_id = forwarding_rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateForwardingRulesResponseBodyForwardingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class UpdateForwardingRulesResponseBody(TeaModel):
    def __init__(self, forwarding_rules=None, request_id=None):
        self.forwarding_rules = forwarding_rules  # type: list[UpdateForwardingRulesResponseBodyForwardingRules]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = UpdateForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateForwardingRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateForwardingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateForwardingRulesResponse, self).to_map()
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
            temp_model = UpdateForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpSetRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, ip_set_id=None, region_id=None):
        self.bandwidth = bandwidth  # type: int
        self.client_token = client_token  # type: str
        self.ip_set_id = ip_set_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetResponseBody, self).to_map()
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


class UpdateIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIpSetResponse, self).to_map()
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
            temp_model = UpdateIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpSetsRequestIpSets(TeaModel):
    def __init__(self, bandwidth=None, ip_set_id=None):
        self.bandwidth = bandwidth  # type: int
        self.ip_set_id = ip_set_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetsRequestIpSets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        return self


class UpdateIpSetsRequest(TeaModel):
    def __init__(self, ip_sets=None, region_id=None):
        self.ip_sets = ip_sets  # type: list[UpdateIpSetsRequestIpSets]
        self.region_id = region_id  # type: str

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateIpSetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = UpdateIpSetsRequestIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIpSetsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIpSetsResponseBody, self).to_map()
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


class UpdateIpSetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateIpSetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIpSetsResponse, self).to_map()
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
            temp_model = UpdateIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateListenerRequestBackendPorts(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestBackendPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateListenerRequestCertificates(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateListenerRequestPortRanges(TeaModel):
    def __init__(self, from_port=None, to_port=None):
        self.from_port = from_port  # type: int
        self.to_port = to_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestPortRanges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateListenerRequestXForwardedForConfig(TeaModel):
    def __init__(self, xforwarded_for_ga_ap_enabled=None, xforwarded_for_ga_id_enabled=None,
                 xforwarded_for_port_enabled=None, xforwarded_for_proto_enabled=None, xreal_ip_enabled=None):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled  # type: bool
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled  # type: bool
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled  # type: bool
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled  # type: bool
        self.xreal_ip_enabled = xreal_ip_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerRequestXForwardedForConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class UpdateListenerRequest(TeaModel):
    def __init__(self, backend_ports=None, certificates=None, client_affinity=None, client_token=None,
                 description=None, listener_id=None, name=None, port_ranges=None, protocol=None, proxy_protocol=None,
                 region_id=None, security_policy_id=None, xforwarded_for_config=None):
        self.backend_ports = backend_ports  # type: list[UpdateListenerRequestBackendPorts]
        self.certificates = certificates  # type: list[UpdateListenerRequestCertificates]
        self.client_affinity = client_affinity  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.listener_id = listener_id  # type: str
        self.name = name  # type: str
        self.port_ranges = port_ranges  # type: list[UpdateListenerRequestPortRanges]
        self.protocol = protocol  # type: str
        self.proxy_protocol = proxy_protocol  # type: str
        self.region_id = region_id  # type: str
        self.security_policy_id = security_policy_id  # type: str
        self.xforwarded_for_config = xforwarded_for_config  # type: UpdateListenerRequestXForwardedForConfig

    def validate(self):
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super(UpdateListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = UpdateListenerRequestBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = UpdateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('XForwardedForConfig') is not None:
            temp_model = UpdateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class UpdateListenerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerResponseBody, self).to_map()
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


class UpdateListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateListenerResponse, self).to_map()
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
            temp_model = UpdateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


