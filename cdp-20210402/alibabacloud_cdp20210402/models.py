# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelOrderRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOrderRequest, self).to_map()
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


class CancelOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelOrderResponse, self).to_map()
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
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckClusterNameRequest(TeaModel):
    def __init__(self, cluster_name=None):
        self.cluster_name = cluster_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckClusterNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class CheckClusterNameResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckClusterNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckClusterNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckClusterNameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckClusterNameResponse, self).to_map()
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
            temp_model = CheckClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmNoticeRequest(TeaModel):
    def __init__(self, cluster_biz_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmNoticeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class ConfirmNoticeResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmNoticeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmNoticeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmNoticeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmNoticeResponse, self).to_map()
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
            temp_model = ConfirmNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, client_token=None, cluster_info=None):
        self.client_token = client_token  # type: str
        self.cluster_info = cluster_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: str
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterDetailRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, instance_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetClusterDetailResponseBodyData(TeaModel):
    def __init__(self, auto_renew=None, begin_time=None, cluster_biz_id=None, cluster_id=None, cluster_name=None,
                 cluster_status=None, cluster_status_value=None, cluster_type=None, control_center_url=None, deploy_mode=None,
                 duration=None, expire_time=None, gmt_create=None, gmt_modified=None, instance_conf=None,
                 notice_confirmed=None, order_biz_id=None, package_type=None, pricing_cycle=None, region_id=None, running_time=None,
                 version=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.begin_time = begin_time  # type: long
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_status = cluster_status  # type: str
        self.cluster_status_value = cluster_status_value  # type: int
        self.cluster_type = cluster_type  # type: str
        self.control_center_url = control_center_url  # type: str
        self.deploy_mode = deploy_mode  # type: str
        self.duration = duration  # type: int
        self.expire_time = expire_time  # type: long
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.instance_conf = instance_conf  # type: dict[str, any]
        self.notice_confirmed = notice_confirmed  # type: bool
        self.order_biz_id = order_biz_id  # type: str
        self.package_type = package_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.running_time = running_time  # type: long
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_conf is not None:
            result['InstanceConf'] = self.instance_conf
        if self.notice_confirmed is not None:
            result['NoticeConfirmed'] = self.notice_confirmed
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceConf') is not None:
            self.instance_conf = m.get('InstanceConf')
        if m.get('NoticeConfirmed') is not None:
            self.notice_confirmed = m.get('NoticeConfirmed')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetClusterDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: GetClusterDetailResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClusterDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterDetailResponse, self).to_map()
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
            temp_model = GetClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HasDefaultRoleResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HasDefaultRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasDefaultRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: HasDefaultRoleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HasDefaultRoleResponse, self).to_map()
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
            temp_model = HasDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeClouderaDataPlatformResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeClouderaDataPlatformResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitializeClouderaDataPlatformResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitializeClouderaDataPlatformResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeClouderaDataPlatformResponse, self).to_map()
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
            temp_model = InitializeClouderaDataPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDefaultComponentsRequest(TeaModel):
    def __init__(self, cluster_type=None, security_mode=None):
        self.cluster_type = cluster_type  # type: str
        self.security_mode = security_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDefaultComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')
        return self


class ListDefaultComponentsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[str]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDefaultComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDefaultComponentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDefaultComponentsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDefaultComponentsResponse, self).to_map()
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
            temp_model = ListDefaultComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeGroupConstraintsRequest(TeaModel):
    def __init__(self, cluster_type=None):
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeGroupConstraintsRequest, self).to_map()
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


