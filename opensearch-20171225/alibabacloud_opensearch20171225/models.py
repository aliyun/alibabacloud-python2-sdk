# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BindESUserAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindESUserAnalyzerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class BindESUserAnalyzerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindESUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindESUserAnalyzerResponse, self).to_map()
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
            temp_model = BindESUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEsInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindEsInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class BindEsInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindEsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindEsInstanceResponse, self).to_map()
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
            temp_model = BindEsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompileSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompileSortScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CompileSortScriptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CompileSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompileSortScriptResponse, self).to_map()
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
            temp_model = CompileSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.online = online  # type: bool
        self.params = params  # type: dict[str, any]
        self.traffic = traffic  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateABTestExperimentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateABTestExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateABTestExperimentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateABTestExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateABTestExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateABTestExperimentResponse, self).to_map()
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
            temp_model = CreateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestGroupResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateABTestGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateABTestGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateABTestGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateABTestGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateABTestGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateABTestGroupResponse, self).to_map()
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
            temp_model = CreateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateABTestSceneResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None, values=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateABTestSceneResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateABTestSceneResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateABTestSceneResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateABTestSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateABTestSceneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateABTestSceneResponse, self).to_map()
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
            temp_model = CreateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppGroupResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class CreateAppGroupResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, domain=None, expire_on=None, first_rank_algo_deployment_id=None,
                 has_pending_quota_review_task=None, id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, type=None, updated=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: int
        self.commodity_code = commodity_code  # type: str
        self.created = created  # type: int
        self.current_version = current_version  # type: str
        self.description = description  # type: str
        self.domain = domain  # type: str
        self.expire_on = expire_on  # type: str
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        self.name = name  # type: str
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        self.processing_order_id = processing_order_id  # type: str
        self.produced = produced  # type: int
        self.project_id = project_id  # type: str
        self.quota = quota  # type: CreateAppGroupResponseBodyResultQuota
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        self.status = status  # type: str
        self.switched_time = switched_time  # type: int
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(CreateAppGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = CreateAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateAppGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCollectionResponseBodyResult(TeaModel):
    def __init__(self, created=None, data_collection_type=None, id=None, industry_name=None, name=None, status=None,
                 sundial_id=None, type=None, updated=None):
        self.created = created  # type: int
        self.data_collection_type = data_collection_type  # type: str
        self.id = id  # type: str
        self.industry_name = industry_name  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.sundial_id = sundial_id  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCollectionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.id is not None:
            result['id'] = self.id
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateDataCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateDataCollectionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateDataCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateDataCollectionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateDataCollectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDataCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataCollectionResponse, self).to_map()
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
            temp_model = CreateDataCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFirstRankRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFirstRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        self.arg = arg  # type: str
        self.attribute = attribute  # type: str
        self.weight = weight  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFirstRankResponseBodyResultMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class CreateFirstRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, meta=None, name=None):
        self.active = active  # type: bool
        self.meta = meta  # type: list[CreateFirstRankResponseBodyResultMeta]
        self.name = name  # type: str

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFirstRankResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = CreateFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateFirstRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateFirstRankResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateFirstRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateFirstRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFirstRankResponse, self).to_map()
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
            temp_model = CreateFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionInstanceRequestCreateParameters(TeaModel):
    def __init__(self, name=None, value=None):
        # 参数名称
        self.name = name  # type: str
        # 参数值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionInstanceRequestCreateParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateFunctionInstanceRequestUsageParameters(TeaModel):
    def __init__(self, name=None, value=None):
        # 参数名称
        self.name = name  # type: str
        # 参数值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionInstanceRequestUsageParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateFunctionInstanceRequest(TeaModel):
    def __init__(self, create_parameters=None, cron=None, description=None, function_type=None, instance_name=None,
                 model_type=None, usage_parameters=None):
        # 创建参数
        self.create_parameters = create_parameters  # type: list[CreateFunctionInstanceRequestCreateParameters]
        # 周期训练
        self.cron = cron  # type: str
        # 实例描述
        self.description = description  # type: str
        # 功能类型
        self.function_type = function_type  # type: str
        # 实例名称
        self.instance_name = instance_name  # type: str
        # 模型类型
        self.model_type = model_type  # type: str
        # 使用参数
        self.usage_parameters = usage_parameters  # type: list[CreateFunctionInstanceRequestUsageParameters]

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFunctionInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['createParameters'].append(k.to_map() if k else None)
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        if self.function_type is not None:
            result['functionType'] = self.function_type
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.model_type is not None:
            result['modelType'] = self.model_type
        result['usageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['usageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k in m.get('createParameters'):
                temp_model = CreateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        self.usage_parameters = []
        if m.get('usageParameters') is not None:
            for k in m.get('usageParameters'):
                temp_model = CreateFunctionInstanceRequestUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class CreateFunctionInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateFunctionInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionInstanceResponse, self).to_map()
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
            temp_model = CreateFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionTaskResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateFunctionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFunctionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionTaskResponse, self).to_map()
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
            temp_model = CreateFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, name=None, type=None, updated=None):
        self.analyzer = analyzer  # type: str
        self.created = created  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInterventionDictionaryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateInterventionDictionaryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateInterventionDictionaryResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateInterventionDictionaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateInterventionDictionaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInterventionDictionaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInterventionDictionaryResponse, self).to_map()
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
            temp_model = CreateInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateModelResponse, self).to_map()
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
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueryProcessorRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueryProcessorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateQueryProcessorResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.domain = domain  # type: str
        self.indexes = indexes  # type: list[str]
        self.name = name  # type: str
        self.processors = processors  # type: list[dict[str, any]]
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQueryProcessorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class CreateQueryProcessorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateQueryProcessorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateQueryProcessorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateQueryProcessorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQueryProcessorResponse, self).to_map()
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
            temp_model = CreateQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScheduledTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScheduledTaskResponse, self).to_map()
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
            temp_model = CreateScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSearchStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSearchStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateSearchStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSearchStrategyResponse, self).to_map()
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
            temp_model = CreateSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecondRankRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecondRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class CreateSecondRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecondRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateSecondRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecondRankResponse, self).to_map()
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
            temp_model = CreateSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSortScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateSortScriptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSortScriptResponse, self).to_map()
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
            temp_model = CreateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserAnalyzerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateUserAnalyzerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserAnalyzerResponse, self).to_map()
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
            temp_model = CreateUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteABTestExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteABTestExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteABTestExperimentResponse, self).to_map()
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
            temp_model = DeleteABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteABTestGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteABTestGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteABTestGroupResponse, self).to_map()
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
            temp_model = DeleteABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteABTestSceneResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteABTestSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteABTestSceneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteABTestSceneResponse, self).to_map()
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
            temp_model = DeleteABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteFunctionInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFunctionInstanceResponse, self).to_map()
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
            temp_model = DeleteFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionTaskResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteFunctionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFunctionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFunctionTaskResponse, self).to_map()
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
            temp_model = DeleteFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteModelResponse, self).to_map()
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
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSortScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSortScriptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSortScriptResponse, self).to_map()
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
            temp_model = DeleteSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSortScriptFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSortScriptFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSortScriptFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSortScriptFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSortScriptFileResponse, self).to_map()
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
            temp_model = DeleteSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestExperimentResponseBodyResultParams(TeaModel):
    def __init__(self, first_formula_name=None):
        self.first_formula_name = first_formula_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeABTestExperimentResponseBodyResultParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_formula_name is not None:
            result['first_formula_name'] = self.first_formula_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('first_formula_name') is not None:
            self.first_formula_name = m.get('first_formula_name')
        return self


class DescribeABTestExperimentResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.online = online  # type: bool
        self.params = params  # type: DescribeABTestExperimentResponseBodyResultParams
        self.traffic = traffic  # type: int
        self.updated = updated  # type: int

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super(DescribeABTestExperimentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            temp_model = DescribeABTestExperimentResponseBodyResultParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeABTestExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeABTestExperimentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeABTestExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeABTestExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeABTestExperimentResponse, self).to_map()
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
            temp_model = DescribeABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestGroupResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeABTestGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeABTestGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeABTestGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeABTestGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeABTestGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeABTestGroupResponse, self).to_map()
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
            temp_model = DescribeABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeABTestSceneResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None, values=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeABTestSceneResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class DescribeABTestSceneResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeABTestSceneResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeABTestSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeABTestSceneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeABTestSceneResponse, self).to_map()
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
            temp_model = DescribeABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppResponseBodyResultDomainFunctions(TeaModel):
    def __init__(self, algo=None, qp=None, service=None):
        self.algo = algo  # type: list[str]
        self.qp = qp  # type: list[str]
        self.service = service  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppResponseBodyResultDomainFunctions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo is not None:
            result['algo'] = self.algo
        if self.qp is not None:
            result['qp'] = self.qp
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('algo') is not None:
            self.algo = m.get('algo')
        if m.get('qp') is not None:
            self.qp = m.get('qp')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self


