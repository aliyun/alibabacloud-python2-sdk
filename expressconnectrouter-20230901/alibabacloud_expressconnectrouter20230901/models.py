# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(self, child_instance_id=None, child_instance_owner_id=None, child_instance_region_id=None,
                 child_instance_type=None, client_token=None, dry_run=None, ecr_id=None):
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachExpressConnectRouterChildInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class AttachExpressConnectRouterChildInstanceResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachExpressConnectRouterChildInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachExpressConnectRouterChildInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachExpressConnectRouterChildInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachExpressConnectRouterChildInstanceResponse, self).to_map()
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
            temp_model = AttachExpressConnectRouterChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAddRegionToExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, fresh_region_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.fresh_region_id = fresh_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAddRegionToExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.fresh_region_id is not None:
            result['FreshRegionId'] = self.fresh_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FreshRegionId') is not None:
            self.fresh_region_id = m.get('FreshRegionId')
        return self


class CheckAddRegionToExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, any_cross_border_link=None, any_inter_region_link=None,
                 code=None, dynamic_code=None, dynamic_message=None, http_status_code=None,
                 is_cdt_cross_border_enabled=None, is_cdt_inter_region_enabled=None, is_user_allowed_to_create_cross_border_link=None,
                 message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.any_cross_border_link = any_cross_border_link  # type: bool
        self.any_inter_region_link = any_inter_region_link  # type: bool
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.is_cdt_cross_border_enabled = is_cdt_cross_border_enabled  # type: bool
        self.is_cdt_inter_region_enabled = is_cdt_inter_region_enabled  # type: bool
        self.is_user_allowed_to_create_cross_border_link = is_user_allowed_to_create_cross_border_link  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAddRegionToExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.any_cross_border_link is not None:
            result['AnyCrossBorderLink'] = self.any_cross_border_link
        if self.any_inter_region_link is not None:
            result['AnyInterRegionLink'] = self.any_inter_region_link
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.is_cdt_cross_border_enabled is not None:
            result['IsCdtCrossBorderEnabled'] = self.is_cdt_cross_border_enabled
        if self.is_cdt_inter_region_enabled is not None:
            result['IsCdtInterRegionEnabled'] = self.is_cdt_inter_region_enabled
        if self.is_user_allowed_to_create_cross_border_link is not None:
            result['IsUserAllowedToCreateCrossBorderLink'] = self.is_user_allowed_to_create_cross_border_link
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AnyCrossBorderLink') is not None:
            self.any_cross_border_link = m.get('AnyCrossBorderLink')
        if m.get('AnyInterRegionLink') is not None:
            self.any_inter_region_link = m.get('AnyInterRegionLink')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IsCdtCrossBorderEnabled') is not None:
            self.is_cdt_cross_border_enabled = m.get('IsCdtCrossBorderEnabled')
        if m.get('IsCdtInterRegionEnabled') is not None:
            self.is_cdt_inter_region_enabled = m.get('IsCdtInterRegionEnabled')
        if m.get('IsUserAllowedToCreateCrossBorderLink') is not None:
            self.is_user_allowed_to_create_cross_border_link = m.get('IsUserAllowedToCreateCrossBorderLink')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckAddRegionToExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckAddRegionToExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAddRegionToExpressConnectRouterResponse, self).to_map()
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
            temp_model = CheckAddRegionToExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExpressConnectRouterRequest(TeaModel):
    def __init__(self, alibaba_side_asn=None, client_token=None, description=None, dry_run=None, name=None,
                 resource_group_id=None):
        self.alibaba_side_asn = alibaba_side_asn  # type: long
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None, ecr_id=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.ecr_id = ecr_id  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExpressConnectRouterResponse, self).to_map()
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
            temp_model = CreateExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExpressConnectRouterAssociationRequest(TeaModel):
    def __init__(self, allowed_prefixes=None, association_region_id=None, cen_id=None, client_token=None,
                 create_attachment=None, dry_run=None, ecr_id=None, transit_router_id=None, transit_router_owner_id=None, vpc_id=None,
                 vpc_owner_id=None):
        self.allowed_prefixes = allowed_prefixes  # type: list[str]
        self.association_region_id = association_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.create_attachment = create_attachment  # type: bool
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_owner_id = transit_router_owner_id  # type: long
        self.vpc_id = vpc_id  # type: str
        self.vpc_owner_id = vpc_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExpressConnectRouterAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes
        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_attachment is not None:
            result['CreateAttachment'] = self.create_attachment
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_owner_id is not None:
            result['TransitRouterOwnerId'] = self.transit_router_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')
        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateAttachment') is not None:
            self.create_attachment = m.get('CreateAttachment')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterOwnerId') is not None:
            self.transit_router_owner_id = m.get('TransitRouterOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        return self


class CreateExpressConnectRouterAssociationResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, association_id=None, code=None, dynamic_code=None,
                 dynamic_message=None, http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.association_id = association_id  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExpressConnectRouterAssociationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateExpressConnectRouterAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateExpressConnectRouterAssociationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExpressConnectRouterAssociationResponse, self).to_map()
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
            temp_model = CreateExpressConnectRouterAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DeleteExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExpressConnectRouterResponse, self).to_map()
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
            temp_model = DeleteExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExpressConnectRouterAssociationRequest(TeaModel):
    def __init__(self, association_id=None, client_token=None, delete_attachment=None, dry_run=None, ecr_id=None):
        self.association_id = association_id  # type: str
        self.client_token = client_token  # type: str
        self.delete_attachment = delete_attachment  # type: bool
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExpressConnectRouterAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.delete_attachment is not None:
            result['DeleteAttachment'] = self.delete_attachment
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeleteAttachment') is not None:
            self.delete_attachment = m.get('DeleteAttachment')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DeleteExpressConnectRouterAssociationResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExpressConnectRouterAssociationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteExpressConnectRouterAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteExpressConnectRouterAssociationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExpressConnectRouterAssociationResponse, self).to_map()
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
            temp_model = DeleteExpressConnectRouterAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, max_results=None, next_token=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisabledExpressConnectRouterRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList(TeaModel):
    def __init__(self, destination_cidr_block=None, ecr_id=None, gmt_create=None, nexthop_instance_id=None,
                 nexthop_instance_region_id=None):
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.ecr_id = ecr_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.nexthop_instance_id = nexthop_instance_id  # type: str
        self.nexthop_instance_region_id = nexthop_instance_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        if self.nexthop_instance_region_id is not None:
            result['NexthopInstanceRegionId'] = self.nexthop_instance_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        if m.get('NexthopInstanceRegionId') is not None:
            self.nexthop_instance_region_id = m.get('NexthopInstanceRegionId')
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, disabled_route_entry_list=None, dynamic_code=None,
                 dynamic_message=None, http_status_code=None, max_results=None, message=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.disabled_route_entry_list = disabled_route_entry_list  # type: list[DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList]
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.disabled_route_entry_list:
            for k in self.disabled_route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDisabledExpressConnectRouterRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['DisabledRouteEntryList'] = []
        if self.disabled_route_entry_list is not None:
            for k in self.disabled_route_entry_list:
                result['DisabledRouteEntryList'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.disabled_route_entry_list = []
        if m.get('DisabledRouteEntryList') is not None:
            for k in m.get('DisabledRouteEntryList'):
                temp_model = DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList()
                self.disabled_route_entry_list.append(temp_model.from_map(k))
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDisabledExpressConnectRouterRouteEntriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDisabledExpressConnectRouterRouteEntriesResponse, self).to_map()
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
            temp_model = DescribeDisabledExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterRequestTagModels(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRequestTagModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, max_results=None, name=None, next_token=None,
                 resource_group_id=None, tag_models=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.max_results = max_results  # type: int
        self.name = name  # type: str
        self.next_token = next_token  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag_models = tag_models  # type: list[DescribeExpressConnectRouterRequestTagModels]

    def validate(self):
        if self.tag_models:
            for k in self.tag_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['TagModels'] = []
        if self.tag_models is not None:
            for k in self.tag_models:
                result['TagModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag_models = []
        if m.get('TagModels') is not None:
            for k in m.get('TagModels'):
                temp_model = DescribeExpressConnectRouterRequestTagModels()
                self.tag_models.append(temp_model.from_map(k))
        return self


class DescribeExpressConnectRouterResponseBodyEcrListTags(TeaModel):
    def __init__(self, ali_uid=None, category=None, id=None, region_no=None, resource_id=None, resuorce_type=None,
                 scope=None, tag_key=None, tag_value=None):
        self.ali_uid = ali_uid  # type: long
        self.category = category  # type: int
        self.id = id  # type: long
        self.region_no = region_no  # type: str
        self.resource_id = resource_id  # type: str
        self.resuorce_type = resuorce_type  # type: str
        self.scope = scope  # type: int
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterResponseBodyEcrListTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resuorce_type is not None:
            result['ResuorceType'] = self.resuorce_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResuorceType') is not None:
            self.resuorce_type = m.get('ResuorceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeExpressConnectRouterResponseBodyEcrList(TeaModel):
    def __init__(self, alibaba_side_asn=None, biz_status=None, description=None, ecr_id=None, gmt_create=None,
                 gmt_modified=None, name=None, owner_id=None, resource_group_id=None, status=None, tags=None):
        self.alibaba_side_asn = alibaba_side_asn  # type: long
        self.biz_status = biz_status  # type: str
        self.description = description  # type: str
        self.ecr_id = ecr_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[DescribeExpressConnectRouterResponseBodyEcrListTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterResponseBodyEcrList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.description is not None:
            result['Description'] = self.description
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeExpressConnectRouterResponseBodyEcrListTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None, ecr_list=None,
                 http_status_code=None, max_results=None, message=None, next_token=None, request_id=None, success=None,
                 total_count=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.ecr_list = ecr_list  # type: list[DescribeExpressConnectRouterResponseBodyEcrList]
        self.http_status_code = http_status_code  # type: int
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ecr_list:
            for k in self.ecr_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['EcrList'] = []
        if self.ecr_list is not None:
            for k in self.ecr_list:
                result['EcrList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.ecr_list = []
        if m.get('EcrList') is not None:
            for k in m.get('EcrList'):
                temp_model = DescribeExpressConnectRouterResponseBodyEcrList()
                self.ecr_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryRequest(TeaModel):
    def __init__(self, associaton_id=None, client_token=None, dry_run=None, ecr_id=None, instance_id=None,
                 instance_type=None):
        self.associaton_id = associaton_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAllowedPrefixHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associaton_id is not None:
            result['AssociatonId'] = self.associaton_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociatonId') is not None:
            self.associaton_id = m.get('AssociatonId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList(TeaModel):
    def __init__(self, allowed_prefix=None, gmt_create=None):
        self.allowed_prefix = allowed_prefix  # type: list[str]
        self.gmt_create = gmt_create  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefix is not None:
            result['AllowedPrefix'] = self.allowed_prefix
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedPrefix') is not None:
            self.allowed_prefix = m.get('AllowedPrefix')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, allowed_prefix_history_list=None, code=None, dynamic_code=None,
                 dynamic_message=None, http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.allowed_prefix_history_list = allowed_prefix_history_list  # type: list[DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList]
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.allowed_prefix_history_list:
            for k in self.allowed_prefix_history_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['AllowedPrefixHistoryList'] = []
        if self.allowed_prefix_history_list is not None:
            for k in self.allowed_prefix_history_list:
                result['AllowedPrefixHistoryList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.allowed_prefix_history_list = []
        if m.get('AllowedPrefixHistoryList') is not None:
            for k in m.get('AllowedPrefixHistoryList'):
                temp_model = DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList()
                self.allowed_prefix_history_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAllowedPrefixHistoryResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterAssociationRequest(TeaModel):
    def __init__(self, association_id=None, association_node_type=None, association_region_id=None, cen_id=None,
                 client_token=None, dry_run=None, ecr_id=None, max_results=None, next_token=None, transit_router_id=None,
                 vpc_id=None):
        self.association_id = association_id  # type: str
        self.association_node_type = association_node_type  # type: str
        self.association_region_id = association_region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type
        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')
        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeExpressConnectRouterAssociationResponseBodyAssociationList(TeaModel):
    def __init__(self, allowed_prefixes=None, association_id=None, association_node_type=None, cen_id=None,
                 ecr_id=None, gmt_create=None, gmt_modified=None, owner_id=None, region_id=None, status=None,
                 transit_router_id=None, transit_router_owner_id=None, vpc_id=None, vpc_owner_id=None):
        self.allowed_prefixes = allowed_prefixes  # type: list[str]
        self.association_id = association_id  # type: str
        self.association_node_type = association_node_type  # type: str
        self.cen_id = cen_id  # type: str
        self.ecr_id = ecr_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.transit_router_id = transit_router_id  # type: str
        self.transit_router_owner_id = transit_router_owner_id  # type: long
        self.vpc_id = vpc_id  # type: str
        self.vpc_owner_id = vpc_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAssociationResponseBodyAssociationList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_owner_id is not None:
            result['TransitRouterOwnerId'] = self.transit_router_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterOwnerId') is not None:
            self.transit_router_owner_id = m.get('TransitRouterOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        return self


class DescribeExpressConnectRouterAssociationResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, association_list=None, code=None, dynamic_code=None,
                 dynamic_message=None, http_status_code=None, max_results=None, message=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.association_list = association_list  # type: list[DescribeExpressConnectRouterAssociationResponseBodyAssociationList]
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.association_list:
            for k in self.association_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAssociationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['AssociationList'] = []
        if self.association_list is not None:
            for k in self.association_list:
                result['AssociationList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.association_list = []
        if m.get('AssociationList') is not None:
            for k in m.get('AssociationList'):
                temp_model = DescribeExpressConnectRouterAssociationResponseBodyAssociationList()
                self.association_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterAssociationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterAssociationResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(self, association_id=None, child_instance_id=None, child_instance_region_id=None,
                 child_instance_type=None, client_token=None, dry_run=None, ecr_id=None, max_results=None, next_token=None):
        self.association_id = association_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterChildInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList(TeaModel):
    def __init__(self, association_id=None, child_instance_id=None, child_instance_owner_id=None,
                 child_instance_region_id=None, child_instance_type=None, gmt_create=None, gmt_modified=None, owner_id=None, region_id=None,
                 status=None):
        self.association_id = association_id  # type: str
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_owner_id = child_instance_owner_id  # type: long
        self.child_instance_region_id = child_instance_region_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeExpressConnectRouterChildInstanceResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, child_instance_list=None, code=None, dynamic_code=None,
                 dynamic_message=None, http_status_code=None, max_results=None, message=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.child_instance_list = child_instance_list  # type: list[DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList]
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.child_instance_list:
            for k in self.child_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterChildInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['ChildInstanceList'] = []
        if self.child_instance_list is not None:
            for k in self.child_instance_list:
                result['ChildInstanceList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.child_instance_list = []
        if m.get('ChildInstanceList') is not None:
            for k in m.get('ChildInstanceList'):
                temp_model = DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList()
                self.child_instance_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterChildInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterChildInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterChildInstanceResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterInterRegionTransitModeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterInterRegionTransitModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList(TeaModel):
    def __init__(self, mode=None, region_id=None):
        self.mode = mode  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeExpressConnectRouterInterRegionTransitModeResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, inter_region_transit_mode_list=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.inter_region_transit_mode_list = inter_region_transit_mode_list  # type: list[DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.inter_region_transit_mode_list:
            for k in self.inter_region_transit_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterInterRegionTransitModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InterRegionTransitModeList'] = []
        if self.inter_region_transit_mode_list is not None:
            for k in self.inter_region_transit_mode_list:
                result['InterRegionTransitModeList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.inter_region_transit_mode_list = []
        if m.get('InterRegionTransitModeList') is not None:
            for k in m.get('InterRegionTransitModeList'):
                temp_model = DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList()
                self.inter_region_transit_mode_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressConnectRouterInterRegionTransitModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterInterRegionTransitModeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterInterRegionTransitModeResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterInterRegionTransitModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterRegionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRegionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DescribeExpressConnectRouterRegionResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, region_id_list=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.region_id_list = region_id_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id_list is not None:
            result['RegionIdList'] = self.region_id_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionIdList') is not None:
            self.region_id_list = m.get('RegionIdList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressConnectRouterRegionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterRegionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRegionResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(self, as_path=None, client_token=None, community=None, destination_cidr_block=None, dry_run=None,
                 ecr_id=None, max_results=None, next_token=None, nexthop_instance_id=None, query_region_id=None):
        self.as_path = as_path  # type: str
        self.client_token = client_token  # type: str
        self.community = community  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.nexthop_instance_id = nexthop_instance_id  # type: str
        self.query_region_id = query_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.community is not None:
            result['Community'] = self.community
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Community') is not None:
            self.community = m.get('Community')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')
        return self


class DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList(TeaModel):
    def __init__(self, as_path=None, community=None, destination_cidr_block=None, nexthop_instance_id=None,
                 nexthop_instance_region_id=None, status=None):
        self.as_path = as_path  # type: str
        self.community = community  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.nexthop_instance_id = nexthop_instance_id  # type: str
        self.nexthop_instance_region_id = nexthop_instance_region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        if self.community is not None:
            result['Community'] = self.community
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        if self.nexthop_instance_region_id is not None:
            result['NexthopInstanceRegionId'] = self.nexthop_instance_region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        if m.get('Community') is not None:
            self.community = m.get('Community')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        if m.get('NexthopInstanceRegionId') is not None:
            self.nexthop_instance_region_id = m.get('NexthopInstanceRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, max_results=None, message=None, next_token=None, request_id=None, route_entries_list=None,
                 success=None, total_count=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.route_entries_list = route_entries_list  # type: list[DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList]
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.route_entries_list:
            for k in self.route_entries_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RouteEntriesList'] = []
        if self.route_entries_list is not None:
            for k in self.route_entries_list:
                result['RouteEntriesList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.route_entries_list = []
        if m.get('RouteEntriesList') is not None:
            for k in m.get('RouteEntriesList'):
                temp_model = DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList()
                self.route_entries_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExpressConnectRouterRouteEntriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExpressConnectRouterRouteEntriesResponse, self).to_map()
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
            temp_model = DescribeExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceGrantedToExpressConnectRouterRequestTagModels(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceGrantedToExpressConnectRouterRequestTagModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeInstanceGrantedToExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, instance_id=None, instance_owner_id=None,
                 instance_region_id=None, instance_type=None, max_results=None, next_token=None, resource_group_id=None,
                 tag_models=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_owner_id = instance_owner_id  # type: long
        self.instance_region_id = instance_region_id  # type: str
        self.instance_type = instance_type  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag_models = tag_models  # type: list[DescribeInstanceGrantedToExpressConnectRouterRequestTagModels]

    def validate(self):
        if self.tag_models:
            for k in self.tag_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceGrantedToExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['TagModels'] = []
        if self.tag_models is not None:
            for k in self.tag_models:
                result['TagModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag_models = []
        if m.get('TagModels') is not None:
            for k in m.get('TagModels'):
                temp_model = DescribeInstanceGrantedToExpressConnectRouterRequestTagModels()
                self.tag_models.append(temp_model.from_map(k))
        return self


class DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList(TeaModel):
    def __init__(self, ecr_id=None, gmt_create=None, gmt_modified=None, grant_id=None, node_id=None,
                 node_owner_bid=None, node_owner_uid=None, node_region_id=None, node_type=None, status=None):
        self.ecr_id = ecr_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.grant_id = grant_id  # type: str
        self.node_id = node_id  # type: str
        self.node_owner_bid = node_owner_bid  # type: str
        self.node_owner_uid = node_owner_uid  # type: long
        self.node_region_id = node_region_id  # type: str
        self.node_type = node_type  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.grant_id is not None:
            result['GrantId'] = self.grant_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_owner_bid is not None:
            result['NodeOwnerBid'] = self.node_owner_bid
        if self.node_owner_uid is not None:
            result['NodeOwnerUid'] = self.node_owner_uid
        if self.node_region_id is not None:
            result['NodeRegionId'] = self.node_region_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GrantId') is not None:
            self.grant_id = m.get('GrantId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeOwnerBid') is not None:
            self.node_owner_bid = m.get('NodeOwnerBid')
        if m.get('NodeOwnerUid') is not None:
            self.node_owner_uid = m.get('NodeOwnerUid')
        if m.get('NodeRegionId') is not None:
            self.node_region_id = m.get('NodeRegionId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceGrantedToExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 ecr_granted_instance_list=None, http_status_code=None, max_results=None, message=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.ecr_granted_instance_list = ecr_granted_instance_list  # type: list[DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList]
        self.http_status_code = http_status_code  # type: int
        self.max_results = max_results  # type: int
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ecr_granted_instance_list:
            for k in self.ecr_granted_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceGrantedToExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['EcrGrantedInstanceList'] = []
        if self.ecr_granted_instance_list is not None:
            for k in self.ecr_granted_instance_list:
                result['EcrGrantedInstanceList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.ecr_granted_instance_list = []
        if m.get('EcrGrantedInstanceList') is not None:
            for k in m.get('EcrGrantedInstanceList'):
                temp_model = DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList()
                self.ecr_granted_instance_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstanceGrantedToExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceGrantedToExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceGrantedToExpressConnectRouterResponse, self).to_map()
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
            temp_model = DescribeInstanceGrantedToExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(self, child_instance_id=None, child_instance_type=None, client_token=None, dry_run=None,
                 ecr_id=None):
        self.child_instance_id = child_instance_id  # type: str
        self.child_instance_type = child_instance_type  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachExpressConnectRouterChildInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DetachExpressConnectRouterChildInstanceResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachExpressConnectRouterChildInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachExpressConnectRouterChildInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachExpressConnectRouterChildInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachExpressConnectRouterChildInstanceResponse, self).to_map()
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
            temp_model = DetachExpressConnectRouterChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(self, client_token=None, destination_cidr_block=None, dry_run=None, ecr_id=None,
                 nexthop_instance_id=None):
        self.client_token = client_token  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.nexthop_instance_id = nexthop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableExpressConnectRouterRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        return self


class DisableExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableExpressConnectRouterRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableExpressConnectRouterRouteEntriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableExpressConnectRouterRouteEntriesResponse, self).to_map()
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
            temp_model = DisableExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(self, client_token=None, destination_cidr_block=None, dry_run=None, ecr_id=None,
                 nexthop_instance_id=None):
        self.client_token = client_token  # type: str
        self.destination_cidr_block = destination_cidr_block  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.nexthop_instance_id = nexthop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableExpressConnectRouterRouteEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        return self


class EnableExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableExpressConnectRouterRouteEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableExpressConnectRouterRouteEntriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableExpressConnectRouterRouteEntriesResponse, self).to_map()
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
            temp_model = EnableExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceDeleteExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceDeleteExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class ForceDeleteExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceDeleteExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ForceDeleteExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ForceDeleteExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ForceDeleteExpressConnectRouterResponse, self).to_map()
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
            temp_model = ForceDeleteExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class GetExpressConnectRouterResponseBodyTags(TeaModel):
    def __init__(self, ali_uid=None, category=None, id=None, region_no=None, resource_id=None, resuorce_type=None,
                 scope=None, tag_key=None, tag_value=None):
        self.ali_uid = ali_uid  # type: long
        self.category = category  # type: int
        self.id = id  # type: long
        self.region_no = region_no  # type: str
        self.resource_id = resource_id  # type: str
        self.resuorce_type = resuorce_type  # type: str
        self.scope = scope  # type: int
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExpressConnectRouterResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resuorce_type is not None:
            result['ResuorceType'] = self.resuorce_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResuorceType') is not None:
            self.resuorce_type = m.get('ResuorceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, alibaba_side_asn=None, biz_status=None, code=None,
                 description=None, dynamic_code=None, dynamic_message=None, ecr_id=None, gmt_create=None, gmt_modified=None,
                 http_status_code=None, message=None, name=None, owner_id=None, request_id=None, resource_group_id=None, status=None,
                 success=None, tags=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.alibaba_side_asn = alibaba_side_asn  # type: long
        self.biz_status = biz_status  # type: str
        self.code = code  # type: str
        self.description = description  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.ecr_id = ecr_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool
        self.tags = tags  # type: list[GetExpressConnectRouterResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetExpressConnectRouterResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExpressConnectRouterResponse, self).to_map()
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
            temp_model = GetExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantInstanceToExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, ecr_owner_ali_uid=None, instance_id=None,
                 instance_region_id=None, instance_type=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.ecr_owner_ali_uid = ecr_owner_ali_uid  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_region_id = instance_region_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantInstanceToExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.ecr_owner_ali_uid is not None:
            result['EcrOwnerAliUid'] = self.ecr_owner_ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('EcrOwnerAliUid') is not None:
            self.ecr_owner_ali_uid = m.get('EcrOwnerAliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class GrantInstanceToExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantInstanceToExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantInstanceToExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantInstanceToExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantInstanceToExpressConnectRouterResponse, self).to_map()
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
            temp_model = GrantInstanceToExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExpressConnectRouterSupportedRegionRequest(TeaModel):
    def __init__(self, client_token=None, node_type=None):
        self.client_token = client_token  # type: str
        self.node_type = node_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExpressConnectRouterSupportedRegionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class ListExpressConnectRouterSupportedRegionResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None,
                 supported_region_id_list=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.supported_region_id_list = supported_region_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExpressConnectRouterSupportedRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.supported_region_id_list is not None:
            result['SupportedRegionIdList'] = self.supported_region_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SupportedRegionIdList') is not None:
            self.supported_region_id_list = m.get('SupportedRegionIdList')
        return self


class ListExpressConnectRouterSupportedRegionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExpressConnectRouterSupportedRegionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExpressConnectRouterSupportedRegionResponse, self).to_map()
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
            temp_model = ListExpressConnectRouterSupportedRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, ecr_id=None, name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyExpressConnectRouterResponse, self).to_map()
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
            temp_model = ModifyExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExpressConnectRouterAssociationAllowedPrefixRequest(TeaModel):
    def __init__(self, allowed_prefixes=None, association_id=None, client_token=None, dry_run=None, ecr_id=None,
                 owner_account=None):
        self.allowed_prefixes = allowed_prefixes  # type: list[str]
        self.association_id = association_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.owner_account = owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyExpressConnectRouterAssociationAllowedPrefixRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyExpressConnectRouterAssociationAllowedPrefixResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyExpressConnectRouterAssociationAllowedPrefixResponse, self).to_map()
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
            temp_model = ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList(TeaModel):
    def __init__(self, mode=None, region_id=None):
        self.mode = mode  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyExpressConnectRouterInterRegionTransitModeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, transit_mode_list=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.transit_mode_list = transit_mode_list  # type: list[ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList]

    def validate(self):
        if self.transit_mode_list:
            for k in self.transit_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyExpressConnectRouterInterRegionTransitModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        result['TransitModeList'] = []
        if self.transit_mode_list is not None:
            for k in self.transit_mode_list:
                result['TransitModeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        self.transit_mode_list = []
        if m.get('TransitModeList') is not None:
            for k in m.get('TransitModeList'):
                temp_model = ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList()
                self.transit_mode_list.append(temp_model.from_map(k))
        return self


class ModifyExpressConnectRouterInterRegionTransitModeResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyExpressConnectRouterInterRegionTransitModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyExpressConnectRouterInterRegionTransitModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyExpressConnectRouterInterRegionTransitModeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyExpressConnectRouterInterRegionTransitModeResponse, self).to_map()
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
            temp_model = ModifyExpressConnectRouterInterRegionTransitModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeInstanceFromExpressConnectRouterRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None, ecr_owner_ali_uid=None, instance_id=None,
                 instance_region_id=None, instance_type=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str
        self.ecr_owner_ali_uid = ecr_owner_ali_uid  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_region_id = instance_region_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeInstanceFromExpressConnectRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.ecr_owner_ali_uid is not None:
            result['EcrOwnerAliUid'] = self.ecr_owner_ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('EcrOwnerAliUid') is not None:
            self.ecr_owner_ali_uid = m.get('EcrOwnerAliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class RevokeInstanceFromExpressConnectRouterResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeInstanceFromExpressConnectRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeInstanceFromExpressConnectRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeInstanceFromExpressConnectRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeInstanceFromExpressConnectRouterResponse, self).to_map()
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
            temp_model = RevokeInstanceFromExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SynchronizeExpressConnectRouterInterRegionBandwidthRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, ecr_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ecr_id = ecr_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SynchronizeExpressConnectRouterInterRegionBandwidthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody(TeaModel):
    def __init__(self, access_denied_detail=None, code=None, dynamic_code=None, dynamic_message=None,
                 http_status_code=None, message=None, request_id=None, success=None):
        self.access_denied_detail = access_denied_detail  # type: str
        self.code = code  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SynchronizeExpressConnectRouterInterRegionBandwidthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SynchronizeExpressConnectRouterInterRegionBandwidthResponse, self).to_map()
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
            temp_model = SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