class ListNodeGroupConstraintsResponseBodyData(TeaModel):
    def __init__(self, host_group_type=None, recommended_instance_types=None, available_data_disk_categories=None,
                 available_instance_types=None, available_system_disk_categories=None, default_data_disk_count=None,
                 default_data_disk_size=None, default_node_count=None, default_system_disk_size=None, max_data_disk_count=None,
                 max_data_disk_size=None, max_node_count=None, max_system_disk_size=None, min_data_disk_count=None,
                 min_data_disk_size=None, min_node_count=None, min_system_disk_size=None, node_group_name=None):
        self.host_group_type = host_group_type  # type: str
        self.recommended_instance_types = recommended_instance_types  # type: list[str]
        self.available_data_disk_categories = available_data_disk_categories  # type: list[str]
        self.available_instance_types = available_instance_types  # type: list[str]
        self.available_system_disk_categories = available_system_disk_categories  # type: list[str]
        self.default_data_disk_count = default_data_disk_count  # type: int
        self.default_data_disk_size = default_data_disk_size  # type: int
        self.default_node_count = default_node_count  # type: int
        self.default_system_disk_size = default_system_disk_size  # type: int
        self.max_data_disk_count = max_data_disk_count  # type: int
        self.max_data_disk_size = max_data_disk_size  # type: int
        self.max_node_count = max_node_count  # type: int
        self.max_system_disk_size = max_system_disk_size  # type: int
        self.min_data_disk_count = min_data_disk_count  # type: int
        self.min_data_disk_size = min_data_disk_size  # type: int
        self.min_node_count = min_node_count  # type: int
        self.min_system_disk_size = min_system_disk_size  # type: int
        self.node_group_name = node_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeGroupConstraintsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.recommended_instance_types is not None:
            result['RecommendedInstanceTypes'] = self.recommended_instance_types
        if self.available_data_disk_categories is not None:
            result['availableDataDiskCategories'] = self.available_data_disk_categories
        if self.available_instance_types is not None:
            result['availableInstanceTypes'] = self.available_instance_types
        if self.available_system_disk_categories is not None:
            result['availableSystemDiskCategories'] = self.available_system_disk_categories
        if self.default_data_disk_count is not None:
            result['defaultDataDiskCount'] = self.default_data_disk_count
        if self.default_data_disk_size is not None:
            result['defaultDataDiskSize'] = self.default_data_disk_size
        if self.default_node_count is not None:
            result['defaultNodeCount'] = self.default_node_count
        if self.default_system_disk_size is not None:
            result['defaultSystemDiskSize'] = self.default_system_disk_size
        if self.max_data_disk_count is not None:
            result['maxDataDiskCount'] = self.max_data_disk_count
        if self.max_data_disk_size is not None:
            result['maxDataDiskSize'] = self.max_data_disk_size
        if self.max_node_count is not None:
            result['maxNodeCount'] = self.max_node_count
        if self.max_system_disk_size is not None:
            result['maxSystemDiskSize'] = self.max_system_disk_size
        if self.min_data_disk_count is not None:
            result['minDataDiskCount'] = self.min_data_disk_count
        if self.min_data_disk_size is not None:
            result['minDataDiskSize'] = self.min_data_disk_size
        if self.min_node_count is not None:
            result['minNodeCount'] = self.min_node_count
        if self.min_system_disk_size is not None:
            result['minSystemDiskSize'] = self.min_system_disk_size
        if self.node_group_name is not None:
            result['nodeGroupName'] = self.node_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('RecommendedInstanceTypes') is not None:
            self.recommended_instance_types = m.get('RecommendedInstanceTypes')
        if m.get('availableDataDiskCategories') is not None:
            self.available_data_disk_categories = m.get('availableDataDiskCategories')
        if m.get('availableInstanceTypes') is not None:
            self.available_instance_types = m.get('availableInstanceTypes')
        if m.get('availableSystemDiskCategories') is not None:
            self.available_system_disk_categories = m.get('availableSystemDiskCategories')
        if m.get('defaultDataDiskCount') is not None:
            self.default_data_disk_count = m.get('defaultDataDiskCount')
        if m.get('defaultDataDiskSize') is not None:
            self.default_data_disk_size = m.get('defaultDataDiskSize')
        if m.get('defaultNodeCount') is not None:
            self.default_node_count = m.get('defaultNodeCount')
        if m.get('defaultSystemDiskSize') is not None:
            self.default_system_disk_size = m.get('defaultSystemDiskSize')
        if m.get('maxDataDiskCount') is not None:
            self.max_data_disk_count = m.get('maxDataDiskCount')
        if m.get('maxDataDiskSize') is not None:
            self.max_data_disk_size = m.get('maxDataDiskSize')
        if m.get('maxNodeCount') is not None:
            self.max_node_count = m.get('maxNodeCount')
        if m.get('maxSystemDiskSize') is not None:
            self.max_system_disk_size = m.get('maxSystemDiskSize')
        if m.get('minDataDiskCount') is not None:
            self.min_data_disk_count = m.get('minDataDiskCount')
        if m.get('minDataDiskSize') is not None:
            self.min_data_disk_size = m.get('minDataDiskSize')
        if m.get('minNodeCount') is not None:
            self.min_node_count = m.get('minNodeCount')
        if m.get('minSystemDiskSize') is not None:
            self.min_system_disk_size = m.get('minSystemDiskSize')
        if m.get('nodeGroupName') is not None:
            self.node_group_name = m.get('nodeGroupName')
        return self


class ListNodeGroupConstraintsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListNodeGroupConstraintsResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeGroupConstraintsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNodeGroupConstraintsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNodeGroupConstraintsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodeGroupConstraintsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeGroupConstraintsResponse, self).to_map()
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
            temp_model = ListNodeGroupConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(self, cluster_biz_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class ListNodesResponseBodyDataEcsNodeDtoList(TeaModel):
    def __init__(self, begin_time=None, cpu_count=None, disk_capacity=None, disk_count=None, disk_type=None,
                 expire_time=None, gmt_create=None, gmt_modified=None, index=None, instance_type=None, memory_size=None,
                 node_group_id=None, node_group_name=None, node_group_type=None, node_id=None, node_name=None,
                 node_resource_type=None, node_status=None, private_ip=None, public_ip=None, running_time=None, serial_number=None,
                 system_disk_capacity=None, system_disk_count=None, system_disk_type=None):
        self.begin_time = begin_time  # type: str
        self.cpu_count = cpu_count  # type: int
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.expire_time = expire_time  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.index = index  # type: int
        self.instance_type = instance_type  # type: str
        self.memory_size = memory_size  # type: int
        self.node_group_id = node_group_id  # type: str
        self.node_group_name = node_group_name  # type: str
        self.node_group_type = node_group_type  # type: str
        self.node_id = node_id  # type: str
        self.node_name = node_name  # type: str
        self.node_resource_type = node_resource_type  # type: str
        self.node_status = node_status  # type: str
        self.private_ip = private_ip  # type: str
        self.public_ip = public_ip  # type: str
        self.running_time = running_time  # type: long
        self.serial_number = serial_number  # type: str
        self.system_disk_capacity = system_disk_capacity  # type: int
        self.system_disk_count = system_disk_count  # type: int
        self.system_disk_type = system_disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyDataEcsNodeDtoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.index is not None:
            result['Index'] = self.index
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_resource_type is not None:
            result['NodeResourceType'] = self.node_resource_type
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        if self.system_disk_count is not None:
            result['SystemDiskCount'] = self.system_disk_count
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeResourceType') is not None:
            self.node_resource_type = m.get('NodeResourceType')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        if m.get('SystemDiskCount') is not None:
            self.system_disk_count = m.get('SystemDiskCount')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        return self


class ListNodesResponseBodyData(TeaModel):
    def __init__(self, create_time=None, ecs_node_dto_list=None, expire_time=None, instance_conf=None,
                 instance_id=None, instance_name=None):
        self.create_time = create_time  # type: long
        self.ecs_node_dto_list = ecs_node_dto_list  # type: list[ListNodesResponseBodyDataEcsNodeDtoList]
        self.expire_time = expire_time  # type: long
        self.instance_conf = instance_conf  # type: dict[str, any]
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str

    def validate(self):
        if self.ecs_node_dto_list:
            for k in self.ecs_node_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['EcsNodeDtoList'] = []
        if self.ecs_node_dto_list is not None:
            for k in self.ecs_node_dto_list:
                result['EcsNodeDtoList'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_conf is not None:
            result['InstanceConf'] = self.instance_conf
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.ecs_node_dto_list = []
        if m.get('EcsNodeDtoList') is not None:
            for k in m.get('EcsNodeDtoList'):
                temp_model = ListNodesResponseBodyDataEcsNodeDtoList()
                self.ecs_node_dto_list.append(temp_model.from_map(k))
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceConf') is not None:
            self.instance_conf = m.get('InstanceConf')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListNodesResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNodesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodesResponse, self).to_map()
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
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationsRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, parent_operation_node_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.parent_operation_node_id = parent_operation_node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.parent_operation_node_id is not None:
            result['ParentOperationNodeId'] = self.parent_operation_node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ParentOperationNodeId') is not None:
            self.parent_operation_node_id = m.get('ParentOperationNodeId')
        return self


class ListOperationsResponseBodyData(TeaModel):
    def __init__(self, end_time=None, has_child_operation_nodes=None, has_operation_task=None, operation_id=None,
                 operation_node_id=None, operation_node_name=None, start_time=None, status=None):
        self.end_time = end_time  # type: long
        self.has_child_operation_nodes = has_child_operation_nodes  # type: bool
        self.has_operation_task = has_operation_task  # type: bool
        self.operation_id = operation_id  # type: str
        self.operation_node_id = operation_node_id  # type: str
        self.operation_node_name = operation_node_name  # type: int
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.has_child_operation_nodes is not None:
            result['HasChildOperationNodes'] = self.has_child_operation_nodes
        if self.has_operation_task is not None:
            result['HasOperationTask'] = self.has_operation_task
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_node_id is not None:
            result['OperationNodeId'] = self.operation_node_id
        if self.operation_node_name is not None:
            result['OperationNodeName'] = self.operation_node_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HasChildOperationNodes') is not None:
            self.has_child_operation_nodes = m.get('HasChildOperationNodes')
        if m.get('HasOperationTask') is not None:
            self.has_operation_task = m.get('HasOperationTask')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationNodeId') is not None:
            self.operation_node_id = m.get('OperationNodeId')
        if m.get('OperationNodeName') is not None:
            self.operation_node_name = m.get('OperationNodeName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOperationsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListOperationsResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOperationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOperationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOperationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOperationsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOperationsResponse, self).to_map()
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
            temp_model = ListOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyData(TeaModel):
    def __init__(self, description=None, region_id=None, region_name=None):
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListRegionsResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZonesRequest, self).to_map()
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


class ListZonesResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[str]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListZonesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListZonesResponse, self).to_map()
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderRequest(TeaModel):
    def __init__(self, cluster_biz_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class QueryOrderResponseBodyData(TeaModel):
    def __init__(self, instance_ids=None, order_id=None, order_status=None, order_type=None):
        self.instance_ids = instance_ids  # type: list[str]
        self.order_id = order_id  # type: str
        self.order_status = order_status  # type: str
        self.order_type = order_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class QueryOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[QueryOrderResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrderResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrderResponse, self).to_map()
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
            temp_model = QueryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPriceRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, node_group_specs=None, pricing_cycle=None, region_id=None):
        self.duration = duration  # type: int
        self.instance_id = instance_id  # type: str
        self.node_group_specs = node_group_specs  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_specs is not None:
            result['NodeGroupSpecs'] = self.node_group_specs
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupSpecs') is not None:
            self.node_group_specs = m.get('NodeGroupSpecs')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryPriceResponseBodyDataEcsPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPriceResponseBodyDataEcsPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryPriceResponseBodyDataSoftPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPriceResponseBodyDataSoftPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryPriceResponseBodyData(TeaModel):
    def __init__(self, discount_price=None, ecs_price_info=None, soft_price_info=None, sum_price=None):
        self.discount_price = discount_price  # type: float
        self.ecs_price_info = ecs_price_info  # type: QueryPriceResponseBodyDataEcsPriceInfo
        self.soft_price_info = soft_price_info  # type: QueryPriceResponseBodyDataSoftPriceInfo
        self.sum_price = sum_price  # type: float

    def validate(self):
        if self.ecs_price_info:
            self.ecs_price_info.validate()
        if self.soft_price_info:
            self.soft_price_info.validate()

    def to_map(self):
        _map = super(QueryPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.ecs_price_info is not None:
            result['EcsPriceInfo'] = self.ecs_price_info.to_map()
        if self.soft_price_info is not None:
            result['SoftPriceInfo'] = self.soft_price_info.to_map()
        if self.sum_price is not None:
            result['SumPrice'] = self.sum_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('EcsPriceInfo') is not None:
            temp_model = QueryPriceResponseBodyDataEcsPriceInfo()
            self.ecs_price_info = temp_model.from_map(m['EcsPriceInfo'])
        if m.get('SoftPriceInfo') is not None:
            temp_model = QueryPriceResponseBodyDataSoftPriceInfo()
            self.soft_price_info = temp_model.from_map(m['SoftPriceInfo'])
        if m.get('SumPrice') is not None:
            self.sum_price = m.get('SumPrice')
        return self


class QueryPriceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: QueryPriceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPriceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPriceResponse, self).to_map()
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
            temp_model = QueryPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewOrderRequest(TeaModel):
    def __init__(self, cluster_biz_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class QueryRenewOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[long]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRenewOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRenewOrderResponse, self).to_map()
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
            temp_model = QueryRenewOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewPriceRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, instances=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.instances = instances  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instances is not None:
            result['Instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        return self


class QueryRenewPriceResponseBodyDataCdpSoftPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewPriceResponseBodyDataCdpSoftPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryRenewPriceResponseBodyDataEcsPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewPriceResponseBodyDataEcsPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryRenewPriceResponseBodyData(TeaModel):
    def __init__(self, cdp_soft_price_info=None, discount_price=None, ecs_price_info=None, sum_price=None):
        self.cdp_soft_price_info = cdp_soft_price_info  # type: QueryRenewPriceResponseBodyDataCdpSoftPriceInfo
        self.discount_price = discount_price  # type: float
        self.ecs_price_info = ecs_price_info  # type: QueryRenewPriceResponseBodyDataEcsPriceInfo
        self.sum_price = sum_price  # type: float

    def validate(self):
        if self.cdp_soft_price_info:
            self.cdp_soft_price_info.validate()
        if self.ecs_price_info:
            self.ecs_price_info.validate()

    def to_map(self):
        _map = super(QueryRenewPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdp_soft_price_info is not None:
            result['CdpSoftPriceInfo'] = self.cdp_soft_price_info.to_map()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.ecs_price_info is not None:
            result['EcsPriceInfo'] = self.ecs_price_info.to_map()
        if self.sum_price is not None:
            result['SumPrice'] = self.sum_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdpSoftPriceInfo') is not None:
            temp_model = QueryRenewPriceResponseBodyDataCdpSoftPriceInfo()
            self.cdp_soft_price_info = temp_model.from_map(m['CdpSoftPriceInfo'])
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('EcsPriceInfo') is not None:
            temp_model = QueryRenewPriceResponseBodyDataEcsPriceInfo()
            self.ecs_price_info = temp_model.from_map(m['EcsPriceInfo'])
        if m.get('SumPrice') is not None:
            self.sum_price = m.get('SumPrice')
        return self


class QueryRenewPriceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: QueryRenewPriceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRenewPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRenewPriceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRenewPriceResponse, self).to_map()
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
            temp_model = QueryRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScaleUpOrderRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, instance_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryScaleUpOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[long]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScaleUpOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryScaleUpOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryScaleUpOrderResponse, self).to_map()
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
            temp_model = QueryScaleUpOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScaleUpPriceRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, core_number=None, duration=None, instance_id=None, instance_type=None,
                 node_group_type=None, pricing_cycle=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.core_number = core_number  # type: long
        self.duration = duration  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.node_group_type = node_group_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.core_number is not None:
            result['CoreNumber'] = self.core_number
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CoreNumber') is not None:
            self.core_number = m.get('CoreNumber')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class QueryScaleUpPriceResponseBodyDataEcsPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBodyDataEcsPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryScaleUpPriceResponseBodyDataSoftPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBodyDataSoftPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryScaleUpPriceResponseBodyData(TeaModel):
    def __init__(self, discount_price=None, ecs_price_info=None, soft_price_info=None, sum_price=None):
        self.discount_price = discount_price  # type: float
        self.ecs_price_info = ecs_price_info  # type: QueryScaleUpPriceResponseBodyDataEcsPriceInfo
        self.soft_price_info = soft_price_info  # type: QueryScaleUpPriceResponseBodyDataSoftPriceInfo
        self.sum_price = sum_price  # type: float

    def validate(self):
        if self.ecs_price_info:
            self.ecs_price_info.validate()
        if self.soft_price_info:
            self.soft_price_info.validate()

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.ecs_price_info is not None:
            result['EcsPriceInfo'] = self.ecs_price_info.to_map()
        if self.soft_price_info is not None:
            result['SoftPriceInfo'] = self.soft_price_info.to_map()
        if self.sum_price is not None:
            result['SumPrice'] = self.sum_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('EcsPriceInfo') is not None:
            temp_model = QueryScaleUpPriceResponseBodyDataEcsPriceInfo()
            self.ecs_price_info = temp_model.from_map(m['EcsPriceInfo'])
        if m.get('SoftPriceInfo') is not None:
            temp_model = QueryScaleUpPriceResponseBodyDataSoftPriceInfo()
            self.soft_price_info = temp_model.from_map(m['SoftPriceInfo'])
        if m.get('SumPrice') is not None:
            self.sum_price = m.get('SumPrice')
        return self


class QueryScaleUpPriceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: QueryScaleUpPriceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryScaleUpPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScaleUpPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryScaleUpPriceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryScaleUpPriceResponse, self).to_map()
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
            temp_model = QueryScaleUpPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseClusterRequest, self).to_map()
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


class ReleaseClusterResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseClusterResponse, self).to_map()
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
            temp_model = ReleaseClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, instances=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.instances = instances  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instances is not None:
            result['Instances'] = self.instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(self, order_ids=None):
        self.order_ids = order_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: RenewInstanceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RenewInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewInstanceResponse, self).to_map()
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleUpClusterRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, core_number=None, duration=None, instance_id=None, instance_type=None,
                 node_group_type=None, pricing_cycle=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.core_number = core_number  # type: long
        self.duration = duration  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.node_group_type = node_group_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleUpClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.core_number is not None:
            result['CoreNumber'] = self.core_number
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CoreNumber') is not None:
            self.core_number = m.get('CoreNumber')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class ScaleUpClusterResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleUpClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleUpClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScaleUpClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleUpClusterResponse, self).to_map()
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
            temp_model = ScaleUpClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchClusterInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, page_number=None, page_size=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchClusterInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchClusterInstancesResponseBodyDataClusterInstanceInfo(TeaModel):
    def __init__(self, control_center_login_name=None, control_center_url=None, sg_id=None, vpc_id=None,
                 vsw_id=None):
        self.control_center_login_name = control_center_login_name  # type: str
        self.control_center_url = control_center_url  # type: str
        self.sg_id = sg_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vsw_id = vsw_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBodyDataClusterInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_center_login_name is not None:
            result['ControlCenterLoginName'] = self.control_center_login_name
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlCenterLoginName') is not None:
            self.control_center_login_name = m.get('ControlCenterLoginName')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class SearchClusterInstancesResponseBodyDataEcsGroupList(TeaModel):
    def __init__(self, cpu_count=None, disk_capacity=None, disk_count=None, disk_type=None, host_group_name=None,
                 host_group_type=None, instance_type=None, memory_size=None, node_count=None, system_disk_capacity=None,
                 system_disk_count=None, system_disk_type=None):
        self.cpu_count = cpu_count  # type: int
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.host_group_name = host_group_name  # type: str
        self.host_group_type = host_group_type  # type: str
        self.instance_type = instance_type  # type: str
        self.memory_size = memory_size  # type: int
        self.node_count = node_count  # type: int
        self.system_disk_capacity = system_disk_capacity  # type: str
        self.system_disk_count = system_disk_count  # type: int
        self.system_disk_type = system_disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBodyDataEcsGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        if self.system_disk_count is not None:
            result['SystemDiskCount'] = self.system_disk_count
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        if m.get('SystemDiskCount') is not None:
            self.system_disk_count = m.get('SystemDiskCount')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        return self