class DescribeAppResponseBodyResultDomain(TeaModel):
    def __init__(self, category=None, functions=None, name=None):
        self.category = category  # type: str
        self.functions = functions  # type: DescribeAppResponseBodyResultDomainFunctions
        self.name = name  # type: str

    def validate(self):
        if self.functions:
            self.functions.validate()

    def to_map(self):
        _map = super(DescribeAppResponseBodyResultDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.functions is not None:
            result['functions'] = self.functions.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('functions') is not None:
            temp_model = DescribeAppResponseBodyResultDomainFunctions()
            self.functions = temp_model.from_map(m['functions'])
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAppResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, qps=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.qps = qps  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.qps is not None:
            result['qps'] = self.qps
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('qps') is not None:
            self.qps = m.get('qps')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeAppResponseBodyResult(TeaModel):
    def __init__(self, algo_deployment_id=None, auto_switch=None, cluster_name=None, created=None, description=None,
                 domain=None, fetch_fields=None, id=None, progress_percent=None, quota=None, schema=None, status=None,
                 type=None):
        self.algo_deployment_id = algo_deployment_id  # type: int
        self.auto_switch = auto_switch  # type: bool
        self.cluster_name = cluster_name  # type: str
        self.created = created  # type: int
        self.description = description  # type: str
        self.domain = domain  # type: DescribeAppResponseBodyResultDomain
        self.fetch_fields = fetch_fields  # type: list[str]
        self.id = id  # type: str
        self.progress_percent = progress_percent  # type: int
        self.quota = quota  # type: DescribeAppResponseBodyResultQuota
        self.schema = schema  # type: dict[str, any]
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.domain:
            self.domain.validate()
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(DescribeAppResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algo_deployment_id is not None:
            result['algoDeploymentId'] = self.algo_deployment_id
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain.to_map()
        if self.fetch_fields is not None:
            result['fetchFields'] = self.fetch_fields
        if self.id is not None:
            result['id'] = self.id
        if self.progress_percent is not None:
            result['progressPercent'] = self.progress_percent
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.schema is not None:
            result['schema'] = self.schema
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('algoDeploymentId') is not None:
            self.algo_deployment_id = m.get('algoDeploymentId')
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            temp_model = DescribeAppResponseBodyResultDomain()
            self.domain = temp_model.from_map(m['domain'])
        if m.get('fetchFields') is not None:
            self.fetch_fields = m.get('fetchFields')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('progressPercent') is not None:
            self.progress_percent = m.get('progressPercent')
        if m.get('quota') is not None:
            temp_model = DescribeAppResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppResponse, self).to_map()
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
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class DescribeAppGroupResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, domain=None, expire_on=None, first_rank_algo_deployment_id=None,
                 has_pending_quota_review_task=None, id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None, resource_group_id=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, type=None, updated=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: int
        self.commodity_code = commodity_code  # type: str
        self.created = created  # type: int
        self.current_version = current_version  # type: str
        self.description = description  # type: str
        self.domain = domain  # type: str
        self.expire_on = expire_on  # type: str
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        self.name = name  # type: str
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        self.processing_order_id = processing_order_id  # type: str
        self.produced = produced  # type: int
        self.project_id = project_id  # type: str
        self.quota = quota  # type: DescribeAppGroupResponseBodyResultQuota
        self.resource_group_id = resource_group_id  # type: str
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        self.status = status  # type: str
        self.switched_time = switched_time  # type: int
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(DescribeAppGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = DescribeAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeAppGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppGroupResponse, self).to_map()
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
            temp_model = DescribeAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupDataReportRequest(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupDataReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage(TeaModel):
    def __init__(self, arg_1=None, arg_3=None, args=None, client_ip=None, event_id=None, page=None, sdk_type=None,
                 sdk_version=None, session_id=None, user_id=None):
        self.arg_1 = arg_1  # type: str
        self.arg_3 = arg_3  # type: str
        self.args = args  # type: str
        self.client_ip = client_ip  # type: str
        self.event_id = event_id  # type: int
        self.page = page  # type: str
        self.sdk_type = sdk_type  # type: str
        self.sdk_version = sdk_version  # type: str
        self.session_id = session_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_1 is not None:
            result['arg1'] = self.arg_1
        if self.arg_3 is not None:
            result['arg3'] = self.arg_3
        if self.args is not None:
            result['args'] = self.args
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.page is not None:
            result['page'] = self.page
        if self.sdk_type is not None:
            result['sdkType'] = self.sdk_type
        if self.sdk_version is not None:
            result['sdkVersion'] = self.sdk_version
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arg1') is not None:
            self.arg_1 = m.get('arg1')
        if m.get('arg3') is not None:
            self.arg_3 = m.get('arg3')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('sdkType') is not None:
            self.sdk_type = m.get('sdkType')
        if m.get('sdkVersion') is not None:
            self.sdk_version = m.get('sdkVersion')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DescribeAppGroupDataReportResponseBodyResultReceivedSample(TeaModel):
    def __init__(self, message=None, received_time_ms=None):
        self.message = message  # type: DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage
        self.received_time_ms = received_time_ms  # type: long

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super(DescribeAppGroupDataReportResponseBodyResultReceivedSample, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message.to_map()
        if self.received_time_ms is not None:
            result['receivedTimeMs'] = self.received_time_ms
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            temp_model = DescribeAppGroupDataReportResponseBodyResultReceivedSampleMessage()
            self.message = temp_model.from_map(m['message'])
        if m.get('receivedTimeMs') is not None:
            self.received_time_ms = m.get('receivedTimeMs')
        return self


class DescribeAppGroupDataReportResponseBodyResult(TeaModel):
    def __init__(self, received_count=None, received_sample=None):
        self.received_count = received_count  # type: int
        self.received_sample = received_sample  # type: list[DescribeAppGroupDataReportResponseBodyResultReceivedSample]

    def validate(self):
        if self.received_sample:
            for k in self.received_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppGroupDataReportResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.received_count is not None:
            result['receivedCount'] = self.received_count
        result['receivedSample'] = []
        if self.received_sample is not None:
            for k in self.received_sample:
                result['receivedSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('receivedCount') is not None:
            self.received_count = m.get('receivedCount')
        self.received_sample = []
        if m.get('receivedSample') is not None:
            for k in m.get('receivedSample'):
                temp_model = DescribeAppGroupDataReportResponseBodyResultReceivedSample()
                self.received_sample.append(temp_model.from_map(k))
        return self


class DescribeAppGroupDataReportResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeAppGroupDataReportResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeAppGroupDataReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeAppGroupDataReportResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeAppGroupDataReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppGroupDataReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppGroupDataReportResponse, self).to_map()
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
            temp_model = DescribeAppGroupDataReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppGroupStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppGroupStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeAppGroupStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppGroupStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppGroupStatisticsResponse, self).to_map()
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
            temp_model = DescribeAppGroupStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeAppStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppStatisticsResponse, self).to_map()
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
            temp_model = DescribeAppStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppsResponse, self).to_map()
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
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCollctionResponseBodyResult(TeaModel):
    def __init__(self, created=None, data_collection_type=None, id=None, industry_name=None, name=None, status=None,
                 sundial_id=None, type=None, updated=None):
        self.created = created  # type: int
        self.data_collection_type = data_collection_type  # type: str
        self.id = id  # type: str
        self.industry_name = industry_name  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.sundial_id = sundial_id  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCollctionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.id is not None:
            result['id'] = self.id
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeDataCollctionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeDataCollctionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeDataCollctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeDataCollctionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeDataCollctionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDataCollctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataCollctionResponse, self).to_map()
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
            temp_model = DescribeDataCollctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        self.arg = arg  # type: str
        self.attribute = attribute  # type: str
        self.weight = weight  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFirstRankResponseBodyResultMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class DescribeFirstRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, description=None, meta=None, name=None):
        self.active = active  # type: bool
        self.description = description  # type: str
        self.meta = meta  # type: list[DescribeFirstRankResponseBodyResultMeta]
        self.name = name  # type: str

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFirstRankResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = DescribeFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeFirstRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeFirstRankResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeFirstRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeFirstRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFirstRankResponse, self).to_map()
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
            temp_model = DescribeFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, name=None, type=None, updated=None):
        self.analyzer = analyzer  # type: str
        self.created = created  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInterventionDictionaryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeInterventionDictionaryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeInterventionDictionaryResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeInterventionDictionaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeInterventionDictionaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInterventionDictionaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInterventionDictionaryResponse, self).to_map()
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
            temp_model = DescribeInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeModelResponse, self).to_map()
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
            temp_model = DescribeModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeQueryProcessorResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.domain = domain  # type: str
        self.indexes = indexes  # type: list[str]
        self.name = name  # type: str
        self.processors = processors  # type: list[dict[str, any]]
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeQueryProcessorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeQueryProcessorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeQueryProcessorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeQueryProcessorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeQueryProcessorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeQueryProcessorResponse, self).to_map()
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
            temp_model = DescribeQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionResponseBodyResult(TeaModel):
    def __init__(self, config=None, region_id=None):
        self.config = config  # type: dict[str, any]
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeRegionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeRegionResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeRegionResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeRegionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionResponse, self).to_map()
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
            temp_model = DescribeRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyResult(TeaModel):
    def __init__(self, console_url=None, endpoint=None, local_name=None, region_id=None):
        self.console_url = console_url  # type: str
        self.endpoint = endpoint  # type: str
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_url is not None:
            result['consoleUrl'] = self.console_url
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('consoleUrl') is not None:
            self.console_url = m.get('consoleUrl')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeRegionsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescribeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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


class DescribeScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScheduledTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScheduledTaskResponse, self).to_map()
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
            temp_model = DescribeScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecondRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, id=None, is_default=None, is_sys=None, meta=None,
                 name=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.description = description  # type: str
        self.id = id  # type: str
        self.is_default = is_default  # type: str
        self.is_sys = is_sys  # type: str
        self.meta = meta  # type: str
        self.name = name  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecondRankResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeSecondRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeSecondRankResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeSecondRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSecondRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSecondRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecondRankResponse, self).to_map()
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
            temp_model = DescribeSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowQueryStatusResponseBodyResult(TeaModel):
    def __init__(self, app_group_id=None, region=None, status=None):
        self.app_group_id = app_group_id  # type: str
        self.region = region  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlowQueryStatusResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeSlowQueryStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeSlowQueryStatusResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeSlowQueryStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DescribeSlowQueryStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DescribeSlowQueryStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSlowQueryStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlowQueryStatusResponse, self).to_map()
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
            temp_model = DescribeSlowQueryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserAnalyzerRequest(TeaModel):
    def __init__(self, with_=None):
        self.with_ = with_  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserAnalyzerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.with_ is not None:
            result['with'] = self.with_
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('with') is not None:
            self.with_ = m.get('with')
        return self


class DescribeUserAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserAnalyzerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DescribeUserAnalyzerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserAnalyzerResponse, self).to_map()
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
            temp_model = DescribeUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSlowQueryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSlowQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DisableSlowQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableSlowQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableSlowQueryResponse, self).to_map()
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
            temp_model = DisableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSlowQueryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSlowQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class EnableSlowQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableSlowQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableSlowQueryResponse, self).to_map()
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
            temp_model = EnableSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateMergedTableRequest(TeaModel):
    def __init__(self, spec=None):
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateMergedTableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class GenerateMergedTableResponseBodyResult(TeaModel):
    def __init__(self, from_table=None, merge_table=None, primary_key=None):
        self.from_table = from_table  # type: dict[str, any]
        self.merge_table = merge_table  # type: dict[str, any]
        self.primary_key = primary_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateMergedTableResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_table is not None:
            result['fromTable'] = self.from_table
        if self.merge_table is not None:
            result['mergeTable'] = self.merge_table
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fromTable') is not None:
            self.from_table = m.get('fromTable')
        if m.get('mergeTable') is not None:
            self.merge_table = m.get('mergeTable')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        return self


class GenerateMergedTableResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GenerateMergedTableResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GenerateMergedTableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GenerateMergedTableResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GenerateMergedTableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateMergedTableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateMergedTableResponse, self).to_map()
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
            temp_model = GenerateMergedTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(self, app_group_identity=None):
        self.app_group_identity = app_group_identity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_identity is not None:
            result['appGroupIdentity'] = self.app_group_identity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appGroupIdentity') is not None:
            self.app_group_identity = m.get('appGroupIdentity')
        return self


class GetDomainResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDomainResponse, self).to_map()
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
            temp_model = GetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCurrentVersionRequest(TeaModel):
    def __init__(self, category=None, domain=None, function_type=None, model_type=None):
        self.category = category  # type: str
        self.domain = domain  # type: str
        self.function_type = function_type  # type: str
        self.model_type = model_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCurrentVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.domain is not None:
            result['domain'] = self.domain
        if self.function_type is not None:
            result['functionType'] = self.function_type
        if self.model_type is not None:
            result['modelType'] = self.model_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends(TeaModel):
    def __init__(self, condition=None, dependency=None, description=None):
        self.condition = condition  # type: str
        self.dependency = dependency  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.dependency is not None:
            result['Dependency'] = self.dependency
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Dependency') is not None:
            self.dependency = m.get('Dependency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionCurrentVersionResponseBodyResultVersionConfig(TeaModel):
    def __init__(self, create_parameters=None, depends=None, usage_parameters=None):
        self.create_parameters = create_parameters  # type: list[GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters]
        self.depends = depends  # type: list[GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends]
        self.usage_parameters = usage_parameters  # type: list[GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters]

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.depends:
            for k in self.depends:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponseBodyResultVersionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        result['Depends'] = []
        if self.depends is not None:
            for k in self.depends:
                result['Depends'].append(k.to_map() if k else None)
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfigCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        self.depends = []
        if m.get('Depends') is not None:
            for k in m.get('Depends'):
                temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfigDepends()
                self.depends.append(temp_model.from_map(k))
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfigUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class GetFunctionCurrentVersionResponseBodyResult(TeaModel):
    def __init__(self, function_name=None, function_type=None, model_type=None, version_config=None,
                 version_id=None, version_name=None):
        self.function_name = function_name  # type: str
        self.function_type = function_type  # type: str
        self.model_type = model_type  # type: str
        self.version_config = version_config  # type: GetFunctionCurrentVersionResponseBodyResultVersionConfig
        self.version_id = version_id  # type: long
        self.version_name = version_name  # type: str

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.version_config is not None:
            result['VersionConfig'] = self.version_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('VersionConfig') is not None:
            temp_model = GetFunctionCurrentVersionResponseBodyResultVersionConfig()
            self.version_config = temp_model.from_map(m['VersionConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetFunctionCurrentVersionResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFunctionCurrentVersionResponseBodyResult
        self.status = status  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionCurrentVersionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionCurrentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFunctionCurrentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionCurrentVersionResponse, self).to_map()
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
            temp_model = GetFunctionCurrentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionDefaultInstanceResponseBodyResult(TeaModel):
    def __init__(self, instance_name=None):
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionDefaultInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class GetFunctionDefaultInstanceResponseBody(TeaModel):
    def __init__(self, code=None, function_name=None, http_code=None, instance_name=None, latency=None, message=None,
                 request_id=None, result=None, status=None):
        self.code = code  # type: str
        # 功能名称
        self.function_name = function_name  # type: str
        self.http_code = http_code  # type: long
        # 实例名称
        self.instance_name = instance_name  # type: str
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFunctionDefaultInstanceResponseBodyResult
        self.status = status  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFunctionDefaultInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionDefaultInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionDefaultInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFunctionDefaultInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionDefaultInstanceResponse, self).to_map()
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
            temp_model = GetFunctionDefaultInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionInstanceRequest(TeaModel):
    def __init__(self, output=None):
        self.output = output  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        return self


class GetFunctionInstanceResponseBodyResultBelongs(TeaModel):
    def __init__(self, category=None, domain=None, language=None):
        self.category = category  # type: str
        self.domain = domain  # type: str
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionInstanceResponseBodyResultBelongs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetFunctionInstanceResponseBodyResultCreateParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionInstanceResponseBodyResultCreateParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetFunctionInstanceResponseBodyResultTask(TeaModel):
    def __init__(self, dag_status=None, last_run_time=None):
        self.dag_status = dag_status  # type: str
        self.last_run_time = last_run_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionInstanceResponseBodyResultTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_status is not None:
            result['DagStatus'] = self.dag_status
        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DagStatus') is not None:
            self.dag_status = m.get('DagStatus')
        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')
        return self


class GetFunctionInstanceResponseBodyResultUsageParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionInstanceResponseBodyResultUsageParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetFunctionInstanceResponseBodyResult(TeaModel):
    def __init__(self, belongs=None, create_parameters=None, create_time=None, cron=None, description=None,
                 extend_info=None, function_name=None, function_type=None, instance_name=None, model_type=None, source=None,
                 status=None, task=None, usage_parameters=None, version_id=None):
        self.belongs = belongs  # type: GetFunctionInstanceResponseBodyResultBelongs
        self.create_parameters = create_parameters  # type: list[GetFunctionInstanceResponseBodyResultCreateParameters]
        self.create_time = create_time  # type: long
        self.cron = cron  # type: str
        self.description = description  # type: str
        self.extend_info = extend_info  # type: str
        self.function_name = function_name  # type: str
        self.function_type = function_type  # type: str
        self.instance_name = instance_name  # type: str
        self.model_type = model_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.task = task  # type: GetFunctionInstanceResponseBodyResultTask
        self.usage_parameters = usage_parameters  # type: list[GetFunctionInstanceResponseBodyResultUsageParameters]
        self.version_id = version_id  # type: long

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.task:
            self.task.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFunctionInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belongs is not None:
            result['Belongs'] = self.belongs.to_map()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.description is not None:
            result['Description'] = self.description
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.task is not None:
            result['Task'] = self.task.to_map()
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Belongs') is not None:
            temp_model = GetFunctionInstanceResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m['Belongs'])
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = GetFunctionInstanceResponseBodyResultCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Task') is not None:
            temp_model = GetFunctionInstanceResponseBodyResultTask()
            self.task = temp_model.from_map(m['Task'])
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = GetFunctionInstanceResponseBodyResultUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetFunctionInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFunctionInstanceResponseBodyResult
        self.status = status  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFunctionInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionInstanceResponse, self).to_map()
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
            temp_model = GetFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionTaskResponseBodyResult(TeaModel):
    def __init__(self, end_time=None, extend_info=None, function_name=None, generation=None, progress=None,
                 run_id=None, start_time=None, status=None):
        self.end_time = end_time  # type: long
        self.extend_info = extend_info  # type: str
        self.function_name = function_name  # type: str
        self.generation = generation  # type: str
        self.progress = progress  # type: long
        self.run_id = run_id  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionTaskResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionTaskResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFunctionTaskResponseBodyResult
        self.status = status  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFunctionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionTaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFunctionTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionTaskResponse, self).to_map()
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
            temp_model = GetFunctionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionVersionResponseBodyResultVersionConfigCreateParameters(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionVersionResponseBodyResultVersionConfigCreateParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionVersionResponseBodyResultVersionConfigDepends(TeaModel):
    def __init__(self, condition=None, dependency=None, description=None):
        self.condition = condition  # type: str
        self.dependency = dependency  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionVersionResponseBodyResultVersionConfigDepends, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.dependency is not None:
            result['Dependency'] = self.dependency
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Dependency') is not None:
            self.dependency = m.get('Dependency')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetFunctionVersionResponseBodyResultVersionConfigUsageParameters(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionVersionResponseBodyResultVersionConfigUsageParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class GetFunctionVersionResponseBodyResultVersionConfig(TeaModel):
    def __init__(self, create_parameters=None, depends=None, usage_parameters=None):
        self.create_parameters = create_parameters  # type: list[GetFunctionVersionResponseBodyResultVersionConfigCreateParameters]
        self.depends = depends  # type: list[GetFunctionVersionResponseBodyResultVersionConfigDepends]
        self.usage_parameters = usage_parameters  # type: list[GetFunctionVersionResponseBodyResultVersionConfigUsageParameters]

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.depends:
            for k in self.depends:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFunctionVersionResponseBodyResultVersionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        result['Depends'] = []
        if self.depends is not None:
            for k in self.depends:
                result['Depends'].append(k.to_map() if k else None)
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = GetFunctionVersionResponseBodyResultVersionConfigCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        self.depends = []
        if m.get('Depends') is not None:
            for k in m.get('Depends'):
                temp_model = GetFunctionVersionResponseBodyResultVersionConfigDepends()
                self.depends.append(temp_model.from_map(k))
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = GetFunctionVersionResponseBodyResultVersionConfigUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class GetFunctionVersionResponseBodyResult(TeaModel):
    def __init__(self, function_name=None, function_type=None, model_type=None, version_config=None,
                 version_id=None, version_name=None):
        self.function_name = function_name  # type: str
        self.function_type = function_type  # type: str
        self.model_type = model_type  # type: str
        self.version_config = version_config  # type: GetFunctionVersionResponseBodyResultVersionConfig
        self.version_id = version_id  # type: long
        self.version_name = version_name  # type: str

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        _map = super(GetFunctionVersionResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.version_config is not None:
            result['VersionConfig'] = self.version_config.to_map()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('VersionConfig') is not None:
            temp_model = GetFunctionVersionResponseBodyResultVersionConfig()
            self.version_config = temp_model.from_map(m['VersionConfig'])
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetFunctionVersionResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetFunctionVersionResponseBodyResult
        self.status = status  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFunctionVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFunctionVersionResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFunctionVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFunctionVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionVersionResponse, self).to_map()
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
            temp_model = GetFunctionVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelProgressResponseBodyResult(TeaModel):
    def __init__(self, progress=None, status=None):
        self.progress = progress  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelProgressResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetModelProgressResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetModelProgressResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetModelProgressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetModelProgressResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetModelProgressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetModelProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModelProgressResponse, self).to_map()
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
            temp_model = GetModelProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelReportResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetModelReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetModelReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetModelReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetModelReportResponse, self).to_map()
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
            temp_model = GetModelReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScriptFileNamesResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, file_name=None, modify_time=None):
        self.create_time = create_time  # type: str
        self.file_name = file_name  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScriptFileNamesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        return self


class GetScriptFileNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[GetScriptFileNamesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetScriptFileNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetScriptFileNamesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class GetScriptFileNamesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetScriptFileNamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScriptFileNamesResponse, self).to_map()
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
            temp_model = GetScriptFileNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSearchStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSearchStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSearchStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSearchStrategyResponse, self).to_map()
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
            temp_model = GetSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, modify_time=None, scope=None, status=None, type=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.scope = scope  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSortScriptResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetSortScriptResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetSortScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSortScriptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSortScriptResponse, self).to_map()
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
            temp_model = GetSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSortScriptFileResponseBodyResult(TeaModel):
    def __init__(self, content=None, create_time=None, modify_time=None, version=None):
        self.content = content  # type: str
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.version = version  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSortScriptFileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetSortScriptFileResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: GetSortScriptFileResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetSortScriptFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetSortScriptFileResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetSortScriptFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSortScriptFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSortScriptFileResponse, self).to_map()
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
            temp_model = GetSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidationErrorRequest(TeaModel):
    def __init__(self, error_code=None):
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetValidationErrorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        return self


class GetValidationErrorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetValidationErrorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetValidationErrorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetValidationErrorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetValidationErrorResponse, self).to_map()
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
            temp_model = GetValidationErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetValidationReportRequest(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetValidationReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetValidationReportResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetValidationReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetValidationReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetValidationReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetValidationReportResponse, self).to_map()
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
            temp_model = GetValidationReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestExperimentsResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.online = online  # type: bool
        self.params = params  # type: dict[str, any]
        self.traffic = traffic  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListABTestExperimentsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListABTestExperimentsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListABTestExperimentsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListABTestExperimentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestExperimentsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestExperimentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListABTestExperimentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListABTestExperimentsResponse, self).to_map()
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
            temp_model = ListABTestExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListABTestFixedFlowDividersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListABTestFixedFlowDividersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListABTestFixedFlowDividersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListABTestFixedFlowDividersResponse, self).to_map()
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
            temp_model = ListABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestGroupsResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListABTestGroupsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListABTestGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListABTestGroupsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListABTestGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListABTestGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListABTestGroupsResponse, self).to_map()
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
            temp_model = ListABTestGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestMetricsResponseBodyResult(TeaModel):
    def __init__(self, ctr=None, date=None, experiment_name=None, ipv=None, ipv_uv=None, pv=None, uv=None,
                 zero_hit_rate=None):
        self.ctr = ctr  # type: float
        self.date = date  # type: str
        self.experiment_name = experiment_name  # type: str
        self.ipv = ipv  # type: int
        self.ipv_uv = ipv_uv  # type: int
        self.pv = pv  # type: int
        self.uv = uv  # type: int
        self.zero_hit_rate = zero_hit_rate  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListABTestMetricsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ctr is not None:
            result['ctr'] = self.ctr
        if self.date is not None:
            result['date'] = self.date
        if self.experiment_name is not None:
            result['experimentName'] = self.experiment_name
        if self.ipv is not None:
            result['ipv'] = self.ipv
        if self.ipv_uv is not None:
            result['ipvUv'] = self.ipv_uv
        if self.pv is not None:
            result['pv'] = self.pv
        if self.uv is not None:
            result['uv'] = self.uv
        if self.zero_hit_rate is not None:
            result['zeroHitRate'] = self.zero_hit_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ctr') is not None:
            self.ctr = m.get('ctr')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('experimentName') is not None:
            self.experiment_name = m.get('experimentName')
        if m.get('ipv') is not None:
            self.ipv = m.get('ipv')
        if m.get('ipvUv') is not None:
            self.ipv_uv = m.get('ipvUv')
        if m.get('pv') is not None:
            self.pv = m.get('pv')
        if m.get('uv') is not None:
            self.uv = m.get('uv')
        if m.get('zeroHitRate') is not None:
            self.zero_hit_rate = m.get('zeroHitRate')
        return self


class ListABTestMetricsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListABTestMetricsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListABTestMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestMetricsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestMetricsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListABTestMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListABTestMetricsResponse, self).to_map()
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
            temp_model = ListABTestMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListABTestScenesResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None, values=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListABTestScenesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListABTestScenesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListABTestScenesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListABTestScenesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListABTestScenesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListABTestScenesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListABTestScenesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListABTestScenesResponse, self).to_map()
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
            temp_model = ListABTestScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupErrorsRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, start_time=None, stop_time=None):
        self.app_id = app_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: int
        self.stop_time = stop_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupErrorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_time is not None:
            result['stopTime'] = self.stop_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')
        return self


class ListAppGroupErrorsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupErrorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppGroupErrorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppGroupErrorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppGroupErrorsResponse, self).to_map()
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
            temp_model = ListAppGroupErrorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupMetricsRequest(TeaModel):
    def __init__(self, end_time=None, indexes=None, metric_type=None, start_time=None):
        self.end_time = end_time  # type: int
        self.indexes = indexes  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListAppGroupMetricsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListAppGroupMetricsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppGroupMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppGroupMetricsResponse, self).to_map()
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
            temp_model = ListAppGroupMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppGroupsRequest(TeaModel):
    def __init__(self, instance_id=None, name=None, page_number=None, page_size=None, resource_group_id=None,
                 sort_by=None, type=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.sort_by = sort_by  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAppGroupsResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppGroupsResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ListAppGroupsResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, domain=None, expire_on=None, first_rank_algo_deployment_id=None,
                 has_pending_quota_review_task=None, id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None, resource_group_id=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, type=None, updated=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: int
        self.commodity_code = commodity_code  # type: str
        self.created = created  # type: int
        self.current_version = current_version  # type: str
        self.description = description  # type: str
        self.domain = domain  # type: str
        self.expire_on = expire_on  # type: str
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        self.name = name  # type: str
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        self.processing_order_id = processing_order_id  # type: str
        self.produced = produced  # type: int
        self.project_id = project_id  # type: str
        self.quota = quota  # type: ListAppGroupsResponseBodyResultQuota
        self.resource_group_id = resource_group_id  # type: str
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        self.status = status  # type: str
        self.switched_time = switched_time  # type: int
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(ListAppGroupsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ListAppGroupsResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListAppGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListAppGroupsResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAppGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppGroupsResponse, self).to_map()
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
            temp_model = ListAppGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(self, group=None, page=None, size=None):
        self.group = group  # type: bool
        self.page = page  # type: int
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListAppsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers  # type: dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        _map = super(ListAppsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListDataCollectionsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataCollectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDataCollectionsResponseBodyResult(TeaModel):
    def __init__(self, created=None, data_collection_type=None, id=None, industry_name=None, name=None, status=None,
                 sundial_id=None, type=None, updated=None):
        self.created = created  # type: int
        self.data_collection_type = data_collection_type  # type: str
        self.id = id  # type: str
        self.industry_name = industry_name  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.sundial_id = sundial_id  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataCollectionsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.data_collection_type is not None:
            result['dataCollectionType'] = self.data_collection_type
        if self.id is not None:
            result['id'] = self.id
        if self.industry_name is not None:
            result['industryName'] = self.industry_name
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.sundial_id is not None:
            result['sundialId'] = self.sundial_id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('dataCollectionType') is not None:
            self.data_collection_type = m.get('dataCollectionType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('industryName') is not None:
            self.industry_name = m.get('industryName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sundialId') is not None:
            self.sundial_id = m.get('sundialId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListDataCollectionsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDataCollectionsResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataCollectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDataCollectionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataCollectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataCollectionsResponse, self).to_map()
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
            temp_model = ListDataCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTableFieldsRequest(TeaModel):
    def __init__(self, params=None):
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTableFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        return self


class ListDataSourceTableFieldsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTableFieldsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListDataSourceTableFieldsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataSourceTableFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceTableFieldsResponse, self).to_map()
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
            temp_model = ListDataSourceTableFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceTablesRequest(TeaModel):
    def __init__(self, params=None):
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        return self


class ListDataSourceTablesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceTablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListDataSourceTablesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataSourceTablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceTablesResponse, self).to_map()
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
            temp_model = ListDataSourceTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeployedAlgorithmModelsRequest(TeaModel):
    def __init__(self, algorithm_type=None, in_service_only=None):
        self.algorithm_type = algorithm_type  # type: str
        self.in_service_only = in_service_only  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployedAlgorithmModelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_type is not None:
            result['algorithmType'] = self.algorithm_type
        if self.in_service_only is not None:
            result['inServiceOnly'] = self.in_service_only
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('algorithmType') is not None:
            self.algorithm_type = m.get('algorithmType')
        if m.get('inServiceOnly') is not None:
            self.in_service_only = m.get('inServiceOnly')
        return self


class ListDeployedAlgorithmModelsResponseBodyResultModels(TeaModel):
    def __init__(self, algorithm_type=None, model_id=None, model_name=None, progress=None, project_id=None,
                 status=None):
        self.algorithm_type = algorithm_type  # type: str
        self.model_id = model_id  # type: int
        self.model_name = model_name  # type: str
        self.progress = progress  # type: int
        self.project_id = project_id  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeployedAlgorithmModelsResponseBodyResultModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_type is not None:
            result['algorithmType'] = self.algorithm_type
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.progress is not None:
            result['progress'] = self.progress
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('algorithmType') is not None:
            self.algorithm_type = m.get('algorithmType')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDeployedAlgorithmModelsResponseBodyResult(TeaModel):
    def __init__(self, app_group_name=None, apps=None, desc=None, gmt_create=None, gmt_modified=None, id=None,
                 models=None, scene=None, status=None):
        self.app_group_name = app_group_name  # type: str
        self.apps = apps  # type: list[str]
        self.desc = desc  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: str
        self.models = models  # type: list[ListDeployedAlgorithmModelsResponseBodyResultModels]
        self.scene = scene  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeployedAlgorithmModelsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_name is not None:
            result['appGroupName'] = self.app_group_name
        if self.apps is not None:
            result['apps'] = self.apps
        if self.desc is not None:
            result['desc'] = self.desc
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        result['models'] = []
        if self.models is not None:
            for k in self.models:
                result['models'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['scene'] = self.scene
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appGroupName') is not None:
            self.app_group_name = m.get('appGroupName')
        if m.get('apps') is not None:
            self.apps = m.get('apps')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.models = []
        if m.get('models') is not None:
            for k in m.get('models'):
                temp_model = ListDeployedAlgorithmModelsResponseBodyResultModels()
                self.models.append(temp_model.from_map(k))
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDeployedAlgorithmModelsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListDeployedAlgorithmModelsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeployedAlgorithmModelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDeployedAlgorithmModelsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDeployedAlgorithmModelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDeployedAlgorithmModelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeployedAlgorithmModelsResponse, self).to_map()
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
            temp_model = ListDeployedAlgorithmModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFirstRanksResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        self.arg = arg  # type: str
        self.attribute = attribute  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFirstRanksResponseBodyResultMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ListFirstRanksResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, meta=None, name=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.description = description  # type: str
        self.meta = meta  # type: list[ListFirstRanksResponseBodyResultMeta]
        self.name = name  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFirstRanksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = ListFirstRanksResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListFirstRanksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListFirstRanksResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFirstRanksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListFirstRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListFirstRanksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFirstRanksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFirstRanksResponse, self).to_map()
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
            temp_model = ListFirstRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionInstancesRequest(TeaModel):
    def __init__(self, function_type=None, model_type=None, output=None, page_number=None, page_size=None,
                 source=None):
        # 功能类型
        self.function_type = function_type  # type: str
        # 模型类型
        self.model_type = model_type  # type: str
        # 返回信息的丰富度
        self.output = output  # type: str
        # 页码
        self.page_number = page_number  # type: int
        # 每页大小
        self.page_size = page_size  # type: int
        # 实例来源
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_type is not None:
            result['functionType'] = self.function_type
        if self.model_type is not None:
            result['modelType'] = self.model_type
        if self.output is not None:
            result['output'] = self.output
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class ListFunctionInstancesResponseBodyResultBelongs(TeaModel):
    def __init__(self, category=None, domain=None, language=None):
        self.category = category  # type: str
        self.domain = domain  # type: str
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionInstancesResponseBodyResultBelongs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class ListFunctionInstancesResponseBodyResultCreateParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionInstancesResponseBodyResultCreateParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListFunctionInstancesResponseBodyResultUsageParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionInstancesResponseBodyResultUsageParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListFunctionInstancesResponseBodyResult(TeaModel):
    def __init__(self, belongs=None, create_parameters=None, create_time=None, cron=None, description=None,
                 extend_info=None, function_name=None, function_type=None, instance_name=None, model_type=None, source=None,
                 status=None, usage_parameters=None, version_id=None):
        self.belongs = belongs  # type: ListFunctionInstancesResponseBodyResultBelongs
        self.create_parameters = create_parameters  # type: list[ListFunctionInstancesResponseBodyResultCreateParameters]
        self.create_time = create_time  # type: long
        self.cron = cron  # type: str
        self.description = description  # type: str
        self.extend_info = extend_info  # type: str
        self.function_name = function_name  # type: str
        self.function_type = function_type  # type: str
        self.instance_name = instance_name  # type: str
        self.model_type = model_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.usage_parameters = usage_parameters  # type: list[ListFunctionInstancesResponseBodyResultUsageParameters]
        self.version_id = version_id  # type: long

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionInstancesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belongs is not None:
            result['Belongs'] = self.belongs.to_map()
        result['CreateParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['CreateParameters'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.description is not None:
            result['Description'] = self.description
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        result['UsageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['UsageParameters'].append(k.to_map() if k else None)
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Belongs') is not None:
            temp_model = ListFunctionInstancesResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m['Belongs'])
        self.create_parameters = []
        if m.get('CreateParameters') is not None:
            for k in m.get('CreateParameters'):
                temp_model = ListFunctionInstancesResponseBodyResultCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.usage_parameters = []
        if m.get('UsageParameters') is not None:
            for k in m.get('UsageParameters'):
                temp_model = ListFunctionInstancesResponseBodyResultUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListFunctionInstancesResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None, total_count=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListFunctionInstancesResponseBodyResult]
        self.status = status  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListFunctionInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFunctionInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionInstancesResponse, self).to_map()
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
            temp_model = ListFunctionInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionTasksRequest(TeaModel):
    def __init__(self, end_time=None, page_number=None, page_size=None, start_time=None, status=None):
        self.end_time = end_time  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListFunctionTasksResponseBodyResult(TeaModel):
    def __init__(self, end_time=None, extend_info=None, function_name=None, generation=None, progress=None,
                 run_id=None, start_time=None, status=None):
        self.end_time = end_time  # type: long
        self.extend_info = extend_info  # type: str
        self.function_name = function_name  # type: str
        self.generation = generation  # type: str
        self.progress = progress  # type: long
        self.run_id = run_id  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionTasksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.run_id is not None:
            result['RunId'] = self.run_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionTasksResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, result=None,
                 status=None, total_count=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListFunctionTasksResponseBodyResult]
        self.status = status  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListFunctionTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFunctionTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionTasksResponse, self).to_map()
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
            temp_model = ListFunctionTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionariesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, types=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.types = types  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListInterventionDictionariesResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, id=None, name=None, type=None, updated=None):
        self.analyzer = analyzer  # type: str
        self.created = created  # type: int
        self.id = id  # type: int
        self.name = name  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionariesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListInterventionDictionariesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListInterventionDictionariesResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterventionDictionariesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionariesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInterventionDictionariesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInterventionDictionariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterventionDictionariesResponse, self).to_map()
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
            temp_model = ListInterventionDictionariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryEntriesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, word=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionaryEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class ListInterventionDictionaryEntriesResponseBodyResultTokens(TeaModel):
    def __init__(self, order=None, tag=None, tag_label=None, token=None):
        self.order = order  # type: int
        self.tag = tag  # type: str
        self.tag_label = tag_label  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionaryEntriesResponseBodyResultTokens, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ListInterventionDictionaryEntriesResponseBodyResult(TeaModel):
    def __init__(self, cmd=None, created=None, relevance=None, status=None, tokens=None, updated=None, word=None):
        self.cmd = cmd  # type: str
        self.created = created  # type: long
        self.relevance = relevance  # type: dict[str, any]
        self.status = status  # type: str
        self.tokens = tokens  # type: list[ListInterventionDictionaryEntriesResponseBodyResultTokens]
        self.updated = updated  # type: long
        self.word = word  # type: str

    def validate(self):
        if self.tokens:
            for k in self.tokens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterventionDictionaryEntriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['cmd'] = self.cmd
        if self.created is not None:
            result['created'] = self.created
        if self.relevance is not None:
            result['relevance'] = self.relevance
        if self.status is not None:
            result['status'] = self.status
        result['tokens'] = []
        if self.tokens is not None:
            for k in self.tokens:
                result['tokens'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cmd') is not None:
            self.cmd = m.get('cmd')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('relevance') is not None:
            self.relevance = m.get('relevance')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tokens = []
        if m.get('tokens') is not None:
            for k in m.get('tokens'):
                temp_model = ListInterventionDictionaryEntriesResponseBodyResultTokens()
                self.tokens.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class ListInterventionDictionaryEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListInterventionDictionaryEntriesResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterventionDictionaryEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionaryEntriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListInterventionDictionaryEntriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInterventionDictionaryEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterventionDictionaryEntriesResponse, self).to_map()
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
            temp_model = ListInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryNerResultsRequest(TeaModel):
    def __init__(self, query=None):
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionaryNerResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class ListInterventionDictionaryNerResultsResponseBodyResult(TeaModel):
    def __init__(self, order=None, tag=None, tag_label=None, token=None):
        self.order = order  # type: int
        self.tag = tag  # type: str
        self.tag_label = tag_label  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionaryNerResultsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tag_label is not None:
            result['tagLabel'] = self.tag_label
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tagLabel') is not None:
            self.tag_label = m.get('tagLabel')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ListInterventionDictionaryNerResultsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListInterventionDictionaryNerResultsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterventionDictionaryNerResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListInterventionDictionaryNerResultsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListInterventionDictionaryNerResultsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInterventionDictionaryNerResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterventionDictionaryNerResultsResponse, self).to_map()
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
            temp_model = ListInterventionDictionaryNerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterventionDictionaryRelatedEntitiesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterventionDictionaryRelatedEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListInterventionDictionaryRelatedEntitiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInterventionDictionaryRelatedEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterventionDictionaryRelatedEntitiesResponse, self).to_map()
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
            temp_model = ListInterventionDictionaryRelatedEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListModelsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListModelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListModelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListModelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListModelsResponse, self).to_map()
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
            temp_model = ListModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProceedingsRequest(TeaModel):
    def __init__(self, filter_finished=None):
        self.filter_finished = filter_finished  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProceedingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_finished is not None:
            result['filterFinished'] = self.filter_finished
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filterFinished') is not None:
            self.filter_finished = m.get('filterFinished')
        return self


class ListProceedingsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProceedingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProceedingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProceedingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProceedingsResponse, self).to_map()
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
            temp_model = ListProceedingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorAnalyzerResultsRequest(TeaModel):
    def __init__(self, text=None):
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryProcessorAnalyzerResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class ListQueryProcessorAnalyzerResultsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryProcessorAnalyzerResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListQueryProcessorAnalyzerResultsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListQueryProcessorAnalyzerResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueryProcessorAnalyzerResultsResponse, self).to_map()
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
            temp_model = ListQueryProcessorAnalyzerResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorNersRequest(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryProcessorNersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class ListQueryProcessorNersResponseBodyResult(TeaModel):
    def __init__(self, label=None, order=None, priority=None, tag=None):
        self.label = label  # type: str
        self.order = order  # type: int
        self.priority = priority  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryProcessorNersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.order is not None:
            result['order'] = self.order
        if self.priority is not None:
            result['priority'] = self.priority
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class ListQueryProcessorNersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListQueryProcessorNersResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueryProcessorNersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQueryProcessorNersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListQueryProcessorNersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListQueryProcessorNersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueryProcessorNersResponse, self).to_map()
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
            temp_model = ListQueryProcessorNersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueryProcessorsRequest(TeaModel):
    def __init__(self, is_active=None):
        self.is_active = is_active  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryProcessorsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_active is not None:
            result['isActive'] = self.is_active
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')
        return self


class ListQueryProcessorsResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.domain = domain  # type: str
        self.indexes = indexes  # type: list[str]
        self.name = name  # type: str
        self.processors = processors  # type: list[dict[str, any]]
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueryProcessorsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListQueryProcessorsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListQueryProcessorsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueryProcessorsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQueryProcessorsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListQueryProcessorsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListQueryProcessorsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueryProcessorsResponse, self).to_map()
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
            temp_model = ListQueryProcessorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaReviewTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotaReviewTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListQuotaReviewTasksResponseBodyResult(TeaModel):
    def __init__(self, app_group_id=None, app_group_name=None, app_group_type=None, approved=None, available=None,
                 gmt_create=None, gmt_modified=None, id=None, memo=None, new_compute_resource=None, new_soc_size=None,
                 new_spec=None, old_compute_resource=None, old_doc_size=None, old_spec=None, pending=None):
        self.app_group_id = app_group_id  # type: int
        self.app_group_name = app_group_name  # type: str
        self.app_group_type = app_group_type  # type: str
        self.approved = approved  # type: bool
        self.available = available  # type: bool
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: int
        self.memo = memo  # type: str
        self.new_compute_resource = new_compute_resource  # type: int
        self.new_soc_size = new_soc_size  # type: int
        self.new_spec = new_spec  # type: str
        self.old_compute_resource = old_compute_resource  # type: int
        self.old_doc_size = old_doc_size  # type: int
        self.old_spec = old_spec  # type: str
        self.pending = pending  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQuotaReviewTasksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id
        if self.app_group_name is not None:
            result['appGroupName'] = self.app_group_name
        if self.app_group_type is not None:
            result['appGroupType'] = self.app_group_type
        if self.approved is not None:
            result['approved'] = self.approved
        if self.available is not None:
            result['available'] = self.available
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.memo is not None:
            result['memo'] = self.memo
        if self.new_compute_resource is not None:
            result['newComputeResource'] = self.new_compute_resource
        if self.new_soc_size is not None:
            result['newSocSize'] = self.new_soc_size
        if self.new_spec is not None:
            result['newSpec'] = self.new_spec
        if self.old_compute_resource is not None:
            result['oldComputeResource'] = self.old_compute_resource
        if self.old_doc_size is not None:
            result['oldDocSize'] = self.old_doc_size
        if self.old_spec is not None:
            result['oldSpec'] = self.old_spec
        if self.pending is not None:
            result['pending'] = self.pending
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')
        if m.get('appGroupName') is not None:
            self.app_group_name = m.get('appGroupName')
        if m.get('appGroupType') is not None:
            self.app_group_type = m.get('appGroupType')
        if m.get('approved') is not None:
            self.approved = m.get('approved')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        if m.get('newComputeResource') is not None:
            self.new_compute_resource = m.get('newComputeResource')
        if m.get('newSocSize') is not None:
            self.new_soc_size = m.get('newSocSize')
        if m.get('newSpec') is not None:
            self.new_spec = m.get('newSpec')
        if m.get('oldComputeResource') is not None:
            self.old_compute_resource = m.get('oldComputeResource')
        if m.get('oldDocSize') is not None:
            self.old_doc_size = m.get('oldDocSize')
        if m.get('oldSpec') is not None:
            self.old_spec = m.get('oldSpec')
        if m.get('pending') is not None:
            self.pending = m.get('pending')
        return self


class ListQuotaReviewTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListQuotaReviewTasksResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQuotaReviewTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListQuotaReviewTasksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListQuotaReviewTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListQuotaReviewTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQuotaReviewTasksResponse, self).to_map()
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
            temp_model = ListQuotaReviewTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRamRolesResponseBodyResult(TeaModel):
    def __init__(self, assumed=None, name=None, service=None, template_id=None):
        self.assumed = assumed  # type: bool
        self.name = name  # type: str
        self.service = service  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRamRolesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assumed is not None:
            result['assumed'] = self.assumed
        if self.name is not None:
            result['name'] = self.name
        if self.service is not None:
            result['service'] = self.service
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assumed') is not None:
            self.assumed = m.get('assumed')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class ListRamRolesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRamRolesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRamRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRamRolesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRamRolesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRamRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRamRolesResponse, self).to_map()
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
            temp_model = ListRamRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScheduledTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListScheduledTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListScheduledTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListScheduledTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListScheduledTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListScheduledTasksResponse, self).to_map()
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
            temp_model = ListScheduledTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSearchStrategiesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSearchStrategiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSearchStrategiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSearchStrategiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSearchStrategiesResponse, self).to_map()
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
            temp_model = ListSearchStrategiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecondRanksResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, id=None, is_default=None, is_sys=None, meta=None,
                 name=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.description = description  # type: str
        self.id = id  # type: str
        self.is_default = is_default  # type: str
        self.is_sys = is_sys  # type: str
        self.meta = meta  # type: str
        self.name = name  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecondRanksResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListSecondRanksResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListSecondRanksResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecondRanksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSecondRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSecondRanksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSecondRanksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecondRanksResponse, self).to_map()
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
            temp_model = ListSecondRanksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryCategoriesResponseBodyResult(TeaModel):
    def __init__(self, analyze_status=None, end=None, start=None):
        self.analyze_status = analyze_status  # type: str
        self.end = end  # type: int
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSlowQueryCategoriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyze_status is not None:
            result['analyzeStatus'] = self.analyze_status
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzeStatus') is not None:
            self.analyze_status = m.get('analyzeStatus')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListSlowQueryCategoriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListSlowQueryCategoriesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListSlowQueryCategoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListSlowQueryCategoriesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListSlowQueryCategoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSlowQueryCategoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSlowQueryCategoriesResponse, self).to_map()
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
            temp_model = ListSlowQueryCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlowQueryQueriesResponseBodyResult(TeaModel):
    def __init__(self, app_query=None, end=None, index=None, start=None):
        self.app_query = app_query  # type: str
        self.end = end  # type: int
        self.index = index  # type: int
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSlowQueryQueriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_query is not None:
            result['appQuery'] = self.app_query
        if self.end is not None:
            result['end'] = self.end
        if self.index is not None:
            result['index'] = self.index
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appQuery') is not None:
            self.app_query = m.get('appQuery')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListSlowQueryQueriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ListSlowQueryQueriesResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ListSlowQueryQueriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ListSlowQueryQueriesResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ListSlowQueryQueriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSlowQueryQueriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSlowQueryQueriesResponse, self).to_map()
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
            temp_model = ListSlowQueryQueriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortExpressionsResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, name=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.description = description  # type: str
        self.name = name  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSortExpressionsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListSortExpressionsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListSortExpressionsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSortExpressionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSortExpressionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSortExpressionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSortExpressionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSortExpressionsResponse, self).to_map()
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
            temp_model = ListSortExpressionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSortScriptsResponseBodyResult(TeaModel):
    def __init__(self, create_time=None, modify_time=None, scope=None, script_name=None, status=None, type=None):
        self.create_time = create_time  # type: str
        self.modify_time = modify_time  # type: str
        self.scope = scope  # type: str
        self.script_name = script_name  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSortScriptsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.scope is not None:
            result['scope'] = self.scope
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListSortScriptsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListSortScriptsResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSortScriptsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListSortScriptsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSortScriptsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSortScriptsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSortScriptsResponse, self).to_map()
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
            temp_model = ListSortScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticLogsRequest(TeaModel):
    def __init__(self, columns=None, distinct=None, page_number=None, page_size=None, query=None, sort_by=None,
                 start_time=None, stop_time=None):
        self.columns = columns  # type: str
        self.distinct = distinct  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: int
        self.stop_time = stop_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatisticLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.distinct is not None:
            result['distinct'] = self.distinct
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_time is not None:
            result['stopTime'] = self.stop_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('distinct') is not None:
            self.distinct = m.get('distinct')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')
        return self


class ListStatisticLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatisticLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStatisticLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStatisticLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStatisticLogsResponse, self).to_map()
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
            temp_model = ListStatisticLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatisticReportRequest(TeaModel):
    def __init__(self, columns=None, end_time=None, page_number=None, page_size=None, query=None, start_time=None):
        self.columns = columns  # type: str
        self.end_time = end_time  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.start_time = start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatisticReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListStatisticReportResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatisticReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStatisticReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListStatisticReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStatisticReportResponse, self).to_map()
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
            temp_model = ListStatisticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzerEntriesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, word=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserAnalyzerEntriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('word') is not None:
            self.word = m.get('word')
        return self


class ListUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserAnalyzerEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListUserAnalyzerEntriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserAnalyzerEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserAnalyzerEntriesResponse, self).to_map()
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
            temp_model = ListUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAnalyzersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserAnalyzersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUserAnalyzersResponseBodyResultDicts(TeaModel):
    def __init__(self, available=None, created=None, entries_count=None, entries_limit=None, id=None, type=None,
                 updated=None):
        self.available = available  # type: bool
        self.created = created  # type: int
        self.entries_count = entries_count  # type: int
        self.entries_limit = entries_limit  # type: int
        self.id = id  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserAnalyzersResponseBodyResultDicts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['available'] = self.available
        if self.created is not None:
            result['created'] = self.created
        if self.entries_count is not None:
            result['entriesCount'] = self.entries_count
        if self.entries_limit is not None:
            result['entriesLimit'] = self.entries_limit
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('entriesCount') is not None:
            self.entries_count = m.get('entriesCount')
        if m.get('entriesLimit') is not None:
            self.entries_limit = m.get('entriesLimit')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListUserAnalyzersResponseBodyResult(TeaModel):
    def __init__(self, available=None, business=None, created=None, dicts=None, id=None, name=None, updated=None):
        self.available = available  # type: bool
        self.business = business  # type: str
        self.created = created  # type: int
        self.dicts = dicts  # type: list[ListUserAnalyzersResponseBodyResultDicts]
        self.id = id  # type: str
        self.name = name  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.dicts:
            for k in self.dicts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserAnalyzersResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['available'] = self.available
        if self.business is not None:
            result['business'] = self.business
        if self.created is not None:
            result['created'] = self.created
        result['dicts'] = []
        if self.dicts is not None:
            for k in self.dicts:
                result['dicts'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('business') is not None:
            self.business = m.get('business')
        if m.get('created') is not None:
            self.created = m.get('created')
        self.dicts = []
        if m.get('dicts') is not None:
            for k in m.get('dicts'):
                temp_model = ListUserAnalyzersResponseBodyResultDicts()
                self.dicts.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListUserAnalyzersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListUserAnalyzersResponseBodyResult]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserAnalyzersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListUserAnalyzersResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListUserAnalyzersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserAnalyzersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserAnalyzersResponse, self).to_map()
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
            temp_model = ListUserAnalyzersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppGroupResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ModifyAppGroupResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, domain=None, expire_on=None, first_rank_algo_deployment_id=None,
                 has_pending_quota_review_task=None, id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, type=None, updated=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: int
        self.commodity_code = commodity_code  # type: str
        self.created = created  # type: int
        self.current_version = current_version  # type: str
        self.description = description  # type: str
        self.domain = domain  # type: str
        self.expire_on = expire_on  # type: str
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        self.name = name  # type: str
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        self.processing_order_id = processing_order_id  # type: str
        self.produced = produced  # type: int
        self.project_id = project_id  # type: str
        self.quota = quota  # type: ModifyAppGroupResponseBodyResultQuota
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        self.status = status  # type: str
        self.switched_time = switched_time  # type: int
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(ModifyAppGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.domain is not None:
            result['domain'] = self.domain
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ModifyAppGroupResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifyAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ModifyAppGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ModifyAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyAppGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyAppGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppGroupResponse, self).to_map()
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
            temp_model = ModifyAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppGroupQuotaResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppGroupQuotaResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ModifyAppGroupQuotaResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, expire_on=None, first_rank_algo_deployment_id=None, has_pending_quota_review_task=None,
                 id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, type=None, updated=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: int
        self.commodity_code = commodity_code  # type: str
        self.created = created  # type: int
        self.current_version = current_version  # type: str
        self.description = description  # type: str
        self.expire_on = expire_on  # type: str
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        self.name = name  # type: str
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        self.processing_order_id = processing_order_id  # type: str
        self.produced = produced  # type: int
        self.project_id = project_id  # type: str
        self.quota = quota  # type: ModifyAppGroupQuotaResponseBodyResultQuota
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        self.status = status  # type: str
        self.switched_time = switched_time  # type: int
        self.type = type  # type: str
        self.updated = updated  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(ModifyAppGroupQuotaResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ModifyAppGroupQuotaResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifyAppGroupQuotaResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ModifyAppGroupQuotaResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ModifyAppGroupQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyAppGroupQuotaResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyAppGroupQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyAppGroupQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppGroupQuotaResponse, self).to_map()
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
            temp_model = ModifyAppGroupQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirstRankRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFirstRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        self.arg = arg  # type: str
        self.attribute = attribute  # type: str
        self.weight = weight  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFirstRankResponseBodyResultMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ModifyFirstRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, description=None, meta=None, name=None):
        self.active = active  # type: bool
        self.description = description  # type: str
        self.meta = meta  # type: list[ModifyFirstRankResponseBodyResultMeta]
        self.name = name  # type: str

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyFirstRankResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = ModifyFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ModifyFirstRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ModifyFirstRankResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ModifyFirstRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyFirstRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFirstRankResponse, self).to_map()
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
            temp_model = ModifyFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyModelResponse, self).to_map()
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
            temp_model = ModifyModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyQueryProcessorRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyQueryProcessorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifyQueryProcessorResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, domain=None, indexes=None, name=None, processors=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.domain = domain  # type: str
        self.indexes = indexes  # type: list[str]
        self.name = name  # type: str
        self.processors = processors  # type: list[dict[str, any]]
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyQueryProcessorResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.domain is not None:
            result['domain'] = self.domain
        if self.indexes is not None:
            result['indexes'] = self.indexes
        if self.name is not None:
            result['name'] = self.name
        if self.processors is not None:
            result['processors'] = self.processors
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('processors') is not None:
            self.processors = m.get('processors')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifyQueryProcessorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ModifyQueryProcessorResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ModifyQueryProcessorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifyQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifyQueryProcessorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyQueryProcessorResponse, self).to_map()
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
            temp_model = ModifyQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyScheduledTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ModifyScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyScheduledTaskResponse, self).to_map()
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
            temp_model = ModifyScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecondRankRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecondRankRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class ModifySecondRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, created=None, description=None, id=None, is_default=None, is_sys=None, meta=None,
                 name=None, updated=None):
        self.active = active  # type: bool
        self.created = created  # type: int
        self.description = description  # type: str
        self.id = id  # type: str
        self.is_default = is_default  # type: str
        self.is_sys = is_sys  # type: str
        self.meta = meta  # type: str
        self.name = name  # type: str
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecondRankResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.is_sys is not None:
            result['isSys'] = self.is_sys
        if self.meta is not None:
            result['meta'] = self.meta
        if self.name is not None:
            result['name'] = self.name
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ModifySecondRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ModifySecondRankResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ModifySecondRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ModifySecondRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ModifySecondRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifySecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecondRankResponse, self).to_map()
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
            temp_model = ModifySecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewModelRequest(TeaModel):
    def __init__(self, query=None):
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class PreviewModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, total_count=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[dict[str, any]]
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreviewModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class PreviewModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PreviewModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PreviewModelResponse, self).to_map()
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
            temp_model = PreviewModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushInterventionDictionaryEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushInterventionDictionaryEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushInterventionDictionaryEntriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PushInterventionDictionaryEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushInterventionDictionaryEntriesResponse, self).to_map()
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
            temp_model = PushInterventionDictionaryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushUserAnalyzerEntriesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushUserAnalyzerEntriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class PushUserAnalyzerEntriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PushUserAnalyzerEntriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PushUserAnalyzerEntriesResponse, self).to_map()
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
            temp_model = PushUserAnalyzerEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RankPreviewQueryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RankPreviewQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RankPreviewQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RankPreviewQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RankPreviewQueryResponse, self).to_map()
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
            temp_model = RankPreviewQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseSortScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ReleaseSortScriptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseSortScriptResponse, self).to_map()
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
            temp_model = ReleaseSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveAppResponse, self).to_map()
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
            temp_model = RemoveAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveAppGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveAppGroupResponse, self).to_map()
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
            temp_model = RemoveAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDataCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDataCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveDataCollectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveDataCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveDataCollectionResponse, self).to_map()
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
            temp_model = RemoveDataCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFirstRankResponseBodyResultMeta(TeaModel):
    def __init__(self, arg=None, attribute=None, weight=None):
        self.arg = arg  # type: str
        self.attribute = attribute  # type: str
        self.weight = weight  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFirstRankResponseBodyResultMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['arg'] = self.arg
        if self.attribute is not None:
            result['attribute'] = self.attribute
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RemoveFirstRankResponseBodyResult(TeaModel):
    def __init__(self, active=None, description=None, meta=None, name=None):
        self.active = active  # type: bool
        self.description = description  # type: str
        self.meta = meta  # type: list[RemoveFirstRankResponseBodyResultMeta]
        self.name = name  # type: str

    def validate(self):
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveFirstRankResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.description is not None:
            result['description'] = self.description
        result['meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['meta'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.meta = []
        if m.get('meta') is not None:
            for k in m.get('meta'):
                temp_model = RemoveFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RemoveFirstRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: RemoveFirstRankResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RemoveFirstRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RemoveFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class RemoveFirstRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveFirstRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveFirstRankResponse, self).to_map()
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
            temp_model = RemoveFirstRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveInterventionDictionaryResponseBodyResult(TeaModel):
    def __init__(self, analyzer=None, created=None, name=None, type=None, updated=None):
        self.analyzer = analyzer  # type: str
        self.created = created  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveInterventionDictionaryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer
        if self.created is not None:
            result['created'] = self.created
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class RemoveInterventionDictionaryResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: RemoveInterventionDictionaryResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(RemoveInterventionDictionaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = RemoveInterventionDictionaryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class RemoveInterventionDictionaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveInterventionDictionaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveInterventionDictionaryResponse, self).to_map()
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
            temp_model = RemoveInterventionDictionaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveQueryProcessorResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveQueryProcessorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveQueryProcessorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveQueryProcessorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveQueryProcessorResponse, self).to_map()
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
            temp_model = RemoveQueryProcessorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveScheduledTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveScheduledTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveScheduledTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveScheduledTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveScheduledTaskResponse, self).to_map()
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
            temp_model = RemoveScheduledTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSearchStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSearchStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveSearchStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSearchStrategyResponse, self).to_map()
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
            temp_model = RemoveSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSecondRankResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSecondRankResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveSecondRankResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveSecondRankResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSecondRankResponse, self).to_map()
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
            temp_model = RemoveSecondRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserAnalyzerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class RemoveUserAnalyzerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUserAnalyzerResponse, self).to_map()
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
            temp_model = RemoveUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAppGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RenewAppGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewAppGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewAppGroupResponse, self).to_map()
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
            temp_model = RenewAppGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResultQuota(TeaModel):
    def __init__(self, compute_resource=None, doc_size=None, spec=None):
        self.compute_resource = compute_resource  # type: int
        self.doc_size = doc_size  # type: int
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplaceAppGroupCommodityCodeResponseBodyResultQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource
        if self.doc_size is not None:
            result['docSize'] = self.doc_size
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')
        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self


