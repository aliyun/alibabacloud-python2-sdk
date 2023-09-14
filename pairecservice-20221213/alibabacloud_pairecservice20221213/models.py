# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BackflowFeatureConsistencyCheckJobDataRequest(TeaModel):
    def __init__(self, feature_consistency_check_job_config_id=None, instance_id=None, item_features=None,
                 log_item_id=None, log_request_id=None, log_request_time=None, log_user_id=None, scene_name=None, scores=None,
                 user_features=None):
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.instance_id = instance_id  # type: str
        self.item_features = item_features  # type: str
        self.log_item_id = log_item_id  # type: str
        self.log_request_id = log_request_id  # type: str
        self.log_request_time = log_request_time  # type: long
        self.log_user_id = log_user_id  # type: str
        self.scene_name = scene_name  # type: str
        self.scores = scores  # type: str
        self.user_features = user_features  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackflowFeatureConsistencyCheckJobDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_features is not None:
            result['ItemFeatures'] = self.item_features
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.scores is not None:
            result['Scores'] = self.scores
        if self.user_features is not None:
            result['UserFeatures'] = self.user_features
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemFeatures') is not None:
            self.item_features = m.get('ItemFeatures')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Scores') is not None:
            self.scores = m.get('Scores')
        if m.get('UserFeatures') is not None:
            self.user_features = m.get('UserFeatures')
        return self


class BackflowFeatureConsistencyCheckJobDataResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackflowFeatureConsistencyCheckJobDataResponseBody, self).to_map()
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


class BackflowFeatureConsistencyCheckJobDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BackflowFeatureConsistencyCheckJobDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BackflowFeatureConsistencyCheckJobDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BackflowFeatureConsistencyCheckJobDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneExperimentRequest, self).to_map()
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


class CloneExperimentResponseBody(TeaModel):
    def __init__(self, experiment_id=None, request_id=None):
        self.experiment_id = experiment_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneExperimentGroupRequest(TeaModel):
    def __init__(self, environment=None, instance_id=None, layer_id=None):
        self.environment = environment  # type: str
        self.instance_id = instance_id  # type: str
        self.layer_id = layer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneExperimentGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        return self


class CloneExperimentGroupResponseBody(TeaModel):
    def __init__(self, experiment_group_id=None, request_id=None):
        self.experiment_group_id = experiment_group_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneExperimentGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFeatureConsistencyCheckJobConfigRequest, self).to_map()
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


class CloneFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(self, feature_consistency_check_id=None, request_id=None):
        self.feature_consistency_check_id = feature_consistency_check_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFeatureConsistencyCheckJobConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_id is not None:
            result['FeatureConsistencyCheckId'] = self.feature_consistency_check_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckId') is not None:
            self.feature_consistency_check_id = m.get('FeatureConsistencyCheckId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneFeatureConsistencyCheckJobConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneFeatureConsistencyCheckJobConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneLaboratoryRequest(TeaModel):
    def __init__(self, clone_experiment_group=None, environment=None, instance_id=None):
        self.clone_experiment_group = clone_experiment_group  # type: bool
        self.environment = environment  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneLaboratoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clone_experiment_group is not None:
            result['CloneExperimentGroup'] = self.clone_experiment_group
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloneExperimentGroup') is not None:
            self.clone_experiment_group = m.get('CloneExperimentGroup')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CloneLaboratoryResponseBody(TeaModel):
    def __init__(self, laboratory_id=None, request_id=None):
        self.laboratory_id = laboratory_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneLaboratoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCrowdRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, label=None, name=None, source=None, users=None):
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.label = label  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCrowdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateCrowdResponseBody(TeaModel):
    def __init__(self, crowd_id=None, request_id=None):
        self.crowd_id = crowd_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCrowdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCrowdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCrowdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCrowdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(self, config=None, debug_crowd_id=None, debug_users=None, description=None,
                 experiment_group_id=None, flow_percent=None, instance_id=None, name=None, type=None):
        self.config = config  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.experiment_group_id = experiment_group_id  # type: str
        self.flow_percent = flow_percent  # type: int
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(self, experiment_id=None, request_id=None):
        self.experiment_id = experiment_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentGroupRequest(TeaModel):
    def __init__(self, config=None, crowd_id=None, debug_crowd_id=None, debug_users=None, description=None,
                 distribution_time_duration=None, distribution_type=None, filter=None, instance_id=None, layer_id=None, name=None, need_aa=None,
                 reserved_buckets=None):
        self.config = config  # type: str
        self.crowd_id = crowd_id  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.distribution_time_duration = distribution_time_duration  # type: int
        self.distribution_type = distribution_type  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        self.need_aa = need_aa  # type: bool
        self.reserved_buckets = reserved_buckets  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        return self


class CreateExperimentGroupResponseBody(TeaModel):
    def __init__(self, experiment_group_id=None, request_id=None):
        self.experiment_group_id = experiment_group_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateExperimentGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(self, environment=None, feature_consistency_check_job_config_id=None, instance_id=None,
                 sampling_duration=None):
        self.environment = environment  # type: str
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.instance_id = instance_id  # type: str
        self.sampling_duration = sampling_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureConsistencyCheckJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sampling_duration is not None:
            result['SamplingDuration'] = self.sampling_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SamplingDuration') is not None:
            self.sampling_duration = m.get('SamplingDuration')
        return self


class CreateFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(self, feature_consistency_check_job_id=None, request_id=None):
        self.feature_consistency_check_job_id = feature_consistency_check_job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureConsistencyCheckJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFeatureConsistencyCheckJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFeatureConsistencyCheckJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(self, compare_feature=None, eas_service_name=None, easy_rec_package_path=None,
                 easy_rec_version=None, feature_display_exclude=None, feature_landing_resource_id=None, feature_priority=None,
                 fg_jar_version=None, fg_json_file_name=None, generate_zip=None, instance_id=None, item_id_field=None,
                 item_table=None, item_table_partition_field=None, item_table_partition_field_format=None, name=None,
                 oss_resource_id=None, sample_rate=None, scene_id=None, service_id=None, user_id_field=None, user_table=None,
                 user_table_partition_field=None, user_table_partition_field_format=None, workflow_name=None):
        self.compare_feature = compare_feature  # type: bool
        self.eas_service_name = eas_service_name  # type: str
        self.easy_rec_package_path = easy_rec_package_path  # type: str
        self.easy_rec_version = easy_rec_version  # type: str
        self.feature_display_exclude = feature_display_exclude  # type: str
        self.feature_landing_resource_id = feature_landing_resource_id  # type: str
        self.feature_priority = feature_priority  # type: str
        self.fg_jar_version = fg_jar_version  # type: str
        self.fg_json_file_name = fg_json_file_name  # type: str
        self.generate_zip = generate_zip  # type: bool
        self.instance_id = instance_id  # type: str
        self.item_id_field = item_id_field  # type: str
        self.item_table = item_table  # type: str
        self.item_table_partition_field = item_table_partition_field  # type: str
        self.item_table_partition_field_format = item_table_partition_field_format  # type: str
        self.name = name  # type: str
        self.oss_resource_id = oss_resource_id  # type: str
        self.sample_rate = sample_rate  # type: float
        self.scene_id = scene_id  # type: str
        self.service_id = service_id  # type: str
        self.user_id_field = user_id_field  # type: str
        self.user_table = user_table  # type: str
        self.user_table_partition_field = user_table_partition_field  # type: str
        self.user_table_partition_field_format = user_table_partition_field_format  # type: str
        self.workflow_name = workflow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureConsistencyCheckJobConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class CreateFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(self, feature_consistency_check_job_config_id=None, request_id=None):
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFeatureConsistencyCheckJobConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFeatureConsistencyCheckJobConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFeatureConsistencyCheckJobConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLaboratoryRequest(TeaModel):
    def __init__(self, bucket_count=None, bucket_type=None, buckets=None, debug_crowd_id=None, debug_users=None,
                 description=None, environment=None, filter=None, instance_id=None, name=None, scene_id=None, type=None):
        self.bucket_count = bucket_count  # type: int
        self.bucket_type = bucket_type  # type: str
        self.buckets = buckets  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.environment = environment  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLaboratoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLaboratoryResponseBody(TeaModel):
    def __init__(self, laboratory_id=None, request_id=None):
        self.laboratory_id = laboratory_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLaboratoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, laboratory_id=None, name=None):
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLayerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateLayerResponseBody(TeaModel):
    def __init__(self, layer_id=None, request_id=None):
        self.layer_id = layer_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLayerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLayerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParamRequest(TeaModel):
    def __init__(self, environment=None, instance_id=None, name=None, scene_id=None, value=None):
        self.environment = environment  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParamResponseBody(TeaModel):
    def __init__(self, param_id=None, request_id=None):
        self.param_id = param_id  # type: long
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_id is not None:
            result['ParamId'] = self.param_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateParamResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequestFlows(TeaModel):
    def __init__(self, flow_code=None, flow_name=None):
        self.flow_code = flow_code  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSceneRequestFlows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class CreateSceneRequest(TeaModel):
    def __init__(self, description=None, flows=None, instance_id=None, name=None):
        self.description = description  # type: str
        self.flows = flows  # type: list[CreateSceneRequestFlows]
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = CreateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(self, request_id=None, scene_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubCrowdRequest(TeaModel):
    def __init__(self, instance_id=None, source=None, users=None):
        self.instance_id = instance_id  # type: str
        self.source = source  # type: str
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubCrowdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateSubCrowdResponseBody(TeaModel):
    def __init__(self, request_id=None, sub_crowd_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.sub_crowd_id = sub_crowd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubCrowdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')
        return self


class CreateSubCrowdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSubCrowdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSubCrowdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCrowdRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCrowdRequest, self).to_map()
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


class DeleteCrowdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCrowdResponseBody, self).to_map()
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


class DeleteCrowdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCrowdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCrowdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExperimentRequest, self).to_map()
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


class DeleteExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExperimentResponseBody, self).to_map()
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


class DeleteExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExperimentGroupRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExperimentGroupRequest, self).to_map()
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


class DeleteExperimentGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteExperimentGroupResponseBody, self).to_map()
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


class DeleteExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLaboratoryRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLaboratoryRequest, self).to_map()
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


class DeleteLaboratoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLaboratoryResponseBody, self).to_map()
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


class DeleteLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayerRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLayerRequest, self).to_map()
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


class DeleteLayerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLayerResponseBody, self).to_map()
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


class DeleteLayerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParamRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParamRequest, self).to_map()
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


class DeleteParamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParamResponseBody, self).to_map()
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


class DeleteParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteParamResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSceneRequest, self).to_map()
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


class DeleteSceneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSceneResponseBody, self).to_map()
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


class DeleteSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubCrowdRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubCrowdRequest, self).to_map()
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


class DeleteSubCrowdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubCrowdResponseBody, self).to_map()
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


class DeleteSubCrowdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSubCrowdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSubCrowdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentRequest, self).to_map()
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


class GetExperimentResponseBody(TeaModel):
    def __init__(self, alias_experiment_id=None, buckets=None, config=None, debug_crowd_id=None, debug_users=None,
                 description=None, experiment_group_id=None, flow_percent=None, gmt_create_time=None, gmt_modified_time=None,
                 laboratory_id=None, layer_id=None, name=None, request_id=None, scene_id=None, status=None, type=None):
        self.alias_experiment_id = alias_experiment_id  # type: str
        self.buckets = buckets  # type: str
        self.config = config  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.experiment_group_id = experiment_group_id  # type: str
        self.flow_percent = flow_percent  # type: int
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentGroupRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentGroupRequest, self).to_map()
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


class GetExperimentGroupResponseBody(TeaModel):
    def __init__(self, config=None, crowd_id=None, debug_crowd_id=None, debug_users=None, description=None,
                 distribution_time_duration=None, distribution_type=None, filter=None, laboratory_id=None, layer_id=None, name=None,
                 need_aa=None, owner=None, request_id=None, reserved_buckets=None, scene_id=None, status=None):
        self.config = config  # type: str
        self.crowd_id = crowd_id  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.distribution_time_duration = distribution_time_duration  # type: int
        self.distribution_type = distribution_type  # type: str
        self.filter = filter  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        self.need_aa = need_aa  # type: bool
        self.owner = owner  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.reserved_buckets = reserved_buckets  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetExperimentGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFeatureConsistencyCheckJobRequest, self).to_map()
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


class GetFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(self, config=None, feature_consistency_check_job_config_id=None,
                 feature_consistency_check_job_config_name=None, gmt_end_time=None, gmt_start_time=None, logs=None, request_id=None, status=None):
        self.config = config  # type: str
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name  # type: str
        self.gmt_end_time = gmt_end_time  # type: str
        self.gmt_start_time = gmt_start_time  # type: str
        self.logs = logs  # type: list[str]
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFeatureConsistencyCheckJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFeatureConsistencyCheckJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFeatureConsistencyCheckJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFeatureConsistencyCheckJobConfigRequest, self).to_map()
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


class GetFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(self, compare_feature=None, eas_service_name=None, easy_rec_package_path=None,
                 easy_rec_version=None, feature_display_exclude=None, feature_landing_resource_id=None,
                 feature_landing_resource_uri=None, feature_priority=None, fg_jar_version=None, fg_json_file_name=None, generate_zip=None,
                 gmt_create_time=None, gmt_modified_time=None, item_id_field=None, item_table=None,
                 item_table_partition_field=None, item_table_partition_field_format=None, latest_job_gmt_sampling_end_time=None,
                 latest_job_gmt_sampling_start_time=None, latest_job_id=None, name=None, oss_bucket=None, oss_resource_id=None, request_id=None,
                 sample_rate=None, scene_id=None, scene_name=None, service_id=None, service_name=None, status=None,
                 user_id_field=None, user_table=None, user_table_partition_field=None, user_table_partition_field_format=None,
                 workflow_name=None):
        self.compare_feature = compare_feature  # type: bool
        self.eas_service_name = eas_service_name  # type: str
        self.easy_rec_package_path = easy_rec_package_path  # type: str
        self.easy_rec_version = easy_rec_version  # type: str
        self.feature_display_exclude = feature_display_exclude  # type: str
        self.feature_landing_resource_id = feature_landing_resource_id  # type: str
        self.feature_landing_resource_uri = feature_landing_resource_uri  # type: str
        self.feature_priority = feature_priority  # type: str
        self.fg_jar_version = fg_jar_version  # type: str
        self.fg_json_file_name = fg_json_file_name  # type: str
        self.generate_zip = generate_zip  # type: bool
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.item_id_field = item_id_field  # type: str
        self.item_table = item_table  # type: str
        self.item_table_partition_field = item_table_partition_field  # type: str
        self.item_table_partition_field_format = item_table_partition_field_format  # type: str
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time  # type: str
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time  # type: str
        self.latest_job_id = latest_job_id  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_resource_id = oss_resource_id  # type: str
        self.request_id = request_id  # type: str
        self.sample_rate = sample_rate  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_name = scene_name  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.status = status  # type: str
        self.user_id_field = user_id_field  # type: str
        self.user_table = user_table  # type: str
        self.user_table_partition_field = user_table_partition_field  # type: str
        self.user_table_partition_field_format = user_table_partition_field_format  # type: str
        self.workflow_name = workflow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFeatureConsistencyCheckJobConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time
        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time
        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')
        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')
        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class GetFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFeatureConsistencyCheckJobConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFeatureConsistencyCheckJobConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBodyConfigDataManagements(TeaModel):
    def __init__(self, component_code=None, meta=None, type=None):
        self.component_code = component_code  # type: str
        self.meta = meta  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyConfigDataManagements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfigEngines(TeaModel):
    def __init__(self, component_code=None, meta=None, type=None):
        self.component_code = component_code  # type: str
        self.meta = meta  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyConfigEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfigMonitors(TeaModel):
    def __init__(self, component_code=None, meta=None, type=None):
        self.component_code = component_code  # type: str
        self.meta = meta  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyConfigMonitors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponseBodyConfig(TeaModel):
    def __init__(self, data_managements=None, engines=None, monitors=None):
        self.data_managements = data_managements  # type: list[GetInstanceResponseBodyConfigDataManagements]
        self.engines = engines  # type: list[GetInstanceResponseBodyConfigEngines]
        self.monitors = monitors  # type: list[GetInstanceResponseBodyConfigMonitors]

    def validate(self):
        if self.data_managements:
            for k in self.data_managements:
                if k:
                    k.validate()
        if self.engines:
            for k in self.engines:
                if k:
                    k.validate()
        if self.monitors:
            for k in self.monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k in self.data_managements:
                result['DataManagements'].append(k.to_map() if k else None)
        result['Engines'] = []
        if self.engines is not None:
            for k in self.engines:
                result['Engines'].append(k.to_map() if k else None)
        result['Monitors'] = []
        if self.monitors is not None:
            for k in self.monitors:
                result['Monitors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k in m.get('DataManagements'):
                temp_model = GetInstanceResponseBodyConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k))
        self.engines = []
        if m.get('Engines') is not None:
            for k in m.get('Engines'):
                temp_model = GetInstanceResponseBodyConfigEngines()
                self.engines.append(temp_model.from_map(k))
        self.monitors = []
        if m.get('Monitors') is not None:
            for k in m.get('Monitors'):
                temp_model = GetInstanceResponseBodyConfigMonitors()
                self.monitors.append(temp_model.from_map(k))
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, charge_type=None, commodity_code=None, config=None, expired_time=None, gmt_create_time=None,
                 gmt_modified_time=None, instance_id=None, region_id=None, request_id=None, status=None, type=None):
        self.charge_type = charge_type  # type: str
        self.commodity_code = commodity_code  # type: str
        self.config = config  # type: GetInstanceResponseBodyConfig
        self.expired_time = expired_time  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Config') is not None:
            temp_model = GetInstanceResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLaboratoryRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLaboratoryRequest, self).to_map()
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


class GetLaboratoryResponseBody(TeaModel):
    def __init__(self, bucket_count=None, bucket_type=None, buckets=None, crowd_id=None, debug_crowd_id=None,
                 debug_users=None, description=None, environment=None, filter=None, name=None, request_id=None, scene_id=None,
                 status=None, type=None):
        self.bucket_count = bucket_count  # type: int
        self.bucket_type = bucket_type  # type: str
        self.buckets = buckets  # type: str
        self.crowd_id = crowd_id  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.environment = environment  # type: str
        self.filter = filter  # type: str
        self.name = name  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLaboratoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLayerRequest, self).to_map()
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


class GetLayerResponseBody(TeaModel):
    def __init__(self, description=None, laboratory_id=None, name=None, request_id=None, scene_id=None):
        self.description = description  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.name = name  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLayerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetLayerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSceneRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSceneRequest, self).to_map()
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


class GetSceneResponseBodyFlows(TeaModel):
    def __init__(self, flow_code=None, flow_name=None):
        self.flow_code = flow_code  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSceneResponseBodyFlows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class GetSceneResponseBody(TeaModel):
    def __init__(self, description=None, flows=None, name=None, request_id=None):
        self.description = description  # type: str
        self.flows = flows  # type: list[GetSceneResponseBodyFlows]
        self.name = name  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = GetSceneResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubCrowdRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubCrowdRequest, self).to_map()
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


class GetSubCrowdResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, quantity=None, request_id=None, source=None, users=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.quantity = quantity  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.source = source  # type: str
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubCrowdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class GetSubCrowdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubCrowdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubCrowdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrowdUsersRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCrowdUsersRequest, self).to_map()
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


class ListCrowdUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCrowdUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListCrowdUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCrowdUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCrowdUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCrowdUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCrowdsRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCrowdsRequest, self).to_map()
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


