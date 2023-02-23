# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddCloudConnectorGatewayPrivilegeRequest(TeaModel):
    def __init__(self, io_tcloud_connector_gateway_id=None, region_id=None, user_ali_uid=None):
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.region_id = region_id  # type: str
        self.user_ali_uid = user_ali_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCloudConnectorGatewayPrivilegeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        return self


class AddCloudConnectorGatewayPrivilegeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCloudConnectorGatewayPrivilegeResponseBody, self).to_map()
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
        return self


class AddCloudConnectorGatewayPrivilegeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddCloudConnectorGatewayPrivilegeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCloudConnectorGatewayPrivilegeResponse, self).to_map()
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
            temp_model = AddCloudConnectorGatewayPrivilegeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIpToConnectionPoolFromExcelRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, cciot_id=None, connection_pool_id=None, ip_oss_excel_name=None,
                 isp=None, region_id=None, status=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.cciot_id = cciot_id  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.ip_oss_excel_name = ip_oss_excel_name  # type: str
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpToConnectionPoolFromExcelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.cciot_id is not None:
            result['CciotId'] = self.cciot_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip_oss_excel_name is not None:
            result['IpOssExcelName'] = self.ip_oss_excel_name
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('CciotId') is not None:
            self.cciot_id = m.get('CciotId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('IpOssExcelName') is not None:
            self.ip_oss_excel_name = m.get('IpOssExcelName')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class AddIpToConnectionPoolFromExcelResponseBody(TeaModel):
    def __init__(self, asyn_token=None, code=None, message=None, request_id=None, success=None):
        self.asyn_token = asyn_token  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpToConnectionPoolFromExcelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asyn_token is not None:
            result['AsynToken'] = self.asyn_token
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsynToken') is not None:
            self.asyn_token = m.get('AsynToken')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddIpToConnectionPoolFromExcelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddIpToConnectionPoolFromExcelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIpToConnectionPoolFromExcelResponse, self).to_map()
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
            temp_model = AddIpToConnectionPoolFromExcelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateIpsRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, client_token=None, dry_run=None, ip_count=None, ips=None, isp=None,
                 region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.ip_count = ip_count  # type: int
        self.ips = ips  # type: list[str]
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AllocateIpsResponseBody(TeaModel):
    def __init__(self, asyn_token=None, code=None, message=None, request_id=None, success=None):
        self.asyn_token = asyn_token  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocateIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asyn_token is not None:
            result['AsynToken'] = self.asyn_token
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsynToken') is not None:
            self.asyn_token = m.get('AsynToken')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AllocateIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocateIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocateIpsResponse, self).to_map()
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
            temp_model = AllocateIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateIccidToIpRequestIccidIpList(TeaModel):
    def __init__(self, card_type=None, iccid=None, ip=None):
        self.card_type = card_type  # type: str
        self.iccid = iccid  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateIccidToIpRequestIccidIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class AssociateIccidToIpRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, client_token=None, iccid_ip_list=None, isp=None, region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.iccid_ip_list = iccid_ip_list  # type: list[AssociateIccidToIpRequestIccidIpList]
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.iccid_ip_list:
            for k in self.iccid_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateIccidToIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['IccidIpList'] = []
        if self.iccid_ip_list is not None:
            for k in self.iccid_ip_list:
                result['IccidIpList'].append(k.to_map() if k else None)
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.iccid_ip_list = []
        if m.get('IccidIpList') is not None:
            for k in m.get('IccidIpList'):
                temp_model = AssociateIccidToIpRequestIccidIpList()
                self.iccid_ip_list.append(temp_model.from_map(k))
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateIccidToIpResponseBodyErrorIpList(TeaModel):
    def __init__(self, cause=None, ip=None):
        self.cause = cause  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateIccidToIpResponseBodyErrorIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class AssociateIccidToIpResponseBody(TeaModel):
    def __init__(self, code=None, error_ip_list=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_ip_list = error_ip_list  # type: list[AssociateIccidToIpResponseBodyErrorIpList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.error_ip_list:
            for k in self.error_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateIccidToIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['ErrorIpList'] = []
        if self.error_ip_list is not None:
            for k in self.error_ip_list:
                result['ErrorIpList'].append(k.to_map() if k else None)
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
        self.error_ip_list = []
        if m.get('ErrorIpList') is not None:
            for k in m.get('ErrorIpList'):
                temp_model = AssociateIccidToIpResponseBodyErrorIpList()
                self.error_ip_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssociateIccidToIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateIccidToIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateIccidToIpResponse, self).to_map()
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
            temp_model = AssociateIccidToIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateIccidToIpExcelRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, client_token=None, iccid_ips_file_url_list=None, isp=None,
                 region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.iccid_ips_file_url_list = iccid_ips_file_url_list  # type: list[str]
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateIccidToIpExcelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.iccid_ips_file_url_list is not None:
            result['IccidIpsFileUrlList'] = self.iccid_ips_file_url_list
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IccidIpsFileUrlList') is not None:
            self.iccid_ips_file_url_list = m.get('IccidIpsFileUrlList')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateIccidToIpExcelResponseBody(TeaModel):
    def __init__(self, asyn_token=None, code=None, message=None, request_id=None, success=None):
        self.asyn_token = asyn_token  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateIccidToIpExcelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asyn_token is not None:
            result['AsynToken'] = self.asyn_token
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsynToken') is not None:
            self.asyn_token = m.get('AsynToken')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssociateIccidToIpExcelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateIccidToIpExcelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateIccidToIpExcelResponse, self).to_map()
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
            temp_model = AssociateIccidToIpExcelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCloudConnectorGatewayPrivilegeRequest(TeaModel):
    def __init__(self, io_tcloud_connector_gateway_id=None, region_id=None, user_ali_uid=None):
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.region_id = region_id  # type: str
        self.user_ali_uid = user_ali_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCloudConnectorGatewayPrivilegeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        return self