class ReplaceAppGroupCommodityCodeResponseBodyResult(TeaModel):
    def __init__(self, charge_type=None, charging_way=None, commodity_code=None, created=None, current_version=None,
                 description=None, expire_on=None, first_rank_algo_deployment_id=None, has_pending_quota_review_task=None,
                 id=None, instance_id=None, lock_mode=None, locked_by_expiration=None, name=None,
                 pending_second_rank_algo_deployment_id=None, processing_order_id=None, produced=None, project_id=None, quota=None,
                 second_rank_algo_deployment_id=None, status=None, switched_time=None, type=None, updated=None, versions=None):
        self.charge_type = charge_type  # type: str
        self.charging_way = charging_way  # type: int
        self.commodity_code = commodity_code  # type: str
        self.created = created  # type: int
        self.current_version = current_version  # type: str
        self.description = description  # type: str
        self.expire_on = expire_on  # type: str
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id  # type: int
        self.has_pending_quota_review_task = has_pending_quota_review_task  # type: int
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.lock_mode = lock_mode  # type: str
        self.locked_by_expiration = locked_by_expiration  # type: int
        self.name = name  # type: str
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id  # type: int
        self.processing_order_id = processing_order_id  # type: str
        self.produced = produced  # type: int
        self.project_id = project_id  # type: str
        self.quota = quota  # type: ReplaceAppGroupCommodityCodeResponseBodyResultQuota
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id  # type: int
        self.status = status  # type: str
        self.switched_time = switched_time  # type: int
        self.type = type  # type: str
        self.updated = updated  # type: int
        self.versions = versions  # type: list[str]

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super(ReplaceAppGroupCommodityCodeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.description is not None:
            result['description'] = self.description
        if self.expire_on is not None:
            result['expireOn'] = self.expire_on
        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id
        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration
        if self.name is not None:
            result['name'] = self.name
        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id
        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id
        if self.produced is not None:
            result['produced'] = self.produced
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id
        if self.status is not None:
            result['status'] = self.status
        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        if self.versions is not None:
            result['versions'] = self.versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')
        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')
        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')
        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')
        if m.get('produced') is not None:
            self.produced = m.get('produced')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('quota') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBodyResultQuota()
            self.quota = temp_model.from_map(m['quota'])
        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        return self


class ReplaceAppGroupCommodityCodeResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: ReplaceAppGroupCommodityCodeResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(ReplaceAppGroupCommodityCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = ReplaceAppGroupCommodityCodeResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class ReplaceAppGroupCommodityCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReplaceAppGroupCommodityCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplaceAppGroupCommodityCodeResponse, self).to_map()
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
            temp_model = ReplaceAppGroupCommodityCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSortScriptFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSortScriptFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SaveSortScriptFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveSortScriptFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSortScriptFileResponse, self).to_map()
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
            temp_model = SaveSortScriptFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSlowQueryAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSlowQueryAnalyzerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class StartSlowQueryAnalyzerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartSlowQueryAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartSlowQueryAnalyzerResponse, self).to_map()
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
            temp_model = StartSlowQueryAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainModelResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrainModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class TrainModelResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TrainModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TrainModelResponse, self).to_map()
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
            temp_model = TrainModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindESUserAnalyzerResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindESUserAnalyzerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UnbindESUserAnalyzerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindESUserAnalyzerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindESUserAnalyzerResponse, self).to_map()
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
            temp_model = UnbindESUserAnalyzerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEsInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindEsInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UnbindEsInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindEsInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindEsInstanceResponse, self).to_map()
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
            temp_model = UnbindEsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestExperimentResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.online = online  # type: bool
        self.params = params  # type: dict[str, any]
        self.traffic = traffic  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateABTestExperimentResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class UpdateABTestExperimentResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateABTestExperimentResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateABTestExperimentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateABTestExperimentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateABTestExperimentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestExperimentResponse, self).to_map()
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
            temp_model = UpdateABTestExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestFixedFlowDividersResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateABTestFixedFlowDividersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateABTestFixedFlowDividersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateABTestFixedFlowDividersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestFixedFlowDividersResponse, self).to_map()
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
            temp_model = UpdateABTestFixedFlowDividersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestGroupResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, status=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.status = status  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateABTestGroupResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class UpdateABTestGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateABTestGroupResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateABTestGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateABTestGroupResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateABTestGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateABTestGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestGroupResponse, self).to_map()
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
            temp_model = UpdateABTestGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateABTestSceneResponseBodyResult(TeaModel):
    def __init__(self, created=None, id=None, name=None, online=None, params=None, traffic=None, updated=None):
        self.created = created  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.online = online  # type: bool
        self.params = params  # type: dict[str, any]
        self.traffic = traffic  # type: int
        self.updated = updated  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateABTestSceneResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.online is not None:
            result['online'] = self.online
        if self.params is not None:
            result['params'] = self.params
        if self.traffic is not None:
            result['traffic'] = self.traffic
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online') is not None:
            self.online = m.get('online')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class UpdateABTestSceneResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: UpdateABTestSceneResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UpdateABTestSceneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateABTestSceneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateABTestSceneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateABTestSceneResponse, self).to_map()
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
            temp_model = UpdateABTestSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFetchFieldsRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFetchFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateFetchFieldsResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFetchFieldsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateFetchFieldsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFetchFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFetchFieldsResponse, self).to_map()
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
            temp_model = UpdateFetchFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionDefaultInstanceRequest(TeaModel):
    def __init__(self, instance_name=None):
        # 实例名称
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionDefaultInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        return self


class UpdateFunctionDefaultInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        self.latency = latency  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionDefaultInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFunctionDefaultInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFunctionDefaultInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFunctionDefaultInstanceResponse, self).to_map()
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
            temp_model = UpdateFunctionDefaultInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionInstanceRequestCreateParameters(TeaModel):
    def __init__(self, name=None, value=None):
        # 参数名称
        self.name = name  # type: str
        # 参数值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionInstanceRequestCreateParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateFunctionInstanceRequestUsageParameters(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionInstanceRequestUsageParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateFunctionInstanceRequest(TeaModel):
    def __init__(self, create_parameters=None, cron=None, description=None, usage_parameters=None):
        # 创建参数
        self.create_parameters = create_parameters  # type: list[UpdateFunctionInstanceRequestCreateParameters]
        # 周期训练
        self.cron = cron  # type: str
        # 实例描述
        self.description = description  # type: str
        # 使用参数
        self.usage_parameters = usage_parameters  # type: list[UpdateFunctionInstanceRequestUsageParameters]

    def validate(self):
        if self.create_parameters:
            for k in self.create_parameters:
                if k:
                    k.validate()
        if self.usage_parameters:
            for k in self.usage_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateFunctionInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createParameters'] = []
        if self.create_parameters is not None:
            for k in self.create_parameters:
                result['createParameters'].append(k.to_map() if k else None)
        if self.cron is not None:
            result['cron'] = self.cron
        if self.description is not None:
            result['description'] = self.description
        result['usageParameters'] = []
        if self.usage_parameters is not None:
            for k in self.usage_parameters:
                result['usageParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k in m.get('createParameters'):
                temp_model = UpdateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k))
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.usage_parameters = []
        if m.get('usageParameters') is not None:
            for k in m.get('usageParameters'):
                temp_model = UpdateFunctionInstanceRequestUsageParameters()
                self.usage_parameters.append(temp_model.from_map(k))
        return self


class UpdateFunctionInstanceResponseBody(TeaModel):
    def __init__(self, code=None, http_code=None, latency=None, message=None, request_id=None, status=None):
        # 错误码
        self.code = code  # type: str
        self.http_code = http_code  # type: long
        # 耗时
        self.latency = latency  # type: long
        # 错误信息
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.latency is not None:
            result['Latency'] = self.latency
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Latency') is not None:
            self.latency = m.get('Latency')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateFunctionInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFunctionInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFunctionInstanceResponse, self).to_map()
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
            temp_model = UpdateFunctionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSearchStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSearchStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateSearchStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSearchStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSearchStrategyResponse, self).to_map()
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
            temp_model = UpdateSearchStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSortScriptResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSortScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateSortScriptResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSortScriptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSortScriptResponse, self).to_map()
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
            temp_model = UpdateSortScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSummariesRequest(TeaModel):
    def __init__(self, dry_run=None):
        self.dry_run = dry_run  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSummariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        return self


class UpdateSummariesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSummariesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateSummariesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSummariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSummariesResponse, self).to_map()
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
            temp_model = UpdateSummariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateDataSourcesResponseBodyResultDataSource(TeaModel):
    def __init__(self, parameters=None, table_name=None, type=None):
        self.parameters = parameters  # type: dict[str, any]
        self.table_name = table_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateDataSourcesResponseBodyResultDataSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ValidateDataSourcesResponseBodyResult(TeaModel):
    def __init__(self, code=None, data_source=None, message=None):
        self.code = code  # type: str
        self.data_source = data_source  # type: ValidateDataSourcesResponseBodyResultDataSource
        self.message = message  # type: str

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super(ValidateDataSourcesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('dataSource') is not None:
            temp_model = ValidateDataSourcesResponseBodyResultDataSource()
            self.data_source = temp_model.from_map(m['dataSource'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ValidateDataSourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ValidateDataSourcesResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValidateDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ValidateDataSourcesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ValidateDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ValidateDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateDataSourcesResponse, self).to_map()
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
            temp_model = ValidateDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