class ListCrowdsResponseBodyCrowds(TeaModel):
    def __init__(self, crowd_id=None, description=None, gmt_create_time=None, label=None, name=None, quantity=None,
                 source=None, users=None):
        self.crowd_id = crowd_id  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.label = label  # type: str
        self.name = name  # type: str
        self.quantity = quantity  # type: str
        self.source = source  # type: str
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCrowdsResponseBodyCrowds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.label is not None:
            result['Label'] = self.label
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.source is not None:
            result['Source'] = self.source
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListCrowdsResponseBody(TeaModel):
    def __init__(self, crowds=None, request_id=None, total_count=None):
        self.crowds = crowds  # type: list[ListCrowdsResponseBodyCrowds]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.crowds:
            for k in self.crowds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCrowdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Crowds'] = []
        if self.crowds is not None:
            for k in self.crowds:
                result['Crowds'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.crowds = []
        if m.get('Crowds') is not None:
            for k in m.get('Crowds'):
                temp_model = ListCrowdsResponseBodyCrowds()
                self.crowds.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCrowdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCrowdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCrowdsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCrowdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentGroupsRequest(TeaModel):
    def __init__(self, instance_id=None, layer_id=None, status=None):
        self.instance_id = instance_id  # type: str
        self.layer_id = layer_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExperimentGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentGroupsResponseBodyExperimentGroups(TeaModel):
    def __init__(self, config=None, crowd_id=None, debug_crowd_id=None, debug_users=None, description=None,
                 distribution_time_duration=None, distribution_type=None, experiment_group_id=None, filter=None, laboratory_id=None,
                 layer_id=None, name=None, need_aa=None, owner=None, reserved_buckets=None, scene_id=None, status=None):
        self.config = config  # type: str
        self.crowd_id = crowd_id  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.distribution_time_duration = distribution_time_duration  # type: int
        self.distribution_type = distribution_type  # type: str
        self.experiment_group_id = experiment_group_id  # type: str
        self.filter = filter  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        self.need_aa = need_aa  # type: bool
        self.owner = owner  # type: str
        self.reserved_buckets = reserved_buckets  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExperimentGroupsResponseBodyExperimentGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.reserved_buckets is not None:
            result['ReservedBuckets'] = self.reserved_buckets
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ReservedBuckets') is not None:
            self.reserved_buckets = m.get('ReservedBuckets')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentGroupsResponseBody(TeaModel):
    def __init__(self, experiment_groups=None, request_id=None, total_count=None):
        self.experiment_groups = experiment_groups  # type: list[ListExperimentGroupsResponseBodyExperimentGroups]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.experiment_groups:
            for k in self.experiment_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExperimentGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExperimentGroups'] = []
        if self.experiment_groups is not None:
            for k in self.experiment_groups:
                result['ExperimentGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.experiment_groups = []
        if m.get('ExperimentGroups') is not None:
            for k in m.get('ExperimentGroups'):
                temp_model = ListExperimentGroupsResponseBodyExperimentGroups()
                self.experiment_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExperimentGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExperimentGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(self, experiment_group_id=None, instance_id=None, query=None, status=None):
        self.experiment_group_id = experiment_group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.query = query  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExperimentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query is not None:
            result['Query'] = self.query
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExperimentsResponseBodyExperiments(TeaModel):
    def __init__(self, alias_experiment_id=None, buckets=None, config=None, debug_crowd_id=None, debug_users=None,
                 description=None, experiment_group_id=None, experiment_id=None, flow_percent=None, gmt_create_time=None,
                 gmt_modified_time=None, laboratory_id=None, layer_id=None, name=None, scene_id=None, status=None, type=None):
        self.alias_experiment_id = alias_experiment_id  # type: str
        self.buckets = buckets  # type: str
        self.config = config  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.experiment_group_id = experiment_group_id  # type: str
        self.experiment_id = experiment_id  # type: str
        self.flow_percent = flow_percent  # type: int
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListExperimentsResponseBodyExperiments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_experiment_id is not None:
            result['AliasExperimentId'] = self.alias_experiment_id
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasExperimentId') is not None:
            self.alias_experiment_id = m.get('AliasExperimentId')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(self, experiments=None, request_id=None, total_count=None):
        self.experiments = experiments  # type: list[ListExperimentsResponseBodyExperiments]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListExperimentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['Experiments'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.experiments = []
        if m.get('Experiments') is not None:
            for k in m.get('Experiments'):
                temp_model = ListExperimentsResponseBodyExperiments()
                self.experiments.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListExperimentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListExperimentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobConfigsRequest(TeaModel):
    def __init__(self, instance_id=None, order=None, page_number=None, page_size=None, sort_by=None):
        self.instance_id = instance_id  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs(TeaModel):
    def __init__(self, compare_feature=None, eas_service_name=None, easy_rec_package_path=None,
                 easy_rec_version=None, feature_consistency_check_job_config_id=None, feature_display_exclude=None,
                 feature_landing_resource_id=None, feature_landing_resource_uri=None, feature_priority=None, fg_jar_version=None,
                 fg_json_file_name=None, generate_zip=None, gmt_create_time=None, gmt_modified_time=None, item_id_field=None,
                 item_table=None, item_table_partition_field=None, item_table_partition_field_format=None,
                 latest_job_gmt_sampling_end_time=None, latest_job_gmt_sampling_start_time=None, latest_job_id=None, name=None, oss_bucket=None,
                 oss_resource_id=None, sample_rate=None, scene_id=None, scene_name=None, service_id=None, service_name=None,
                 status=None, user_id_field=None, user_table=None, user_table_partition_field=None,
                 user_table_partition_field_format=None, workflow_name=None):
        self.compare_feature = compare_feature  # type: bool
        self.eas_service_name = eas_service_name  # type: str
        self.easy_rec_package_path = easy_rec_package_path  # type: str
        self.easy_rec_version = easy_rec_version  # type: str
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.feature_display_exclude = feature_display_exclude  # type: str
        self.feature_landing_resource_id = feature_landing_resource_id  # type: str
        self.feature_landing_resource_uri = feature_landing_resource_uri  # type: str
        self.feature_priority = feature_priority  # type: str
        self.fg_jar_version = fg_jar_version  # type: str
        self.fg_json_file_name = fg_json_file_name  # type: str
        self.generate_zip = generate_zip  # type: bool
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.item_id_field = item_id_field  # type: str
        self.item_table = item_table  # type: str
        self.item_table_partition_field = item_table_partition_field  # type: str
        self.item_table_partition_field_format = item_table_partition_field_format  # type: str
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time  # type: str
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time  # type: str
        self.latest_job_id = latest_job_id  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_resource_id = oss_resource_id  # type: str
        self.sample_rate = sample_rate  # type: str
        self.scene_id = scene_id  # type: str
        self.scene_name = scene_name  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.status = status  # type: str
        self.user_id_field = user_id_field  # type: str
        self.user_table = user_table  # type: str
        self.user_table_partition_field = user_table_partition_field  # type: str
        self.user_table_partition_field_format = user_table_partition_field_format  # type: str
        self.workflow_name = workflow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time
        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time
        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')
        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')
        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class ListFeatureConsistencyCheckJobConfigsResponseBody(TeaModel):
    def __init__(self, feature_consistency_check_configs=None, request_id=None, total_count=None):
        self.feature_consistency_check_configs = feature_consistency_check_configs  # type: list[ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.feature_consistency_check_configs:
            for k in self.feature_consistency_check_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureConsistencyCheckConfigs'] = []
        if self.feature_consistency_check_configs is not None:
            for k in self.feature_consistency_check_configs:
                result['FeatureConsistencyCheckConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.feature_consistency_check_configs = []
        if m.get('FeatureConsistencyCheckConfigs') is not None:
            for k in m.get('FeatureConsistencyCheckConfigs'):
                temp_model = ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs()
                self.feature_consistency_check_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureConsistencyCheckJobConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureConsistencyCheckJobConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobFeatureReportsRequest(TeaModel):
    def __init__(self, instance_id=None, log_item_id=None, log_request_id=None, log_user_id=None):
        self.instance_id = instance_id  # type: str
        self.log_item_id = log_item_id  # type: str
        self.log_request_id = log_request_id  # type: str
        self.log_user_id = log_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobFeatureReportsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff(TeaModel):
    def __init__(self, feature_name=None, log_item_id=None, log_request_id=None, log_user_id=None,
                 offline_value=None, online_value=None):
        self.feature_name = feature_name  # type: str
        self.log_item_id = log_item_id  # type: str
        self.log_request_id = log_request_id  # type: str
        self.log_user_id = log_user_id  # type: str
        self.offline_value = offline_value  # type: str
        self.online_value = online_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.offline_value is not None:
            result['OfflineValue'] = self.offline_value
        if self.online_value is not None:
            result['OnlineValue'] = self.online_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('OfflineValue') is not None:
            self.offline_value = m.get('OfflineValue')
        if m.get('OnlineValue') is not None:
            self.online_value = m.get('OnlineValue')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponseBody(TeaModel):
    def __init__(self, data_path=None, oss_path=None, reports_of_feature_diff=None, request_id=None):
        self.data_path = data_path  # type: str
        self.oss_path = oss_path  # type: str
        self.reports_of_feature_diff = reports_of_feature_diff  # type: list[ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.reports_of_feature_diff:
            for k in self.reports_of_feature_diff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobFeatureReportsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        result['ReportsOfFeatureDiff'] = []
        if self.reports_of_feature_diff is not None:
            for k in self.reports_of_feature_diff:
                result['ReportsOfFeatureDiff'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        self.reports_of_feature_diff = []
        if m.get('ReportsOfFeatureDiff') is not None:
            for k in m.get('ReportsOfFeatureDiff'):
                temp_model = ListFeatureConsistencyCheckJobFeatureReportsResponseBodyReportsOfFeatureDiff()
                self.reports_of_feature_diff.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureConsistencyCheckJobFeatureReportsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureConsistencyCheckJobFeatureReportsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobFeatureReportsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobFeatureReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobScoreReportsRequest(TeaModel):
    def __init__(self, exclude_request_ids=None, instance_id=None):
        self.exclude_request_ids = exclude_request_ids  # type: list[str]
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobScoreReportsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_request_ids is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids = m.get('ExcludeRequestIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsShrinkRequest(TeaModel):
    def __init__(self, exclude_request_ids_shrink=None, instance_id=None):
        self.exclude_request_ids_shrink = exclude_request_ids_shrink  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobScoreReportsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_request_ids_shrink is not None:
            result['ExcludeRequestIds'] = self.exclude_request_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeRequestIds') is not None:
            self.exclude_request_ids_shrink = m.get('ExcludeRequestIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff(TeaModel):
    def __init__(self, log_item_id=None, log_request_id=None, log_user_id=None, score_diff=None,
                 score_diff_detail=None):
        self.log_item_id = log_item_id  # type: str
        self.log_request_id = log_request_id  # type: str
        self.log_user_id = log_user_id  # type: str
        self.score_diff = score_diff  # type: str
        self.score_diff_detail = score_diff_detail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.score_diff is not None:
            result['ScoreDiff'] = self.score_diff
        if self.score_diff_detail is not None:
            result['ScoreDiffDetail'] = self.score_diff_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('ScoreDiff') is not None:
            self.score_diff = m.get('ScoreDiff')
        if m.get('ScoreDiffDetail') is not None:
            self.score_diff_detail = m.get('ScoreDiffDetail')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponseBody(TeaModel):
    def __init__(self, data_path=None, oss_path=None, reports_of_score_diff=None, request_id=None):
        self.data_path = data_path  # type: str
        self.oss_path = oss_path  # type: str
        self.reports_of_score_diff = reports_of_score_diff  # type: list[ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.reports_of_score_diff:
            for k in self.reports_of_score_diff:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobScoreReportsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_path is not None:
            result['DataPath'] = self.data_path
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        result['ReportsOfScoreDiff'] = []
        if self.reports_of_score_diff is not None:
            for k in self.reports_of_score_diff:
                result['ReportsOfScoreDiff'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        self.reports_of_score_diff = []
        if m.get('ReportsOfScoreDiff') is not None:
            for k in m.get('ReportsOfScoreDiff'):
                temp_model = ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff()
                self.reports_of_score_diff.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFeatureConsistencyCheckJobScoreReportsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureConsistencyCheckJobScoreReportsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobScoreReportsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobScoreReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFeatureConsistencyCheckJobsRequest(TeaModel):
    def __init__(self, instance_id=None, order=None, page_number=None, page_size=None, sort_by=None, status=None):
        self.instance_id = instance_id  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.sort_by = sort_by  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs(TeaModel):
    def __init__(self, config=None, feature_consistency_check_job_config_id=None,
                 feature_consistency_check_job_config_name=None, feature_consistency_check_job_id=None, gmt_end_time=None, gmt_start_time=None, logs=None,
                 status=None):
        self.config = config  # type: str
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.feature_consistency_check_job_config_name = feature_consistency_check_job_config_name  # type: str
        self.feature_consistency_check_job_id = feature_consistency_check_job_id  # type: str
        self.gmt_end_time = gmt_end_time  # type: str
        self.gmt_start_time = gmt_start_time  # type: str
        self.logs = logs  # type: list[str]
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.feature_consistency_check_job_config_name is not None:
            result['FeatureConsistencyCheckJobConfigName'] = self.feature_consistency_check_job_config_name
        if self.feature_consistency_check_job_id is not None:
            result['FeatureConsistencyCheckJobId'] = self.feature_consistency_check_job_id
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('FeatureConsistencyCheckJobConfigName') is not None:
            self.feature_consistency_check_job_config_name = m.get('FeatureConsistencyCheckJobConfigName')
        if m.get('FeatureConsistencyCheckJobId') is not None:
            self.feature_consistency_check_job_id = m.get('FeatureConsistencyCheckJobId')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFeatureConsistencyCheckJobsResponseBody(TeaModel):
    def __init__(self, feature_consistency_check_jobs=None, request_id=None, total_count=None):
        self.feature_consistency_check_jobs = feature_consistency_check_jobs  # type: list[ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.feature_consistency_check_jobs:
            for k in self.feature_consistency_check_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FeatureConsistencyCheckJobs'] = []
        if self.feature_consistency_check_jobs is not None:
            for k in self.feature_consistency_check_jobs:
                result['FeatureConsistencyCheckJobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.feature_consistency_check_jobs = []
        if m.get('FeatureConsistencyCheckJobs') is not None:
            for k in m.get('FeatureConsistencyCheckJobs'):
                temp_model = ListFeatureConsistencyCheckJobsResponseBodyFeatureConsistencyCheckJobs()
                self.feature_consistency_check_jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFeatureConsistencyCheckJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFeatureConsistencyCheckJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFeatureConsistencyCheckJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFeatureConsistencyCheckJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, instance_id=None, order=None, page_number=None, page_size=None, sort_by=None, type=None):
        self.instance_id = instance_id  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigDataManagements(TeaModel):
    def __init__(self, component_code=None, meta=None, type=None):
        self.component_code = component_code  # type: str
        self.meta = meta  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesConfigDataManagements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigEngines(TeaModel):
    def __init__(self, component_code=None, meta=None, type=None):
        self.component_code = component_code  # type: str
        self.meta = meta  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesConfigEngines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfigMonitors(TeaModel):
    def __init__(self, component_code=None, meta=None, type=None):
        self.component_code = component_code  # type: str
        self.meta = meta  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesConfigMonitors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesConfig(TeaModel):
    def __init__(self, data_managements=None, engines=None, monitors=None):
        self.data_managements = data_managements  # type: list[ListInstancesResponseBodyInstancesConfigDataManagements]
        self.engines = engines  # type: list[ListInstancesResponseBodyInstancesConfigEngines]
        self.monitors = monitors  # type: list[ListInstancesResponseBodyInstancesConfigMonitors]

    def validate(self):
        if self.data_managements:
            for k in self.data_managements:
                if k:
                    k.validate()
        if self.engines:
            for k in self.engines:
                if k:
                    k.validate()
        if self.monitors:
            for k in self.monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataManagements'] = []
        if self.data_managements is not None:
            for k in self.data_managements:
                result['DataManagements'].append(k.to_map() if k else None)
        result['Engines'] = []
        if self.engines is not None:
            for k in self.engines:
                result['Engines'].append(k.to_map() if k else None)
        result['Monitors'] = []
        if self.monitors is not None:
            for k in self.monitors:
                result['Monitors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_managements = []
        if m.get('DataManagements') is not None:
            for k in m.get('DataManagements'):
                temp_model = ListInstancesResponseBodyInstancesConfigDataManagements()
                self.data_managements.append(temp_model.from_map(k))
        self.engines = []
        if m.get('Engines') is not None:
            for k in m.get('Engines'):
                temp_model = ListInstancesResponseBodyInstancesConfigEngines()
                self.engines.append(temp_model.from_map(k))
        self.monitors = []
        if m.get('Monitors') is not None:
            for k in m.get('Monitors'):
                temp_model = ListInstancesResponseBodyInstancesConfigMonitors()
                self.monitors.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, charge_type=None, commodity_code=None, config=None, expired_time=None, gmt_create_time=None,
                 gmt_modified_time=None, instance_id=None, region_id=None, status=None, type=None):
        self.charge_type = charge_type  # type: str
        self.commodity_code = commodity_code  # type: str
        self.config = config  # type: ListInstancesResponseBodyInstancesConfig
        self.expired_time = expired_time  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Config') is not None:
            temp_model = ListInstancesResponseBodyInstancesConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLaboratoriesRequest(TeaModel):
    def __init__(self, environment=None, instance_id=None, scene_id=None, status=None):
        self.environment = environment  # type: str
        self.instance_id = instance_id  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLaboratoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLaboratoriesResponseBodyLaboratories(TeaModel):
    def __init__(self, bucket_count=None, bucket_type=None, buckets=None, crowd_id=None, debug_crowd_id=None,
                 debug_users=None, description=None, environment=None, filter=None, laboratory_id=None, name=None, scene_id=None,
                 status=None, type=None):
        self.bucket_count = bucket_count  # type: int
        self.bucket_type = bucket_type  # type: str
        self.buckets = buckets  # type: str
        self.crowd_id = crowd_id  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.environment = environment  # type: str
        self.filter = filter  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLaboratoriesResponseBodyLaboratories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListLaboratoriesResponseBody(TeaModel):
    def __init__(self, laboratories=None, request_id=None, total_count=None):
        self.laboratories = laboratories  # type: list[ListLaboratoriesResponseBodyLaboratories]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.laboratories:
            for k in self.laboratories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLaboratoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Laboratories'] = []
        if self.laboratories is not None:
            for k in self.laboratories:
                result['Laboratories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.laboratories = []
        if m.get('Laboratories') is not None:
            for k in m.get('Laboratories'):
                temp_model = ListLaboratoriesResponseBodyLaboratories()
                self.laboratories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLaboratoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLaboratoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLaboratoriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLaboratoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersRequest(TeaModel):
    def __init__(self, instance_id=None, laboratory_id=None):
        self.instance_id = instance_id  # type: str
        self.laboratory_id = laboratory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLayersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        return self


class ListLayersResponseBodyLayers(TeaModel):
    def __init__(self, description=None, laboratory_id=None, layer_id=None, name=None, scene_id=None):
        self.description = description  # type: str
        self.laboratory_id = laboratory_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLayersResponseBodyLayers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListLayersResponseBody(TeaModel):
    def __init__(self, layers=None, request_id=None, total_count=None):
        self.layers = layers  # type: list[ListLayersResponseBodyLayers]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLayersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = ListLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLayersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLayersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLayersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParamsRequest(TeaModel):
    def __init__(self, environment=None, instance_id=None, name=None, page_number=None, page_size=None,
                 scene_id=None):
        self.environment = environment  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.scene_id = scene_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListParamsResponseBodyParams(TeaModel):
    def __init__(self, environment=None, gmt_modified_time=None, name=None, param_id=None, value=None):
        self.environment = environment  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.param_id = param_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListParamsResponseBodyParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.param_id is not None:
            result['ParamId'] = self.param_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListParamsResponseBody(TeaModel):
    def __init__(self, params=None, request_id=None, total_count=None):
        self.params = params  # type: list[ListParamsResponseBodyParams]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListParamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = ListParamsResponseBodyParams()
                self.params.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListParamsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListParamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListParamsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(self, instance_id=None, name=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScenesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListScenesResponseBodyScenesFlows(TeaModel):
    def __init__(self, flow_code=None, flow_name=None):
        self.flow_code = flow_code  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScenesResponseBodyScenesFlows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class ListScenesResponseBodyScenes(TeaModel):
    def __init__(self, description=None, flows=None, name=None, scene_id=None):
        self.description = description  # type: str
        self.flows = flows  # type: list[ListScenesResponseBodyScenesFlows]
        self.name = name  # type: str
        self.scene_id = scene_id  # type: str

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListScenesResponseBodyScenes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListScenesResponseBodyScenesFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(self, request_id=None, scenes=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.scenes = scenes  # type: list[ListScenesResponseBodyScenes]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.scenes:
            for k in self.scenes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListScenesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Scenes'] = []
        if self.scenes is not None:
            for k in self.scenes:
                result['Scenes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scenes = []
        if m.get('Scenes') is not None:
            for k in m.get('Scenes'):
                temp_model = ListScenesResponseBodyScenes()
                self.scenes.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScenesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListScenesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListScenesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubCrowdsRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubCrowdsRequest, self).to_map()
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


class ListSubCrowdsResponseBodySubCrowds(TeaModel):
    def __init__(self, gmt_create_time=None, quantity=None, source=None, sub_crowd_id=None, users=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.quantity = quantity  # type: int
        self.source = source  # type: str
        self.sub_crowd_id = sub_crowd_id  # type: str
        self.users = users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubCrowdsResponseBodySubCrowds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.source is not None:
            result['Source'] = self.source
        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListSubCrowdsResponseBody(TeaModel):
    def __init__(self, request_id=None, sub_crowds=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.sub_crowds = sub_crowds  # type: list[ListSubCrowdsResponseBodySubCrowds]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.sub_crowds:
            for k in self.sub_crowds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubCrowdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubCrowds'] = []
        if self.sub_crowds is not None:
            for k in self.sub_crowds:
                result['SubCrowds'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_crowds = []
        if m.get('SubCrowds') is not None:
            for k in m.get('SubCrowds'):
                temp_model = ListSubCrowdsResponseBodySubCrowds()
                self.sub_crowds.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSubCrowdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubCrowdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubCrowdsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubCrowdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineExperimentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineExperimentRequest, self).to_map()
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


class OfflineExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineExperimentResponseBody, self).to_map()
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


class OfflineExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OfflineExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OfflineExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineExperimentGroupRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineExperimentGroupRequest, self).to_map()
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


class OfflineExperimentGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineExperimentGroupResponseBody, self).to_map()
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


class OfflineExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OfflineExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OfflineExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineLaboratoryRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineLaboratoryRequest, self).to_map()
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


class OfflineLaboratoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineLaboratoryResponseBody, self).to_map()
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


class OfflineLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OfflineLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OfflineLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OfflineLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineExperimentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnlineExperimentRequest, self).to_map()
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


class OnlineExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnlineExperimentResponseBody, self).to_map()
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


class OnlineExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OnlineExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OnlineExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineExperimentGroupRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnlineExperimentGroupRequest, self).to_map()
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


class OnlineExperimentGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnlineExperimentGroupResponseBody, self).to_map()
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


class OnlineExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OnlineExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OnlineExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnlineLaboratoryRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnlineLaboratoryRequest, self).to_map()
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


class OnlineLaboratoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnlineLaboratoryResponseBody, self).to_map()
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


class OnlineLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OnlineLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OnlineLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnlineLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushAllExperimentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushAllExperimentRequest, self).to_map()
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


class PushAllExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushAllExperimentResponseBody, self).to_map()
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


class PushAllExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PushAllExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushAllExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushAllExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncFeatureConsistencyCheckJobReplayLogRequest(TeaModel):
    def __init__(self, context_features=None, feature_consistency_check_job_config_id=None,
                 generated_features=None, instance_id=None, log_item_id=None, log_request_id=None, log_request_time=None,
                 log_user_id=None, raw_features=None, scene_name=None):
        self.context_features = context_features  # type: str
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id  # type: str
        self.generated_features = generated_features  # type: str
        self.instance_id = instance_id  # type: str
        self.log_item_id = log_item_id  # type: str
        self.log_request_id = log_request_id  # type: str
        self.log_request_time = log_request_time  # type: long
        self.log_user_id = log_user_id  # type: str
        self.raw_features = raw_features  # type: str
        self.scene_name = scene_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncFeatureConsistencyCheckJobReplayLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context_features is not None:
            result['ContextFeatures'] = self.context_features
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id
        if self.generated_features is not None:
            result['GeneratedFeatures'] = self.generated_features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time
        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id
        if self.raw_features is not None:
            result['RawFeatures'] = self.raw_features
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContextFeatures') is not None:
            self.context_features = m.get('ContextFeatures')
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')
        if m.get('GeneratedFeatures') is not None:
            self.generated_features = m.get('GeneratedFeatures')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')
        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')
        if m.get('RawFeatures') is not None:
            self.raw_features = m.get('RawFeatures')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class SyncFeatureConsistencyCheckJobReplayLogResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncFeatureConsistencyCheckJobReplayLogResponseBody, self).to_map()
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


class SyncFeatureConsistencyCheckJobReplayLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncFeatureConsistencyCheckJobReplayLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncFeatureConsistencyCheckJobReplayLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncFeatureConsistencyCheckJobReplayLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateFeatureConsistencyCheckJobRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TerminateFeatureConsistencyCheckJobRequest, self).to_map()
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


class TerminateFeatureConsistencyCheckJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TerminateFeatureConsistencyCheckJobResponseBody, self).to_map()
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


class TerminateFeatureConsistencyCheckJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TerminateFeatureConsistencyCheckJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TerminateFeatureConsistencyCheckJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TerminateFeatureConsistencyCheckJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCrowdRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, name=None):
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCrowdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateCrowdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCrowdResponseBody, self).to_map()
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


class UpdateCrowdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCrowdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCrowdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentRequest(TeaModel):
    def __init__(self, config=None, debug_crowd_id=None, debug_users=None, description=None, flow_percent=None,
                 instance_id=None, name=None, type=None):
        self.config = config  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.flow_percent = flow_percent  # type: int
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentResponseBody, self).to_map()
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


class UpdateExperimentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExperimentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExperimentGroupRequest(TeaModel):
    def __init__(self, config=None, crowd_id=None, debug_crowd_id=None, debug_users=None, description=None,
                 distribution_time_duration=None, distribution_type=None, filter=None, instance_id=None, layer_id=None, name=None, need_aa=None,
                 reservced_buckets=None):
        self.config = config  # type: str
        self.crowd_id = crowd_id  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.distribution_time_duration = distribution_time_duration  # type: int
        self.distribution_type = distribution_type  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.layer_id = layer_id  # type: str
        self.name = name  # type: str
        self.need_aa = need_aa  # type: bool
        self.reservced_buckets = reservced_buckets  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.distribution_time_duration is not None:
            result['DistributionTimeDuration'] = self.distribution_time_duration
        if self.distribution_type is not None:
            result['DistributionType'] = self.distribution_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.layer_id is not None:
            result['LayerId'] = self.layer_id
        if self.name is not None:
            result['Name'] = self.name
        if self.need_aa is not None:
            result['NeedAA'] = self.need_aa
        if self.reservced_buckets is not None:
            result['ReservcedBuckets'] = self.reservced_buckets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistributionTimeDuration') is not None:
            self.distribution_time_duration = m.get('DistributionTimeDuration')
        if m.get('DistributionType') is not None:
            self.distribution_type = m.get('DistributionType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedAA') is not None:
            self.need_aa = m.get('NeedAA')
        if m.get('ReservcedBuckets') is not None:
            self.reservced_buckets = m.get('ReservcedBuckets')
        return self


class UpdateExperimentGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateExperimentGroupResponseBody, self).to_map()
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


class UpdateExperimentGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateExperimentGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateExperimentGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExperimentGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFeatureConsistencyCheckJobConfigRequest(TeaModel):
    def __init__(self, compare_feature=None, eas_service_name=None, easy_rec_package_path=None,
                 easy_rec_version=None, feature_display_exclude=None, feature_landing_resource_id=None, feature_priority=None,
                 fg_jar_version=None, fg_json_file_name=None, generate_zip=None, instance_id=None, item_id_field=None,
                 item_table=None, item_table_partition_field=None, item_table_partition_field_format=None, name=None,
                 oss_resource_id=None, sample_rate=None, scene_id=None, service_id=None, user_id_field=None, user_table=None,
                 user_table_partition_field=None, user_table_partition_field_format=None, workflow_name=None):
        self.compare_feature = compare_feature  # type: bool
        self.eas_service_name = eas_service_name  # type: str
        self.easy_rec_package_path = easy_rec_package_path  # type: str
        self.easy_rec_version = easy_rec_version  # type: str
        self.feature_display_exclude = feature_display_exclude  # type: str
        self.feature_landing_resource_id = feature_landing_resource_id  # type: str
        self.feature_priority = feature_priority  # type: str
        self.fg_jar_version = fg_jar_version  # type: str
        self.fg_json_file_name = fg_json_file_name  # type: str
        self.generate_zip = generate_zip  # type: bool
        self.instance_id = instance_id  # type: str
        self.item_id_field = item_id_field  # type: str
        self.item_table = item_table  # type: str
        self.item_table_partition_field = item_table_partition_field  # type: str
        self.item_table_partition_field_format = item_table_partition_field_format  # type: str
        self.name = name  # type: str
        self.oss_resource_id = oss_resource_id  # type: str
        self.sample_rate = sample_rate  # type: float
        self.scene_id = scene_id  # type: str
        self.service_id = service_id  # type: str
        self.user_id_field = user_id_field  # type: str
        self.user_table = user_table  # type: str
        self.user_table_partition_field = user_table_partition_field  # type: str
        self.user_table_partition_field_format = user_table_partition_field_format  # type: str
        self.workflow_name = workflow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFeatureConsistencyCheckJobConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path
        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version
        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude
        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id
        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority
        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version
        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name
        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field
        if self.item_table is not None:
            result['ItemTable'] = self.item_table
        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field
        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field
        if self.user_table is not None:
            result['UserTable'] = self.user_table
        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field
        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format
        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')
        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')
        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')
        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')
        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')
        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')
        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')
        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')
        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')
        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')
        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')
        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')
        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')
        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')
        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')
        return self


class UpdateFeatureConsistencyCheckJobConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFeatureConsistencyCheckJobConfigResponseBody, self).to_map()
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


class UpdateFeatureConsistencyCheckJobConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFeatureConsistencyCheckJobConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFeatureConsistencyCheckJobConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFeatureConsistencyCheckJobConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLaboratoryRequest(TeaModel):
    def __init__(self, bucket_count=None, bucket_type=None, buckets=None, debug_crowd_id=None, debug_users=None,
                 description=None, environment=None, filter=None, instance_id=None, name=None, type=None):
        self.bucket_count = bucket_count  # type: int
        self.bucket_type = bucket_type  # type: str
        self.buckets = buckets  # type: str
        self.debug_crowd_id = debug_crowd_id  # type: str
        self.debug_users = debug_users  # type: str
        self.description = description  # type: str
        self.environment = environment  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLaboratoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type
        if self.buckets is not None:
            result['Buckets'] = self.buckets
        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id
        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')
        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')
        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateLaboratoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLaboratoryResponseBody, self).to_map()
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


class UpdateLaboratoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLaboratoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLaboratoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLaboratoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLayerRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, name=None):
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLayerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateLayerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLayerResponseBody, self).to_map()
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


class UpdateLayerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParamRequest(TeaModel):
    def __init__(self, instance_id=None, value=None):
        self.instance_id = instance_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateParamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateParamResponseBody, self).to_map()
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


class UpdateParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateParamResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSceneRequestFlows(TeaModel):
    def __init__(self, flow_code=None, flow_name=None):
        self.flow_code = flow_code  # type: str
        self.flow_name = flow_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSceneRequestFlows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class UpdateSceneRequest(TeaModel):
    def __init__(self, description=None, flows=None, instance_id=None, name=None):
        self.description = description  # type: str
        self.flows = flows  # type: list[UpdateSceneRequestFlows]
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateSceneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = UpdateSceneRequestFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateSceneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSceneResponseBody, self).to_map()
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


class UpdateSceneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSceneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