class DeleteCloudConnectorGatewayPrivilegeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCloudConnectorGatewayPrivilegeResponseBody, self).to_map()
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
        return self


class DeleteCloudConnectorGatewayPrivilegeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCloudConnectorGatewayPrivilegeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCloudConnectorGatewayPrivilegeResponse, self).to_map()
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
            temp_model = DeleteCloudConnectorGatewayPrivilegeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeIpCountRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, isp=None, region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeIpCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetFreeIpCountResponseBody(TeaModel):
    def __init__(self, code=None, count=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeIpCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
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
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeIpCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFreeIpCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFreeIpCountResponse, self).to_map()
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
            temp_model = GetFreeIpCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIccidAndIpRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, client_token=None, iccid=None, ip=None, isp=None, region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.iccid = iccid  # type: str
        self.ip = ip  # type: str
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIccidAndIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIccidAndIpResponseBody(TeaModel):
    def __init__(self, cciot_id=None, code=None, iccid=None, ip=None, message=None, request_id=None, status=None,
                 success=None):
        self.cciot_id = cciot_id  # type: str
        self.code = code  # type: str
        self.iccid = iccid  # type: str
        self.ip = ip  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIccidAndIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cciot_id is not None:
            result['CciotId'] = self.cciot_id
        if self.code is not None:
            result['Code'] = self.code
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CciotId') is not None:
            self.cciot_id = m.get('CciotId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIccidAndIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIccidAndIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIccidAndIpResponse, self).to_map()
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
            temp_model = GetIccidAndIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIoTCloudConnectorGatewayRequest(TeaModel):
    def __init__(self, io_tcloud_connector_gateway_id=None, region_id=None):
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIoTCloudConnectorGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIoTCloudConnectorGatewayResponseBody(TeaModel):
    def __init__(self, apn=None, description=None, feature_list=None, forwarding_unit_count=None,
                 forwarding_unit_ids=None, ha_mode=None, io_tcloud_connector_gateway_id=None, isp=None, name=None, request_id=None,
                 resource_uid=None, schedule_factor=None, spec=None, state=None, zone_list=None):
        self.apn = apn  # type: str
        self.description = description  # type: str
        self.feature_list = feature_list  # type: list[str]
        self.forwarding_unit_count = forwarding_unit_count  # type: int
        self.forwarding_unit_ids = forwarding_unit_ids  # type: list[str]
        self.ha_mode = ha_mode  # type: str
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.resource_uid = resource_uid  # type: long
        self.schedule_factor = schedule_factor  # type: dict[str, any]
        self.spec = spec  # type: str
        self.state = state  # type: str
        self.zone_list = zone_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIoTCloudConnectorGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list
        if self.forwarding_unit_count is not None:
            result['ForwardingUnitCount'] = self.forwarding_unit_count
        if self.forwarding_unit_ids is not None:
            result['ForwardingUnitIds'] = self.forwarding_unit_ids
        if self.ha_mode is not None:
            result['HaMode'] = self.ha_mode
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.schedule_factor is not None:
            result['ScheduleFactor'] = self.schedule_factor
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')
        if m.get('ForwardingUnitCount') is not None:
            self.forwarding_unit_count = m.get('ForwardingUnitCount')
        if m.get('ForwardingUnitIds') is not None:
            self.forwarding_unit_ids = m.get('ForwardingUnitIds')
        if m.get('HaMode') is not None:
            self.ha_mode = m.get('HaMode')
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('ScheduleFactor') is not None:
            self.schedule_factor = m.get('ScheduleFactor')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ZoneList') is not None:
            self.zone_list = m.get('ZoneList')
        return self


class GetIoTCloudConnectorGatewayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIoTCloudConnectorGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIoTCloudConnectorGatewayResponse, self).to_map()
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
            temp_model = GetIoTCloudConnectorGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIpStatusRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, ip=None, isp=None, region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.ip = ip  # type: str
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIpStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIpStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, status=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIpStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIpStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIpStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIpStatusResponse, self).to_map()
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
            temp_model = GetIpStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudConnectorGatewayPrivilegeRequest(TeaModel):
    def __init__(self, io_tcloud_connector_gateway_id=None, region_id=None):
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudConnectorGatewayPrivilegeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCloudConnectorGatewayPrivilegeResponseBodyIoTCloudConnectorGatewayPrivileges(TeaModel):
    def __init__(self, aliuid=None, type=None):
        self.aliuid = aliuid  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudConnectorGatewayPrivilegeResponseBodyIoTCloudConnectorGatewayPrivileges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCloudConnectorGatewayPrivilegeResponseBody(TeaModel):
    def __init__(self, code=None, io_tcloud_connector_gateway_id=None,
                 io_tcloud_connector_gateway_privileges=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.io_tcloud_connector_gateway_privileges = io_tcloud_connector_gateway_privileges  # type: list[ListCloudConnectorGatewayPrivilegeResponseBodyIoTCloudConnectorGatewayPrivileges]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.io_tcloud_connector_gateway_privileges:
            for k in self.io_tcloud_connector_gateway_privileges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCloudConnectorGatewayPrivilegeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        result['IoTCloudConnectorGatewayPrivileges'] = []
        if self.io_tcloud_connector_gateway_privileges is not None:
            for k in self.io_tcloud_connector_gateway_privileges:
                result['IoTCloudConnectorGatewayPrivileges'].append(k.to_map() if k else None)
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
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        self.io_tcloud_connector_gateway_privileges = []
        if m.get('IoTCloudConnectorGatewayPrivileges') is not None:
            for k in m.get('IoTCloudConnectorGatewayPrivileges'):
                temp_model = ListCloudConnectorGatewayPrivilegeResponseBodyIoTCloudConnectorGatewayPrivileges()
                self.io_tcloud_connector_gateway_privileges.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCloudConnectorGatewayPrivilegeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCloudConnectorGatewayPrivilegeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCloudConnectorGatewayPrivilegeResponse, self).to_map()
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
            temp_model = ListCloudConnectorGatewayPrivilegeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolIpRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, cciot_id=None, client_token=None, connection_pool_id=None,
                 ip=None, isp=None, page_id=None, page_size=None, region_id=None, status=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.cciot_id = cciot_id  # type: str
        self.client_token = client_token  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.ip = ip  # type: str
        self.isp = isp  # type: str
        self.page_id = page_id  # type: str
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.cciot_id is not None:
            result['CciotId'] = self.cciot_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.page_id is not None:
            result['PageId'] = self.page_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('CciotId') is not None:
            self.cciot_id = m.get('CciotId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConnectionPoolIpResponseBodyIpInfoList(TeaModel):
    def __init__(self, cciot_id=None, connection_pool_id=None, ip=None, status=None):
        self.cciot_id = cciot_id  # type: str
        self.connection_pool_id = connection_pool_id  # type: str
        self.ip = ip  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConnectionPoolIpResponseBodyIpInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cciot_id is not None:
            result['CciotId'] = self.cciot_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CciotId') is not None:
            self.cciot_id = m.get('CciotId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConnectionPoolIpResponseBody(TeaModel):
    def __init__(self, code=None, count=None, ip_info_list=None, message=None, page_id=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: long
        self.ip_info_list = ip_info_list  # type: list[ListConnectionPoolIpResponseBodyIpInfoList]
        self.message = message  # type: str
        self.page_id = page_id  # type: str
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.ip_info_list:
            for k in self.ip_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConnectionPoolIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['IpInfoList'] = []
        if self.ip_info_list is not None:
            for k in self.ip_info_list:
                result['IpInfoList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_id is not None:
            result['PageId'] = self.page_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.ip_info_list = []
        if m.get('IpInfoList') is not None:
            for k in m.get('IpInfoList'):
                temp_model = ListConnectionPoolIpResponseBodyIpInfoList()
                self.ip_info_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListConnectionPoolIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConnectionPoolIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConnectionPoolIpResponse, self).to_map()
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
            temp_model = ListConnectionPoolIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGreInterfacesRequest(TeaModel):
    def __init__(self, gre_interface_id=None, io_tcloud_connector_gateway_id=None, region_id=None):
        self.gre_interface_id = gre_interface_id  # type: str
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGreInterfacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gre_interface_id is not None:
            result['GreInterfaceId'] = self.gre_interface_id
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GreInterfaceId') is not None:
            self.gre_interface_id = m.get('GreInterfaceId')
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListGreInterfacesResponseBodyGreInterface(TeaModel):
    def __init__(self, customer_ip=None, customer_tunnel_ip=None, enable_keepalive=None, forwarding_unit_id=None,
                 gre_cidrs=None, gre_gw_id=None, gre_interface_id=None, io_tcloud_connector_gateway_id=None, local_ip=None,
                 local_tunnel_ip=None, state=None):
        self.customer_ip = customer_ip  # type: str
        self.customer_tunnel_ip = customer_tunnel_ip  # type: str
        self.enable_keepalive = enable_keepalive  # type: bool
        self.forwarding_unit_id = forwarding_unit_id  # type: str
        self.gre_cidrs = gre_cidrs  # type: str
        self.gre_gw_id = gre_gw_id  # type: str
        self.gre_interface_id = gre_interface_id  # type: str
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.local_ip = local_ip  # type: str
        self.local_tunnel_ip = local_tunnel_ip  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGreInterfacesResponseBodyGreInterface, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_ip is not None:
            result['CustomerIp'] = self.customer_ip
        if self.customer_tunnel_ip is not None:
            result['CustomerTunnelIp'] = self.customer_tunnel_ip
        if self.enable_keepalive is not None:
            result['EnableKeepalive'] = self.enable_keepalive
        if self.forwarding_unit_id is not None:
            result['ForwardingUnitId'] = self.forwarding_unit_id
        if self.gre_cidrs is not None:
            result['GreCidrs'] = self.gre_cidrs
        if self.gre_gw_id is not None:
            result['GreGwId'] = self.gre_gw_id
        if self.gre_interface_id is not None:
            result['GreInterfaceId'] = self.gre_interface_id
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.local_ip is not None:
            result['LocalIp'] = self.local_ip
        if self.local_tunnel_ip is not None:
            result['LocalTunnelIp'] = self.local_tunnel_ip
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerIp') is not None:
            self.customer_ip = m.get('CustomerIp')
        if m.get('CustomerTunnelIp') is not None:
            self.customer_tunnel_ip = m.get('CustomerTunnelIp')
        if m.get('EnableKeepalive') is not None:
            self.enable_keepalive = m.get('EnableKeepalive')
        if m.get('ForwardingUnitId') is not None:
            self.forwarding_unit_id = m.get('ForwardingUnitId')
        if m.get('GreCidrs') is not None:
            self.gre_cidrs = m.get('GreCidrs')
        if m.get('GreGwId') is not None:
            self.gre_gw_id = m.get('GreGwId')
        if m.get('GreInterfaceId') is not None:
            self.gre_interface_id = m.get('GreInterfaceId')
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('LocalIp') is not None:
            self.local_ip = m.get('LocalIp')
        if m.get('LocalTunnelIp') is not None:
            self.local_tunnel_ip = m.get('LocalTunnelIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListGreInterfacesResponseBody(TeaModel):
    def __init__(self, gre_interface=None, io_tcloud_connector_gateway_id=None, request_id=None):
        self.gre_interface = gre_interface  # type: list[ListGreInterfacesResponseBodyGreInterface]
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.gre_interface:
            for k in self.gre_interface:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGreInterfacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GreInterface'] = []
        if self.gre_interface is not None:
            for k in self.gre_interface:
                result['GreInterface'].append(k.to_map() if k else None)
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.gre_interface = []
        if m.get('GreInterface') is not None:
            for k in m.get('GreInterface'):
                temp_model = ListGreInterfacesResponseBodyGreInterface()
                self.gre_interface.append(temp_model.from_map(k))
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGreInterfacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGreInterfacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGreInterfacesResponse, self).to_map()
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
            temp_model = ListGreInterfacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorGatewaysRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorGatewaysRequest, self).to_map()
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


class ListIoTCloudConnectorGatewaysResponseBodyIoTCloudConnectorGateways(TeaModel):
    def __init__(self, apn=None, description=None, feature_list=None, forwarding_unit_count=None,
                 forwarding_unit_ids=None, io_tcloud_connector_gateway_id=None, isp=None, name=None, resource_uid=None,
                 schedule_factor=None, spec=None, state=None, zone_list=None):
        self.apn = apn  # type: str
        self.description = description  # type: str
        self.feature_list = feature_list  # type: list[str]
        self.forwarding_unit_count = forwarding_unit_count  # type: int
        self.forwarding_unit_ids = forwarding_unit_ids  # type: list[str]
        self.io_tcloud_connector_gateway_id = io_tcloud_connector_gateway_id  # type: str
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.resource_uid = resource_uid  # type: long
        self.schedule_factor = schedule_factor  # type: dict[str, any]
        self.spec = spec  # type: str
        self.state = state  # type: str
        self.zone_list = zone_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIoTCloudConnectorGatewaysResponseBodyIoTCloudConnectorGateways, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.description is not None:
            result['Description'] = self.description
        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list
        if self.forwarding_unit_count is not None:
            result['ForwardingUnitCount'] = self.forwarding_unit_count
        if self.forwarding_unit_ids is not None:
            result['ForwardingUnitIds'] = self.forwarding_unit_ids
        if self.io_tcloud_connector_gateway_id is not None:
            result['IoTCloudConnectorGatewayId'] = self.io_tcloud_connector_gateway_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid
        if self.schedule_factor is not None:
            result['ScheduleFactor'] = self.schedule_factor
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')
        if m.get('ForwardingUnitCount') is not None:
            self.forwarding_unit_count = m.get('ForwardingUnitCount')
        if m.get('ForwardingUnitIds') is not None:
            self.forwarding_unit_ids = m.get('ForwardingUnitIds')
        if m.get('IoTCloudConnectorGatewayId') is not None:
            self.io_tcloud_connector_gateway_id = m.get('IoTCloudConnectorGatewayId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')
        if m.get('ScheduleFactor') is not None:
            self.schedule_factor = m.get('ScheduleFactor')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ZoneList') is not None:
            self.zone_list = m.get('ZoneList')
        return self


class ListIoTCloudConnectorGatewaysResponseBody(TeaModel):
    def __init__(self, io_tcloud_connector_gateways=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.io_tcloud_connector_gateways = io_tcloud_connector_gateways  # type: list[ListIoTCloudConnectorGatewaysResponseBodyIoTCloudConnectorGateways]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.io_tcloud_connector_gateways:
            for k in self.io_tcloud_connector_gateways:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorGatewaysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IoTCloudConnectorGateways'] = []
        if self.io_tcloud_connector_gateways is not None:
            for k in self.io_tcloud_connector_gateways:
                result['IoTCloudConnectorGateways'].append(k.to_map() if k else None)
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
        self.io_tcloud_connector_gateways = []
        if m.get('IoTCloudConnectorGateways') is not None:
            for k in m.get('IoTCloudConnectorGateways'):
                temp_model = ListIoTCloudConnectorGatewaysResponseBodyIoTCloudConnectorGateways()
                self.io_tcloud_connector_gateways.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIoTCloudConnectorGatewaysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIoTCloudConnectorGatewaysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIoTCloudConnectorGatewaysResponse, self).to_map()
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
            temp_model = ListIoTCloudConnectorGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpsStatusRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, ips=None, isp=None, region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.ips = ips  # type: list[str]
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpsStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIpsStatusResponseBodyIps(TeaModel):
    def __init__(self, ip=None, status=None):
        self.ip = ip  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpsStatusResponseBodyIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListIpsStatusResponseBody(TeaModel):
    def __init__(self, code=None, ips=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.ips = ips  # type: list[ListIpsStatusResponseBodyIps]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIpsStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
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
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = ListIpsStatusResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIpsStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIpsStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIpsStatusResponse, self).to_map()
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
            temp_model = ListIpsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResultTokenUrlRequest(TeaModel):
    def __init__(self, asyn_token=None, region_id=None):
        self.asyn_token = asyn_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResultTokenUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asyn_token is not None:
            result['AsynToken'] = self.asyn_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsynToken') is not None:
            self.asyn_token = m.get('AsynToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListResultTokenUrlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, oss_urls=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.oss_urls = oss_urls  # type: list[str]
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResultTokenUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.oss_urls is not None:
            result['OssUrls'] = self.oss_urls
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OssUrls') is not None:
            self.oss_urls = m.get('OssUrls')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListResultTokenUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResultTokenUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResultTokenUrlResponse, self).to_map()
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
            temp_model = ListResultTokenUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpStatusRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, client_token=None, ip_list=None, isp=None, region_id=None,
                 status=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.ip_list = ip_list  # type: list[str]
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyIpStatusResponseBodyErrorIpList(TeaModel):
    def __init__(self, cause=None, ip=None):
        self.cause = cause  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpStatusResponseBodyErrorIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class ModifyIpStatusResponseBody(TeaModel):
    def __init__(self, code=None, error_ip_list=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_ip_list = error_ip_list  # type: list[ModifyIpStatusResponseBodyErrorIpList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.error_ip_list:
            for k in self.error_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyIpStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['ErrorIpList'] = []
        if self.error_ip_list is not None:
            for k in self.error_ip_list:
                result['ErrorIpList'].append(k.to_map() if k else None)
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
        self.error_ip_list = []
        if m.get('ErrorIpList') is not None:
            for k in m.get('ErrorIpList'):
                temp_model = ModifyIpStatusResponseBodyErrorIpList()
                self.error_ip_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyIpStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIpStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIpStatusResponse, self).to_map()
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
            temp_model = ModifyIpStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAsynTokenResultRequest(TeaModel):
    def __init__(self, asyn_token=None, region_id=None):
        self.asyn_token = asyn_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAsynTokenResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asyn_token is not None:
            result['AsynToken'] = self.asyn_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsynToken') is not None:
            self.asyn_token = m.get('AsynToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryAsynTokenResultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None, status=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str
        self.status = status  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAsynTokenResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAsynTokenResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAsynTokenResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAsynTokenResultResponse, self).to_map()
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
            temp_model = QueryAsynTokenResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchVpcRouteToBackUpZoneRequest(TeaModel):
    def __init__(self, cciot_gw_id=None, client_token=None, dry_run=None, gre_gw_id=None, gre_interface_id=None,
                 region_id=None):
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.gre_gw_id = gre_gw_id  # type: str
        self.gre_interface_id = gre_interface_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchVpcRouteToBackUpZoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.gre_gw_id is not None:
            result['GreGwId'] = self.gre_gw_id
        if self.gre_interface_id is not None:
            result['GreInterfaceId'] = self.gre_interface_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GreGwId') is not None:
            self.gre_gw_id = m.get('GreGwId')
        if m.get('GreInterfaceId') is not None:
            self.gre_interface_id = m.get('GreInterfaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SwitchVpcRouteToBackUpZoneResponseBody(TeaModel):
    def __init__(self, asyn_token=None, code=None, message=None, request_id=None, success=None):
        self.asyn_token = asyn_token  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchVpcRouteToBackUpZoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asyn_token is not None:
            result['AsynToken'] = self.asyn_token
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsynToken') is not None:
            self.asyn_token = m.get('AsynToken')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SwitchVpcRouteToBackUpZoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchVpcRouteToBackUpZoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchVpcRouteToBackUpZoneResponse, self).to_map()
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
            temp_model = SwitchVpcRouteToBackUpZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnAssociateIccidToIpRequestIccidIpList(TeaModel):
    def __init__(self, iccid=None, ip=None):
        self.iccid = iccid  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnAssociateIccidToIpRequestIccidIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class UnAssociateIccidToIpRequest(TeaModel):
    def __init__(self, apn=None, cciot_gw_id=None, client_token=None, iccid_ip_list=None, isp=None, region_id=None):
        self.apn = apn  # type: str
        self.cciot_gw_id = cciot_gw_id  # type: str
        self.client_token = client_token  # type: str
        self.iccid_ip_list = iccid_ip_list  # type: list[UnAssociateIccidToIpRequestIccidIpList]
        self.isp = isp  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.iccid_ip_list:
            for k in self.iccid_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnAssociateIccidToIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.cciot_gw_id is not None:
            result['CciotGwId'] = self.cciot_gw_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['IccidIpList'] = []
        if self.iccid_ip_list is not None:
            for k in self.iccid_ip_list:
                result['IccidIpList'].append(k.to_map() if k else None)
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('CciotGwId') is not None:
            self.cciot_gw_id = m.get('CciotGwId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.iccid_ip_list = []
        if m.get('IccidIpList') is not None:
            for k in m.get('IccidIpList'):
                temp_model = UnAssociateIccidToIpRequestIccidIpList()
                self.iccid_ip_list.append(temp_model.from_map(k))
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UnAssociateIccidToIpResponseBodyErrorIpList(TeaModel):
    def __init__(self, cause=None, ip=None):
        self.cause = cause  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnAssociateIccidToIpResponseBodyErrorIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class UnAssociateIccidToIpResponseBody(TeaModel):
    def __init__(self, code=None, error_ip_list=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_ip_list = error_ip_list  # type: list[UnAssociateIccidToIpResponseBodyErrorIpList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.error_ip_list:
            for k in self.error_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnAssociateIccidToIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['ErrorIpList'] = []
        if self.error_ip_list is not None:
            for k in self.error_ip_list:
                result['ErrorIpList'].append(k.to_map() if k else None)
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
        self.error_ip_list = []
        if m.get('ErrorIpList') is not None:
            for k in m.get('ErrorIpList'):
                temp_model = UnAssociateIccidToIpResponseBodyErrorIpList()
                self.error_ip_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnAssociateIccidToIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnAssociateIccidToIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnAssociateIccidToIpResponse, self).to_map()
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
            temp_model = UnAssociateIccidToIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