class SearchClusterInstancesResponseBodyData(TeaModel):
    def __init__(self, begin_time=None, cluster_biz_id=None, cluster_id=None, cluster_instance_info=None,
                 cluster_name=None, cluster_status=None, cluster_status_value=None, cluster_type=None, control_center_url=None,
                 duration=None, ecs_group_list=None, expire_time=None, fail_reason=None, gmt_create=None, gmt_modified=None,
                 instance_conf=None, notice_confirmed=None, order_biz_id=None, package_type=None, pricing_cycle=None,
                 region_id=None, running_time=None, zone_id=None):
        self.begin_time = begin_time  # type: long
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_instance_info = cluster_instance_info  # type: SearchClusterInstancesResponseBodyDataClusterInstanceInfo
        self.cluster_name = cluster_name  # type: str
        self.cluster_status = cluster_status  # type: str
        self.cluster_status_value = cluster_status_value  # type: int
        self.cluster_type = cluster_type  # type: str
        self.control_center_url = control_center_url  # type: str
        self.duration = duration  # type: int
        self.ecs_group_list = ecs_group_list  # type: list[SearchClusterInstancesResponseBodyDataEcsGroupList]
        self.expire_time = expire_time  # type: long
        self.fail_reason = fail_reason  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.instance_conf = instance_conf  # type: dict[str, any]
        self.notice_confirmed = notice_confirmed  # type: bool
        self.order_biz_id = order_biz_id  # type: str
        self.package_type = package_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.region_id = region_id  # type: str
        self.running_time = running_time  # type: long
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.cluster_instance_info:
            self.cluster_instance_info.validate()
        if self.ecs_group_list:
            for k in self.ecs_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_instance_info is not None:
            result['ClusterInstanceInfo'] = self.cluster_instance_info.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.duration is not None:
            result['Duration'] = self.duration
        result['EcsGroupList'] = []
        if self.ecs_group_list is not None:
            for k in self.ecs_group_list:
                result['EcsGroupList'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_conf is not None:
            result['InstanceConf'] = self.instance_conf
        if self.notice_confirmed is not None:
            result['NoticeConfirmed'] = self.notice_confirmed
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInstanceInfo') is not None:
            temp_model = SearchClusterInstancesResponseBodyDataClusterInstanceInfo()
            self.cluster_instance_info = temp_model.from_map(m['ClusterInstanceInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.ecs_group_list = []
        if m.get('EcsGroupList') is not None:
            for k in m.get('EcsGroupList'):
                temp_model = SearchClusterInstancesResponseBodyDataEcsGroupList()
                self.ecs_group_list.append(temp_model.from_map(k))
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceConf') is not None:
            self.instance_conf = m.get('InstanceConf')
        if m.get('NoticeConfirmed') is not None:
            self.notice_confirmed = m.get('NoticeConfirmed')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchClusterInstancesResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: list[SearchClusterInstancesResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchClusterInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchClusterInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchClusterInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchClusterInstancesResponse, self).to_map()
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
            temp_model = SearchClusterInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleOrderRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleOrderRequest, self).to_map()
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


class SingleOrderResponseBodyDataEcsGroupList(TeaModel):
    def __init__(self, cpu_count=None, disk_capacity=None, disk_count=None, disk_type=None, host_group_name=None,
                 host_group_type=None, instance_type=None, memory_size=None, node_count=None, system_disk_capacity=None,
                 system_disk_count=None, system_disk_type=None):
        self.cpu_count = cpu_count  # type: int
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.host_group_name = host_group_name  # type: str
        self.host_group_type = host_group_type  # type: str
        self.instance_type = instance_type  # type: str
        self.memory_size = memory_size  # type: int
        self.node_count = node_count  # type: int
        self.system_disk_capacity = system_disk_capacity  # type: int
        self.system_disk_count = system_disk_count  # type: int
        self.system_disk_type = system_disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleOrderResponseBodyDataEcsGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        if self.system_disk_count is not None:
            result['SystemDiskCount'] = self.system_disk_count
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        if m.get('SystemDiskCount') is not None:
            self.system_disk_count = m.get('SystemDiskCount')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        return self


class SingleOrderResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, cluster_size=None, cluster_status=None, deploy_mode=None, duration=None,
                 ecs_group_list=None, instance_id=None, order_id=None, package_type=None, pricing_cycle=None, storage_size=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_size = cluster_size  # type: int
        self.cluster_status = cluster_status  # type: int
        self.deploy_mode = deploy_mode  # type: str
        self.duration = duration  # type: int
        self.ecs_group_list = ecs_group_list  # type: list[SingleOrderResponseBodyDataEcsGroupList]
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: str
        self.package_type = package_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.storage_size = storage_size  # type: int

    def validate(self):
        if self.ecs_group_list:
            for k in self.ecs_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SingleOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_size is not None:
            result['ClusterSize'] = self.cluster_size
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.duration is not None:
            result['Duration'] = self.duration
        result['EcsGroupList'] = []
        if self.ecs_group_list is not None:
            for k in self.ecs_group_list:
                result['EcsGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSize') is not None:
            self.cluster_size = m.get('ClusterSize')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.ecs_group_list = []
        if m.get('EcsGroupList') is not None:
            for k in m.get('EcsGroupList'):
                temp_model = SingleOrderResponseBodyDataEcsGroupList()
                self.ecs_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class SingleOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: SingleOrderResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SingleOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SingleOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SingleOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SingleOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SingleOrderResponse, self).to_map()
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
            temp_model = SingleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterNameRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, cluster_name=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_name = cluster_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class UpdateClusterNameResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateClusterNameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClusterNameResponse, self).to_map()
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
            temp_model = UpdateClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadLicenseResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: str
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class UploadLicenseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadLicenseResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadLicenseResponse, self).to_map()
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
            temp_model = UploadLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


