# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Artifact(TeaModel):
    def __init__(self, jar_artifact=None, kind=None, python_artifact=None, sql_artifact=None):
        self.jar_artifact = jar_artifact  # type: JarArtifact
        self.kind = kind  # type: str
        self.python_artifact = python_artifact  # type: PythonArtifact
        self.sql_artifact = sql_artifact  # type: SqlArtifact

    def validate(self):
        if self.jar_artifact:
            self.jar_artifact.validate()
        if self.python_artifact:
            self.python_artifact.validate()
        if self.sql_artifact:
            self.sql_artifact.validate()

    def to_map(self):
        _map = super(Artifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jar_artifact is not None:
            result['jarArtifact'] = self.jar_artifact.to_map()
        if self.kind is not None:
            result['kind'] = self.kind
        if self.python_artifact is not None:
            result['pythonArtifact'] = self.python_artifact.to_map()
        if self.sql_artifact is not None:
            result['sqlArtifact'] = self.sql_artifact.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jarArtifact') is not None:
            temp_model = JarArtifact()
            self.jar_artifact = temp_model.from_map(m['jarArtifact'])
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('pythonArtifact') is not None:
            temp_model = PythonArtifact()
            self.python_artifact = temp_model.from_map(m['pythonArtifact'])
        if m.get('sqlArtifact') is not None:
            temp_model = SqlArtifact()
            self.sql_artifact = temp_model.from_map(m['sqlArtifact'])
        return self


class AsyncResourcePlanOperationResult(TeaModel):
    def __init__(self, message=None, plan=None, ticket_status=None):
        self.message = message  # type: str
        self.plan = plan  # type: str
        self.ticket_status = ticket_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsyncResourcePlanOperationResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.plan is not None:
            result['plan'] = self.plan
        if self.ticket_status is not None:
            result['ticketStatus'] = self.ticket_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('ticketStatus') is not None:
            self.ticket_status = m.get('ticketStatus')
        return self


class BasicResourceSetting(TeaModel):
    def __init__(self, jobmanager_resource_setting_spec=None, parallelism=None,
                 taskmanager_resource_setting_spec=None):
        self.jobmanager_resource_setting_spec = jobmanager_resource_setting_spec  # type: BasicResourceSettingSpec
        self.parallelism = parallelism  # type: long
        self.taskmanager_resource_setting_spec = taskmanager_resource_setting_spec  # type: BasicResourceSettingSpec

    def validate(self):
        if self.jobmanager_resource_setting_spec:
            self.jobmanager_resource_setting_spec.validate()
        if self.taskmanager_resource_setting_spec:
            self.taskmanager_resource_setting_spec.validate()

    def to_map(self):
        _map = super(BasicResourceSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jobmanager_resource_setting_spec is not None:
            result['jobmanagerResourceSettingSpec'] = self.jobmanager_resource_setting_spec.to_map()
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.taskmanager_resource_setting_spec is not None:
            result['taskmanagerResourceSettingSpec'] = self.taskmanager_resource_setting_spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobmanagerResourceSettingSpec') is not None:
            temp_model = BasicResourceSettingSpec()
            self.jobmanager_resource_setting_spec = temp_model.from_map(m['jobmanagerResourceSettingSpec'])
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('taskmanagerResourceSettingSpec') is not None:
            temp_model = BasicResourceSettingSpec()
            self.taskmanager_resource_setting_spec = temp_model.from_map(m['taskmanagerResourceSettingSpec'])
        return self


class BasicResourceSettingSpec(TeaModel):
    def __init__(self, cpu=None, memory=None):
        self.cpu = cpu  # type: float
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BasicResourceSettingSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        return self


class BatchResourceSetting(TeaModel):
    def __init__(self, basic_resource_setting=None, max_slot=None):
        self.basic_resource_setting = basic_resource_setting  # type: BasicResourceSetting
        self.max_slot = max_slot  # type: long

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()

    def to_map(self):
        _map = super(BatchResourceSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()
        if self.max_slot is not None:
            result['maxSlot'] = self.max_slot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m['basicResourceSetting'])
        if m.get('maxSlot') is not None:
            self.max_slot = m.get('maxSlot')
        return self


class BriefDeploymentTarget(TeaModel):
    def __init__(self, mode=None, name=None):
        self.mode = mode  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BriefDeploymentTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class BriefResourceSetting(TeaModel):
    def __init__(self, batch_resource_setting=None, flink_conf=None, streaming_resource_setting=None):
        self.batch_resource_setting = batch_resource_setting  # type: BatchResourceSetting
        self.flink_conf = flink_conf  # type: dict[str, any]
        self.streaming_resource_setting = streaming_resource_setting  # type: StreamingResourceSetting

    def validate(self):
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        _map = super(BriefResourceSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('batchResourceSetting') is not None:
            temp_model = BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m['batchResourceSetting'])
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('streamingResourceSetting') is not None:
            temp_model = StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m['streamingResourceSetting'])
        return self


class Deployment(TeaModel):
    def __init__(self, artifact=None, deployment_has_changed=None, deployment_id=None, deployment_target=None,
                 description=None, engine_version=None, execution_mode=None, flink_conf=None, job_summary=None, logging=None,
                 name=None, namespace=None):
        self.artifact = artifact  # type: Artifact
        self.deployment_has_changed = deployment_has_changed  # type: bool
        self.deployment_id = deployment_id  # type: str
        self.deployment_target = deployment_target  # type: BriefDeploymentTarget
        self.description = description  # type: str
        self.engine_version = engine_version  # type: str
        self.execution_mode = execution_mode  # type: str
        self.flink_conf = flink_conf  # type: dict[str, any]
        self.job_summary = job_summary  # type: JobSummary
        self.logging = logging  # type: Logging
        self.name = name  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.deployment_target:
            self.deployment_target.validate()
        if self.job_summary:
            self.job_summary.validate()
        if self.logging:
            self.logging.validate()

    def to_map(self):
        _map = super(Deployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.deployment_has_changed is not None:
            result['deploymentHasChanged'] = self.deployment_has_changed
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.deployment_target is not None:
            result['deploymentTarget'] = self.deployment_target.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.job_summary is not None:
            result['jobSummary'] = self.job_summary.to_map()
        if self.logging is not None:
            result['logging'] = self.logging.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = Artifact()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('deploymentHasChanged') is not None:
            self.deployment_has_changed = m.get('deploymentHasChanged')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('deploymentTarget') is not None:
            temp_model = BriefDeploymentTarget()
            self.deployment_target = temp_model.from_map(m['deploymentTarget'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('jobSummary') is not None:
            temp_model = JobSummary()
            self.job_summary = temp_model.from_map(m['jobSummary'])
        if m.get('logging') is not None:
            temp_model = Logging()
            self.logging = temp_model.from_map(m['logging'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class DeploymentRestoreStrategy(TeaModel):
    def __init__(self, allow_non_restored_state=None, job_start_time_in_ms=None, kind=None, savepoint_id=None):
        self.allow_non_restored_state = allow_non_restored_state  # type: bool
        self.job_start_time_in_ms = job_start_time_in_ms  # type: long
        self.kind = kind  # type: str
        self.savepoint_id = savepoint_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeploymentRestoreStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_non_restored_state is not None:
            result['allowNonRestoredState'] = self.allow_non_restored_state
        if self.job_start_time_in_ms is not None:
            result['jobStartTimeInMs'] = self.job_start_time_in_ms
        if self.kind is not None:
            result['kind'] = self.kind
        if self.savepoint_id is not None:
            result['savepointId'] = self.savepoint_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('allowNonRestoredState') is not None:
            self.allow_non_restored_state = m.get('allowNonRestoredState')
        if m.get('jobStartTimeInMs') is not None:
            self.job_start_time_in_ms = m.get('jobStartTimeInMs')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('savepointId') is not None:
            self.savepoint_id = m.get('savepointId')
        return self


class DeploymentTarget(TeaModel):
    def __init__(self, name=None, namespace=None):
        self.name = name  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeploymentTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class EngineVersionMetadata(TeaModel):
    def __init__(self, engine_version=None, features=None, status=None):
        self.engine_version = engine_version  # type: str
        self.features = features  # type: EngineVersionSupportedFeatures
        self.status = status  # type: str

    def validate(self):
        if self.features:
            self.features.validate()

    def to_map(self):
        _map = super(EngineVersionMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.features is not None:
            result['features'] = self.features.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('features') is not None:
            temp_model = EngineVersionSupportedFeatures()
            self.features = temp_model.from_map(m['features'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class EngineVersionMetadataIndex(TeaModel):
    def __init__(self, default_engine_version=None, engine_version_metadata=None):
        self.default_engine_version = default_engine_version  # type: str
        self.engine_version_metadata = engine_version_metadata  # type: list[EngineVersionMetadata]

    def validate(self):
        if self.engine_version_metadata:
            for k in self.engine_version_metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EngineVersionMetadataIndex, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_engine_version is not None:
            result['defaultEngineVersion'] = self.default_engine_version
        result['engineVersionMetadata'] = []
        if self.engine_version_metadata is not None:
            for k in self.engine_version_metadata:
                result['engineVersionMetadata'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('defaultEngineVersion') is not None:
            self.default_engine_version = m.get('defaultEngineVersion')
        self.engine_version_metadata = []
        if m.get('engineVersionMetadata') is not None:
            for k in m.get('engineVersionMetadata'):
                temp_model = EngineVersionMetadata()
                self.engine_version_metadata.append(temp_model.from_map(k))
        return self


class EngineVersionSupportedFeatures(TeaModel):
    def __init__(self, support_native_savepoint=None, use_for_sql_deployments=None):
        self.support_native_savepoint = support_native_savepoint  # type: bool
        self.use_for_sql_deployments = use_for_sql_deployments  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EngineVersionSupportedFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_native_savepoint is not None:
            result['supportNativeSavepoint'] = self.support_native_savepoint
        if self.use_for_sql_deployments is not None:
            result['useForSqlDeployments'] = self.use_for_sql_deployments
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('supportNativeSavepoint') is not None:
            self.support_native_savepoint = m.get('supportNativeSavepoint')
        if m.get('useForSqlDeployments') is not None:
            self.use_for_sql_deployments = m.get('useForSqlDeployments')
        return self


class ExpertResourceSetting(TeaModel):
    def __init__(self, jobmanager_resource_setting_spec=None, resource_plan=None):
        self.jobmanager_resource_setting_spec = jobmanager_resource_setting_spec  # type: BasicResourceSettingSpec
        self.resource_plan = resource_plan  # type: str

    def validate(self):
        if self.jobmanager_resource_setting_spec:
            self.jobmanager_resource_setting_spec.validate()

    def to_map(self):
        _map = super(ExpertResourceSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jobmanager_resource_setting_spec is not None:
            result['jobmanagerResourceSettingSpec'] = self.jobmanager_resource_setting_spec.to_map()
        if self.resource_plan is not None:
            result['resourcePlan'] = self.resource_plan
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobmanagerResourceSettingSpec') is not None:
            temp_model = BasicResourceSettingSpec()
            self.jobmanager_resource_setting_spec = temp_model.from_map(m['jobmanagerResourceSettingSpec'])
        if m.get('resourcePlan') is not None:
            self.resource_plan = m.get('resourcePlan')
        return self


class JarArtifact(TeaModel):
    def __init__(self, additional_dependencies=None, entry_class=None, jar_uri=None, main_args=None):
        self.additional_dependencies = additional_dependencies  # type: list[str]
        self.entry_class = entry_class  # type: str
        self.jar_uri = jar_uri  # type: str
        self.main_args = main_args  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JarArtifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.entry_class is not None:
            result['entryClass'] = self.entry_class
        if self.jar_uri is not None:
            result['jarUri'] = self.jar_uri
        if self.main_args is not None:
            result['mainArgs'] = self.main_args
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('entryClass') is not None:
            self.entry_class = m.get('entryClass')
        if m.get('jarUri') is not None:
            self.jar_uri = m.get('jarUri')
        if m.get('mainArgs') is not None:
            self.main_args = m.get('mainArgs')
        return self


class Job(TeaModel):
    def __init__(self, artifact=None, batch_resource_setting=None, deployment_id=None, deployment_name=None,
                 end_time=None, engine_version=None, execution_mode=None, flink_conf=None, job_id=None, logging=None,
                 metric=None, namespace=None, restore_strategy=None, session_cluster_name=None, start_time=None,
                 status=None, streaming_resource_setting=None):
        self.artifact = artifact  # type: Artifact
        self.batch_resource_setting = batch_resource_setting  # type: BatchResourceSetting
        self.deployment_id = deployment_id  # type: str
        self.deployment_name = deployment_name  # type: str
        self.end_time = end_time  # type: long
        self.engine_version = engine_version  # type: str
        self.execution_mode = execution_mode  # type: str
        self.flink_conf = flink_conf  # type: dict[str, any]
        self.job_id = job_id  # type: str
        self.logging = logging  # type: Logging
        self.metric = metric  # type: JobMetric
        self.namespace = namespace  # type: str
        self.restore_strategy = restore_strategy  # type: DeploymentRestoreStrategy
        self.session_cluster_name = session_cluster_name  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: JobStatus
        self.streaming_resource_setting = streaming_resource_setting  # type: StreamingResourceSetting

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.logging:
            self.logging.validate()
        if self.metric:
            self.metric.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()
        if self.status:
            self.status.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        _map = super(Job, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.logging is not None:
            result['logging'] = self.logging.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()
        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = Artifact()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('batchResourceSetting') is not None:
            temp_model = BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m['batchResourceSetting'])
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('logging') is not None:
            temp_model = Logging()
            self.logging = temp_model.from_map(m['logging'])
        if m.get('metric') is not None:
            temp_model = JobMetric()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('restoreStrategy') is not None:
            temp_model = DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m['restoreStrategy'])
        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            temp_model = JobStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('streamingResourceSetting') is not None:
            temp_model = StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m['streamingResourceSetting'])
        return self


class JobFailure(TeaModel):
    def __init__(self, failed_at=None, message=None, reason=None):
        self.failed_at = failed_at  # type: long
        self.message = message  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobFailure, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_at is not None:
            result['failedAt'] = self.failed_at
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class JobMetric(TeaModel):
    def __init__(self, total_cpu=None, total_memory_byte=None):
        self.total_cpu = total_cpu  # type: float
        self.total_memory_byte = total_memory_byte  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['totalCpu'] = self.total_cpu
        if self.total_memory_byte is not None:
            result['totalMemoryByte'] = self.total_memory_byte
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('totalCpu') is not None:
            self.total_cpu = m.get('totalCpu')
        if m.get('totalMemoryByte') is not None:
            self.total_memory_byte = m.get('totalMemoryByte')
        return self


class JobStatus(TeaModel):
    def __init__(self, current_job_status=None, failure=None, running=None):
        self.current_job_status = current_job_status  # type: str
        self.failure = failure  # type: JobFailure
        self.running = running  # type: JobStatusRunning

    def validate(self):
        if self.failure:
            self.failure.validate()
        if self.running:
            self.running.validate()

    def to_map(self):
        _map = super(JobStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
        if self.running is not None:
            result['running'] = self.running.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('failure') is not None:
            temp_model = JobFailure()
            self.failure = temp_model.from_map(m['failure'])
        if m.get('running') is not None:
            temp_model = JobStatusRunning()
            self.running = temp_model.from_map(m['running'])
        return self


class JobStatusRunning(TeaModel):
    def __init__(self, observed_flink_job_restarts=None, observed_flink_job_status=None):
        self.observed_flink_job_restarts = observed_flink_job_restarts  # type: long
        self.observed_flink_job_status = observed_flink_job_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobStatusRunning, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_flink_job_restarts is not None:
            result['observedFlinkJobRestarts'] = self.observed_flink_job_restarts
        if self.observed_flink_job_status is not None:
            result['observedFlinkJobStatus'] = self.observed_flink_job_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('observedFlinkJobRestarts') is not None:
            self.observed_flink_job_restarts = m.get('observedFlinkJobRestarts')
        if m.get('observedFlinkJobStatus') is not None:
            self.observed_flink_job_status = m.get('observedFlinkJobStatus')
        return self


class JobSummary(TeaModel):
    def __init__(self, cancelled=None, cancelling=None, failed=None, finished=None, running=None, starting=None):
        self.cancelled = cancelled  # type: int
        self.cancelling = cancelling  # type: int
        self.failed = failed  # type: int
        self.finished = finished  # type: int
        self.running = running  # type: int
        self.starting = starting  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancelled is not None:
            result['cancelled'] = self.cancelled
        if self.cancelling is not None:
            result['cancelling'] = self.cancelling
        if self.failed is not None:
            result['failed'] = self.failed
        if self.finished is not None:
            result['finished'] = self.finished
        if self.running is not None:
            result['running'] = self.running
        if self.starting is not None:
            result['starting'] = self.starting
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cancelled') is not None:
            self.cancelled = m.get('cancelled')
        if m.get('cancelling') is not None:
            self.cancelling = m.get('cancelling')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('running') is not None:
            self.running = m.get('running')
        if m.get('starting') is not None:
            self.starting = m.get('starting')
        return self


class Log4jLogger(TeaModel):
    def __init__(self, logger_level=None, logger_name=None):
        self.logger_level = logger_level  # type: str
        self.logger_name = logger_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Log4jLogger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logger_level is not None:
            result['loggerLevel'] = self.logger_level
        if self.logger_name is not None:
            result['loggerName'] = self.logger_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('loggerLevel') is not None:
            self.logger_level = m.get('loggerLevel')
        if m.get('loggerName') is not None:
            self.logger_name = m.get('loggerName')
        return self


class LogReservePolicy(TeaModel):
    def __init__(self, expiration_days=None, open_history=None):
        self.expiration_days = expiration_days  # type: long
        self.open_history = open_history  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogReservePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_days is not None:
            result['expirationDays'] = self.expiration_days
        if self.open_history is not None:
            result['openHistory'] = self.open_history
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expirationDays') is not None:
            self.expiration_days = m.get('expirationDays')
        if m.get('openHistory') is not None:
            self.open_history = m.get('openHistory')
        return self


class Logging(TeaModel):
    def __init__(self, log_4j_2configuration_template=None, log_4j_loggers=None, log_reserve_policy=None,
                 logging_profile=None):
        self.log_4j_2configuration_template = log_4j_2configuration_template  # type: str
        self.log_4j_loggers = log_4j_loggers  # type: list[Log4jLogger]
        self.log_reserve_policy = log_reserve_policy  # type: LogReservePolicy
        self.logging_profile = logging_profile  # type: str

    def validate(self):
        if self.log_4j_loggers:
            for k in self.log_4j_loggers:
                if k:
                    k.validate()
        if self.log_reserve_policy:
            self.log_reserve_policy.validate()

    def to_map(self):
        _map = super(Logging, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_4j_2configuration_template is not None:
            result['log4j2ConfigurationTemplate'] = self.log_4j_2configuration_template
        result['log4jLoggers'] = []
        if self.log_4j_loggers is not None:
            for k in self.log_4j_loggers:
                result['log4jLoggers'].append(k.to_map() if k else None)
        if self.log_reserve_policy is not None:
            result['logReservePolicy'] = self.log_reserve_policy.to_map()
        if self.logging_profile is not None:
            result['loggingProfile'] = self.logging_profile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('log4j2ConfigurationTemplate') is not None:
            self.log_4j_2configuration_template = m.get('log4j2ConfigurationTemplate')
        self.log_4j_loggers = []
        if m.get('log4jLoggers') is not None:
            for k in m.get('log4jLoggers'):
                temp_model = Log4jLogger()
                self.log_4j_loggers.append(temp_model.from_map(k))
        if m.get('logReservePolicy') is not None:
            temp_model = LogReservePolicy()
            self.log_reserve_policy = temp_model.from_map(m['logReservePolicy'])
        if m.get('loggingProfile') is not None:
            self.logging_profile = m.get('loggingProfile')
        return self


class PythonArtifact(TeaModel):
    def __init__(self, additional_dependencies=None, additional_python_archives=None,
                 additional_python_libraries=None, entry_module=None, main_args=None, python_artifact_uri=None):
        self.additional_dependencies = additional_dependencies  # type: list[str]
        self.additional_python_archives = additional_python_archives  # type: list[str]
        self.additional_python_libraries = additional_python_libraries  # type: list[str]
        self.entry_module = entry_module  # type: str
        self.main_args = main_args  # type: str
        self.python_artifact_uri = python_artifact_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PythonArtifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.additional_python_archives is not None:
            result['additionalPythonArchives'] = self.additional_python_archives
        if self.additional_python_libraries is not None:
            result['additionalPythonLibraries'] = self.additional_python_libraries
        if self.entry_module is not None:
            result['entryModule'] = self.entry_module
        if self.main_args is not None:
            result['mainArgs'] = self.main_args
        if self.python_artifact_uri is not None:
            result['pythonArtifactUri'] = self.python_artifact_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('additionalPythonArchives') is not None:
            self.additional_python_archives = m.get('additionalPythonArchives')
        if m.get('additionalPythonLibraries') is not None:
            self.additional_python_libraries = m.get('additionalPythonLibraries')
        if m.get('entryModule') is not None:
            self.entry_module = m.get('entryModule')
        if m.get('mainArgs') is not None:
            self.main_args = m.get('mainArgs')
        if m.get('pythonArtifactUri') is not None:
            self.python_artifact_uri = m.get('pythonArtifactUri')
        return self


class Savepoint(TeaModel):
    def __init__(self, created_at=None, deployment_id=None, description=None, job_id=None, modified_at=None,
                 namespace=None, native_format=None, savepoint_id=None, savepoint_location=None, savepoint_origin=None,
                 status=None, stop_with_drain_enabled=None):
        self.created_at = created_at  # type: long
        self.deployment_id = deployment_id  # type: str
        self.description = description  # type: str
        self.job_id = job_id  # type: str
        self.modified_at = modified_at  # type: long
        self.namespace = namespace  # type: str
        self.native_format = native_format  # type: bool
        self.savepoint_id = savepoint_id  # type: str
        self.savepoint_location = savepoint_location  # type: str
        self.savepoint_origin = savepoint_origin  # type: str
        self.status = status  # type: SavepointStatus
        self.stop_with_drain_enabled = stop_with_drain_enabled  # type: bool

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(Savepoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.description is not None:
            result['description'] = self.description
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.native_format is not None:
            result['nativeFormat'] = self.native_format
        if self.savepoint_id is not None:
            result['savepointId'] = self.savepoint_id
        if self.savepoint_location is not None:
            result['savepointLocation'] = self.savepoint_location
        if self.savepoint_origin is not None:
            result['savepointOrigin'] = self.savepoint_origin
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.stop_with_drain_enabled is not None:
            result['stopWithDrainEnabled'] = self.stop_with_drain_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('nativeFormat') is not None:
            self.native_format = m.get('nativeFormat')
        if m.get('savepointId') is not None:
            self.savepoint_id = m.get('savepointId')
        if m.get('savepointLocation') is not None:
            self.savepoint_location = m.get('savepointLocation')
        if m.get('savepointOrigin') is not None:
            self.savepoint_origin = m.get('savepointOrigin')
        if m.get('status') is not None:
            temp_model = SavepointStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('stopWithDrainEnabled') is not None:
            self.stop_with_drain_enabled = m.get('stopWithDrainEnabled')
        return self


class SavepointFailure(TeaModel):
    def __init__(self, failed_at=None, message=None, reason=None):
        self.failed_at = failed_at  # type: long
        self.message = message  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SavepointFailure, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_at is not None:
            result['failedAt'] = self.failed_at
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class SavepointStatus(TeaModel):
    def __init__(self, failure=None, state=None):
        self.failure = failure  # type: SavepointFailure
        self.state = state  # type: str

    def validate(self):
        if self.failure:
            self.failure.validate()

    def to_map(self):
        _map = super(SavepointStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failure') is not None:
            temp_model = SavepointFailure()
            self.failure = temp_model.from_map(m['failure'])
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class SqlArtifact(TeaModel):
    def __init__(self, additional_dependencies=None, sql_script=None):
        self.additional_dependencies = additional_dependencies  # type: list[str]
        self.sql_script = sql_script  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SqlArtifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')
        return self


class StartJobRequestBody(TeaModel):
    def __init__(self, deployment_id=None, resource_setting_spec=None, restore_strategy=None):
        self.deployment_id = deployment_id  # type: str
        self.resource_setting_spec = resource_setting_spec  # type: BriefResourceSetting
        self.restore_strategy = restore_strategy  # type: DeploymentRestoreStrategy

    def validate(self):
        if self.resource_setting_spec:
            self.resource_setting_spec.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()

    def to_map(self):
        _map = super(StartJobRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.resource_setting_spec is not None:
            result['resourceSettingSpec'] = self.resource_setting_spec.to_map()
        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('resourceSettingSpec') is not None:
            temp_model = BriefResourceSetting()
            self.resource_setting_spec = temp_model.from_map(m['resourceSettingSpec'])
        if m.get('restoreStrategy') is not None:
            temp_model = DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m['restoreStrategy'])
        return self


class StopJobRequestBody(TeaModel):
    def __init__(self, stop_strategy=None):
        self.stop_strategy = stop_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopJobRequestBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stop_strategy is not None:
            result['stopStrategy'] = self.stop_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('stopStrategy') is not None:
            self.stop_strategy = m.get('stopStrategy')
        return self


class StreamingResourceSetting(TeaModel):
    def __init__(self, basic_resource_setting=None, expert_resource_setting=None, resource_setting_mode=None):
        self.basic_resource_setting = basic_resource_setting  # type: BasicResourceSetting
        self.expert_resource_setting = expert_resource_setting  # type: ExpertResourceSetting
        self.resource_setting_mode = resource_setting_mode  # type: str

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()
        if self.expert_resource_setting:
            self.expert_resource_setting.validate()

    def to_map(self):
        _map = super(StreamingResourceSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()
        if self.expert_resource_setting is not None:
            result['expertResourceSetting'] = self.expert_resource_setting.to_map()
        if self.resource_setting_mode is not None:
            result['resourceSettingMode'] = self.resource_setting_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m['basicResourceSetting'])
        if m.get('expertResourceSetting') is not None:
            temp_model = ExpertResourceSetting()
            self.expert_resource_setting = temp_model.from_map(m['expertResourceSetting'])
        if m.get('resourceSettingMode') is not None:
            self.resource_setting_mode = m.get('resourceSettingMode')
        return self


class Variable(TeaModel):
    def __init__(self, description=None, kind=None, name=None, value=None):
        self.description = description  # type: str
        self.kind = kind  # type: str
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Variable, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateDeploymentHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeploymentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateDeploymentRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Deployment

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeploymentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Deployment()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Deployment
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Deployment()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateDeploymentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDeploymentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeploymentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSavepointHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSavepointHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateSavepointRequest(TeaModel):
    def __init__(self, deployment_id=None, description=None, native_format=None):
        self.deployment_id = deployment_id  # type: str
        self.description = description  # type: str
        self.native_format = native_format  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSavepointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.description is not None:
            result['description'] = self.description
        if self.native_format is not None:
            result['nativeFormat'] = self.native_format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('nativeFormat') is not None:
            self.native_format = m.get('nativeFormat')
        return self


class CreateSavepointResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Savepoint
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSavepointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Savepoint()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSavepointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSavepointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSavepointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSavepointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVariableHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVariableHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateVariableRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Variable

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVariableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Variable()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVariableResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Variable
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateVariableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Variable()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateVariableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVariableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVariableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeploymentHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeploymentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteDeploymentResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteDeploymentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDeploymentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDeploymentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSavepointHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSavepointHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteSavepointResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSavepointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSavepointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSavepointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSavepointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSavepointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVariableHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVariableHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteVariableResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVariableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteVariableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVariableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVariableResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlinkApiProxyHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlinkApiProxyHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class FlinkApiProxyRequest(TeaModel):
    def __init__(self, flink_api_path=None, namespace=None, resource_id=None, resource_type=None):
        self.flink_api_path = flink_api_path  # type: str
        self.namespace = namespace  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlinkApiProxyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flink_api_path is not None:
            result['flinkApiPath'] = self.flink_api_path
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flinkApiPath') is not None:
            self.flink_api_path = m.get('flinkApiPath')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class FlinkApiProxyResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlinkApiProxyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class FlinkApiProxyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FlinkApiProxyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FlinkApiProxyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlinkApiProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateResourcePlanWithFlinkConfAsyncHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateResourcePlanWithFlinkConfAsyncHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GenerateResourcePlanWithFlinkConfAsyncRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateResourcePlanWithFlinkConfAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GenerateResourcePlanWithFlinkConfAsyncResponseBodyData(TeaModel):
    def __init__(self, ticket_id=None):
        self.ticket_id = ticket_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateResourcePlanWithFlinkConfAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        return self


class GenerateResourcePlanWithFlinkConfAsyncResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: GenerateResourcePlanWithFlinkConfAsyncResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateResourcePlanWithFlinkConfAsyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GenerateResourcePlanWithFlinkConfAsyncResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GenerateResourcePlanWithFlinkConfAsyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateResourcePlanWithFlinkConfAsyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateResourcePlanWithFlinkConfAsyncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenerateResourcePlanWithFlinkConfAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeploymentHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeploymentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetDeploymentResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Deployment
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Deployment()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeploymentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeploymentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeploymentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGenerateResourcePlanResultHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGenerateResourcePlanResultHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetGenerateResourcePlanResultResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: AsyncResourcePlanOperationResult
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGenerateResourcePlanResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AsyncResourcePlanOperationResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetGenerateResourcePlanResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGenerateResourcePlanResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGenerateResourcePlanResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGenerateResourcePlanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Job
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavepointHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSavepointHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetSavepointResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Savepoint
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSavepointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Savepoint()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSavepointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSavepointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSavepointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSavepointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentTargetsHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeploymentTargetsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListDeploymentTargetsRequest(TeaModel):
    def __init__(self, page_index=None, page_size=None):
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeploymentTargetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDeploymentTargetsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, page_index=None,
                 page_size=None, request_id=None, success=None, total_size=None):
        self.data = data  # type: list[DeploymentTarget]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeploymentTargetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DeploymentTarget()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListDeploymentTargetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeploymentTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeploymentTargetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeploymentTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentsHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeploymentsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListDeploymentsRequest(TeaModel):
    def __init__(self, page_index=None, page_size=None):
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeploymentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDeploymentsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, page_index=None,
                 page_size=None, request_id=None, success=None, total_size=None):
        self.data = data  # type: list[Deployment]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeploymentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Deployment()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListDeploymentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeploymentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeploymentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeploymentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEngineVersionMetadataHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEngineVersionMetadataHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListEngineVersionMetadataResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: EngineVersionMetadataIndex
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEngineVersionMetadataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EngineVersionMetadataIndex()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEngineVersionMetadataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEngineVersionMetadataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEngineVersionMetadataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEngineVersionMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, deployment_id=None, page_index=None, page_size=None):
        self.deployment_id = deployment_id  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, page_index=None,
                 page_size=None, request_id=None, success=None, total_size=None):
        self.data = data  # type: list[Job]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Job()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSavepointsHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSavepointsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListSavepointsRequest(TeaModel):
    def __init__(self, deployment_id=None, job_id=None, page_index=None, page_size=None):
        self.deployment_id = deployment_id  # type: str
        self.job_id = job_id  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSavepointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListSavepointsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, page_index=None,
                 page_size=None, request_id=None, success=None, total_size=None):
        self.data = data  # type: list[Savepoint]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSavepointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Savepoint()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListSavepointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSavepointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSavepointsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSavepointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVariablesHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariablesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListVariablesRequest(TeaModel):
    def __init__(self, page_index=None, page_size=None):
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariablesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListVariablesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, page_index=None,
                 page_size=None, request_id=None, success=None, total_size=None):
        self.data = data  # type: list[Variable]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVariablesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Variable()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListVariablesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVariablesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVariablesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVariablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartJobHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StartJobRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: StartJobRequestBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = StartJobRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Job
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StartJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopJobHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StopJobRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: StopJobRequestBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = StopJobRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Job
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StopJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentHeaders(TeaModel):
    def __init__(self, common_headers=None, workspace=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.workspace = workspace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDeploymentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateDeploymentRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: Deployment

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDeploymentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Deployment()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, http_code=None, request_id=None, success=None):
        self.data = data  # type: Deployment
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateDeploymentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Deployment()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateDeploymentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDeploymentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDeploymentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


