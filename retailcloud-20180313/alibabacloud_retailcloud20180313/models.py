# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddClusterNodeRequest(TeaModel):
    def __init__(self, cluster_instance_id=None, ecs_instance_id_list=None):
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.ecs_instance_id_list = ecs_instance_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClusterNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.ecs_instance_id_list is not None:
            result['EcsInstanceIdList'] = self.ecs_instance_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('EcsInstanceIdList') is not None:
            self.ecs_instance_id_list = m.get('EcsInstanceIdList')
        return self


class AddClusterNodeResponseBodyResult(TeaModel):
    def __init__(self, nonsense=None):
        self.nonsense = nonsense  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClusterNodeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonsense is not None:
            result['Nonsense'] = self.nonsense
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Nonsense') is not None:
            self.nonsense = m.get('Nonsense')
        return self


class AddClusterNodeResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AddClusterNodeResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AddClusterNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddClusterNodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddClusterNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddClusterNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddClusterNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddClusterNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocatePodConfigRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, request_id=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePodConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocatePodConfigResponseBodyResult(TeaModel):
    def __init__(self, config_data=None):
        self.config_data = config_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePodConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_data is not None:
            result['ConfigData'] = self.config_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigData') is not None:
            self.config_data = m.get('ConfigData')
        return self


class AllocatePodConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AllocatePodConfigResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AllocatePodConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AllocatePodConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AllocatePodConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocatePodConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocatePodConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AllocatePodConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddServersRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, sign=None, vpc_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.sign = sign  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddServersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class BatchAddServersResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddServersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchAddServersResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: BatchAddServersResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(BatchAddServersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = BatchAddServersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class BatchAddServersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchAddServersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchAddServersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchAddServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindGroupRequest(TeaModel):
    def __init__(self, app_id=None, biz_code=None, name=None):
        self.app_id = app_id  # type: long
        self.biz_code = biz_code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class BindGroupResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindGroupResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: BindGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(BindGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = BindGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class BindGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindNodeLabelRequest(TeaModel):
    def __init__(self, cluster_id=None, instance_id=None, label_key=None, label_value=None):
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindNodeLabelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class BindNodeLabelResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindNodeLabelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindNodeLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindNodeLabelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindNodeLabelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindNodeLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseDeployOrderRequest(TeaModel):
    def __init__(self, deploy_order_id=None):
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDeployOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class CloseDeployOrderResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseDeployOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseDeployOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseDeployOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseDeployOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloseDeployOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, account_type=None, db_instance_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.account_type = account_type  # type: str
        self.db_instance_id = db_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestUserRoles(TeaModel):
    def __init__(self, role_name=None, user_id=None, user_type=None):
        self.role_name = role_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequestUserRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, biz_code=None, biz_title=None, description=None, group_name=None, language=None,
                 middle_ware_id_list=None, namespace=None, operating_system=None, service_type=None, state_type=None, title=None,
                 user_roles=None):
        self.biz_code = biz_code  # type: str
        self.biz_title = biz_title  # type: str
        self.description = description  # type: str
        self.group_name = group_name  # type: str
        self.language = language  # type: str
        self.middle_ware_id_list = middle_ware_id_list  # type: list[int]
        self.namespace = namespace  # type: str
        self.operating_system = operating_system  # type: str
        self.service_type = service_type  # type: str
        self.state_type = state_type  # type: int
        self.title = title  # type: str
        self.user_roles = user_roles  # type: list[CreateAppRequestUserRoles]

    def validate(self):
        if self.user_roles:
            for k in self.user_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.biz_title is not None:
            result['BizTitle'] = self.biz_title
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.language is not None:
            result['Language'] = self.language
        if self.middle_ware_id_list is not None:
            result['MiddleWareIdList'] = self.middle_ware_id_list
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.operating_system is not None:
            result['OperatingSystem'] = self.operating_system
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.state_type is not None:
            result['StateType'] = self.state_type
        if self.title is not None:
            result['Title'] = self.title
        result['UserRoles'] = []
        if self.user_roles is not None:
            for k in self.user_roles:
                result['UserRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('BizTitle') is not None:
            self.biz_title = m.get('BizTitle')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MiddleWareIdList') is not None:
            self.middle_ware_id_list = m.get('MiddleWareIdList')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('OperatingSystem') is not None:
            self.operating_system = m.get('OperatingSystem')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('StateType') is not None:
            self.state_type = m.get('StateType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        self.user_roles = []
        if m.get('UserRoles') is not None:
            for k in m.get('UserRoles'):
                temp_model = CreateAppRequestUserRoles()
                self.user_roles.append(temp_model.from_map(k))
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateAppResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupRequest(TeaModel):
    def __init__(self, biz_code=None, name=None):
        self.biz_code = biz_code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateAppGroupResponseBodyResult(TeaModel):
    def __init__(self, app_group_id=None):
        self.app_group_id = app_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        return self


class CreateAppGroupResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateAppGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppMonitorsRequest(TeaModel):
    def __init__(self, alarm_template_id=None, app_ids=None, env_type=None, main_user_id=None, silence_time=None):
        self.alarm_template_id = alarm_template_id  # type: long
        self.app_ids = app_ids  # type: list[long]
        self.env_type = env_type  # type: int
        self.main_user_id = main_user_id  # type: long
        self.silence_time = silence_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppMonitorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_template_id is not None:
            result['AlarmTemplateId'] = self.alarm_template_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmTemplateId') is not None:
            self.alarm_template_id = m.get('AlarmTemplateId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        return self


class CreateAppMonitorsResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None, success=None):
        self.code = code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppMonitorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAppMonitorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppMonitorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppMonitorsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppMonitorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppResourceAllocRequest(TeaModel):
    def __init__(self, app_env_id=None, app_id=None, cluster_id=None):
        self.app_env_id = app_env_id  # type: long
        self.app_id = app_id  # type: long
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResourceAllocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateAppResourceAllocResponseBodyResult(TeaModel):
    def __init__(self, app_env_id=None, app_id=None, cluster_id=None, id=None, resource_def=None):
        self.app_env_id = app_env_id  # type: long
        self.app_id = app_id  # type: long
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: long
        self.resource_def = resource_def  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResourceAllocResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_def is not None:
            result['ResourceDef'] = self.resource_def
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceDef') is not None:
            self.resource_def = m.get('ResourceDef')
        return self


class CreateAppResourceAllocResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateAppResourceAllocResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateAppResourceAllocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAppResourceAllocResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAppResourceAllocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResourceAllocResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResourceAllocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppResourceAllocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, business_code=None, cloud_monitor_flags=None, cluster_env_type=None, cluster_id=None,
                 cluster_title=None, cluster_type=None, create_with_arms_integration=None, create_with_log_integration=None,
                 key_pair=None, net_plug=None, password=None, pod_cidr=None, private_zone=None, public_slb=None,
                 region_id=None, region_name=None, service_cidr=None, snat_entry=None, vpc_id=None, vswitchids=None):
        self.business_code = business_code  # type: str
        self.cloud_monitor_flags = cloud_monitor_flags  # type: int
        self.cluster_env_type = cluster_env_type  # type: str
        self.cluster_id = cluster_id  # type: long
        self.cluster_title = cluster_title  # type: str
        self.cluster_type = cluster_type  # type: str
        self.create_with_arms_integration = create_with_arms_integration  # type: bool
        self.create_with_log_integration = create_with_log_integration  # type: bool
        self.key_pair = key_pair  # type: str
        self.net_plug = net_plug  # type: str
        self.password = password  # type: str
        self.pod_cidr = pod_cidr  # type: str
        self.private_zone = private_zone  # type: bool
        self.public_slb = public_slb  # type: int
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str
        self.service_cidr = service_cidr  # type: str
        self.snat_entry = snat_entry  # type: int
        self.vpc_id = vpc_id  # type: str
        self.vswitchids = vswitchids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.cloud_monitor_flags is not None:
            result['CloudMonitorFlags'] = self.cloud_monitor_flags
        if self.cluster_env_type is not None:
            result['ClusterEnvType'] = self.cluster_env_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_title is not None:
            result['ClusterTitle'] = self.cluster_title
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_with_arms_integration is not None:
            result['CreateWithArmsIntegration'] = self.create_with_arms_integration
        if self.create_with_log_integration is not None:
            result['CreateWithLogIntegration'] = self.create_with_log_integration
        if self.key_pair is not None:
            result['KeyPair'] = self.key_pair
        if self.net_plug is not None:
            result['NetPlug'] = self.net_plug
        if self.password is not None:
            result['Password'] = self.password
        if self.pod_cidr is not None:
            result['PodCIDR'] = self.pod_cidr
        if self.private_zone is not None:
            result['PrivateZone'] = self.private_zone
        if self.public_slb is not None:
            result['PublicSlb'] = self.public_slb
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.service_cidr is not None:
            result['ServiceCIDR'] = self.service_cidr
        if self.snat_entry is not None:
            result['SnatEntry'] = self.snat_entry
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitchids is not None:
            result['Vswitchids'] = self.vswitchids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('CloudMonitorFlags') is not None:
            self.cloud_monitor_flags = m.get('CloudMonitorFlags')
        if m.get('ClusterEnvType') is not None:
            self.cluster_env_type = m.get('ClusterEnvType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterTitle') is not None:
            self.cluster_title = m.get('ClusterTitle')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateWithArmsIntegration') is not None:
            self.create_with_arms_integration = m.get('CreateWithArmsIntegration')
        if m.get('CreateWithLogIntegration') is not None:
            self.create_with_log_integration = m.get('CreateWithLogIntegration')
        if m.get('KeyPair') is not None:
            self.key_pair = m.get('KeyPair')
        if m.get('NetPlug') is not None:
            self.net_plug = m.get('NetPlug')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PodCIDR') is not None:
            self.pod_cidr = m.get('PodCIDR')
        if m.get('PrivateZone') is not None:
            self.private_zone = m.get('PrivateZone')
        if m.get('PublicSlb') is not None:
            self.public_slb = m.get('PublicSlb')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ServiceCIDR') is not None:
            self.service_cidr = m.get('ServiceCIDR')
        if m.get('SnatEntry') is not None:
            self.snat_entry = m.get('SnatEntry')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Vswitchids') is not None:
            self.vswitchids = m.get('Vswitchids')
        return self


class CreateClusterResponseBodyResult(TeaModel):
    def __init__(self, cluster_instance_id=None):
        self.cluster_instance_id = cluster_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateClusterResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateClusterResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class CreateDbRequest(TeaModel):
    def __init__(self, character_set_name=None, db_description=None, db_instance_id=None, db_name=None):
        self.character_set_name = character_set_name  # type: str
        self.db_description = db_description  # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.db_name = db_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class CreateDbResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDbResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDbResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeployConfigRequest(TeaModel):
    def __init__(self, app_id=None, code_path=None, config_map=None, config_map_list=None, cron_job=None,
                 deployment=None, env_type=None, name=None, secret_list=None, stateful_set=None):
        self.app_id = app_id  # type: long
        self.code_path = code_path  # type: str
        self.config_map = config_map  # type: str
        self.config_map_list = config_map_list  # type: list[str]
        self.cron_job = cron_job  # type: str
        self.deployment = deployment  # type: str
        self.env_type = env_type  # type: str
        self.name = name  # type: str
        self.secret_list = secret_list  # type: list[str]
        self.stateful_set = stateful_set  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeployConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code_path is not None:
            result['CodePath'] = self.code_path
        if self.config_map is not None:
            result['ConfigMap'] = self.config_map
        if self.config_map_list is not None:
            result['ConfigMapList'] = self.config_map_list
        if self.cron_job is not None:
            result['CronJob'] = self.cron_job
        if self.deployment is not None:
            result['Deployment'] = self.deployment
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.name is not None:
            result['Name'] = self.name
        if self.secret_list is not None:
            result['SecretList'] = self.secret_list
        if self.stateful_set is not None:
            result['StatefulSet'] = self.stateful_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CodePath') is not None:
            self.code_path = m.get('CodePath')
        if m.get('ConfigMap') is not None:
            self.config_map = m.get('ConfigMap')
        if m.get('ConfigMapList') is not None:
            self.config_map_list = m.get('ConfigMapList')
        if m.get('CronJob') is not None:
            self.cron_job = m.get('CronJob')
        if m.get('Deployment') is not None:
            self.deployment = m.get('Deployment')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecretList') is not None:
            self.secret_list = m.get('SecretList')
        if m.get('StatefulSet') is not None:
            self.stateful_set = m.get('StatefulSet')
        return self


class CreateDeployConfigResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, name=None, schema_id=None):
        self.app_id = app_id  # type: long
        self.name = name  # type: str
        self.schema_id = schema_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeployConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class CreateDeployConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_message=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateDeployConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateDeployConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateDeployConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateDeployConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDeployConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeployConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeployConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEciConfigRequest(TeaModel):
    def __init__(self, app_env_id=None, eip_bandwidth=None, enable_eci_schedule_policy=None, mirror_cache=None,
                 normal_instance_limit=None, schedule_virtual_node=None):
        self.app_env_id = app_env_id  # type: long
        self.eip_bandwidth = eip_bandwidth  # type: int
        self.enable_eci_schedule_policy = enable_eci_schedule_policy  # type: bool
        self.mirror_cache = mirror_cache  # type: bool
        self.normal_instance_limit = normal_instance_limit  # type: int
        self.schedule_virtual_node = schedule_virtual_node  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEciConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.enable_eci_schedule_policy is not None:
            result['EnableEciSchedulePolicy'] = self.enable_eci_schedule_policy
        if self.mirror_cache is not None:
            result['MirrorCache'] = self.mirror_cache
        if self.normal_instance_limit is not None:
            result['NormalInstanceLimit'] = self.normal_instance_limit
        if self.schedule_virtual_node is not None:
            result['ScheduleVirtualNode'] = self.schedule_virtual_node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EnableEciSchedulePolicy') is not None:
            self.enable_eci_schedule_policy = m.get('EnableEciSchedulePolicy')
        if m.get('MirrorCache') is not None:
            self.mirror_cache = m.get('MirrorCache')
        if m.get('NormalInstanceLimit') is not None:
            self.normal_instance_limit = m.get('NormalInstanceLimit')
        if m.get('ScheduleVirtualNode') is not None:
            self.schedule_virtual_node = m.get('ScheduleVirtualNode')
        return self


class CreateEciConfigResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEciConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEciConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateEciConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateEciConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateEciConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateEciConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEciConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEciConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEciConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(self, app_id=None, app_schema_id=None, cluster_id=None, env_name=None, env_type=None, region=None,
                 replicas=None):
        self.app_id = app_id  # type: long
        self.app_schema_id = app_schema_id  # type: long
        self.cluster_id = cluster_id  # type: str
        self.env_name = env_name  # type: str
        self.env_type = env_type  # type: int
        self.region = region  # type: str
        self.replicas = replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_schema_id is not None:
            result['AppSchemaId'] = self.app_schema_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.region is not None:
            result['Region'] = self.region
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSchemaId') is not None:
            self.app_schema_id = m.get('AppSchemaId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class CreateEnvironmentResponseBodyResult(TeaModel):
    def __init__(self, app_env_id=None):
        self.app_env_id = app_env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateEnvironmentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateEnvironmentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodeLabelRequest(TeaModel):
    def __init__(self, cluster_id=None, label_key=None, label_value=None):
        self.cluster_id = cluster_id  # type: str
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNodeLabelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class CreateNodeLabelResponseBodyResult(TeaModel):
    def __init__(self, cluster_id=None, id=None, label_key=None, label_value=None):
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: long
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNodeLabelResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class CreateNodeLabelResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateNodeLabelResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateNodeLabelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateNodeLabelResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNodeLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNodeLabelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNodeLabelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNodeLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePersistentVolumeRequest(TeaModel):
    def __init__(self, access_modes=None, capacity=None, cluster_instance_id=None, mount_dir=None,
                 mount_target_domain=None, nfsversion=None, name=None, nas_type=None, reclaim_policy=None, storage_class=None):
        self.access_modes = access_modes  # type: str
        self.capacity = capacity  # type: str
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.mount_dir = mount_dir  # type: str
        self.mount_target_domain = mount_target_domain  # type: str
        self.nfsversion = nfsversion  # type: str
        self.name = name  # type: str
        self.nas_type = nas_type  # type: str
        self.reclaim_policy = reclaim_policy  # type: str
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePersistentVolumeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['AccessModes'] = self.access_modes
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.nfsversion is not None:
            result['NFSVersion'] = self.nfsversion
        if self.name is not None:
            result['Name'] = self.name
        if self.nas_type is not None:
            result['NasType'] = self.nas_type
        if self.reclaim_policy is not None:
            result['ReclaimPolicy'] = self.reclaim_policy
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessModes') is not None:
            self.access_modes = m.get('AccessModes')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NFSVersion') is not None:
            self.nfsversion = m.get('NFSVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NasType') is not None:
            self.nas_type = m.get('NasType')
        if m.get('ReclaimPolicy') is not None:
            self.reclaim_policy = m.get('ReclaimPolicy')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class CreatePersistentVolumeResponseBodyResult(TeaModel):
    def __init__(self, persistent_volume_id=None):
        self.persistent_volume_id = persistent_volume_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePersistentVolumeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.persistent_volume_id is not None:
            result['PersistentVolumeId'] = self.persistent_volume_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PersistentVolumeId') is not None:
            self.persistent_volume_id = m.get('PersistentVolumeId')
        return self


class CreatePersistentVolumeResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreatePersistentVolumeResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreatePersistentVolumeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreatePersistentVolumeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreatePersistentVolumeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePersistentVolumeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePersistentVolumeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePersistentVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePersistentVolumeClaimRequest(TeaModel):
    def __init__(self, access_modes=None, app_id=None, capacity=None, env_id=None, name=None, storage_class=None):
        self.access_modes = access_modes  # type: str
        self.app_id = app_id  # type: long
        self.capacity = capacity  # type: str
        self.env_id = env_id  # type: long
        self.name = name  # type: str
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePersistentVolumeClaimRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['AccessModes'] = self.access_modes
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.name is not None:
            result['Name'] = self.name
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessModes') is not None:
            self.access_modes = m.get('AccessModes')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class CreatePersistentVolumeClaimResponseBodyResult(TeaModel):
    def __init__(self, persistent_volume_claim_id=None):
        self.persistent_volume_claim_id = persistent_volume_claim_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePersistentVolumeClaimResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.persistent_volume_claim_id is not None:
            result['PersistentVolumeClaimId'] = self.persistent_volume_claim_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PersistentVolumeClaimId') is not None:
            self.persistent_volume_claim_id = m.get('PersistentVolumeClaimId')
        return self


class CreatePersistentVolumeClaimResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreatePersistentVolumeClaimResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreatePersistentVolumeClaimResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreatePersistentVolumeClaimResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreatePersistentVolumeClaimResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePersistentVolumeClaimResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePersistentVolumeClaimResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePersistentVolumeClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestPortMappings(TeaModel):
    def __init__(self, name=None, node_port=None, port=None, protocol=None, target_port=None):
        self.name = name  # type: str
        self.node_port = node_port  # type: int
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.target_port = target_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequestPortMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, env_id=None, headless=None, k_8s_service_id=None, name=None, port_mappings=None,
                 service_type=None):
        self.env_id = env_id  # type: long
        self.headless = headless  # type: bool
        self.k_8s_service_id = k_8s_service_id  # type: str
        self.name = name  # type: str
        self.port_mappings = port_mappings  # type: list[CreateServiceRequestPortMappings]
        self.service_type = service_type  # type: str

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.headless is not None:
            result['Headless'] = self.headless
        if self.k_8s_service_id is not None:
            result['K8sServiceId'] = self.k_8s_service_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Headless') is not None:
            self.headless = m.get('Headless')
        if m.get('K8sServiceId') is not None:
            self.k_8s_service_id = m.get('K8sServiceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = CreateServiceRequestPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class CreateServiceResponseBodyResult(TeaModel):
    def __init__(self, service_id=None):
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateServiceResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateServiceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlbAPRequest(TeaModel):
    def __init__(self, cookie_timeout=None, env_id=None, established_timeout=None, listener_port=None, name=None,
                 protocol=None, real_server_port=None, slb_id=None, ssl_cert_id=None, sticky_session=None):
        self.cookie_timeout = cookie_timeout  # type: int
        self.env_id = env_id  # type: long
        self.established_timeout = established_timeout  # type: int
        self.listener_port = listener_port  # type: int
        self.name = name  # type: str
        self.protocol = protocol  # type: str
        self.real_server_port = real_server_port  # type: int
        self.slb_id = slb_id  # type: str
        self.ssl_cert_id = ssl_cert_id  # type: str
        self.sticky_session = sticky_session  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlbAPRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_server_port is not None:
            result['RealServerPort'] = self.real_server_port
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.ssl_cert_id is not None:
            result['SslCertId'] = self.ssl_cert_id
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServerPort') is not None:
            self.real_server_port = m.get('RealServerPort')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SslCertId') is not None:
            self.ssl_cert_id = m.get('SslCertId')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        return self


class CreateSlbAPResponseBodyResult(TeaModel):
    def __init__(self, slb_apid=None):
        self.slb_apid = slb_apid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlbAPResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_apid is not None:
            result['SlbAPId'] = self.slb_apid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlbAPId') is not None:
            self.slb_apid = m.get('SlbAPId')
        return self


class CreateSlbAPResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateSlbAPResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateSlbAPResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateSlbAPResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSlbAPResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSlbAPResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSlbAPResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSlbAPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppDetailRequest(TeaModel):
    def __init__(self, app_id=None, force=None):
        self.app_id = app_id  # type: long
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteAppDetailResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteAppDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteAppDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteAppDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteAppDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppEnvironmentRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, force=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteAppEnvironmentResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppEnvironmentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteAppEnvironmentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteAppEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteAppEnvironmentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteAppEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppGroupRequest(TeaModel):
    def __init__(self, force=None, group_id=None):
        self.force = force  # type: bool
        self.group_id = group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteAppGroupResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppGroupResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteAppGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteAppGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppResourceAllocRequest(TeaModel):
    def __init__(self, app_env_id=None):
        self.app_env_id = app_env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResourceAllocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        return self


class DeleteAppResourceAllocResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResourceAllocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppResourceAllocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppResourceAllocResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppResourceAllocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppResourceAllocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_instance_id=None):
        self.cluster_instance_id = cluster_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        return self


class DeleteClusterResponseBodyResult(TeaModel):
    def __init__(self, nonsense=None):
        self.nonsense = nonsense  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonsense is not None:
            result['Nonsense'] = self.nonsense
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Nonsense') is not None:
            self.nonsense = m.get('Nonsense')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteClusterResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteClusterResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabaseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DeleteDatabaseResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatabaseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDatabaseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDatabaseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDatabaseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeployConfigRequest(TeaModel):
    def __init__(self, schema_id=None):
        self.schema_id = schema_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeployConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class DeleteDeployConfigResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeployConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDeployConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteDeployConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteDeployConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteDeployConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteDeployConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDeployConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDeployConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDeployConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodeLabelRequest(TeaModel):
    def __init__(self, cluster_id=None, force=None, label_key=None, label_value=None):
        self.cluster_id = cluster_id  # type: str
        self.force = force  # type: bool
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodeLabelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.force is not None:
            result['Force'] = self.force
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class DeleteNodeLabelResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodeLabelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNodeLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNodeLabelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNodeLabelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNodeLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePersistentVolumeRequest(TeaModel):
    def __init__(self, cluster_instance_id=None, persistent_volume_name=None):
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.persistent_volume_name = persistent_volume_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePersistentVolumeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.persistent_volume_name is not None:
            result['PersistentVolumeName'] = self.persistent_volume_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('PersistentVolumeName') is not None:
            self.persistent_volume_name = m.get('PersistentVolumeName')
        return self


class DeletePersistentVolumeResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePersistentVolumeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePersistentVolumeResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeletePersistentVolumeResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeletePersistentVolumeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeletePersistentVolumeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeletePersistentVolumeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePersistentVolumeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePersistentVolumeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePersistentVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePersistentVolumeClaimRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, persistent_volume_claim_name=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.persistent_volume_claim_name = persistent_volume_claim_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePersistentVolumeClaimRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.persistent_volume_claim_name is not None:
            result['PersistentVolumeClaimName'] = self.persistent_volume_claim_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PersistentVolumeClaimName') is not None:
            self.persistent_volume_claim_name = m.get('PersistentVolumeClaimName')
        return self


class DeletePersistentVolumeClaimResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePersistentVolumeClaimResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePersistentVolumeClaimResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeletePersistentVolumeClaimResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeletePersistentVolumeClaimResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeletePersistentVolumeClaimResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeletePersistentVolumeClaimResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePersistentVolumeClaimResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePersistentVolumeClaimResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePersistentVolumeClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRdsAccountRequest(TeaModel):
    def __init__(self, account_name=None, db_instance_id=None):
        self.account_name = account_name  # type: str
        self.db_instance_id = db_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRdsAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        return self


class DeleteRdsAccountResponseBodyResult(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRdsAccountResponseBodyResult, self).to_map()
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


class DeleteRdsAccountResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteRdsAccountResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteRdsAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteRdsAccountResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteRdsAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRdsAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRdsAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRdsAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(self, service_id=None):
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSlbAPRequest(TeaModel):
    def __init__(self, slb_apid=None):
        self.slb_apid = slb_apid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSlbAPRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_apid is not None:
            result['SlbAPId'] = self.slb_apid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlbAPId') is not None:
            self.slb_apid = m.get('SlbAPId')
        return self


class DeleteSlbAPResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSlbAPResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSlbAPResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSlbAPResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSlbAPResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSlbAPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployAppRequest(TeaModel):
    def __init__(self, arms_flag=None, container_image_list=None, default_packet_of_app_group=None,
                 deploy_packet_id=None, deploy_packet_url=None, description=None, env_id=None, init_container_image_list=None,
                 name=None, pause_type=None, total_partitions=None, update_strategy_type=None):
        self.arms_flag = arms_flag  # type: bool
        self.container_image_list = container_image_list  # type: list[str]
        self.default_packet_of_app_group = default_packet_of_app_group  # type: str
        self.deploy_packet_id = deploy_packet_id  # type: long
        self.deploy_packet_url = deploy_packet_url  # type: str
        self.description = description  # type: str
        self.env_id = env_id  # type: long
        self.init_container_image_list = init_container_image_list  # type: list[str]
        self.name = name  # type: str
        self.pause_type = pause_type  # type: str
        self.total_partitions = total_partitions  # type: int
        self.update_strategy_type = update_strategy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arms_flag is not None:
            result['ArmsFlag'] = self.arms_flag
        if self.container_image_list is not None:
            result['ContainerImageList'] = self.container_image_list
        if self.default_packet_of_app_group is not None:
            result['DefaultPacketOfAppGroup'] = self.default_packet_of_app_group
        if self.deploy_packet_id is not None:
            result['DeployPacketId'] = self.deploy_packet_id
        if self.deploy_packet_url is not None:
            result['DeployPacketUrl'] = self.deploy_packet_url
        if self.description is not None:
            result['Description'] = self.description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.init_container_image_list is not None:
            result['InitContainerImageList'] = self.init_container_image_list
        if self.name is not None:
            result['Name'] = self.name
        if self.pause_type is not None:
            result['PauseType'] = self.pause_type
        if self.total_partitions is not None:
            result['TotalPartitions'] = self.total_partitions
        if self.update_strategy_type is not None:
            result['UpdateStrategyType'] = self.update_strategy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArmsFlag') is not None:
            self.arms_flag = m.get('ArmsFlag')
        if m.get('ContainerImageList') is not None:
            self.container_image_list = m.get('ContainerImageList')
        if m.get('DefaultPacketOfAppGroup') is not None:
            self.default_packet_of_app_group = m.get('DefaultPacketOfAppGroup')
        if m.get('DeployPacketId') is not None:
            self.deploy_packet_id = m.get('DeployPacketId')
        if m.get('DeployPacketUrl') is not None:
            self.deploy_packet_url = m.get('DeployPacketUrl')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('InitContainerImageList') is not None:
            self.init_container_image_list = m.get('InitContainerImageList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PauseType') is not None:
            self.pause_type = m.get('PauseType')
        if m.get('TotalPartitions') is not None:
            self.total_partitions = m.get('TotalPartitions')
        if m.get('UpdateStrategyType') is not None:
            self.update_strategy_type = m.get('UpdateStrategyType')
        return self


class DeployAppResponseBodyResult(TeaModel):
    def __init__(self, admitted=None, business_code=None, deploy_order_id=None):
        self.admitted = admitted  # type: bool
        self.business_code = business_code  # type: str
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admitted is not None:
            result['Admitted'] = self.admitted
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Admitted') is not None:
            self.admitted = m.get('Admitted')
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class DeployAppResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeployAppResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeployAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeployAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeployAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeployAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppDetailRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAppDetailResponseBodyResultMiddleWareInfoList(TeaModel):
    def __init__(self, app_id=None, code=None, name=None):
        self.app_id = app_id  # type: long
        self.code = code  # type: int
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppDetailResponseBodyResultMiddleWareInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAppDetailResponseBodyResultUserRoles(TeaModel):
    def __init__(self, real_name=None, role_name=None, user_id=None, user_type=None):
        self.real_name = real_name  # type: str
        self.role_name = role_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppDetailResponseBodyResultUserRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeAppDetailResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, app_state_type=None, biz_name=None, biz_title=None, deploy_type=None,
                 description=None, language=None, middle_ware_info_list=None, operating_system=None, service_type=None,
                 title=None, user_roles=None):
        self.app_id = app_id  # type: long
        self.app_state_type = app_state_type  # type: str
        self.biz_name = biz_name  # type: str
        self.biz_title = biz_title  # type: str
        self.deploy_type = deploy_type  # type: str
        self.description = description  # type: str
        self.language = language  # type: str
        self.middle_ware_info_list = middle_ware_info_list  # type: list[DescribeAppDetailResponseBodyResultMiddleWareInfoList]
        self.operating_system = operating_system  # type: str
        self.service_type = service_type  # type: str
        self.title = title  # type: str
        self.user_roles = user_roles  # type: list[DescribeAppDetailResponseBodyResultUserRoles]

    def validate(self):
        if self.middle_ware_info_list:
            for k in self.middle_ware_info_list:
                if k:
                    k.validate()
        if self.user_roles:
            for k in self.user_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_state_type is not None:
            result['AppStateType'] = self.app_state_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_title is not None:
            result['BizTitle'] = self.biz_title
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.language is not None:
            result['Language'] = self.language
        result['MiddleWareInfoList'] = []
        if self.middle_ware_info_list is not None:
            for k in self.middle_ware_info_list:
                result['MiddleWareInfoList'].append(k.to_map() if k else None)
        if self.operating_system is not None:
            result['OperatingSystem'] = self.operating_system
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.title is not None:
            result['Title'] = self.title
        result['UserRoles'] = []
        if self.user_roles is not None:
            for k in self.user_roles:
                result['UserRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppStateType') is not None:
            self.app_state_type = m.get('AppStateType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizTitle') is not None:
            self.biz_title = m.get('BizTitle')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        self.middle_ware_info_list = []
        if m.get('MiddleWareInfoList') is not None:
            for k in m.get('MiddleWareInfoList'):
                temp_model = DescribeAppDetailResponseBodyResultMiddleWareInfoList()
                self.middle_ware_info_list.append(temp_model.from_map(k))
        if m.get('OperatingSystem') is not None:
            self.operating_system = m.get('OperatingSystem')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        self.user_roles = []
        if m.get('UserRoles') is not None:
            for k in m.get('UserRoles'):
                temp_model = DescribeAppDetailResponseBodyResultUserRoles()
                self.user_roles.append(temp_model.from_map(k))
        return self


class DescribeAppDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_message=None, request_id=None, result=None):
        self.code = code  # type: long
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAppDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAppDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppEnvDeployBaselineRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppEnvDeployBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DescribeAppEnvDeployBaselineResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, create_time=None, env_id=None, packet_comment=None, packet_id=None,
                 packet_url=None, schema_id=None):
        self.app_id = app_id  # type: long
        self.create_time = create_time  # type: str
        self.env_id = env_id  # type: long
        self.packet_comment = packet_comment  # type: str
        self.packet_id = packet_id  # type: long
        self.packet_url = packet_url  # type: str
        self.schema_id = schema_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppEnvDeployBaselineResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.packet_comment is not None:
            result['PacketComment'] = self.packet_comment
        if self.packet_id is not None:
            result['PacketId'] = self.packet_id
        if self.packet_url is not None:
            result['PacketUrl'] = self.packet_url
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PacketComment') is not None:
            self.packet_comment = m.get('PacketComment')
        if m.get('PacketId') is not None:
            self.packet_id = m.get('PacketId')
        if m.get('PacketUrl') is not None:
            self.packet_url = m.get('PacketUrl')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        return self


class DescribeAppEnvDeployBaselineResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppEnvDeployBaselineResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppEnvDeployBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAppEnvDeployBaselineResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAppEnvDeployBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppEnvDeployBaselineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppEnvDeployBaselineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppEnvDeployBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppEnvironmentDetailRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppEnvironmentDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DescribeAppEnvironmentDetailResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, app_schema_id=None, env_id=None, env_name=None, env_type=None,
                 env_type_name=None, region=None, replicas=None):
        self.app_id = app_id  # type: long
        self.app_schema_id = app_schema_id  # type: long
        self.env_id = env_id  # type: long
        self.env_name = env_name  # type: str
        self.env_type = env_type  # type: int
        self.env_type_name = env_type_name  # type: str
        self.region = region  # type: str
        self.replicas = replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppEnvironmentDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_schema_id is not None:
            result['AppSchemaId'] = self.app_schema_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.env_type_name is not None:
            result['EnvTypeName'] = self.env_type_name
        if self.region is not None:
            result['Region'] = self.region
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSchemaId') is not None:
            self.app_schema_id = m.get('AppSchemaId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('EnvTypeName') is not None:
            self.env_type_name = m.get('EnvTypeName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class DescribeAppEnvironmentDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppEnvironmentDetailResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppEnvironmentDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAppEnvironmentDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeAppEnvironmentDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppEnvironmentDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppEnvironmentDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppEnvironmentDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupDeploySettingRequest(TeaModel):
    def __init__(self, app_group_id=None, env_type=None):
        self.app_group_id = app_group_id  # type: long
        self.env_type = env_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupDeploySettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class DescribeAppGroupDeploySettingResponseBodyResult(TeaModel):
    def __init__(self, default_packet_comment=None, default_packet_id=None):
        self.default_packet_comment = default_packet_comment  # type: str
        self.default_packet_id = default_packet_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupDeploySettingResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_packet_comment is not None:
            result['DefaultPacketComment'] = self.default_packet_comment
        if self.default_packet_id is not None:
            result['DefaultPacketId'] = self.default_packet_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultPacketComment') is not None:
            self.default_packet_comment = m.get('DefaultPacketComment')
        if m.get('DefaultPacketId') is not None:
            self.default_packet_id = m.get('DefaultPacketId')
        return self


class DescribeAppGroupDeploySettingResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppGroupDeploySettingResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppGroupDeploySettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAppGroupDeploySettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAppGroupDeploySettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppGroupDeploySettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppGroupDeploySettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppGroupDeploySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppMonitorMetricRequest(TeaModel):
    def __init__(self, app_id=None, deploy_order_id=None, end_time=None, env_id=None, metric=None, pod_name=None,
                 start_time=None, type=None):
        self.app_id = app_id  # type: long
        self.deploy_order_id = deploy_order_id  # type: str
        self.end_time = end_time  # type: long
        self.env_id = env_id  # type: long
        self.metric = metric  # type: str
        self.pod_name = pod_name  # type: str
        self.start_time = start_time  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppMonitorMetricRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAppMonitorMetricResponseBodyResult(TeaModel):
    def __init__(self, categories=None, data=None, name=None):
        self.categories = categories  # type: list[str]
        self.data = data  # type: list[float]
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppMonitorMetricResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.data is not None:
            result['Data'] = self.data
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAppMonitorMetricResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeAppMonitorMetricResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppMonitorMetricResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeAppMonitorMetricResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAppMonitorMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppMonitorMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppMonitorMetricResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppMonitorMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppResourceAllocRequest(TeaModel):
    def __init__(self, app_env_id=None):
        self.app_env_id = app_env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppResourceAllocRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        return self


class DescribeAppResourceAllocResponseBodyResult(TeaModel):
    def __init__(self, app_env_id=None, app_id=None, cluster_id=None, id=None, resource_def=None):
        self.app_env_id = app_env_id  # type: long
        self.app_id = app_id  # type: long
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: long
        self.resource_def = resource_def  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppResourceAllocResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_def is not None:
            result['ResourceDef'] = self.resource_def
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceDef') is not None:
            self.resource_def = m.get('ResourceDef')
        return self


class DescribeAppResourceAllocResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppResourceAllocResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppResourceAllocResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeAppResourceAllocResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAppResourceAllocResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppResourceAllocResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppResourceAllocResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppResourceAllocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterDetailRequest(TeaModel):
    def __init__(self, cluster_instance_id=None):
        self.cluster_instance_id = cluster_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        return self


class DescribeClusterDetailResponseBodyResultBasicInfo(TeaModel):
    def __init__(self, business_code=None, cluster_id=None, cluster_instance_id=None, cluster_name=None,
                 ecs_ids=None, env_type=None, has_install_arms_pilot=None, has_install_log_controller=None,
                 install_arms_in_process=None, install_log_in_process=None, main_user_id=None, region_id=None, region_name=None,
                 user_nick=None, vpc_id=None, vswitchs=None):
        self.business_code = business_code  # type: str
        self.cluster_id = cluster_id  # type: long
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.ecs_ids = ecs_ids  # type: list[str]
        self.env_type = env_type  # type: str
        self.has_install_arms_pilot = has_install_arms_pilot  # type: bool
        self.has_install_log_controller = has_install_log_controller  # type: bool
        self.install_arms_in_process = install_arms_in_process  # type: bool
        self.install_log_in_process = install_log_in_process  # type: bool
        self.main_user_id = main_user_id  # type: str
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str
        self.user_nick = user_nick  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitchs = vswitchs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.ecs_ids is not None:
            result['EcsIds'] = self.ecs_ids
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.has_install_arms_pilot is not None:
            result['HasInstallArmsPilot'] = self.has_install_arms_pilot
        if self.has_install_log_controller is not None:
            result['HasInstallLogController'] = self.has_install_log_controller
        if self.install_arms_in_process is not None:
            result['InstallArmsInProcess'] = self.install_arms_in_process
        if self.install_log_in_process is not None:
            result['InstallLogInProcess'] = self.install_log_in_process
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitchs is not None:
            result['Vswitchs'] = self.vswitchs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('EcsIds') is not None:
            self.ecs_ids = m.get('EcsIds')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('HasInstallArmsPilot') is not None:
            self.has_install_arms_pilot = m.get('HasInstallArmsPilot')
        if m.get('HasInstallLogController') is not None:
            self.has_install_log_controller = m.get('HasInstallLogController')
        if m.get('InstallArmsInProcess') is not None:
            self.install_arms_in_process = m.get('InstallArmsInProcess')
        if m.get('InstallLogInProcess') is not None:
            self.install_log_in_process = m.get('InstallLogInProcess')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Vswitchs') is not None:
            self.vswitchs = m.get('Vswitchs')
        return self


class DescribeClusterDetailResponseBodyResultInstanceInfoAllocatedPodInfoList(TeaModel):
    def __init__(self, app_id=None, app_name=None, cup_request=None, env_id=None, env_name=None, mem_request=None,
                 pod_count=None):
        self.app_id = app_id  # type: long
        self.app_name = app_name  # type: str
        self.cup_request = cup_request  # type: str
        self.env_id = env_id  # type: long
        self.env_name = env_name  # type: str
        self.mem_request = mem_request  # type: str
        self.pod_count = pod_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultInstanceInfoAllocatedPodInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cup_request is not None:
            result['CupRequest'] = self.cup_request
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.mem_request is not None:
            result['MemRequest'] = self.mem_request
        if self.pod_count is not None:
            result['PodCount'] = self.pod_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CupRequest') is not None:
            self.cup_request = m.get('CupRequest')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('MemRequest') is not None:
            self.mem_request = m.get('MemRequest')
        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')
        return self


class DescribeClusterDetailResponseBodyResultInstanceInfoAvailablePodInfoList(TeaModel):
    def __init__(self, available_pod_count=None, cup_request=None, mem_request=None):
        self.available_pod_count = available_pod_count  # type: int
        self.cup_request = cup_request  # type: str
        self.mem_request = mem_request  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultInstanceInfoAvailablePodInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_pod_count is not None:
            result['AvailablePodCount'] = self.available_pod_count
        if self.cup_request is not None:
            result['CupRequest'] = self.cup_request
        if self.mem_request is not None:
            result['MemRequest'] = self.mem_request
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailablePodCount') is not None:
            self.available_pod_count = m.get('AvailablePodCount')
        if m.get('CupRequest') is not None:
            self.cup_request = m.get('CupRequest')
        if m.get('MemRequest') is not None:
            self.mem_request = m.get('MemRequest')
        return self


class DescribeClusterDetailResponseBodyResultInstanceInfo(TeaModel):
    def __init__(self, allocate_pod_count=None, allocated_pod_info_list=None, app_count=None,
                 available_pod_info_list=None):
        self.allocate_pod_count = allocate_pod_count  # type: int
        self.allocated_pod_info_list = allocated_pod_info_list  # type: list[DescribeClusterDetailResponseBodyResultInstanceInfoAllocatedPodInfoList]
        self.app_count = app_count  # type: int
        self.available_pod_info_list = available_pod_info_list  # type: list[DescribeClusterDetailResponseBodyResultInstanceInfoAvailablePodInfoList]

    def validate(self):
        if self.allocated_pod_info_list:
            for k in self.allocated_pod_info_list:
                if k:
                    k.validate()
        if self.available_pod_info_list:
            for k in self.available_pod_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_pod_count is not None:
            result['AllocatePodCount'] = self.allocate_pod_count
        result['AllocatedPodInfoList'] = []
        if self.allocated_pod_info_list is not None:
            for k in self.allocated_pod_info_list:
                result['AllocatedPodInfoList'].append(k.to_map() if k else None)
        if self.app_count is not None:
            result['AppCount'] = self.app_count
        result['AvailablePodInfoList'] = []
        if self.available_pod_info_list is not None:
            for k in self.available_pod_info_list:
                result['AvailablePodInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocatePodCount') is not None:
            self.allocate_pod_count = m.get('AllocatePodCount')
        self.allocated_pod_info_list = []
        if m.get('AllocatedPodInfoList') is not None:
            for k in m.get('AllocatedPodInfoList'):
                temp_model = DescribeClusterDetailResponseBodyResultInstanceInfoAllocatedPodInfoList()
                self.allocated_pod_info_list.append(temp_model.from_map(k))
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')
        self.available_pod_info_list = []
        if m.get('AvailablePodInfoList') is not None:
            for k in m.get('AvailablePodInfoList'):
                temp_model = DescribeClusterDetailResponseBodyResultInstanceInfoAvailablePodInfoList()
                self.available_pod_info_list.append(temp_model.from_map(k))
        return self


class DescribeClusterDetailResponseBodyResultNetInfo(TeaModel):
    def __init__(self, net_plug_type=None, prod_cidr=None, service_cidr=None):
        self.net_plug_type = net_plug_type  # type: str
        self.prod_cidr = prod_cidr  # type: str
        self.service_cidr = service_cidr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultNetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_plug_type is not None:
            result['NetPlugType'] = self.net_plug_type
        if self.prod_cidr is not None:
            result['ProdCIDR'] = self.prod_cidr
        if self.service_cidr is not None:
            result['ServiceCIDR'] = self.service_cidr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetPlugType') is not None:
            self.net_plug_type = m.get('NetPlugType')
        if m.get('ProdCIDR') is not None:
            self.prod_cidr = m.get('ProdCIDR')
        if m.get('ServiceCIDR') is not None:
            self.service_cidr = m.get('ServiceCIDR')
        return self


class DescribeClusterDetailResponseBodyResultNodeWorkLoadList(TeaModel):
    def __init__(self, app_pod_count=None, cpu_request=None, cpu_total=None, cpu_use=None, instance_id=None,
                 mem_request=None, mem_total=None, mem_use=None, node_name=None, pod_count=None, ready=None, unschedulable=None):
        self.app_pod_count = app_pod_count  # type: int
        self.cpu_request = cpu_request  # type: str
        self.cpu_total = cpu_total  # type: str
        self.cpu_use = cpu_use  # type: str
        self.instance_id = instance_id  # type: str
        self.mem_request = mem_request  # type: str
        self.mem_total = mem_total  # type: str
        self.mem_use = mem_use  # type: str
        self.node_name = node_name  # type: str
        self.pod_count = pod_count  # type: int
        self.ready = ready  # type: bool
        self.unschedulable = unschedulable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultNodeWorkLoadList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_pod_count is not None:
            result['AppPodCount'] = self.app_pod_count
        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request
        if self.cpu_total is not None:
            result['CpuTotal'] = self.cpu_total
        if self.cpu_use is not None:
            result['CpuUse'] = self.cpu_use
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mem_request is not None:
            result['MemRequest'] = self.mem_request
        if self.mem_total is not None:
            result['MemTotal'] = self.mem_total
        if self.mem_use is not None:
            result['MemUse'] = self.mem_use
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.pod_count is not None:
            result['PodCount'] = self.pod_count
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.unschedulable is not None:
            result['Unschedulable'] = self.unschedulable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppPodCount') is not None:
            self.app_pod_count = m.get('AppPodCount')
        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')
        if m.get('CpuTotal') is not None:
            self.cpu_total = m.get('CpuTotal')
        if m.get('CpuUse') is not None:
            self.cpu_use = m.get('CpuUse')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemRequest') is not None:
            self.mem_request = m.get('MemRequest')
        if m.get('MemTotal') is not None:
            self.mem_total = m.get('MemTotal')
        if m.get('MemUse') is not None:
            self.mem_use = m.get('MemUse')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('Unschedulable') is not None:
            self.unschedulable = m.get('Unschedulable')
        return self


class DescribeClusterDetailResponseBodyResultWorkLoad(TeaModel):
    def __init__(self, all_node_count=None, allocate_all_pod_count=None, allocate_app_pod_count=None,
                 cpu_capacity_total=None, cpu_level=None, cpu_request=None, cpu_request_percent=None, cpu_total=None, cpu_use=None,
                 cpu_use_percent=None, mem_capacity_total=None, mem_level=None, mem_request=None, mem_request_percent=None,
                 mem_total=None, mem_use=None, mem_use_percent=None):
        self.all_node_count = all_node_count  # type: int
        self.allocate_all_pod_count = allocate_all_pod_count  # type: int
        self.allocate_app_pod_count = allocate_app_pod_count  # type: int
        self.cpu_capacity_total = cpu_capacity_total  # type: str
        self.cpu_level = cpu_level  # type: str
        self.cpu_request = cpu_request  # type: str
        self.cpu_request_percent = cpu_request_percent  # type: str
        self.cpu_total = cpu_total  # type: str
        self.cpu_use = cpu_use  # type: str
        self.cpu_use_percent = cpu_use_percent  # type: str
        self.mem_capacity_total = mem_capacity_total  # type: str
        self.mem_level = mem_level  # type: str
        self.mem_request = mem_request  # type: str
        self.mem_request_percent = mem_request_percent  # type: str
        self.mem_total = mem_total  # type: str
        self.mem_use = mem_use  # type: str
        self.mem_use_percent = mem_use_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResultWorkLoad, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_node_count is not None:
            result['AllNodeCount'] = self.all_node_count
        if self.allocate_all_pod_count is not None:
            result['AllocateAllPodCount'] = self.allocate_all_pod_count
        if self.allocate_app_pod_count is not None:
            result['AllocateAppPodCount'] = self.allocate_app_pod_count
        if self.cpu_capacity_total is not None:
            result['CpuCapacityTotal'] = self.cpu_capacity_total
        if self.cpu_level is not None:
            result['CpuLevel'] = self.cpu_level
        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request
        if self.cpu_request_percent is not None:
            result['CpuRequestPercent'] = self.cpu_request_percent
        if self.cpu_total is not None:
            result['CpuTotal'] = self.cpu_total
        if self.cpu_use is not None:
            result['CpuUse'] = self.cpu_use
        if self.cpu_use_percent is not None:
            result['CpuUsePercent'] = self.cpu_use_percent
        if self.mem_capacity_total is not None:
            result['MemCapacityTotal'] = self.mem_capacity_total
        if self.mem_level is not None:
            result['MemLevel'] = self.mem_level
        if self.mem_request is not None:
            result['MemRequest'] = self.mem_request
        if self.mem_request_percent is not None:
            result['MemRequestPercent'] = self.mem_request_percent
        if self.mem_total is not None:
            result['MemTotal'] = self.mem_total
        if self.mem_use is not None:
            result['MemUse'] = self.mem_use
        if self.mem_use_percent is not None:
            result['MemUsePercent'] = self.mem_use_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllNodeCount') is not None:
            self.all_node_count = m.get('AllNodeCount')
        if m.get('AllocateAllPodCount') is not None:
            self.allocate_all_pod_count = m.get('AllocateAllPodCount')
        if m.get('AllocateAppPodCount') is not None:
            self.allocate_app_pod_count = m.get('AllocateAppPodCount')
        if m.get('CpuCapacityTotal') is not None:
            self.cpu_capacity_total = m.get('CpuCapacityTotal')
        if m.get('CpuLevel') is not None:
            self.cpu_level = m.get('CpuLevel')
        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')
        if m.get('CpuRequestPercent') is not None:
            self.cpu_request_percent = m.get('CpuRequestPercent')
        if m.get('CpuTotal') is not None:
            self.cpu_total = m.get('CpuTotal')
        if m.get('CpuUse') is not None:
            self.cpu_use = m.get('CpuUse')
        if m.get('CpuUsePercent') is not None:
            self.cpu_use_percent = m.get('CpuUsePercent')
        if m.get('MemCapacityTotal') is not None:
            self.mem_capacity_total = m.get('MemCapacityTotal')
        if m.get('MemLevel') is not None:
            self.mem_level = m.get('MemLevel')
        if m.get('MemRequest') is not None:
            self.mem_request = m.get('MemRequest')
        if m.get('MemRequestPercent') is not None:
            self.mem_request_percent = m.get('MemRequestPercent')
        if m.get('MemTotal') is not None:
            self.mem_total = m.get('MemTotal')
        if m.get('MemUse') is not None:
            self.mem_use = m.get('MemUse')
        if m.get('MemUsePercent') is not None:
            self.mem_use_percent = m.get('MemUsePercent')
        return self


class DescribeClusterDetailResponseBodyResult(TeaModel):
    def __init__(self, basic_info=None, instance_info=None, net_info=None, node_work_load_list=None, work_load=None):
        self.basic_info = basic_info  # type: DescribeClusterDetailResponseBodyResultBasicInfo
        self.instance_info = instance_info  # type: DescribeClusterDetailResponseBodyResultInstanceInfo
        self.net_info = net_info  # type: DescribeClusterDetailResponseBodyResultNetInfo
        self.node_work_load_list = node_work_load_list  # type: list[DescribeClusterDetailResponseBodyResultNodeWorkLoadList]
        self.work_load = work_load  # type: DescribeClusterDetailResponseBodyResultWorkLoad

    def validate(self):
        if self.basic_info:
            self.basic_info.validate()
        if self.instance_info:
            self.instance_info.validate()
        if self.net_info:
            self.net_info.validate()
        if self.node_work_load_list:
            for k in self.node_work_load_list:
                if k:
                    k.validate()
        if self.work_load:
            self.work_load.validate()

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_info is not None:
            result['BasicInfo'] = self.basic_info.to_map()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.net_info is not None:
            result['NetInfo'] = self.net_info.to_map()
        result['NodeWorkLoadList'] = []
        if self.node_work_load_list is not None:
            for k in self.node_work_load_list:
                result['NodeWorkLoadList'].append(k.to_map() if k else None)
        if self.work_load is not None:
            result['WorkLoad'] = self.work_load.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicInfo') is not None:
            temp_model = DescribeClusterDetailResponseBodyResultBasicInfo()
            self.basic_info = temp_model.from_map(m['BasicInfo'])
        if m.get('InstanceInfo') is not None:
            temp_model = DescribeClusterDetailResponseBodyResultInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('NetInfo') is not None:
            temp_model = DescribeClusterDetailResponseBodyResultNetInfo()
            self.net_info = temp_model.from_map(m['NetInfo'])
        self.node_work_load_list = []
        if m.get('NodeWorkLoadList') is not None:
            for k in m.get('NodeWorkLoadList'):
                temp_model = DescribeClusterDetailResponseBodyResultNodeWorkLoadList()
                self.node_work_load_list.append(temp_model.from_map(k))
        if m.get('WorkLoad') is not None:
            temp_model = DescribeClusterDetailResponseBodyResultWorkLoad()
            self.work_load = temp_model.from_map(m['WorkLoad'])
        return self


class DescribeClusterDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeClusterDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeClusterDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabasesRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesRequest, self).to_map()
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


class DescribeDatabasesResponseBodyResultDatabasesAccounts(TeaModel):
    def __init__(self, account=None, account_privilege=None, account_privilege_detail=None):
        self.account = account  # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_privilege_detail = account_privilege_detail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyResultDatabasesAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_privilege_detail is not None:
            result['AccountPrivilegeDetail'] = self.account_privilege_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountPrivilegeDetail') is not None:
            self.account_privilege_detail = m.get('AccountPrivilegeDetail')
        return self


class DescribeDatabasesResponseBodyResultDatabases(TeaModel):
    def __init__(self, accounts=None, character_set_name=None, dbdescription=None, dbinstance_id=None, dbname=None,
                 dbstatus=None, engine=None):
        self.accounts = accounts  # type: list[DescribeDatabasesResponseBodyResultDatabasesAccounts]
        self.character_set_name = character_set_name  # type: str
        self.dbdescription = dbdescription  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname  # type: str
        self.dbstatus = dbstatus  # type: str
        self.engine = engine  # type: str

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyResultDatabases, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.dbstatus is not None:
            result['DBStatus'] = self.dbstatus
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeDatabasesResponseBodyResultDatabasesAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('DBStatus') is not None:
            self.dbstatus = m.get('DBStatus')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeDatabasesResponseBodyResult(TeaModel):
    def __init__(self, databases=None):
        self.databases = databases  # type: list[DescribeDatabasesResponseBodyResultDatabases]

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeDatabasesResponseBodyResultDatabases()
                self.databases.append(temp_model.from_map(k))
        return self


class DescribeDatabasesResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeDatabasesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDatabasesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeDatabasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDatabasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDatabasesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployOrderDetailRequest(TeaModel):
    def __init__(self, deploy_order_id=None):
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployOrderDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class DescribeDeployOrderDetailResponseBodyResult(TeaModel):
    def __init__(self, app_instance_type=None, current_partition_num=None, deploy_order_id=None,
                 deploy_pause_type=None, deploy_pause_type_name=None, deploy_type=None, deploy_type_name=None, description=None,
                 elapsed_time=None, end_time=None, env_id=None, env_type=None, failure_rate=None, finish_app_instance_ct=None,
                 name=None, partition_type=None, partition_type_name=None, result=None, result_name=None, schema_id=None,
                 start_time=None, status=None, status_name=None, total_app_instance_ct=None, total_partitions=None,
                 user_id=None, user_nick=None):
        self.app_instance_type = app_instance_type  # type: str
        self.current_partition_num = current_partition_num  # type: int
        self.deploy_order_id = deploy_order_id  # type: long
        self.deploy_pause_type = deploy_pause_type  # type: str
        self.deploy_pause_type_name = deploy_pause_type_name  # type: str
        self.deploy_type = deploy_type  # type: str
        self.deploy_type_name = deploy_type_name  # type: str
        self.description = description  # type: str
        self.elapsed_time = elapsed_time  # type: int
        self.end_time = end_time  # type: str
        self.env_id = env_id  # type: long
        self.env_type = env_type  # type: str
        self.failure_rate = failure_rate  # type: str
        self.finish_app_instance_ct = finish_app_instance_ct  # type: int
        self.name = name  # type: str
        self.partition_type = partition_type  # type: str
        self.partition_type_name = partition_type_name  # type: str
        self.result = result  # type: int
        self.result_name = result_name  # type: str
        self.schema_id = schema_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.status_name = status_name  # type: str
        self.total_app_instance_ct = total_app_instance_ct  # type: int
        self.total_partitions = total_partitions  # type: int
        self.user_id = user_id  # type: str
        self.user_nick = user_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeployOrderDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.current_partition_num is not None:
            result['CurrentPartitionNum'] = self.current_partition_num
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        if self.deploy_pause_type is not None:
            result['DeployPauseType'] = self.deploy_pause_type
        if self.deploy_pause_type_name is not None:
            result['DeployPauseTypeName'] = self.deploy_pause_type_name
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.deploy_type_name is not None:
            result['DeployTypeName'] = self.deploy_type_name
        if self.description is not None:
            result['Description'] = self.description
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.failure_rate is not None:
            result['FailureRate'] = self.failure_rate
        if self.finish_app_instance_ct is not None:
            result['FinishAppInstanceCt'] = self.finish_app_instance_ct
        if self.name is not None:
            result['Name'] = self.name
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        if self.partition_type_name is not None:
            result['PartitionTypeName'] = self.partition_type_name
        if self.result is not None:
            result['Result'] = self.result
        if self.result_name is not None:
            result['ResultName'] = self.result_name
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.total_app_instance_ct is not None:
            result['TotalAppInstanceCt'] = self.total_app_instance_ct
        if self.total_partitions is not None:
            result['TotalPartitions'] = self.total_partitions
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('CurrentPartitionNum') is not None:
            self.current_partition_num = m.get('CurrentPartitionNum')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        if m.get('DeployPauseType') is not None:
            self.deploy_pause_type = m.get('DeployPauseType')
        if m.get('DeployPauseTypeName') is not None:
            self.deploy_pause_type_name = m.get('DeployPauseTypeName')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DeployTypeName') is not None:
            self.deploy_type_name = m.get('DeployTypeName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('FailureRate') is not None:
            self.failure_rate = m.get('FailureRate')
        if m.get('FinishAppInstanceCt') is not None:
            self.finish_app_instance_ct = m.get('FinishAppInstanceCt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        if m.get('PartitionTypeName') is not None:
            self.partition_type_name = m.get('PartitionTypeName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultName') is not None:
            self.result_name = m.get('ResultName')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('TotalAppInstanceCt') is not None:
            self.total_app_instance_ct = m.get('TotalAppInstanceCt')
        if m.get('TotalPartitions') is not None:
            self.total_partitions = m.get('TotalPartitions')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class DescribeDeployOrderDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeDeployOrderDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeDeployOrderDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeDeployOrderDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDeployOrderDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDeployOrderDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeployOrderDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDeployOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEciConfigRequest(TeaModel):
    def __init__(self, app_env_id=None):
        self.app_env_id = app_env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEciConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        return self


class DescribeEciConfigResponseBodyResult(TeaModel):
    def __init__(self, app_env_id=None, eip_bandwidth=None, enable_eci_schedule_policy=None, mirror_cache=None,
                 normal_instance_limit=None, schedule_virtual_node=None):
        self.app_env_id = app_env_id  # type: long
        self.eip_bandwidth = eip_bandwidth  # type: int
        self.enable_eci_schedule_policy = enable_eci_schedule_policy  # type: bool
        self.mirror_cache = mirror_cache  # type: bool
        self.normal_instance_limit = normal_instance_limit  # type: int
        self.schedule_virtual_node = schedule_virtual_node  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEciConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.enable_eci_schedule_policy is not None:
            result['EnableEciSchedulePolicy'] = self.enable_eci_schedule_policy
        if self.mirror_cache is not None:
            result['MirrorCache'] = self.mirror_cache
        if self.normal_instance_limit is not None:
            result['NormalInstanceLimit'] = self.normal_instance_limit
        if self.schedule_virtual_node is not None:
            result['ScheduleVirtualNode'] = self.schedule_virtual_node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EnableEciSchedulePolicy') is not None:
            self.enable_eci_schedule_policy = m.get('EnableEciSchedulePolicy')
        if m.get('MirrorCache') is not None:
            self.mirror_cache = m.get('MirrorCache')
        if m.get('NormalInstanceLimit') is not None:
            self.normal_instance_limit = m.get('NormalInstanceLimit')
        if m.get('ScheduleVirtualNode') is not None:
            self.schedule_virtual_node = m.get('ScheduleVirtualNode')
        return self


class DescribeEciConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeEciConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeEciConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeEciConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeEciConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEciConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEciConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEciConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventMonitorListRequest(TeaModel):
    def __init__(self, app_id=None, end_time=None, env_id=None, event_level=None, event_type=None, page_num=None,
                 page_size=None, pod_name=None, start_time=None):
        self.app_id = app_id  # type: long
        self.end_time = end_time  # type: long
        self.env_id = env_id  # type: long
        self.event_level = event_level  # type: str
        self.event_type = event_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.pod_name = pod_name  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventMonitorListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeEventMonitorListResponseBodyData(TeaModel):
    def __init__(self, count=None, event_time=None, host_name=None, kind=None, level=None, message=None,
                 name_space=None, pod_name=None, reason=None):
        self.count = count  # type: int
        self.event_time = event_time  # type: str
        self.host_name = host_name  # type: str
        self.kind = kind  # type: str
        self.level = level  # type: str
        self.message = message  # type: str
        self.name_space = name_space  # type: str
        self.pod_name = pod_name  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEventMonitorListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class DescribeEventMonitorListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[DescribeEventMonitorListResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEventMonitorListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeEventMonitorListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEventMonitorListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEventMonitorListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEventMonitorListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventMonitorListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobLogRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, pod_name=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.pod_name = pod_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class DescribeJobLogResponseBodyResultEvents(TeaModel):
    def __init__(self, action=None, count=None, event_time=None, first_timestamp=None, last_timestamp=None,
                 mesage=None, reason=None, type=None):
        self.action = action  # type: str
        self.count = count  # type: int
        self.event_time = event_time  # type: str
        self.first_timestamp = first_timestamp  # type: str
        self.last_timestamp = last_timestamp  # type: str
        self.mesage = mesage  # type: str
        self.reason = reason  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobLogResponseBodyResultEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.count is not None:
            result['Count'] = self.count
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.mesage is not None:
            result['Mesage'] = self.mesage
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Mesage') is not None:
            self.mesage = m.get('Mesage')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeJobLogResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, env_id=None, events=None, job_log=None, pod_name=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.events = events  # type: list[DescribeJobLogResponseBodyResultEvents]
        self.job_log = job_log  # type: str
        self.pod_name = pod_name  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeJobLogResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.job_log is not None:
            result['JobLog'] = self.job_log
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeJobLogResponseBodyResultEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('JobLog') is not None:
            self.job_log = m.get('JobLog')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class DescribeJobLogResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeJobLogResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeJobLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeJobLogResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeJobLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeJobLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeJobLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePodContainerLogListRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, line=None, pod_name=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.line = line  # type: int
        self.pod_name = pod_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePodContainerLogListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.line is not None:
            result['Line'] = self.line
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class DescribePodContainerLogListResponseBodyResultContainerLogList(TeaModel):
    def __init__(self, container_name=None, content=None, pod_name=None):
        self.container_name = container_name  # type: str
        self.content = content  # type: str
        self.pod_name = pod_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePodContainerLogListResponseBodyResultContainerLogList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.content is not None:
            result['Content'] = self.content
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class DescribePodContainerLogListResponseBodyResult(TeaModel):
    def __init__(self, container_log_list=None):
        self.container_log_list = container_log_list  # type: list[DescribePodContainerLogListResponseBodyResultContainerLogList]

    def validate(self):
        if self.container_log_list:
            for k in self.container_log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePodContainerLogListResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerLogList'] = []
        if self.container_log_list is not None:
            for k in self.container_log_list:
                result['ContainerLogList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.container_log_list = []
        if m.get('ContainerLogList') is not None:
            for k in m.get('ContainerLogList'):
                temp_model = DescribePodContainerLogListResponseBodyResultContainerLogList()
                self.container_log_list.append(temp_model.from_map(k))
        return self


class DescribePodContainerLogListResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribePodContainerLogListResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribePodContainerLogListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribePodContainerLogListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePodContainerLogListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePodContainerLogListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePodContainerLogListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePodContainerLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePodEventsRequest(TeaModel):
    def __init__(self, app_inst_id=None, deploy_order_id=None):
        self.app_inst_id = app_inst_id  # type: str
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePodEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_inst_id is not None:
            result['AppInstId'] = self.app_inst_id
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstId') is not None:
            self.app_inst_id = m.get('AppInstId')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class DescribePodEventsResponseBodyResultPodEvents(TeaModel):
    def __init__(self, action=None, count=None, event_time=None, first_timestamp=None, last_timestamp=None,
                 message=None, reason=None, type=None):
        self.action = action  # type: str
        self.count = count  # type: int
        self.event_time = event_time  # type: str
        self.first_timestamp = first_timestamp  # type: str
        self.last_timestamp = last_timestamp  # type: str
        self.message = message  # type: str
        self.reason = reason  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePodEventsResponseBodyResultPodEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.count is not None:
            result['Count'] = self.count
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePodEventsResponseBodyResult(TeaModel):
    def __init__(self, deploy_order_name=None, pod_events=None):
        self.deploy_order_name = deploy_order_name  # type: str
        self.pod_events = pod_events  # type: list[DescribePodEventsResponseBodyResultPodEvents]

    def validate(self):
        if self.pod_events:
            for k in self.pod_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePodEventsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_name is not None:
            result['DeployOrderName'] = self.deploy_order_name
        result['PodEvents'] = []
        if self.pod_events is not None:
            for k in self.pod_events:
                result['PodEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderName') is not None:
            self.deploy_order_name = m.get('DeployOrderName')
        self.pod_events = []
        if m.get('PodEvents') is not None:
            for k in m.get('PodEvents'):
                temp_model = DescribePodEventsResponseBodyResultPodEvents()
                self.pod_events.append(temp_model.from_map(k))
        return self


class DescribePodEventsResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribePodEventsResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribePodEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribePodEventsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePodEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePodEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePodEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePodEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePodLogRequest(TeaModel):
    def __init__(self, app_inst_id=None, deploy_order_id=None):
        self.app_inst_id = app_inst_id  # type: str
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePodLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_inst_id is not None:
            result['AppInstId'] = self.app_inst_id
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstId') is not None:
            self.app_inst_id = m.get('AppInstId')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class DescribePodLogResponseBodyResultDeployStepList(TeaModel):
    def __init__(self, status=None, step_code=None, step_log=None, step_name=None):
        self.status = status  # type: str
        self.step_code = step_code  # type: str
        self.step_log = step_log  # type: str
        self.step_name = step_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePodLogResponseBodyResultDeployStepList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.step_code is not None:
            result['StepCode'] = self.step_code
        if self.step_log is not None:
            result['StepLog'] = self.step_log
        if self.step_name is not None:
            result['StepName'] = self.step_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StepCode') is not None:
            self.step_code = m.get('StepCode')
        if m.get('StepLog') is not None:
            self.step_log = m.get('StepLog')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        return self


class DescribePodLogResponseBodyResult(TeaModel):
    def __init__(self, deploy_order_name=None, deploy_step_list=None, env_type_name=None):
        self.deploy_order_name = deploy_order_name  # type: str
        self.deploy_step_list = deploy_step_list  # type: list[DescribePodLogResponseBodyResultDeployStepList]
        self.env_type_name = env_type_name  # type: str

    def validate(self):
        if self.deploy_step_list:
            for k in self.deploy_step_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePodLogResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_name is not None:
            result['DeployOrderName'] = self.deploy_order_name
        result['DeployStepList'] = []
        if self.deploy_step_list is not None:
            for k in self.deploy_step_list:
                result['DeployStepList'].append(k.to_map() if k else None)
        if self.env_type_name is not None:
            result['EnvTypeName'] = self.env_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderName') is not None:
            self.deploy_order_name = m.get('DeployOrderName')
        self.deploy_step_list = []
        if m.get('DeployStepList') is not None:
            for k in m.get('DeployStepList'):
                temp_model = DescribePodLogResponseBodyResultDeployStepList()
                self.deploy_step_list.append(temp_model.from_map(k))
        if m.get('EnvTypeName') is not None:
            self.env_type_name = m.get('EnvTypeName')
        return self


class DescribePodLogResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribePodLogResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribePodLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribePodLogResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePodLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePodLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePodLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePodLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRdsAccountsRequest(TeaModel):
    def __init__(self, account_name=None, db_instance_id=None):
        self.account_name = account_name  # type: str
        self.db_instance_id = db_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        return self


class DescribeRdsAccountsResponseBodyResultAccountsDatabasePrivileges(TeaModel):
    def __init__(self, account_privilege=None, account_privilege_detail=None, dbname=None):
        self.account_privilege = account_privilege  # type: str
        self.account_privilege_detail = account_privilege_detail  # type: str
        self.dbname = dbname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRdsAccountsResponseBodyResultAccountsDatabasePrivileges, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_privilege_detail is not None:
            result['AccountPrivilegeDetail'] = self.account_privilege_detail
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountPrivilegeDetail') is not None:
            self.account_privilege_detail = m.get('AccountPrivilegeDetail')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeRdsAccountsResponseBodyResultAccounts(TeaModel):
    def __init__(self, account_description=None, account_name=None, account_status=None, account_type=None,
                 dbinstance_id=None, database_privileges=None, priv_exceeded=None):
        self.account_description = account_description  # type: str
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.account_type = account_type  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.database_privileges = database_privileges  # type: list[DescribeRdsAccountsResponseBodyResultAccountsDatabasePrivileges]
        self.priv_exceeded = priv_exceeded  # type: str

    def validate(self):
        if self.database_privileges:
            for k in self.database_privileges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsAccountsResponseBodyResultAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        result['DatabasePrivileges'] = []
        if self.database_privileges is not None:
            for k in self.database_privileges:
                result['DatabasePrivileges'].append(k.to_map() if k else None)
        if self.priv_exceeded is not None:
            result['PrivExceeded'] = self.priv_exceeded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        self.database_privileges = []
        if m.get('DatabasePrivileges') is not None:
            for k in m.get('DatabasePrivileges'):
                temp_model = DescribeRdsAccountsResponseBodyResultAccountsDatabasePrivileges()
                self.database_privileges.append(temp_model.from_map(k))
        if m.get('PrivExceeded') is not None:
            self.priv_exceeded = m.get('PrivExceeded')
        return self


class DescribeRdsAccountsResponseBodyResult(TeaModel):
    def __init__(self, accounts=None):
        self.accounts = accounts  # type: list[DescribeRdsAccountsResponseBodyResultAccounts]

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRdsAccountsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeRdsAccountsResponseBodyResultAccounts()
                self.accounts.append(temp_model.from_map(k))
        return self


class DescribeRdsAccountsResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeRdsAccountsResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeRdsAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeRdsAccountsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeRdsAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRdsAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRdsAccountsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRdsAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceDetailRequest(TeaModel):
    def __init__(self, service_id=None):
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DescribeServiceDetailResponseBodyResultPortMappings(TeaModel):
    def __init__(self, name=None, node_port=None, port=None, protocol=None, target_port=None):
        self.name = name  # type: str
        self.node_port = node_port  # type: int
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.target_port = target_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceDetailResponseBodyResultPortMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeServiceDetailResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, cluster_ip=None, env_id=None, headless=None, k_8s_service_id=None, name=None,
                 port_mappings=None, service_id=None, service_type=None):
        self.app_id = app_id  # type: long
        self.cluster_ip = cluster_ip  # type: str
        self.env_id = env_id  # type: long
        self.headless = headless  # type: bool
        self.k_8s_service_id = k_8s_service_id  # type: str
        self.name = name  # type: str
        self.port_mappings = port_mappings  # type: list[DescribeServiceDetailResponseBodyResultPortMappings]
        self.service_id = service_id  # type: long
        self.service_type = service_type  # type: str

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeServiceDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_ip is not None:
            result['ClusterIP'] = self.cluster_ip
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.headless is not None:
            result['Headless'] = self.headless
        if self.k_8s_service_id is not None:
            result['K8sServiceId'] = self.k_8s_service_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterIP') is not None:
            self.cluster_ip = m.get('ClusterIP')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Headless') is not None:
            self.headless = m.get('Headless')
        if m.get('K8sServiceId') is not None:
            self.k_8s_service_id = m.get('K8sServiceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = DescribeServiceDetailResponseBodyResultPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class DescribeServiceDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeServiceDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeServiceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeServiceDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeServiceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeServiceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlbAPDetailRequest(TeaModel):
    def __init__(self, slb_apid=None):
        self.slb_apid = slb_apid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlbAPDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_apid is not None:
            result['SlbAPId'] = self.slb_apid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlbAPId') is not None:
            self.slb_apid = m.get('SlbAPId')
        return self


class DescribeSlbAPDetailResponseBodyResult(TeaModel):
    def __init__(self, app_id=None, cookie_timeout=None, env_id=None, established_timeout=None, listener_port=None,
                 name=None, network_mode=None, protocol=None, real_server_port=None, slb_apid=None, slb_id=None,
                 slb_ip=None, ssl_cert_id=None, sticky_session=None):
        self.app_id = app_id  # type: long
        self.cookie_timeout = cookie_timeout  # type: int
        self.env_id = env_id  # type: long
        self.established_timeout = established_timeout  # type: int
        self.listener_port = listener_port  # type: int
        self.name = name  # type: str
        self.network_mode = network_mode  # type: str
        self.protocol = protocol  # type: str
        self.real_server_port = real_server_port  # type: int
        self.slb_apid = slb_apid  # type: long
        self.slb_id = slb_id  # type: str
        self.slb_ip = slb_ip  # type: str
        self.ssl_cert_id = ssl_cert_id  # type: str
        self.sticky_session = sticky_session  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlbAPDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.name is not None:
            result['Name'] = self.name
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_server_port is not None:
            result['RealServerPort'] = self.real_server_port
        if self.slb_apid is not None:
            result['SlbAPId'] = self.slb_apid
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.ssl_cert_id is not None:
            result['SslCertId'] = self.ssl_cert_id
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServerPort') is not None:
            self.real_server_port = m.get('RealServerPort')
        if m.get('SlbAPId') is not None:
            self.slb_apid = m.get('SlbAPId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SslCertId') is not None:
            self.ssl_cert_id = m.get('SslCertId')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        return self


class DescribeSlbAPDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeSlbAPDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeSlbAPDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeSlbAPDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSlbAPDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlbAPDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlbAPDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlbAPDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstTransInfoRequest(TeaModel):
    def __init__(self, aliyun_commodity_code=None, aliyun_equip_id=None, aliyun_uid=None):
        self.aliyun_commodity_code = aliyun_commodity_code  # type: str
        self.aliyun_equip_id = aliyun_equip_id  # type: str
        self.aliyun_uid = aliyun_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstTransInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_commodity_code is not None:
            result['aliyunCommodityCode'] = self.aliyun_commodity_code
        if self.aliyun_equip_id is not None:
            result['aliyunEquipId'] = self.aliyun_equip_id
        if self.aliyun_uid is not None:
            result['aliyunUid'] = self.aliyun_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunCommodityCode') is not None:
            self.aliyun_commodity_code = m.get('aliyunCommodityCode')
        if m.get('aliyunEquipId') is not None:
            self.aliyun_equip_id = m.get('aliyunEquipId')
        if m.get('aliyunUid') is not None:
            self.aliyun_uid = m.get('aliyunUid')
        return self


class GetInstTransInfoResponseBody(TeaModel):
    def __init__(self, charge_type=None, end_time=None, instance_id=None, is_auto_renew=None, renew_cycle=None,
                 start_time=None):
        self.charge_type = charge_type  # type: str
        self.end_time = end_time  # type: long
        self.instance_id = instance_id  # type: str
        self.is_auto_renew = is_auto_renew  # type: bool
        self.renew_cycle = renew_cycle  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstTransInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_auto_renew is not None:
            result['isAutoRenew'] = self.is_auto_renew
        if self.renew_cycle is not None:
            result['renewCycle'] = self.renew_cycle
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isAutoRenew') is not None:
            self.is_auto_renew = m.get('isAutoRenew')
        if m.get('renewCycle') is not None:
            self.renew_cycle = m.get('renewCycle')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetInstTransInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstTransInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstTransInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstTransInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRdsBackUpRequest(TeaModel):
    def __init__(self, backup_id=None, backup_type=None, db_instance_id=None, page_number=None, page_size=None):
        self.backup_id = backup_id  # type: str
        self.backup_type = backup_type  # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRdsBackUpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRdsBackUpResponseBodyResultItems(TeaModel):
    def __init__(self, backup_dbnames=None, backup_end_time=None, backup_extraction_status=None, backup_id=None,
                 backup_location=None, backup_method=None, backup_mode=None, backup_scale=None, backup_size=None,
                 backup_start_time=None, backup_status=None, backup_type=None, dbinstance_id=None, host_instance_id=None,
                 meta_status=None, store_status=None, total_backup_size=None):
        self.backup_dbnames = backup_dbnames  # type: str
        self.backup_end_time = backup_end_time  # type: str
        self.backup_extraction_status = backup_extraction_status  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_location = backup_location  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_scale = backup_scale  # type: str
        self.backup_size = backup_size  # type: long
        self.backup_start_time = backup_start_time  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_type = backup_type  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.host_instance_id = host_instance_id  # type: str
        self.meta_status = meta_status  # type: str
        self.store_status = store_status  # type: str
        self.total_backup_size = total_backup_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRdsBackUpResponseBodyResultItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_extraction_status is not None:
            result['BackupExtractionStatus'] = self.backup_extraction_status
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_location is not None:
            result['BackupLocation'] = self.backup_location
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_scale is not None:
            result['BackupScale'] = self.backup_scale
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.host_instance_id is not None:
            result['HostInstanceID'] = self.host_instance_id
        if self.meta_status is not None:
            result['MetaStatus'] = self.meta_status
        if self.store_status is not None:
            result['StoreStatus'] = self.store_status
        if self.total_backup_size is not None:
            result['TotalBackupSize'] = self.total_backup_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupExtractionStatus') is not None:
            self.backup_extraction_status = m.get('BackupExtractionStatus')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupLocation') is not None:
            self.backup_location = m.get('BackupLocation')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupScale') is not None:
            self.backup_scale = m.get('BackupScale')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('HostInstanceID') is not None:
            self.host_instance_id = m.get('HostInstanceID')
        if m.get('MetaStatus') is not None:
            self.meta_status = m.get('MetaStatus')
        if m.get('StoreStatus') is not None:
            self.store_status = m.get('StoreStatus')
        if m.get('TotalBackupSize') is not None:
            self.total_backup_size = m.get('TotalBackupSize')
        return self


class GetRdsBackUpResponseBodyResult(TeaModel):
    def __init__(self, items=None, page_number=None, page_record_count=None, total_backup_size=None,
                 total_record_count=None):
        self.items = items  # type: list[GetRdsBackUpResponseBodyResultItems]
        self.page_number = page_number  # type: str
        self.page_record_count = page_record_count  # type: str
        self.total_backup_size = total_backup_size  # type: long
        self.total_record_count = total_record_count  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRdsBackUpResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_backup_size is not None:
            result['TotalBackupSize'] = self.total_backup_size
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetRdsBackUpResponseBodyResultItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalBackupSize') is not None:
            self.total_backup_size = m.get('TotalBackupSize')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class GetRdsBackUpResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetRdsBackUpResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetRdsBackUpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRdsBackUpResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRdsBackUpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRdsBackUpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRdsBackUpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRdsBackUpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantDbToAccountRequest(TeaModel):
    def __init__(self, account_name=None, account_privilege=None, db_instance_id=None, db_name=None):
        self.account_name = account_name  # type: str
        self.account_privilege = account_privilege  # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.db_name = db_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantDbToAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class GrantDbToAccountResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantDbToAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GrantDbToAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantDbToAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantDbToAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantDbToAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppResponseBodyDataMiddleWareList(TeaModel):
    def __init__(self, app_id=None, code=None, name=None):
        self.app_id = app_id  # type: long
        self.code = code  # type: int
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppResponseBodyDataMiddleWareList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAppResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_state_type=None, biz_name=None, biz_title=None, deploy_type=None,
                 description=None, language=None, middle_ware_list=None, operating_system=None, service_type=None, title=None):
        self.app_id = app_id  # type: long
        self.app_state_type = app_state_type  # type: str
        self.biz_name = biz_name  # type: str
        self.biz_title = biz_title  # type: str
        self.deploy_type = deploy_type  # type: str
        self.description = description  # type: str
        self.language = language  # type: str
        self.middle_ware_list = middle_ware_list  # type: list[ListAppResponseBodyDataMiddleWareList]
        self.operating_system = operating_system  # type: str
        self.service_type = service_type  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.middle_ware_list:
            for k in self.middle_ware_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_state_type is not None:
            result['AppStateType'] = self.app_state_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_title is not None:
            result['BizTitle'] = self.biz_title
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.language is not None:
            result['Language'] = self.language
        result['MiddleWareList'] = []
        if self.middle_ware_list is not None:
            for k in self.middle_ware_list:
                result['MiddleWareList'].append(k.to_map() if k else None)
        if self.operating_system is not None:
            result['OperatingSystem'] = self.operating_system
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppStateType') is not None:
            self.app_state_type = m.get('AppStateType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizTitle') is not None:
            self.biz_title = m.get('BizTitle')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        self.middle_ware_list = []
        if m.get('MiddleWareList') is not None:
            for k in m.get('MiddleWareList'):
                temp_model = ListAppResponseBodyDataMiddleWareList()
                self.middle_ware_list.append(temp_model.from_map(k))
        if m.get('OperatingSystem') is not None:
            self.operating_system = m.get('OperatingSystem')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListAppResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, request_id=None, total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAppResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppCmsGroupsRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, page_number=None, page_size=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppCmsGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppCmsGroupsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[str]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppCmsGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppCmsGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppCmsGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppCmsGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppCmsGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppEnvironmentRequest(TeaModel):
    def __init__(self, app_id=None, env_name=None, env_type=None, page_number=None, page_size=None):
        self.app_id = app_id  # type: long
        self.env_name = env_name  # type: str
        self.env_type = env_type  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppEnvironmentResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_schema_id=None, env_id=None, env_name=None, env_type=None,
                 env_type_name=None, region=None):
        self.app_id = app_id  # type: long
        self.app_schema_id = app_schema_id  # type: long
        self.env_id = env_id  # type: long
        self.env_name = env_name  # type: str
        self.env_type = env_type  # type: int
        self.env_type_name = env_type_name  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_schema_id is not None:
            result['AppSchemaId'] = self.app_schema_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.env_type_name is not None:
            result['EnvTypeName'] = self.env_type_name
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSchemaId') is not None:
            self.app_schema_id = m.get('AppSchemaId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('EnvTypeName') is not None:
            self.env_type_name = m.get('EnvTypeName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListAppEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAppEnvironmentResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppEnvironmentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupRequest(TeaModel):
    def __init__(self, biz_code=None, page_number=None, page_size=None):
        self.biz_code = biz_code  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppGroupResponseBodyData(TeaModel):
    def __init__(self, biz_name=None, id=None, name=None):
        self.biz_name = biz_name  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAppGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAppGroupResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupMappingRequest(TeaModel):
    def __init__(self, biz_code=None, name=None, page_number=None, page_size=None):
        self.biz_code = biz_code  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupMappingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppGroupMappingResponseBodyData(TeaModel):
    def __init__(self, app_id=None, group_id=None, id=None, name=None):
        self.app_id = app_id  # type: long
        self.group_id = group_id  # type: long
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupMappingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAppGroupMappingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAppGroupMappingResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppGroupMappingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppGroupMappingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppGroupMappingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppGroupMappingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppGroupMappingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppGroupMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstanceRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, page_number=None, page_size=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppInstanceResponseBodyData(TeaModel):
    def __init__(self, app_instance_id=None, create_time=None, health=None, host_ip=None, limits=None, pod_ip=None,
                 requests=None, restart_count=None, spec=None, status=None, version=None):
        self.app_instance_id = app_instance_id  # type: str
        self.create_time = create_time  # type: str
        self.health = health  # type: str
        self.host_ip = host_ip  # type: str
        self.limits = limits  # type: str
        self.pod_ip = pod_ip  # type: str
        self.requests = requests  # type: str
        self.restart_count = restart_count  # type: int
        self.spec = spec  # type: str
        self.status = status  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.health is not None:
            result['Health'] = self.health
        if self.host_ip is not None:
            result['HostIp'] = self.host_ip
        if self.limits is not None:
            result['Limits'] = self.limits
        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip
        if self.requests is not None:
            result['Requests'] = self.requests
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Health') is not None:
            self.health = m.get('Health')
        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')
        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')
        if m.get('Requests') is not None:
            self.requests = m.get('Requests')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAppInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAppInstanceResponseBodyData]
        self.err_msg = err_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppResourceAllocsRequest(TeaModel):
    def __init__(self, app_env_id=None, app_id=None, cluster_id=None, page_number=None, page_size=None):
        self.app_env_id = app_env_id  # type: long
        self.app_id = app_id  # type: long
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppResourceAllocsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppResourceAllocsResponseBodyData(TeaModel):
    def __init__(self, app_env_id=None, app_id=None, cluster_id=None, id=None, resource_def=None):
        self.app_env_id = app_env_id  # type: long
        self.app_id = app_id  # type: long
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: long
        self.resource_def = resource_def  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppResourceAllocsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_def is not None:
            result['ResourceDef'] = self.resource_def
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceDef') is not None:
            self.resource_def = m.get('ResourceDef')
        return self


class ListAppResourceAllocsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAppResourceAllocsResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppResourceAllocsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppResourceAllocsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppResourceAllocsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppResourceAllocsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppResourceAllocsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAppResourceAllocsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableClusterNodeRequest(TeaModel):
    def __init__(self, cluster_instance_id=None, page_num=None, page_size=None):
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableClusterNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAvailableClusterNodeResponseBodyData(TeaModel):
    def __init__(self, business_code=None, ecs_configuration=None, ecs_cpu=None, ecs_eip=None,
                 ecs_expired_time=None, ecs_local_storage_capacity=None, ecs_memory=None, ecs_os_type=None, ecs_private_ip=None,
                 ecs_public_ip=None, ecs_zone=None, instance_id=None, instance_name=None, instance_network_type=None,
                 instance_type=None, internet_max_bandwidth_in=None, internet_max_bandwidth_out=None, osname=None,
                 region_id=None, vpc_id=None):
        self.business_code = business_code  # type: str
        self.ecs_configuration = ecs_configuration  # type: str
        self.ecs_cpu = ecs_cpu  # type: str
        self.ecs_eip = ecs_eip  # type: str
        self.ecs_expired_time = ecs_expired_time  # type: str
        self.ecs_local_storage_capacity = ecs_local_storage_capacity  # type: str
        self.ecs_memory = ecs_memory  # type: str
        self.ecs_os_type = ecs_os_type  # type: str
        self.ecs_private_ip = ecs_private_ip  # type: str
        self.ecs_public_ip = ecs_public_ip  # type: str
        self.ecs_zone = ecs_zone  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: str
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: str
        self.osname = osname  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableClusterNodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.ecs_configuration is not None:
            result['EcsConfiguration'] = self.ecs_configuration
        if self.ecs_cpu is not None:
            result['EcsCpu'] = self.ecs_cpu
        if self.ecs_eip is not None:
            result['EcsEip'] = self.ecs_eip
        if self.ecs_expired_time is not None:
            result['EcsExpiredTime'] = self.ecs_expired_time
        if self.ecs_local_storage_capacity is not None:
            result['EcsLocalStorageCapacity'] = self.ecs_local_storage_capacity
        if self.ecs_memory is not None:
            result['EcsMemory'] = self.ecs_memory
        if self.ecs_os_type is not None:
            result['EcsOsType'] = self.ecs_os_type
        if self.ecs_private_ip is not None:
            result['EcsPrivateIp'] = self.ecs_private_ip
        if self.ecs_public_ip is not None:
            result['EcsPublicIp'] = self.ecs_public_ip
        if self.ecs_zone is not None:
            result['EcsZone'] = self.ecs_zone
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('EcsConfiguration') is not None:
            self.ecs_configuration = m.get('EcsConfiguration')
        if m.get('EcsCpu') is not None:
            self.ecs_cpu = m.get('EcsCpu')
        if m.get('EcsEip') is not None:
            self.ecs_eip = m.get('EcsEip')
        if m.get('EcsExpiredTime') is not None:
            self.ecs_expired_time = m.get('EcsExpiredTime')
        if m.get('EcsLocalStorageCapacity') is not None:
            self.ecs_local_storage_capacity = m.get('EcsLocalStorageCapacity')
        if m.get('EcsMemory') is not None:
            self.ecs_memory = m.get('EcsMemory')
        if m.get('EcsOsType') is not None:
            self.ecs_os_type = m.get('EcsOsType')
        if m.get('EcsPrivateIp') is not None:
            self.ecs_private_ip = m.get('EcsPrivateIp')
        if m.get('EcsPublicIp') is not None:
            self.ecs_public_ip = m.get('EcsPublicIp')
        if m.get('EcsZone') is not None:
            self.ecs_zone = m.get('EcsZone')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListAvailableClusterNodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListAvailableClusterNodeResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableClusterNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAvailableClusterNodeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAvailableClusterNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAvailableClusterNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableClusterNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAvailableClusterNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterRequest(TeaModel):
    def __init__(self, business_code=None, env_type=None, page_num=None, page_size=None):
        self.business_code = business_code  # type: str
        self.env_type = env_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListClusterResponseBodyData(TeaModel):
    def __init__(self, business_code=None, cluster_title=None, create_status=None, ecs_ids=None, env_type=None,
                 id=None, instance_id=None, key_pair=None, net_plug=None, password=None, pod_cidr=None, region_id=None,
                 region_name=None, service_cidr=None, status=None, vpc_id=None, vswitch_ids=None, work_load_cpu=None,
                 work_load_mem=None):
        self.business_code = business_code  # type: str
        self.cluster_title = cluster_title  # type: str
        self.create_status = create_status  # type: str
        self.ecs_ids = ecs_ids  # type: list[str]
        self.env_type = env_type  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str
        self.key_pair = key_pair  # type: str
        self.net_plug = net_plug  # type: str
        self.password = password  # type: str
        self.pod_cidr = pod_cidr  # type: str
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str
        self.service_cidr = service_cidr  # type: str
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_ids = vswitch_ids  # type: list[str]
        self.work_load_cpu = work_load_cpu  # type: str
        self.work_load_mem = work_load_mem  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.cluster_title is not None:
            result['ClusterTitle'] = self.cluster_title
        if self.create_status is not None:
            result['CreateStatus'] = self.create_status
        if self.ecs_ids is not None:
            result['EcsIds'] = self.ecs_ids
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_pair is not None:
            result['KeyPair'] = self.key_pair
        if self.net_plug is not None:
            result['NetPlug'] = self.net_plug
        if self.password is not None:
            result['Password'] = self.password
        if self.pod_cidr is not None:
            result['PodCIDR'] = self.pod_cidr
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.service_cidr is not None:
            result['ServiceCIDR'] = self.service_cidr
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids
        if self.work_load_cpu is not None:
            result['WorkLoadCpu'] = self.work_load_cpu
        if self.work_load_mem is not None:
            result['WorkLoadMem'] = self.work_load_mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('ClusterTitle') is not None:
            self.cluster_title = m.get('ClusterTitle')
        if m.get('CreateStatus') is not None:
            self.create_status = m.get('CreateStatus')
        if m.get('EcsIds') is not None:
            self.ecs_ids = m.get('EcsIds')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyPair') is not None:
            self.key_pair = m.get('KeyPair')
        if m.get('NetPlug') is not None:
            self.net_plug = m.get('NetPlug')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PodCIDR') is not None:
            self.pod_cidr = m.get('PodCIDR')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ServiceCIDR') is not None:
            self.service_cidr = m.get('ServiceCIDR')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')
        if m.get('WorkLoadCpu') is not None:
            self.work_load_cpu = m.get('WorkLoadCpu')
        if m.get('WorkLoadMem') is not None:
            self.work_load_mem = m.get('WorkLoadMem')
        return self


class ListClusterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListClusterResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterNodeRequest(TeaModel):
    def __init__(self, cluster_instance_id=None, page_num=None, page_size=None):
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListClusterNodeResponseBodyData(TeaModel):
    def __init__(self, business_code=None, ecs_configuration=None, ecs_cpu=None, ecs_eip=None,
                 ecs_expired_time=None, ecs_local_storage_capacity=None, ecs_memory=None, ecs_os_type=None, ecs_private_ip=None,
                 ecs_public_ip=None, ecs_zone=None, instance_id=None, instance_name=None, instance_network_type=None,
                 instance_type=None, internet_max_bandwidth_in=None, internet_max_bandwidth_out=None, osname=None,
                 region_id=None, vpc_id=None):
        self.business_code = business_code  # type: str
        self.ecs_configuration = ecs_configuration  # type: str
        self.ecs_cpu = ecs_cpu  # type: str
        self.ecs_eip = ecs_eip  # type: str
        self.ecs_expired_time = ecs_expired_time  # type: str
        self.ecs_local_storage_capacity = ecs_local_storage_capacity  # type: str
        self.ecs_memory = ecs_memory  # type: str
        self.ecs_os_type = ecs_os_type  # type: str
        self.ecs_private_ip = ecs_private_ip  # type: str
        self.ecs_public_ip = ecs_public_ip  # type: str
        self.ecs_zone = ecs_zone  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: str
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: str
        self.osname = osname  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterNodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.ecs_configuration is not None:
            result['EcsConfiguration'] = self.ecs_configuration
        if self.ecs_cpu is not None:
            result['EcsCpu'] = self.ecs_cpu
        if self.ecs_eip is not None:
            result['EcsEip'] = self.ecs_eip
        if self.ecs_expired_time is not None:
            result['EcsExpiredTime'] = self.ecs_expired_time
        if self.ecs_local_storage_capacity is not None:
            result['EcsLocalStorageCapacity'] = self.ecs_local_storage_capacity
        if self.ecs_memory is not None:
            result['EcsMemory'] = self.ecs_memory
        if self.ecs_os_type is not None:
            result['EcsOsType'] = self.ecs_os_type
        if self.ecs_private_ip is not None:
            result['EcsPrivateIp'] = self.ecs_private_ip
        if self.ecs_public_ip is not None:
            result['EcsPublicIp'] = self.ecs_public_ip
        if self.ecs_zone is not None:
            result['EcsZone'] = self.ecs_zone
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('EcsConfiguration') is not None:
            self.ecs_configuration = m.get('EcsConfiguration')
        if m.get('EcsCpu') is not None:
            self.ecs_cpu = m.get('EcsCpu')
        if m.get('EcsEip') is not None:
            self.ecs_eip = m.get('EcsEip')
        if m.get('EcsExpiredTime') is not None:
            self.ecs_expired_time = m.get('EcsExpiredTime')
        if m.get('EcsLocalStorageCapacity') is not None:
            self.ecs_local_storage_capacity = m.get('EcsLocalStorageCapacity')
        if m.get('EcsMemory') is not None:
            self.ecs_memory = m.get('EcsMemory')
        if m.get('EcsOsType') is not None:
            self.ecs_os_type = m.get('EcsOsType')
        if m.get('EcsPrivateIp') is not None:
            self.ecs_private_ip = m.get('EcsPrivateIp')
        if m.get('EcsPublicIp') is not None:
            self.ecs_public_ip = m.get('EcsPublicIp')
        if m.get('EcsZone') is not None:
            self.ecs_zone = m.get('EcsZone')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListClusterNodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListClusterNodeResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterNodeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClusterNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployConfigRequest(TeaModel):
    def __init__(self, app_id=None, env_type=None, id=None, name=None):
        self.app_id = app_id  # type: long
        self.env_type = env_type  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListDeployConfigResponseBodyDataContainerCodePath(TeaModel):
    def __init__(self, code_path=None):
        self.code_path = code_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployConfigResponseBodyDataContainerCodePath, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_path is not None:
            result['CodePath'] = self.code_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodePath') is not None:
            self.code_path = m.get('CodePath')
        return self


class ListDeployConfigResponseBodyDataContainerYamlConf(TeaModel):
    def __init__(self, config_map=None, config_map_list=None, cron_job=None, deployment=None, secret_list=None,
                 stateful_set=None):
        self.config_map = config_map  # type: str
        self.config_map_list = config_map_list  # type: list[str]
        self.cron_job = cron_job  # type: str
        self.deployment = deployment  # type: str
        self.secret_list = secret_list  # type: list[str]
        self.stateful_set = stateful_set  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployConfigResponseBodyDataContainerYamlConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map is not None:
            result['ConfigMap'] = self.config_map
        if self.config_map_list is not None:
            result['ConfigMapList'] = self.config_map_list
        if self.cron_job is not None:
            result['CronJob'] = self.cron_job
        if self.deployment is not None:
            result['Deployment'] = self.deployment
        if self.secret_list is not None:
            result['SecretList'] = self.secret_list
        if self.stateful_set is not None:
            result['StatefulSet'] = self.stateful_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMap') is not None:
            self.config_map = m.get('ConfigMap')
        if m.get('ConfigMapList') is not None:
            self.config_map_list = m.get('ConfigMapList')
        if m.get('CronJob') is not None:
            self.cron_job = m.get('CronJob')
        if m.get('Deployment') is not None:
            self.deployment = m.get('Deployment')
        if m.get('SecretList') is not None:
            self.secret_list = m.get('SecretList')
        if m.get('StatefulSet') is not None:
            self.stateful_set = m.get('StatefulSet')
        return self


class ListDeployConfigResponseBodyData(TeaModel):
    def __init__(self, app_id=None, container_code_path=None, container_yaml_conf=None, env_type=None, id=None,
                 name=None):
        self.app_id = app_id  # type: long
        self.container_code_path = container_code_path  # type: ListDeployConfigResponseBodyDataContainerCodePath
        self.container_yaml_conf = container_yaml_conf  # type: ListDeployConfigResponseBodyDataContainerYamlConf
        self.env_type = env_type  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        if self.container_code_path:
            self.container_code_path.validate()
        if self.container_yaml_conf:
            self.container_yaml_conf.validate()

    def to_map(self):
        _map = super(ListDeployConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.container_code_path is not None:
            result['ContainerCodePath'] = self.container_code_path.to_map()
        if self.container_yaml_conf is not None:
            result['ContainerYamlConf'] = self.container_yaml_conf.to_map()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ContainerCodePath') is not None:
            temp_model = ListDeployConfigResponseBodyDataContainerCodePath()
            self.container_code_path = temp_model.from_map(m['ContainerCodePath'])
        if m.get('ContainerYamlConf') is not None:
            temp_model = ListDeployConfigResponseBodyDataContainerYamlConf()
            self.container_yaml_conf = temp_model.from_map(m['ContainerYamlConf'])
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListDeployConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListDeployConfigResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeployConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeployConfigResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeployConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeployConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeployConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeployConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployOrdersRequest(TeaModel):
    def __init__(self, app_id=None, deploy_category=None, deploy_type=None, end_time_greater_than=None,
                 end_time_greater_than_or_equal_to=None, end_time_less_than=None, end_time_less_than_or_equal_to=None, env_id=None, env_type=None,
                 page_number=None, page_size=None, partition_type=None, pause_type=None, result_list=None,
                 start_time_greater_than=None, start_time_greater_than_or_equal_to=None, start_time_less_than=None,
                 start_time_less_than_or_equal_to=None, status=None, status_list=None):
        self.app_id = app_id  # type: long
        self.deploy_category = deploy_category  # type: str
        self.deploy_type = deploy_type  # type: str
        self.end_time_greater_than = end_time_greater_than  # type: str
        self.end_time_greater_than_or_equal_to = end_time_greater_than_or_equal_to  # type: str
        self.end_time_less_than = end_time_less_than  # type: str
        self.end_time_less_than_or_equal_to = end_time_less_than_or_equal_to  # type: str
        self.env_id = env_id  # type: long
        self.env_type = env_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.partition_type = partition_type  # type: str
        self.pause_type = pause_type  # type: str
        self.result_list = result_list  # type: list[int]
        self.start_time_greater_than = start_time_greater_than  # type: str
        self.start_time_greater_than_or_equal_to = start_time_greater_than_or_equal_to  # type: str
        self.start_time_less_than = start_time_less_than  # type: str
        self.start_time_less_than_or_equal_to = start_time_less_than_or_equal_to  # type: str
        self.status = status  # type: int
        self.status_list = status_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.deploy_category is not None:
            result['DeployCategory'] = self.deploy_category
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.end_time_greater_than is not None:
            result['EndTimeGreaterThan'] = self.end_time_greater_than
        if self.end_time_greater_than_or_equal_to is not None:
            result['EndTimeGreaterThanOrEqualTo'] = self.end_time_greater_than_or_equal_to
        if self.end_time_less_than is not None:
            result['EndTimeLessThan'] = self.end_time_less_than
        if self.end_time_less_than_or_equal_to is not None:
            result['EndTimeLessThanOrEqualTo'] = self.end_time_less_than_or_equal_to
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        if self.pause_type is not None:
            result['PauseType'] = self.pause_type
        if self.result_list is not None:
            result['ResultList'] = self.result_list
        if self.start_time_greater_than is not None:
            result['StartTimeGreaterThan'] = self.start_time_greater_than
        if self.start_time_greater_than_or_equal_to is not None:
            result['StartTimeGreaterThanOrEqualTo'] = self.start_time_greater_than_or_equal_to
        if self.start_time_less_than is not None:
            result['StartTimeLessThan'] = self.start_time_less_than
        if self.start_time_less_than_or_equal_to is not None:
            result['StartTimeLessThanOrEqualTo'] = self.start_time_less_than_or_equal_to
        if self.status is not None:
            result['Status'] = self.status
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeployCategory') is not None:
            self.deploy_category = m.get('DeployCategory')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('EndTimeGreaterThan') is not None:
            self.end_time_greater_than = m.get('EndTimeGreaterThan')
        if m.get('EndTimeGreaterThanOrEqualTo') is not None:
            self.end_time_greater_than_or_equal_to = m.get('EndTimeGreaterThanOrEqualTo')
        if m.get('EndTimeLessThan') is not None:
            self.end_time_less_than = m.get('EndTimeLessThan')
        if m.get('EndTimeLessThanOrEqualTo') is not None:
            self.end_time_less_than_or_equal_to = m.get('EndTimeLessThanOrEqualTo')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        if m.get('PauseType') is not None:
            self.pause_type = m.get('PauseType')
        if m.get('ResultList') is not None:
            self.result_list = m.get('ResultList')
        if m.get('StartTimeGreaterThan') is not None:
            self.start_time_greater_than = m.get('StartTimeGreaterThan')
        if m.get('StartTimeGreaterThanOrEqualTo') is not None:
            self.start_time_greater_than_or_equal_to = m.get('StartTimeGreaterThanOrEqualTo')
        if m.get('StartTimeLessThan') is not None:
            self.start_time_less_than = m.get('StartTimeLessThan')
        if m.get('StartTimeLessThanOrEqualTo') is not None:
            self.start_time_less_than_or_equal_to = m.get('StartTimeLessThanOrEqualTo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class ListDeployOrdersResponseBodyData(TeaModel):
    def __init__(self, app_instance_type=None, current_partition_num=None, deploy_order_id=None,
                 deploy_pause_type=None, deploy_pause_type_name=None, deploy_type=None, deploy_type_name=None, description=None,
                 elapsed_time=None, end_time=None, env_id=None, env_type=None, failure_rate=None, finish_app_instance_ct=None,
                 name=None, partition_type=None, partition_type_name=None, result=None, result_name=None, schema_id=None,
                 start_time=None, status=None, status_name=None, total_app_instance_ct=None, total_partitions=None,
                 user_id=None, user_nick=None):
        self.app_instance_type = app_instance_type  # type: str
        self.current_partition_num = current_partition_num  # type: int
        self.deploy_order_id = deploy_order_id  # type: long
        self.deploy_pause_type = deploy_pause_type  # type: str
        self.deploy_pause_type_name = deploy_pause_type_name  # type: str
        self.deploy_type = deploy_type  # type: str
        self.deploy_type_name = deploy_type_name  # type: str
        self.description = description  # type: str
        self.elapsed_time = elapsed_time  # type: int
        self.end_time = end_time  # type: str
        self.env_id = env_id  # type: long
        self.env_type = env_type  # type: str
        self.failure_rate = failure_rate  # type: str
        self.finish_app_instance_ct = finish_app_instance_ct  # type: int
        self.name = name  # type: str
        self.partition_type = partition_type  # type: str
        self.partition_type_name = partition_type_name  # type: str
        self.result = result  # type: int
        self.result_name = result_name  # type: str
        self.schema_id = schema_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.status_name = status_name  # type: str
        self.total_app_instance_ct = total_app_instance_ct  # type: int
        self.total_partitions = total_partitions  # type: int
        self.user_id = user_id  # type: str
        self.user_nick = user_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployOrdersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.current_partition_num is not None:
            result['CurrentPartitionNum'] = self.current_partition_num
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        if self.deploy_pause_type is not None:
            result['DeployPauseType'] = self.deploy_pause_type
        if self.deploy_pause_type_name is not None:
            result['DeployPauseTypeName'] = self.deploy_pause_type_name
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.deploy_type_name is not None:
            result['DeployTypeName'] = self.deploy_type_name
        if self.description is not None:
            result['Description'] = self.description
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.failure_rate is not None:
            result['FailureRate'] = self.failure_rate
        if self.finish_app_instance_ct is not None:
            result['FinishAppInstanceCt'] = self.finish_app_instance_ct
        if self.name is not None:
            result['Name'] = self.name
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        if self.partition_type_name is not None:
            result['PartitionTypeName'] = self.partition_type_name
        if self.result is not None:
            result['Result'] = self.result
        if self.result_name is not None:
            result['ResultName'] = self.result_name
        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.total_app_instance_ct is not None:
            result['TotalAppInstanceCt'] = self.total_app_instance_ct
        if self.total_partitions is not None:
            result['TotalPartitions'] = self.total_partitions
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('CurrentPartitionNum') is not None:
            self.current_partition_num = m.get('CurrentPartitionNum')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        if m.get('DeployPauseType') is not None:
            self.deploy_pause_type = m.get('DeployPauseType')
        if m.get('DeployPauseTypeName') is not None:
            self.deploy_pause_type_name = m.get('DeployPauseTypeName')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DeployTypeName') is not None:
            self.deploy_type_name = m.get('DeployTypeName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('FailureRate') is not None:
            self.failure_rate = m.get('FailureRate')
        if m.get('FinishAppInstanceCt') is not None:
            self.finish_app_instance_ct = m.get('FinishAppInstanceCt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        if m.get('PartitionTypeName') is not None:
            self.partition_type_name = m.get('PartitionTypeName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultName') is not None:
            self.result_name = m.get('ResultName')
        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('TotalAppInstanceCt') is not None:
            self.total_app_instance_ct = m.get('TotalAppInstanceCt')
        if m.get('TotalPartitions') is not None:
            self.total_partitions = m.get('TotalPartitions')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class ListDeployOrdersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListDeployOrdersResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeployOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDeployOrdersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeployOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeployOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeployOrdersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeployOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobHistoriesRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, page_number=None, page_size=None, status=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListJobHistoriesResponseBodyData(TeaModel):
    def __init__(self, active_deadline_seconds=None, backoff_limit=None, completion_time=None, completions=None,
                 failed=None, message=None, name=None, parallelism=None, pod_list=None, start_time=None, succeeded=None):
        self.active_deadline_seconds = active_deadline_seconds  # type: int
        self.backoff_limit = backoff_limit  # type: int
        self.completion_time = completion_time  # type: str
        self.completions = completions  # type: int
        self.failed = failed  # type: int
        self.message = message  # type: str
        self.name = name  # type: str
        self.parallelism = parallelism  # type: int
        self.pod_list = pod_list  # type: list[str]
        self.start_time = start_time  # type: str
        self.succeeded = succeeded  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobHistoriesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds
        if self.backoff_limit is not None:
            result['BackoffLimit'] = self.backoff_limit
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.completions is not None:
            result['Completions'] = self.completions
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        if self.pod_list is not None:
            result['PodList'] = self.pod_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')
        if m.get('BackoffLimit') is not None:
            self.backoff_limit = m.get('BackoffLimit')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('Completions') is not None:
            self.completions = m.get('Completions')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        if m.get('PodList') is not None:
            self.pod_list = m.get('PodList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class ListJobHistoriesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListJobHistoriesResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListJobHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobHistoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobHistoriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeLabelBindingsRequest(TeaModel):
    def __init__(self, cluster_id=None, instance_id=None, label_key=None, label_value=None, page_number=None,
                 page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeLabelBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNodeLabelBindingsResponseBodyData(TeaModel):
    def __init__(self, id=None, instance_id=None, instance_type=None, label_key=None, label_value=None):
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeLabelBindingsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class ListNodeLabelBindingsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListNodeLabelBindingsResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeLabelBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNodeLabelBindingsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeLabelBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodeLabelBindingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeLabelBindingsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeLabelBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeLabelsRequest(TeaModel):
    def __init__(self, cluster_id=None, label_key=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.label_key = label_key  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNodeLabelsResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, id=None, label_key=None, label_value=None):
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: long
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeLabelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class ListNodeLabelsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListNodeLabelsResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeLabelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNodeLabelsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodeLabelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeLabelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersistentVolumeRequest(TeaModel):
    def __init__(self, cluster_instance_id=None, page_number=None, page_size=None):
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPersistentVolumeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPersistentVolumeResponseBodyData(TeaModel):
    def __init__(self, access_modes=None, capacity=None, create_time=None, mount_dir=None, name=None, pvc_name=None,
                 reason=None, reclaim_policy=None, status=None, storage_class=None):
        self.access_modes = access_modes  # type: str
        self.capacity = capacity  # type: str
        self.create_time = create_time  # type: str
        self.mount_dir = mount_dir  # type: str
        self.name = name  # type: str
        self.pvc_name = pvc_name  # type: str
        self.reason = reason  # type: str
        self.reclaim_policy = reclaim_policy  # type: str
        self.status = status  # type: str
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPersistentVolumeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['AccessModes'] = self.access_modes
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir
        if self.name is not None:
            result['Name'] = self.name
        if self.pvc_name is not None:
            result['PvcName'] = self.pvc_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reclaim_policy is not None:
            result['ReclaimPolicy'] = self.reclaim_policy
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessModes') is not None:
            self.access_modes = m.get('AccessModes')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PvcName') is not None:
            self.pvc_name = m.get('PvcName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ReclaimPolicy') is not None:
            self.reclaim_policy = m.get('ReclaimPolicy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class ListPersistentVolumeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListPersistentVolumeResponseBodyData]
        self.err_msg = err_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPersistentVolumeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersistentVolumeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPersistentVolumeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPersistentVolumeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPersistentVolumeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPersistentVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPersistentVolumeClaimRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, page_number=None, page_size=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPersistentVolumeClaimRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPersistentVolumeClaimResponseBodyData(TeaModel):
    def __init__(self, access_modes=None, capacity=None, create_time=None, name=None, status=None,
                 storage_class=None, volume_name=None):
        self.access_modes = access_modes  # type: str
        self.capacity = capacity  # type: str
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.status = status  # type: str
        self.storage_class = storage_class  # type: str
        self.volume_name = volume_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPersistentVolumeClaimResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['AccessModes'] = self.access_modes
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessModes') is not None:
            self.access_modes = m.get('AccessModes')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')
        return self


class ListPersistentVolumeClaimResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListPersistentVolumeClaimResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPersistentVolumeClaimResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPersistentVolumeClaimResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPersistentVolumeClaimResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPersistentVolumeClaimResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPersistentVolumeClaimResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPersistentVolumeClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPodsRequest(TeaModel):
    def __init__(self, deploy_order_id=None, page_number=None, page_size=None, result_list=None, status_list=None):
        self.deploy_order_id = deploy_order_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.result_list = result_list  # type: list[int]
        self.status_list = status_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPodsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.result_list is not None:
            result['ResultList'] = self.result_list
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResultList') is not None:
            self.result_list = m.get('ResultList')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class ListPodsResponseBodyDataDeploySteps(TeaModel):
    def __init__(self, status=None, step_code=None, step_name=None):
        self.status = status  # type: str
        self.step_code = step_code  # type: str
        self.step_name = step_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPodsResponseBodyDataDeploySteps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.step_code is not None:
            result['StepCode'] = self.step_code
        if self.step_name is not None:
            result['StepName'] = self.step_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StepCode') is not None:
            self.step_code = m.get('StepCode')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        return self


class ListPodsResponseBodyData(TeaModel):
    def __init__(self, app_instance_id=None, deploy_order_id=None, deploy_partition_num=None, deploy_steps=None,
                 group_name=None, host_ip=None, host_name=None, pod_ip=None, region=None, result=None, result_name=None,
                 start_time=None, status=None, status_name=None, update_time=None):
        self.app_instance_id = app_instance_id  # type: str
        self.deploy_order_id = deploy_order_id  # type: long
        self.deploy_partition_num = deploy_partition_num  # type: int
        self.deploy_steps = deploy_steps  # type: list[ListPodsResponseBodyDataDeploySteps]
        self.group_name = group_name  # type: str
        self.host_ip = host_ip  # type: str
        self.host_name = host_name  # type: str
        self.pod_ip = pod_ip  # type: str
        self.region = region  # type: str
        self.result = result  # type: int
        self.result_name = result_name  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: int
        self.status_name = status_name  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.deploy_steps:
            for k in self.deploy_steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPodsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        if self.deploy_partition_num is not None:
            result['DeployPartitionNum'] = self.deploy_partition_num
        result['DeploySteps'] = []
        if self.deploy_steps is not None:
            for k in self.deploy_steps:
                result['DeploySteps'].append(k.to_map() if k else None)
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.host_ip is not None:
            result['HostIp'] = self.host_ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip
        if self.region is not None:
            result['Region'] = self.region
        if self.result is not None:
            result['Result'] = self.result
        if self.result_name is not None:
            result['ResultName'] = self.result_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        if m.get('DeployPartitionNum') is not None:
            self.deploy_partition_num = m.get('DeployPartitionNum')
        self.deploy_steps = []
        if m.get('DeploySteps') is not None:
            for k in m.get('DeploySteps'):
                temp_model = ListPodsResponseBodyDataDeploySteps()
                self.deploy_steps.append(temp_model.from_map(k))
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultName') is not None:
            self.result_name = m.get('ResultName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPodsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListPodsResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPodsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPodsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPodsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPodsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPodsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, name=None, page_number=None, page_size=None, service_type=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListServicesResponseBodyDataPortMappings(TeaModel):
    def __init__(self, name=None, node_port=None, port=None, protocol=None, target_port=None):
        self.name = name  # type: str
        self.node_port = node_port  # type: int
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.target_port = target_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesResponseBodyDataPortMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class ListServicesResponseBodyData(TeaModel):
    def __init__(self, app_id=None, cluster_ip=None, env_id=None, headless=None, k_8s_service_id=None, name=None,
                 port_mappings=None, service_id=None, service_type=None):
        self.app_id = app_id  # type: long
        self.cluster_ip = cluster_ip  # type: str
        self.env_id = env_id  # type: long
        self.headless = headless  # type: bool
        self.k_8s_service_id = k_8s_service_id  # type: str
        self.name = name  # type: str
        self.port_mappings = port_mappings  # type: list[ListServicesResponseBodyDataPortMappings]
        self.service_id = service_id  # type: long
        self.service_type = service_type  # type: str

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cluster_ip is not None:
            result['ClusterIP'] = self.cluster_ip
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.headless is not None:
            result['Headless'] = self.headless
        if self.k_8s_service_id is not None:
            result['K8sServiceId'] = self.k_8s_service_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ClusterIP') is not None:
            self.cluster_ip = m.get('ClusterIP')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Headless') is not None:
            self.headless = m.get('Headless')
        if m.get('K8sServiceId') is not None:
            self.k_8s_service_id = m.get('K8sServiceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = ListServicesResponseBodyDataPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, cluster_ip=None, code=None, data=None, error_msg=None, page_number=None, page_size=None,
                 request_id=None, total_count=None):
        self.cluster_ip = cluster_ip  # type: str
        self.code = code  # type: int
        self.data = data  # type: list[ListServicesResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ip is not None:
            result['ClusterIP'] = self.cluster_ip
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ClusterIP') is not None:
            self.cluster_ip = m.get('ClusterIP')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlbAPsRequest(TeaModel):
    def __init__(self, app_id=None, env_id=None, name=None, network_mode=None, page_number=None, page_size=None,
                 protocol_list=None, slb_id=None):
        self.app_id = app_id  # type: long
        self.env_id = env_id  # type: long
        self.name = name  # type: str
        self.network_mode = network_mode  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.protocol_list = protocol_list  # type: list[str]
        self.slb_id = slb_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSlbAPsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.name is not None:
            result['Name'] = self.name
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.protocol_list is not None:
            result['ProtocolList'] = self.protocol_list
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProtocolList') is not None:
            self.protocol_list = m.get('ProtocolList')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        return self


class ListSlbAPsResponseBodyData(TeaModel):
    def __init__(self, app_id=None, cookie_timeout=None, env_id=None, established_timeout=None, listener_port=None,
                 name=None, network_mode=None, protocol=None, real_server_port=None, slb_apid=None, slb_id=None,
                 slb_ip=None, ssl_cert_id=None, sticky_session=None):
        self.app_id = app_id  # type: long
        self.cookie_timeout = cookie_timeout  # type: int
        self.env_id = env_id  # type: long
        self.established_timeout = established_timeout  # type: int
        self.listener_port = listener_port  # type: int
        self.name = name  # type: str
        self.network_mode = network_mode  # type: str
        self.protocol = protocol  # type: str
        self.real_server_port = real_server_port  # type: int
        self.slb_apid = slb_apid  # type: long
        self.slb_id = slb_id  # type: str
        self.slb_ip = slb_ip  # type: str
        self.ssl_cert_id = ssl_cert_id  # type: str
        self.sticky_session = sticky_session  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSlbAPsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.name is not None:
            result['Name'] = self.name
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_server_port is not None:
            result['RealServerPort'] = self.real_server_port
        if self.slb_apid is not None:
            result['SlbAPId'] = self.slb_apid
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.ssl_cert_id is not None:
            result['SslCertId'] = self.ssl_cert_id
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServerPort') is not None:
            self.real_server_port = m.get('RealServerPort')
        if m.get('SlbAPId') is not None:
            self.slb_apid = m.get('SlbAPId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SslCertId') is not None:
            self.ssl_cert_id = m.get('SslCertId')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        return self


class ListSlbAPsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListSlbAPsResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSlbAPsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSlbAPsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSlbAPsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSlbAPsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSlbAPsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSlbAPsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(self, real_name=None, user_id=None, user_type=None):
        self.real_name = real_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_msg=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListUsersResponseBodyData]
        self.error_msg = error_msg  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceRequestPortMappings(TeaModel):
    def __init__(self, name=None, node_port=None, port=None, protocol=None, target_port=None):
        self.name = name  # type: str
        self.node_port = node_port  # type: int
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.target_port = target_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyServiceRequestPortMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class ModifyServiceRequest(TeaModel):
    def __init__(self, name=None, port_mappings=None, service_id=None):
        self.name = name  # type: str
        self.port_mappings = port_mappings  # type: list[ModifyServiceRequestPortMappings]
        self.service_id = service_id  # type: long

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = ModifyServiceRequestPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ModifyServiceResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySlbAPRequest(TeaModel):
    def __init__(self, cookie_timeout=None, established_timeout=None, name=None, real_server_port=None,
                 slb_apid=None, ssl_cert_id=None, sticky_session=None):
        self.cookie_timeout = cookie_timeout  # type: int
        self.established_timeout = established_timeout  # type: int
        self.name = name  # type: str
        self.real_server_port = real_server_port  # type: int
        self.slb_apid = slb_apid  # type: long
        self.ssl_cert_id = ssl_cert_id  # type: str
        self.sticky_session = sticky_session  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySlbAPRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout
        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout
        if self.name is not None:
            result['Name'] = self.name
        if self.real_server_port is not None:
            result['RealServerPort'] = self.real_server_port
        if self.slb_apid is not None:
            result['SlbAPId'] = self.slb_apid
        if self.ssl_cert_id is not None:
            result['SslCertId'] = self.ssl_cert_id
        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')
        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RealServerPort') is not None:
            self.real_server_port = m.get('RealServerPort')
        if m.get('SlbAPId') is not None:
            self.slb_apid = m.get('SlbAPId')
        if m.get('SslCertId') is not None:
            self.ssl_cert_id = m.get('SslCertId')
        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')
        return self


class ModifySlbAPResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySlbAPResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySlbAPResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySlbAPResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySlbAPResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifySlbAPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineAppEnvironmentRequest(TeaModel):
    def __init__(self, app_id=None, delete_pvc=None, env_id=None):
        self.app_id = app_id  # type: long
        self.delete_pvc = delete_pvc  # type: bool
        self.env_id = env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineAppEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.delete_pvc is not None:
            result['DeletePvc'] = self.delete_pvc
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeletePvc') is not None:
            self.delete_pvc = m.get('DeletePvc')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class OfflineAppEnvironmentResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineAppEnvironmentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OfflineAppEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: OfflineAppEnvironmentResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(OfflineAppEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = OfflineAppEnvironmentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OfflineAppEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OfflineAppEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OfflineAppEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineAppEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDetailRequest(TeaModel):
    def __init__(self, cluster_instance_id=None):
        self.cluster_instance_id = cluster_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        return self


class QueryClusterDetailResponseBodyResultBasicInfo(TeaModel):
    def __init__(self, business_code=None, cluster_id=None, cluster_instance_id=None, cluster_name=None,
                 ecs_ids=None, env_type=None, has_install_arms_pilot=None, has_install_log_controller=None,
                 install_arms_in_process=None, install_log_in_process=None, main_user_id=None, region_id=None, region_name=None,
                 user_nick=None, vpc_id=None, vswitchs=None):
        self.business_code = business_code  # type: str
        self.cluster_id = cluster_id  # type: long
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.ecs_ids = ecs_ids  # type: list[str]
        self.env_type = env_type  # type: str
        self.has_install_arms_pilot = has_install_arms_pilot  # type: bool
        self.has_install_log_controller = has_install_log_controller  # type: bool
        self.install_arms_in_process = install_arms_in_process  # type: bool
        self.install_log_in_process = install_log_in_process  # type: bool
        self.main_user_id = main_user_id  # type: str
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str
        self.user_nick = user_nick  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitchs = vswitchs  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyResultBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.ecs_ids is not None:
            result['EcsIds'] = self.ecs_ids
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.has_install_arms_pilot is not None:
            result['HasInstallArmsPilot'] = self.has_install_arms_pilot
        if self.has_install_log_controller is not None:
            result['HasInstallLogController'] = self.has_install_log_controller
        if self.install_arms_in_process is not None:
            result['InstallArmsInProcess'] = self.install_arms_in_process
        if self.install_log_in_process is not None:
            result['InstallLogInProcess'] = self.install_log_in_process
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitchs is not None:
            result['Vswitchs'] = self.vswitchs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('EcsIds') is not None:
            self.ecs_ids = m.get('EcsIds')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('HasInstallArmsPilot') is not None:
            self.has_install_arms_pilot = m.get('HasInstallArmsPilot')
        if m.get('HasInstallLogController') is not None:
            self.has_install_log_controller = m.get('HasInstallLogController')
        if m.get('InstallArmsInProcess') is not None:
            self.install_arms_in_process = m.get('InstallArmsInProcess')
        if m.get('InstallLogInProcess') is not None:
            self.install_log_in_process = m.get('InstallLogInProcess')
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Vswitchs') is not None:
            self.vswitchs = m.get('Vswitchs')
        return self


class QueryClusterDetailResponseBodyResultInstanceInfo(TeaModel):
    def __init__(self, allocate_pod_count=None, allocated_pod_info_list=None, app_count=None,
                 available_pod_info_list=None):
        self.allocate_pod_count = allocate_pod_count  # type: int
        self.allocated_pod_info_list = allocated_pod_info_list  # type: list[str]
        self.app_count = app_count  # type: int
        self.available_pod_info_list = available_pod_info_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyResultInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_pod_count is not None:
            result['AllocatePodCount'] = self.allocate_pod_count
        if self.allocated_pod_info_list is not None:
            result['AllocatedPodInfoList'] = self.allocated_pod_info_list
        if self.app_count is not None:
            result['AppCount'] = self.app_count
        if self.available_pod_info_list is not None:
            result['AvailablePodInfoList'] = self.available_pod_info_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocatePodCount') is not None:
            self.allocate_pod_count = m.get('AllocatePodCount')
        if m.get('AllocatedPodInfoList') is not None:
            self.allocated_pod_info_list = m.get('AllocatedPodInfoList')
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')
        if m.get('AvailablePodInfoList') is not None:
            self.available_pod_info_list = m.get('AvailablePodInfoList')
        return self


class QueryClusterDetailResponseBodyResultNetInfo(TeaModel):
    def __init__(self, net_plug_type=None, prod_cidr=None, service_cidr=None):
        self.net_plug_type = net_plug_type  # type: str
        self.prod_cidr = prod_cidr  # type: str
        self.service_cidr = service_cidr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyResultNetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_plug_type is not None:
            result['NetPlugType'] = self.net_plug_type
        if self.prod_cidr is not None:
            result['ProdCIDR'] = self.prod_cidr
        if self.service_cidr is not None:
            result['ServiceCIDR'] = self.service_cidr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetPlugType') is not None:
            self.net_plug_type = m.get('NetPlugType')
        if m.get('ProdCIDR') is not None:
            self.prod_cidr = m.get('ProdCIDR')
        if m.get('ServiceCIDR') is not None:
            self.service_cidr = m.get('ServiceCIDR')
        return self


class QueryClusterDetailResponseBodyResultWorkLoad(TeaModel):
    def __init__(self, all_node_count=None, allocate_all_pod_count=None, allocate_app_pod_count=None,
                 cpu_capacity_total=None, cpu_level=None, cpu_request=None, cpu_request_percent=None, cpu_total=None, cpu_use=None,
                 cpu_use_percent=None, mem_capacity_total=None, mem_level=None, mem_request=None, mem_request_percent=None,
                 mem_total=None, mem_use=None, mem_use_percent=None):
        self.all_node_count = all_node_count  # type: int
        self.allocate_all_pod_count = allocate_all_pod_count  # type: int
        self.allocate_app_pod_count = allocate_app_pod_count  # type: int
        self.cpu_capacity_total = cpu_capacity_total  # type: str
        self.cpu_level = cpu_level  # type: str
        self.cpu_request = cpu_request  # type: str
        self.cpu_request_percent = cpu_request_percent  # type: str
        self.cpu_total = cpu_total  # type: str
        self.cpu_use = cpu_use  # type: str
        self.cpu_use_percent = cpu_use_percent  # type: str
        self.mem_capacity_total = mem_capacity_total  # type: str
        self.mem_level = mem_level  # type: str
        self.mem_request = mem_request  # type: str
        self.mem_request_percent = mem_request_percent  # type: str
        self.mem_total = mem_total  # type: str
        self.mem_use = mem_use  # type: str
        self.mem_use_percent = mem_use_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyResultWorkLoad, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_node_count is not None:
            result['AllNodeCount'] = self.all_node_count
        if self.allocate_all_pod_count is not None:
            result['AllocateAllPodCount'] = self.allocate_all_pod_count
        if self.allocate_app_pod_count is not None:
            result['AllocateAppPodCount'] = self.allocate_app_pod_count
        if self.cpu_capacity_total is not None:
            result['CpuCapacityTotal'] = self.cpu_capacity_total
        if self.cpu_level is not None:
            result['CpuLevel'] = self.cpu_level
        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request
        if self.cpu_request_percent is not None:
            result['CpuRequestPercent'] = self.cpu_request_percent
        if self.cpu_total is not None:
            result['CpuTotal'] = self.cpu_total
        if self.cpu_use is not None:
            result['CpuUse'] = self.cpu_use
        if self.cpu_use_percent is not None:
            result['CpuUsePercent'] = self.cpu_use_percent
        if self.mem_capacity_total is not None:
            result['MemCapacityTotal'] = self.mem_capacity_total
        if self.mem_level is not None:
            result['MemLevel'] = self.mem_level
        if self.mem_request is not None:
            result['MemRequest'] = self.mem_request
        if self.mem_request_percent is not None:
            result['MemRequestPercent'] = self.mem_request_percent
        if self.mem_total is not None:
            result['MemTotal'] = self.mem_total
        if self.mem_use is not None:
            result['MemUse'] = self.mem_use
        if self.mem_use_percent is not None:
            result['MemUsePercent'] = self.mem_use_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllNodeCount') is not None:
            self.all_node_count = m.get('AllNodeCount')
        if m.get('AllocateAllPodCount') is not None:
            self.allocate_all_pod_count = m.get('AllocateAllPodCount')
        if m.get('AllocateAppPodCount') is not None:
            self.allocate_app_pod_count = m.get('AllocateAppPodCount')
        if m.get('CpuCapacityTotal') is not None:
            self.cpu_capacity_total = m.get('CpuCapacityTotal')
        if m.get('CpuLevel') is not None:
            self.cpu_level = m.get('CpuLevel')
        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')
        if m.get('CpuRequestPercent') is not None:
            self.cpu_request_percent = m.get('CpuRequestPercent')
        if m.get('CpuTotal') is not None:
            self.cpu_total = m.get('CpuTotal')
        if m.get('CpuUse') is not None:
            self.cpu_use = m.get('CpuUse')
        if m.get('CpuUsePercent') is not None:
            self.cpu_use_percent = m.get('CpuUsePercent')
        if m.get('MemCapacityTotal') is not None:
            self.mem_capacity_total = m.get('MemCapacityTotal')
        if m.get('MemLevel') is not None:
            self.mem_level = m.get('MemLevel')
        if m.get('MemRequest') is not None:
            self.mem_request = m.get('MemRequest')
        if m.get('MemRequestPercent') is not None:
            self.mem_request_percent = m.get('MemRequestPercent')
        if m.get('MemTotal') is not None:
            self.mem_total = m.get('MemTotal')
        if m.get('MemUse') is not None:
            self.mem_use = m.get('MemUse')
        if m.get('MemUsePercent') is not None:
            self.mem_use_percent = m.get('MemUsePercent')
        return self


class QueryClusterDetailResponseBodyResult(TeaModel):
    def __init__(self, basic_info=None, instance_info=None, net_info=None, node_work_load_list=None, work_load=None):
        self.basic_info = basic_info  # type: QueryClusterDetailResponseBodyResultBasicInfo
        self.instance_info = instance_info  # type: QueryClusterDetailResponseBodyResultInstanceInfo
        self.net_info = net_info  # type: QueryClusterDetailResponseBodyResultNetInfo
        self.node_work_load_list = node_work_load_list  # type: list[str]
        self.work_load = work_load  # type: QueryClusterDetailResponseBodyResultWorkLoad

    def validate(self):
        if self.basic_info:
            self.basic_info.validate()
        if self.instance_info:
            self.instance_info.validate()
        if self.net_info:
            self.net_info.validate()
        if self.work_load:
            self.work_load.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_info is not None:
            result['BasicInfo'] = self.basic_info.to_map()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.net_info is not None:
            result['NetInfo'] = self.net_info.to_map()
        if self.node_work_load_list is not None:
            result['NodeWorkLoadList'] = self.node_work_load_list
        if self.work_load is not None:
            result['WorkLoad'] = self.work_load.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicInfo') is not None:
            temp_model = QueryClusterDetailResponseBodyResultBasicInfo()
            self.basic_info = temp_model.from_map(m['BasicInfo'])
        if m.get('InstanceInfo') is not None:
            temp_model = QueryClusterDetailResponseBodyResultInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('NetInfo') is not None:
            temp_model = QueryClusterDetailResponseBodyResultNetInfo()
            self.net_info = temp_model.from_map(m['NetInfo'])
        if m.get('NodeWorkLoadList') is not None:
            self.node_work_load_list = m.get('NodeWorkLoadList')
        if m.get('WorkLoad') is not None:
            temp_model = QueryClusterDetailResponseBodyResultWorkLoad()
            self.work_load = temp_model.from_map(m['WorkLoad'])
        return self


class QueryClusterDetailResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: QueryClusterDetailResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryClusterDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildAppInstanceRequest(TeaModel):
    def __init__(self, app_id=None, app_instance_id=None, env_id=None):
        self.app_id = app_id  # type: long
        self.app_instance_id = app_instance_id  # type: str
        self.env_id = env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebuildAppInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class RebuildAppInstanceResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebuildAppInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RebuildAppInstanceResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: RebuildAppInstanceResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RebuildAppInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = RebuildAppInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class RebuildAppInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebuildAppInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebuildAppInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebuildAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterNodeRequest(TeaModel):
    def __init__(self, cluster_instance_id=None, ecs_instance_id_list=None):
        self.cluster_instance_id = cluster_instance_id  # type: str
        self.ecs_instance_id_list = ecs_instance_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClusterNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_instance_id is not None:
            result['ClusterInstanceId'] = self.cluster_instance_id
        if self.ecs_instance_id_list is not None:
            result['EcsInstanceIdList'] = self.ecs_instance_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInstanceId') is not None:
            self.cluster_instance_id = m.get('ClusterInstanceId')
        if m.get('EcsInstanceIdList') is not None:
            self.ecs_instance_id_list = m.get('EcsInstanceIdList')
        return self


class RemoveClusterNodeResponseBodyResult(TeaModel):
    def __init__(self, nonsense=None):
        self.nonsense = nonsense  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClusterNodeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonsense is not None:
            result['Nonsense'] = self.nonsense
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Nonsense') is not None:
            self.nonsense = m.get('Nonsense')
        return self


class RemoveClusterNodeResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: RemoveClusterNodeResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RemoveClusterNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = RemoveClusterNodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveClusterNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveClusterNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveClusterNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveClusterNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, account_name=None, account_password=None, db_instance_id=None):
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.db_instance_id = db_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetAccountPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetAccountPasswordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResourceStatusNotifyRequest(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResourceStatusNotifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ResourceStatusNotifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(ResourceStatusNotifyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RestartAppInstanceRequest(TeaModel):
    def __init__(self, app_id=None, app_instance_id_list=None, env_id=None):
        self.app_id = app_id  # type: long
        self.app_instance_id_list = app_instance_id_list  # type: list[long]
        self.env_id = env_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartAppInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class RestartAppInstanceResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartAppInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RestartAppInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartAppInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartAppInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeDeployRequest(TeaModel):
    def __init__(self, deploy_order_id=None):
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeDeployRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class ResumeDeployResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeDeployResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeDeployResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeDeployResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeDeployResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeDeployResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleAppRequest(TeaModel):
    def __init__(self, env_id=None, replicas=None, total_partitions=None):
        self.env_id = env_id  # type: long
        self.replicas = replicas  # type: int
        self.total_partitions = total_partitions  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.total_partitions is not None:
            result['TotalPartitions'] = self.total_partitions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('TotalPartitions') is not None:
            self.total_partitions = m.get('TotalPartitions')
        return self


class ScaleAppResponseBodyResult(TeaModel):
    def __init__(self, admitted=None, business_code=None, deploy_order_id=None):
        self.admitted = admitted  # type: bool
        self.business_code = business_code  # type: str
        self.deploy_order_id = deploy_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admitted is not None:
            result['Admitted'] = self.admitted
        if self.business_code is not None:
            result['BusinessCode'] = self.business_code
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Admitted') is not None:
            self.admitted = m.get('Admitted')
        if m.get('BusinessCode') is not None:
            self.business_code = m.get('BusinessCode')
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        return self


class ScaleAppResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: ScaleAppResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ScaleAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ScaleAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScaleAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScaleAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeployPauseTypeRequest(TeaModel):
    def __init__(self, deploy_order_id=None, deploy_pause_type=None):
        self.deploy_order_id = deploy_order_id  # type: long
        self.deploy_pause_type = deploy_pause_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeployPauseTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order_id is not None:
            result['DeployOrderId'] = self.deploy_order_id
        if self.deploy_pause_type is not None:
            result['DeployPauseType'] = self.deploy_pause_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployOrderId') is not None:
            self.deploy_order_id = m.get('DeployOrderId')
        if m.get('DeployPauseType') is not None:
            self.deploy_pause_type = m.get('DeployPauseType')
        return self


class SetDeployPauseTypeResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeployPauseTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDeployPauseTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDeployPauseTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDeployPauseTypeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetDeployPauseTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInfoRequestEcsDescList(TeaModel):
    def __init__(self, app_type=None, bussiness_desc=None, bussiness_type=None, env_type=None,
                 middle_ware_desc=None, other_middle_ware_desc=None, resource_id=None, user_id=None):
        self.app_type = app_type  # type: str
        self.bussiness_desc = bussiness_desc  # type: str
        self.bussiness_type = bussiness_type  # type: str
        self.env_type = env_type  # type: str
        self.middle_ware_desc = middle_ware_desc  # type: str
        self.other_middle_ware_desc = other_middle_ware_desc  # type: str
        self.resource_id = resource_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitInfoRequestEcsDescList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.bussiness_desc is not None:
            result['BussinessDesc'] = self.bussiness_desc
        if self.bussiness_type is not None:
            result['BussinessType'] = self.bussiness_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.middle_ware_desc is not None:
            result['MiddleWareDesc'] = self.middle_ware_desc
        if self.other_middle_ware_desc is not None:
            result['OtherMiddleWareDesc'] = self.other_middle_ware_desc
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BussinessDesc') is not None:
            self.bussiness_desc = m.get('BussinessDesc')
        if m.get('BussinessType') is not None:
            self.bussiness_type = m.get('BussinessType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('MiddleWareDesc') is not None:
            self.middle_ware_desc = m.get('MiddleWareDesc')
        if m.get('OtherMiddleWareDesc') is not None:
            self.other_middle_ware_desc = m.get('OtherMiddleWareDesc')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SubmitInfoRequest(TeaModel):
    def __init__(self, caller_uid=None, ecs_desc_list=None, main_user_id=None, request_id=None):
        self.caller_uid = caller_uid  # type: long
        self.ecs_desc_list = ecs_desc_list  # type: list[SubmitInfoRequestEcsDescList]
        self.main_user_id = main_user_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ecs_desc_list:
            for k in self.ecs_desc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubmitInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        result['EcsDescList'] = []
        if self.ecs_desc_list is not None:
            for k in self.ecs_desc_list:
                result['EcsDescList'].append(k.to_map() if k else None)
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        self.ecs_desc_list = []
        if m.get('EcsDescList') is not None:
            for k in m.get('EcsDescList'):
                temp_model = SubmitInfoRequestEcsDescList()
                self.ecs_desc_list.append(temp_model.from_map(k))
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitInfoResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncPodInfoRequest(TeaModel):
    def __init__(self, pod_name=None, reason=None, request_id=None, side_car_type=None, status=None, task_id=None):
        self.pod_name = pod_name  # type: str
        self.reason = reason  # type: str
        self.request_id = request_id  # type: str
        self.side_car_type = side_car_type  # type: str
        self.status = status  # type: bool
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncPodInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.side_car_type is not None:
            result['SideCarType'] = self.side_car_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SideCarType') is not None:
            self.side_car_type = m.get('SideCarType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SyncPodInfoResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncPodInfoResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncPodInfoResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: SyncPodInfoResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(SyncPodInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SyncPodInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SyncPodInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncPodInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncPodInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncPodInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindGroupRequest(TeaModel):
    def __init__(self, app_id=None, biz_code=None, name=None):
        self.app_id = app_id  # type: long
        self.biz_code = biz_code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UnbindGroupResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindGroupResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UnbindGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UnbindGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UnbindGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UnbindGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindNodeLabelRequest(TeaModel):
    def __init__(self, cluster_id=None, instance_id=None, label_key=None, label_value=None):
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str
        self.label_key = label_key  # type: str
        self.label_value = label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindNodeLabelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class UnbindNodeLabelResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindNodeLabelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindNodeLabelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindNodeLabelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindNodeLabelResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindNodeLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequestUserRoles(TeaModel):
    def __init__(self, role_name=None, user_id=None, user_type=None):
        self.role_name = role_name  # type: str
        self.user_id = user_id  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppRequestUserRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class UpdateAppRequest(TeaModel):
    def __init__(self, app_id=None, biz_title=None, description=None, language=None, middle_ware_id_list=None,
                 operating_system=None, service_type=None, user_roles=None):
        self.app_id = app_id  # type: long
        self.biz_title = biz_title  # type: str
        self.description = description  # type: str
        self.language = language  # type: str
        self.middle_ware_id_list = middle_ware_id_list  # type: list[int]
        self.operating_system = operating_system  # type: str
        self.service_type = service_type  # type: str
        self.user_roles = user_roles  # type: list[UpdateAppRequestUserRoles]

    def validate(self):
        if self.user_roles:
            for k in self.user_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_title is not None:
            result['BizTitle'] = self.biz_title
        if self.description is not None:
            result['Description'] = self.description
        if self.language is not None:
            result['Language'] = self.language
        if self.middle_ware_id_list is not None:
            result['MiddleWareIdList'] = self.middle_ware_id_list
        if self.operating_system is not None:
            result['OperatingSystem'] = self.operating_system
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['UserRoles'] = []
        if self.user_roles is not None:
            for k in self.user_roles:
                result['UserRoles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizTitle') is not None:
            self.biz_title = m.get('BizTitle')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MiddleWareIdList') is not None:
            self.middle_ware_id_list = m.get('MiddleWareIdList')
        if m.get('OperatingSystem') is not None:
            self.operating_system = m.get('OperatingSystem')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.user_roles = []
        if m.get('UserRoles') is not None:
            for k in m.get('UserRoles'):
                temp_model = UpdateAppRequestUserRoles()
                self.user_roles.append(temp_model.from_map(k))
        return self


class UpdateAppResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateAppResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppMonitorsRequest(TeaModel):
    def __init__(self, main_user_id=None, monitor_ids=None, silence_time=None, template_id=None):
        self.main_user_id = main_user_id  # type: long
        self.monitor_ids = monitor_ids  # type: list[long]
        self.silence_time = silence_time  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppMonitorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id
        if self.monitor_ids is not None:
            result['MonitorIds'] = self.monitor_ids
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')
        if m.get('MonitorIds') is not None:
            self.monitor_ids = m.get('MonitorIds')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateAppMonitorsResponseBody(TeaModel):
    def __init__(self, code=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppMonitorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAppMonitorsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppMonitorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppMonitorsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppMonitorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeployConfigRequest(TeaModel):
    def __init__(self, app_id=None, code_path=None, config_map=None, config_map_list=None, cron_job=None,
                 deployment=None, id=None, secret_list=None, stateful_set=None):
        self.app_id = app_id  # type: long
        self.code_path = code_path  # type: str
        self.config_map = config_map  # type: str
        self.config_map_list = config_map_list  # type: list[str]
        self.cron_job = cron_job  # type: str
        self.deployment = deployment  # type: str
        self.id = id  # type: long
        self.secret_list = secret_list  # type: list[str]
        self.stateful_set = stateful_set  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDeployConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code_path is not None:
            result['CodePath'] = self.code_path
        if self.config_map is not None:
            result['ConfigMap'] = self.config_map
        if self.config_map_list is not None:
            result['ConfigMapList'] = self.config_map_list
        if self.cron_job is not None:
            result['CronJob'] = self.cron_job
        if self.deployment is not None:
            result['Deployment'] = self.deployment
        if self.id is not None:
            result['Id'] = self.id
        if self.secret_list is not None:
            result['SecretList'] = self.secret_list
        if self.stateful_set is not None:
            result['StatefulSet'] = self.stateful_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CodePath') is not None:
            self.code_path = m.get('CodePath')
        if m.get('ConfigMap') is not None:
            self.config_map = m.get('ConfigMap')
        if m.get('ConfigMapList') is not None:
            self.config_map_list = m.get('ConfigMapList')
        if m.get('CronJob') is not None:
            self.cron_job = m.get('CronJob')
        if m.get('Deployment') is not None:
            self.deployment = m.get('Deployment')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SecretList') is not None:
            self.secret_list = m.get('SecretList')
        if m.get('StatefulSet') is not None:
            self.stateful_set = m.get('StatefulSet')
        return self


class UpdateDeployConfigResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDeployConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDeployConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateDeployConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateDeployConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateDeployConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateDeployConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDeployConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDeployConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDeployConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEciConfigRequest(TeaModel):
    def __init__(self, app_env_id=None, eip_bandwidth=None, enable_eci_schedule_policy=None, mirror_cache=None,
                 normal_instance_limit=None, schedule_virtual_node=None):
        self.app_env_id = app_env_id  # type: long
        self.eip_bandwidth = eip_bandwidth  # type: int
        self.enable_eci_schedule_policy = enable_eci_schedule_policy  # type: bool
        self.mirror_cache = mirror_cache  # type: bool
        self.normal_instance_limit = normal_instance_limit  # type: int
        self.schedule_virtual_node = schedule_virtual_node  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEciConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth
        if self.enable_eci_schedule_policy is not None:
            result['EnableEciSchedulePolicy'] = self.enable_eci_schedule_policy
        if self.mirror_cache is not None:
            result['MirrorCache'] = self.mirror_cache
        if self.normal_instance_limit is not None:
            result['NormalInstanceLimit'] = self.normal_instance_limit
        if self.schedule_virtual_node is not None:
            result['ScheduleVirtualNode'] = self.schedule_virtual_node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')
        if m.get('EnableEciSchedulePolicy') is not None:
            self.enable_eci_schedule_policy = m.get('EnableEciSchedulePolicy')
        if m.get('MirrorCache') is not None:
            self.mirror_cache = m.get('MirrorCache')
        if m.get('NormalInstanceLimit') is not None:
            self.normal_instance_limit = m.get('NormalInstanceLimit')
        if m.get('ScheduleVirtualNode') is not None:
            self.schedule_virtual_node = m.get('ScheduleVirtualNode')
        return self


class UpdateEciConfigResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEciConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEciConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateEciConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateEciConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateEciConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateEciConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEciConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEciConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEciConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(self, app_env_id=None, app_id=None, app_schema_id=None, replicas=None):
        self.app_env_id = app_env_id  # type: long
        self.app_id = app_id  # type: long
        self.app_schema_id = app_schema_id  # type: long
        self.replicas = replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_env_id is not None:
            result['AppEnvId'] = self.app_env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_schema_id is not None:
            result['AppSchemaId'] = self.app_schema_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppEnvId') is not None:
            self.app_env_id = m.get('AppEnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSchemaId') is not None:
            self.app_schema_id = m.get('AppSchemaId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class UpdateEnvironmentResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateEnvironmentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateEnvironmentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNormalDeployConfigRequestContainerResourceLimit(TeaModel):
    def __init__(self, cpu=None, memory=None):
        self.cpu = cpu  # type: str
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNormalDeployConfigRequestContainerResourceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class UpdateNormalDeployConfigRequestContainerResourceRequest(TeaModel):
    def __init__(self, cpu=None, memory=None):
        self.cpu = cpu  # type: str
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNormalDeployConfigRequestContainerResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class UpdateNormalDeployConfigRequest(TeaModel):
    def __init__(self, app_id=None, container_resource_limit=None, container_resource_request=None, id=None):
        self.app_id = app_id  # type: long
        self.container_resource_limit = container_resource_limit  # type: UpdateNormalDeployConfigRequestContainerResourceLimit
        self.container_resource_request = container_resource_request  # type: UpdateNormalDeployConfigRequestContainerResourceRequest
        self.id = id  # type: long

    def validate(self):
        if self.container_resource_limit:
            self.container_resource_limit.validate()
        if self.container_resource_request:
            self.container_resource_request.validate()

    def to_map(self):
        _map = super(UpdateNormalDeployConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.container_resource_limit is not None:
            result['ContainerResourceLimit'] = self.container_resource_limit.to_map()
        if self.container_resource_request is not None:
            result['ContainerResourceRequest'] = self.container_resource_request.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ContainerResourceLimit') is not None:
            temp_model = UpdateNormalDeployConfigRequestContainerResourceLimit()
            self.container_resource_limit = temp_model.from_map(m['ContainerResourceLimit'])
        if m.get('ContainerResourceRequest') is not None:
            temp_model = UpdateNormalDeployConfigRequestContainerResourceRequest()
            self.container_resource_request = temp_model.from_map(m['ContainerResourceRequest'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateNormalDeployConfigShrinkRequest(TeaModel):
    def __init__(self, app_id=None, container_resource_limit_shrink=None, container_resource_request_shrink=None,
                 id=None):
        self.app_id = app_id  # type: long
        self.container_resource_limit_shrink = container_resource_limit_shrink  # type: str
        self.container_resource_request_shrink = container_resource_request_shrink  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNormalDeployConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.container_resource_limit_shrink is not None:
            result['ContainerResourceLimit'] = self.container_resource_limit_shrink
        if self.container_resource_request_shrink is not None:
            result['ContainerResourceRequest'] = self.container_resource_request_shrink
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ContainerResourceLimit') is not None:
            self.container_resource_limit_shrink = m.get('ContainerResourceLimit')
        if m.get('ContainerResourceRequest') is not None:
            self.container_resource_request_shrink = m.get('ContainerResourceRequest')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateNormalDeployConfigResponseBodyResult(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNormalDeployConfigResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNormalDeployConfigResponseBody(TeaModel):
    def __init__(self, code=None, err_msg=None, request_id=None, result=None):
        self.code = code  # type: int
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateNormalDeployConfigResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateNormalDeployConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateNormalDeployConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UpdateNormalDeployConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNormalDeployConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNormalDeployConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateNormalDeployConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


