# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Artifact(TeaModel):
    def __init__(self, biz_id=None, creator=None, credential=None, gmt_created=None, gmt_modified=None,
                 location=None, modifier=None, name=None):
        self.biz_id = biz_id  # type: str
        self.creator = creator  # type: long
        self.credential = credential  # type: Credential
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.location = location  # type: str
        self.modifier = modifier  # type: long
        self.name = name  # type: str

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super(Artifact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.location is not None:
            result['location'] = self.location
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('credential') is not None:
            temp_model = Credential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class Category(TeaModel):
    def __init__(self, biz_id=None, creator=None, gmt_created=None, gmt_modified=None, modifier=None, name=None,
                 parent_biz_id=None, type=None):
        self.biz_id = biz_id  # type: str
        self.creator = creator  # type: long
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.modifier = modifier  # type: long
        self.name = name  # type: str
        self.parent_biz_id = parent_biz_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Category, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.parent_biz_id is not None:
            result['parentBizId'] = self.parent_biz_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentBizId') is not None:
            self.parent_biz_id = m.get('parentBizId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Configuration(TeaModel):
    def __init__(self, config_file_name=None, config_item_key=None, config_item_value=None):
        self.config_file_name = config_file_name  # type: str
        self.config_item_key = config_item_key  # type: str
        self.config_item_value = config_item_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Configuration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')
        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')
        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')
        return self


class Credential(TeaModel):
    def __init__(self, access_id=None, dir=None, expire=None, host=None, policy=None, security_token=None,
                 signature=None):
        self.access_id = access_id  # type: str
        self.dir = dir  # type: str
        self.expire = expire  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.security_token = security_token  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Credential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['accessId'] = self.access_id
        if self.dir is not None:
            result['dir'] = self.dir
        if self.expire is not None:
            result['expire'] = self.expire
        if self.host is not None:
            result['host'] = self.host
        if self.policy is not None:
            result['policy'] = self.policy
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class JobDriverSparkSubmit(TeaModel):
    def __init__(self, entry_point=None, entry_point_arguments=None, spark_submit_parameters=None):
        self.entry_point = entry_point  # type: str
        self.entry_point_arguments = entry_point_arguments  # type: list[str]
        self.spark_submit_parameters = spark_submit_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobDriverSparkSubmit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_point is not None:
            result['entryPoint'] = self.entry_point
        if self.entry_point_arguments is not None:
            result['entryPointArguments'] = self.entry_point_arguments
        if self.spark_submit_parameters is not None:
            result['sparkSubmitParameters'] = self.spark_submit_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('entryPoint') is not None:
            self.entry_point = m.get('entryPoint')
        if m.get('entryPointArguments') is not None:
            self.entry_point_arguments = m.get('entryPointArguments')
        if m.get('sparkSubmitParameters') is not None:
            self.spark_submit_parameters = m.get('sparkSubmitParameters')
        return self


class JobDriver(TeaModel):
    def __init__(self, spark_submit=None):
        self.spark_submit = spark_submit  # type: JobDriverSparkSubmit

    def validate(self):
        if self.spark_submit:
            self.spark_submit.validate()

    def to_map(self):
        _map = super(JobDriver, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spark_submit is not None:
            result['sparkSubmit'] = self.spark_submit.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sparkSubmit') is not None:
            temp_model = JobDriverSparkSubmit()
            self.spark_submit = temp_model.from_map(m['sparkSubmit'])
        return self


class PrincipalAction(TeaModel):
    def __init__(self, action_arn=None, principal_arn=None):
        self.action_arn = action_arn  # type: str
        self.principal_arn = principal_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PrincipalAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn
        if self.principal_arn is not None:
            result['principalArn'] = self.principal_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')
        if m.get('principalArn') is not None:
            self.principal_arn = m.get('principalArn')
        return self


class ReleaseVersionImage(TeaModel):
    def __init__(self, cpu_architecture=None, image_id=None, runtime_engine_type=None):
        self.cpu_architecture = cpu_architecture  # type: str
        self.image_id = image_id  # type: str
        self.runtime_engine_type = runtime_engine_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseVersionImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_architecture is not None:
            result['cpuArchitecture'] = self.cpu_architecture
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.runtime_engine_type is not None:
            result['runtimeEngineType'] = self.runtime_engine_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpuArchitecture') is not None:
            self.cpu_architecture = m.get('cpuArchitecture')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('runtimeEngineType') is not None:
            self.runtime_engine_type = m.get('runtimeEngineType')
        return self


class RunLog(TeaModel):
    def __init__(self, driver_std_error=None, driver_std_out=None):
        self.driver_std_error = driver_std_error  # type: str
        self.driver_std_out = driver_std_out  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver_std_error is not None:
            result['driverStdError'] = self.driver_std_error
        if self.driver_std_out is not None:
            result['driverStdOut'] = self.driver_std_out
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('driverStdError') is not None:
            self.driver_std_error = m.get('driverStdError')
        if m.get('driverStdOut') is not None:
            self.driver_std_out = m.get('driverStdOut')
        return self


class SparkConf(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SparkConf, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SqlOutputRows(TeaModel):
    def __init__(self, values=None):
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SqlOutputRows, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class SqlOutputSchemaFields(TeaModel):
    def __init__(self, name=None, nullable=None, type=None):
        self.name = name  # type: str
        self.nullable = nullable  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SqlOutputSchemaFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SqlOutputSchema(TeaModel):
    def __init__(self, fields=None):
        self.fields = fields  # type: list[SqlOutputSchemaFields]

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SqlOutputSchema, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = SqlOutputSchemaFields()
                self.fields.append(temp_model.from_map(k))
        return self


class SqlOutput(TeaModel):
    def __init__(self, rows=None, schema=None):
        self.rows = rows  # type: list[SqlOutputRows]
        self.schema = schema  # type: SqlOutputSchema

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super(SqlOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rows = []
        if m.get('rows') is not None:
            for k in m.get('rows'):
                temp_model = SqlOutputRows()
                self.rows.append(temp_model.from_map(k))
        if m.get('schema') is not None:
            temp_model = SqlOutputSchema()
            self.schema = temp_model.from_map(m['schema'])
        return self


class Tag(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签key值。
        self.key = key  # type: str
        # 标签key值。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Task(TeaModel):
    def __init__(self, artifact_url=None, biz_id=None, category_biz_id=None, content=None, creator=None,
                 default_catalog_id=None, default_database=None, default_resource_queue_id=None, default_sql_compute_id=None,
                 extra_artifact_ids=None, gmt_created=None, gmt_modified=None, has_changed=None, has_commited=None,
                 last_run_resource_queue_id=None, modifier=None, name=None, py_files=None, spark_args=None, spark_conf=None,
                 spark_driver_cores=None, spark_driver_memory=None, spark_entrypoint=None, spark_executor_cores=None,
                 spark_executor_memory=None, spark_log_level=None, spark_log_path=None, spark_version=None, tags=None, type=None):
        self.artifact_url = artifact_url  # type: str
        self.biz_id = biz_id  # type: str
        self.category_biz_id = category_biz_id  # type: str
        self.content = content  # type: str
        self.creator = creator  # type: long
        self.default_catalog_id = default_catalog_id  # type: str
        self.default_database = default_database  # type: str
        self.default_resource_queue_id = default_resource_queue_id  # type: str
        self.default_sql_compute_id = default_sql_compute_id  # type: str
        self.extra_artifact_ids = extra_artifact_ids  # type: list[str]
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.has_changed = has_changed  # type: bool
        self.has_commited = has_commited  # type: bool
        self.last_run_resource_queue_id = last_run_resource_queue_id  # type: str
        self.modifier = modifier  # type: long
        self.name = name  # type: str
        self.py_files = py_files  # type: list[str]
        self.spark_args = spark_args  # type: str
        self.spark_conf = spark_conf  # type: list[SparkConf]
        self.spark_driver_cores = spark_driver_cores  # type: int
        self.spark_driver_memory = spark_driver_memory  # type: long
        self.spark_entrypoint = spark_entrypoint  # type: str
        self.spark_executor_cores = spark_executor_cores  # type: int
        self.spark_executor_memory = spark_executor_memory  # type: long
        self.spark_log_level = spark_log_level  # type: str
        self.spark_log_path = spark_log_path  # type: str
        self.spark_version = spark_version  # type: str
        self.tags = tags  # type: dict[str, str]
        self.type = type  # type: str

    def validate(self):
        if self.spark_conf:
            for k in self.spark_conf:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Task, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_url is not None:
            result['artifactUrl'] = self.artifact_url
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.category_biz_id is not None:
            result['categoryBizId'] = self.category_biz_id
        if self.content is not None:
            result['content'] = self.content
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_catalog_id is not None:
            result['defaultCatalogId'] = self.default_catalog_id
        if self.default_database is not None:
            result['defaultDatabase'] = self.default_database
        if self.default_resource_queue_id is not None:
            result['defaultResourceQueueId'] = self.default_resource_queue_id
        if self.default_sql_compute_id is not None:
            result['defaultSqlComputeId'] = self.default_sql_compute_id
        if self.extra_artifact_ids is not None:
            result['extraArtifactIds'] = self.extra_artifact_ids
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.has_changed is not None:
            result['hasChanged'] = self.has_changed
        if self.has_commited is not None:
            result['hasCommited'] = self.has_commited
        if self.last_run_resource_queue_id is not None:
            result['lastRunResourceQueueId'] = self.last_run_resource_queue_id
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.py_files is not None:
            result['pyFiles'] = self.py_files
        if self.spark_args is not None:
            result['sparkArgs'] = self.spark_args
        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k in self.spark_conf:
                result['sparkConf'].append(k.to_map() if k else None)
        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores
        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory
        if self.spark_entrypoint is not None:
            result['sparkEntrypoint'] = self.spark_entrypoint
        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores
        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory
        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level
        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path
        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version
        if self.tags is not None:
            result['tags'] = self.tags
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('artifactUrl') is not None:
            self.artifact_url = m.get('artifactUrl')
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('categoryBizId') is not None:
            self.category_biz_id = m.get('categoryBizId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('defaultCatalogId') is not None:
            self.default_catalog_id = m.get('defaultCatalogId')
        if m.get('defaultDatabase') is not None:
            self.default_database = m.get('defaultDatabase')
        if m.get('defaultResourceQueueId') is not None:
            self.default_resource_queue_id = m.get('defaultResourceQueueId')
        if m.get('defaultSqlComputeId') is not None:
            self.default_sql_compute_id = m.get('defaultSqlComputeId')
        if m.get('extraArtifactIds') is not None:
            self.extra_artifact_ids = m.get('extraArtifactIds')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hasChanged') is not None:
            self.has_changed = m.get('hasChanged')
        if m.get('hasCommited') is not None:
            self.has_commited = m.get('hasCommited')
        if m.get('lastRunResourceQueueId') is not None:
            self.last_run_resource_queue_id = m.get('lastRunResourceQueueId')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pyFiles') is not None:
            self.py_files = m.get('pyFiles')
        if m.get('sparkArgs') is not None:
            self.spark_args = m.get('sparkArgs')
        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k in m.get('sparkConf'):
                temp_model = SparkConf()
                self.spark_conf.append(temp_model.from_map(k))
        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')
        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')
        if m.get('sparkEntrypoint') is not None:
            self.spark_entrypoint = m.get('sparkEntrypoint')
        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')
        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')
        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')
        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')
        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TaskInstance(TeaModel):
    def __init__(self, biz_id=None, creator=None, fenix_run_id=None, gmt_created=None, task_biz_id=None,
                 task_info=None, task_status=None, workspace_biz_id=None):
        self.biz_id = biz_id  # type: str
        self.creator = creator  # type: long
        self.fenix_run_id = fenix_run_id  # type: str
        self.gmt_created = gmt_created  # type: str
        self.task_biz_id = task_biz_id  # type: str
        self.task_info = task_info  # type: Task
        self.task_status = task_status  # type: str
        self.workspace_biz_id = workspace_biz_id  # type: str

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super(TaskInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.fenix_run_id is not None:
            result['fenixRunId'] = self.fenix_run_id
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id
        if self.task_info is not None:
            result['taskInfo'] = self.task_info.to_map()
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.workspace_biz_id is not None:
            result['workspaceBizId'] = self.workspace_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fenixRunId') is not None:
            self.fenix_run_id = m.get('fenixRunId')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')
        if m.get('taskInfo') is not None:
            temp_model = Task()
            self.task_info = temp_model.from_map(m['taskInfo'])
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('workspaceBizId') is not None:
            self.workspace_biz_id = m.get('workspaceBizId')
        return self


class TaskSnapshot(TeaModel):
    def __init__(self, biz_id=None, commiter=None, gmt_created=None, item=None, message=None, task_biz_id=None,
                 version=None):
        self.biz_id = biz_id  # type: str
        self.commiter = commiter  # type: long
        self.gmt_created = gmt_created  # type: str
        self.item = item  # type: Task
        self.message = message  # type: str
        self.task_biz_id = task_biz_id  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super(TaskSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.commiter is not None:
            result['commiter'] = self.commiter
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.item is not None:
            result['item'] = self.item.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('commiter') is not None:
            self.commiter = m.get('commiter')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('item') is not None:
            temp_model = Task()
            self.item = temp_model.from_map(m['item'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Template(TeaModel):
    def __init__(self, creator=None, gmt_created=None, gmt_modified=None, modifier=None, spark_conf=None,
                 spark_driver_cores=None, spark_driver_memory=None, spark_executor_cores=None, spark_executor_memory=None,
                 spark_log_level=None, spark_log_path=None, spark_version=None, template_type=None):
        self.creator = creator  # type: long
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.modifier = modifier  # type: long
        self.spark_conf = spark_conf  # type: list[SparkConf]
        self.spark_driver_cores = spark_driver_cores  # type: int
        self.spark_driver_memory = spark_driver_memory  # type: long
        self.spark_executor_cores = spark_executor_cores  # type: int
        self.spark_executor_memory = spark_executor_memory  # type: long
        self.spark_log_level = spark_log_level  # type: str
        self.spark_log_path = spark_log_path  # type: str
        self.spark_version = spark_version  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        if self.spark_conf:
            for k in self.spark_conf:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Template, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k in self.spark_conf:
                result['sparkConf'].append(k.to_map() if k else None)
        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores
        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory
        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores
        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory
        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level
        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path
        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version
        if self.template_type is not None:
            result['templateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k in m.get('sparkConf'):
                temp_model = SparkConf()
                self.spark_conf.append(temp_model.from_map(k))
        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')
        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')
        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')
        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')
        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')
        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')
        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        return self


class TimeRange(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        # 时间范围结束时间。
        self.end_time = end_time  # type: long
        # 时间范围开始时间。
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TimeRange, self).to_map()
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


class CancelJobRunRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelJobRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CancelJobRunResponseBody(TeaModel):
    def __init__(self, job_run_id=None, request_id=None):
        self.job_run_id = job_run_id  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelJobRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelJobRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelJobRunResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRunRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetJobRunResponseBodyJobRunConfigurationOverrides(TeaModel):
    def __init__(self, configurations=None):
        self.configurations = configurations  # type: list[Configuration]

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobRunResponseBodyJobRunConfigurationOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = Configuration()
                self.configurations.append(temp_model.from_map(k))
        return self


class GetJobRunResponseBodyJobRunStateChangeReason(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobRunResponseBodyJobRunStateChangeReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetJobRunResponseBodyJobRun(TeaModel):
    def __init__(self, code_type=None, configuration_overrides=None, end_time=None, execution_timeout_seconds=None,
                 job_driver=None, job_run_id=None, log=None, name=None, release_version=None, resource_owner_id=None,
                 resource_queue_id=None, state=None, state_change_reason=None, submit_time=None, tags=None, web_ui=None,
                 workspace_id=None):
        # 作业代码类型。
        self.code_type = code_type  # type: str
        self.configuration_overrides = configuration_overrides  # type: GetJobRunResponseBodyJobRunConfigurationOverrides
        # 作业结束时间。
        self.end_time = end_time  # type: long
        # 运行超时时间。
        self.execution_timeout_seconds = execution_timeout_seconds  # type: int
        self.job_driver = job_driver  # type: JobDriver
        # 任务实例ID。
        self.job_run_id = job_run_id  # type: str
        self.log = log  # type: RunLog
        # 作业实例名称。
        self.name = name  # type: str
        self.release_version = release_version  # type: str
        # 创建用户Uid。
        self.resource_owner_id = resource_owner_id  # type: str
        self.resource_queue_id = resource_queue_id  # type: str
        # 作业状态。
        self.state = state  # type: str
        self.state_change_reason = state_change_reason  # type: GetJobRunResponseBodyJobRunStateChangeReason
        # 作业提交时间。
        self.submit_time = submit_time  # type: long
        # 标签。
        self.tags = tags  # type: list[Tag]
        # 作业web ui。
        self.web_ui = web_ui  # type: str
        # 工作空间id。
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.log:
            self.log.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetJobRunResponseBodyJobRun, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_type is not None:
            result['codeType'] = self.code_type
        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.resource_owner_id is not None:
            result['resourceOwnerId'] = self.resource_owner_id
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.state is not None:
            result['state'] = self.state
        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.web_ui is not None:
            result['webUI'] = self.web_ui
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        if m.get('configurationOverrides') is not None:
            temp_model = GetJobRunResponseBodyJobRunConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m['configurationOverrides'])
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('log') is not None:
            temp_model = RunLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('resourceOwnerId') is not None:
            self.resource_owner_id = m.get('resourceOwnerId')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateChangeReason') is not None:
            temp_model = GetJobRunResponseBodyJobRunStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['stateChangeReason'])
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class GetJobRunResponseBody(TeaModel):
    def __init__(self, job_run=None, request_id=None):
        self.job_run = job_run  # type: GetJobRunResponseBodyJobRun
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        if self.job_run:
            self.job_run.validate()

    def to_map(self):
        _map = super(GetJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_run is not None:
            result['jobRun'] = self.job_run.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobRun') is not None:
            temp_model = GetJobRunResponseBodyJobRun()
            self.job_run = temp_model.from_map(m['jobRun'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobRunResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobRunsRequestEndTime(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobRunsRequestEndTime, self).to_map()
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


class ListJobRunsRequestStartTime(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobRunsRequestStartTime, self).to_map()
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


class ListJobRunsRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobRunsRequestTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListJobRunsRequest(TeaModel):
    def __init__(self, creator=None, end_time=None, job_run_id=None, max_results=None, name=None, next_token=None,
                 region_id=None, resource_queue_id=None, start_time=None, states=None, tags=None):
        # 创建用户Uid。
        self.creator = creator  # type: str
        self.end_time = end_time  # type: ListJobRunsRequestEndTime
        # 作业id。
        self.job_run_id = job_run_id  # type: str
        # 一次获取的最大记录数。
        self.max_results = max_results  # type: int
        # 作业名称。
        self.name = name  # type: str
        # 标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_queue_id = resource_queue_id  # type: str
        self.start_time = start_time  # type: ListJobRunsRequestStartTime
        # 作业状态。
        self.states = states  # type: list[str]
        # 标签。
        self.tags = tags  # type: list[ListJobRunsRequestTags]

    def validate(self):
        if self.end_time:
            self.end_time.validate()
        if self.start_time:
            self.start_time.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobRunsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.end_time is not None:
            result['endTime'] = self.end_time.to_map()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.start_time is not None:
            result['startTime'] = self.start_time.to_map()
        if self.states is not None:
            result['states'] = self.states
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('endTime') is not None:
            temp_model = ListJobRunsRequestEndTime()
            self.end_time = temp_model.from_map(m['endTime'])
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('startTime') is not None:
            temp_model = ListJobRunsRequestStartTime()
            self.start_time = temp_model.from_map(m['startTime'])
        if m.get('states') is not None:
            self.states = m.get('states')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListJobRunsRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListJobRunsShrinkRequest(TeaModel):
    def __init__(self, creator=None, end_time_shrink=None, job_run_id=None, max_results=None, name=None,
                 next_token=None, region_id=None, resource_queue_id=None, start_time_shrink=None, states_shrink=None,
                 tags_shrink=None):
        # 创建用户Uid。
        self.creator = creator  # type: str
        self.end_time_shrink = end_time_shrink  # type: str
        # 作业id。
        self.job_run_id = job_run_id  # type: str
        # 一次获取的最大记录数。
        self.max_results = max_results  # type: int
        # 作业名称。
        self.name = name  # type: str
        # 标记当前开始读取的位置，置空表示从头开始。
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_queue_id = resource_queue_id  # type: str
        self.start_time_shrink = start_time_shrink  # type: str
        # 作业状态。
        self.states_shrink = states_shrink  # type: str
        # 标签。
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobRunsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.end_time_shrink is not None:
            result['endTime'] = self.end_time_shrink
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.start_time_shrink is not None:
            result['startTime'] = self.start_time_shrink
        if self.states_shrink is not None:
            result['states'] = self.states_shrink
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('endTime') is not None:
            self.end_time_shrink = m.get('endTime')
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('startTime') is not None:
            self.start_time_shrink = m.get('startTime')
        if m.get('states') is not None:
            self.states_shrink = m.get('states')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListJobRunsResponseBodyJobRunsConfigurationOverrides(TeaModel):
    def __init__(self, configurations=None):
        self.configurations = configurations  # type: list[Configuration]

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobRunsResponseBodyJobRunsConfigurationOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = Configuration()
                self.configurations.append(temp_model.from_map(k))
        return self


class ListJobRunsResponseBodyJobRunsStateChangeReason(TeaModel):
    def __init__(self, code=None, message=None):
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobRunsResponseBodyJobRunsStateChangeReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListJobRunsResponseBodyJobRuns(TeaModel):
    def __init__(self, code_type=None, configuration_overrides=None, creator=None, end_time=None,
                 execution_timeout_seconds=None, job_driver=None, job_run_id=None, log=None, name=None, release_version=None, state=None,
                 state_change_reason=None, submit_time=None, tags=None, web_ui=None, workspace_id=None):
        # 作业代码类型。
        self.code_type = code_type  # type: str
        self.configuration_overrides = configuration_overrides  # type: ListJobRunsResponseBodyJobRunsConfigurationOverrides
        # 创建用户Uid。
        self.creator = creator  # type: str
        # 作业结束时间。
        self.end_time = end_time  # type: long
        # 运行超时时间。
        self.execution_timeout_seconds = execution_timeout_seconds  # type: int
        self.job_driver = job_driver  # type: JobDriver
        # 任务实例ID。
        self.job_run_id = job_run_id  # type: str
        self.log = log  # type: RunLog
        # 作业实例名称。
        self.name = name  # type: str
        self.release_version = release_version  # type: str
        # 作业状态。
        self.state = state  # type: str
        self.state_change_reason = state_change_reason  # type: ListJobRunsResponseBodyJobRunsStateChangeReason
        # 作业提交时间。
        self.submit_time = submit_time  # type: long
        # 标签。
        self.tags = tags  # type: list[Tag]
        # 作业web ui。
        self.web_ui = web_ui  # type: str
        # 工作空间id。
        self.workspace_id = workspace_id  # type: str

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.log:
            self.log.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobRunsResponseBodyJobRuns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_type is not None:
            result['codeType'] = self.code_type
        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.state is not None:
            result['state'] = self.state
        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.web_ui is not None:
            result['webUI'] = self.web_ui
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        if m.get('configurationOverrides') is not None:
            temp_model = ListJobRunsResponseBodyJobRunsConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m['configurationOverrides'])
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('log') is not None:
            temp_model = RunLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateChangeReason') is not None:
            temp_model = ListJobRunsResponseBodyJobRunsStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['stateChangeReason'])
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListJobRunsResponseBody(TeaModel):
    def __init__(self, job_runs=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.job_runs = job_runs  # type: list[ListJobRunsResponseBodyJobRuns]
        # 本次请求所返回的最大记录条数。
        self.max_results = max_results  # type: int
        # 返回读取到的数据位置，空代表数据已经读取完毕。
        self.next_token = next_token  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        # 本次请求条件下的数据总量。
        self.total_count = total_count  # type: int

    def validate(self):
        if self.job_runs:
            for k in self.job_runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobRunsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobRuns'] = []
        if self.job_runs is not None:
            for k in self.job_runs:
                result['jobRuns'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_runs = []
        if m.get('jobRuns') is not None:
            for k in m.get('jobRuns'):
                temp_model = ListJobRunsResponseBodyJobRuns()
                self.job_runs.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobRunsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobRunsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobRunsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobRunRequestConfigurationOverridesConfigurations(TeaModel):
    def __init__(self, config_file_name=None, config_item_key=None, config_item_value=None):
        self.config_file_name = config_file_name  # type: str
        self.config_item_key = config_item_key  # type: str
        self.config_item_value = config_item_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartJobRunRequestConfigurationOverridesConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')
        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')
        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')
        return self


class StartJobRunRequestConfigurationOverrides(TeaModel):
    def __init__(self, configurations=None):
        self.configurations = configurations  # type: list[StartJobRunRequestConfigurationOverridesConfigurations]

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartJobRunRequestConfigurationOverrides, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = StartJobRunRequestConfigurationOverridesConfigurations()
                self.configurations.append(temp_model.from_map(k))
        return self


class StartJobRunRequest(TeaModel):
    def __init__(self, client_token=None, code_type=None, configuration_overrides=None,
                 execution_timeout_seconds=None, job_driver=None, job_id=None, name=None, release_version=None, resource_queue_id=None,
                 tags=None, region_id=None):
        self.client_token = client_token  # type: str
        self.code_type = code_type  # type: str
        self.configuration_overrides = configuration_overrides  # type: StartJobRunRequestConfigurationOverrides
        self.execution_timeout_seconds = execution_timeout_seconds  # type: int
        self.job_driver = job_driver  # type: JobDriver
        self.job_id = job_id  # type: str
        self.name = name  # type: str
        self.release_version = release_version  # type: str
        self.resource_queue_id = resource_queue_id  # type: str
        self.tags = tags  # type: list[Tag]
        self.region_id = region_id  # type: str

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartJobRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.code_type is not None:
            result['codeType'] = self.code_type
        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.name is not None:
            result['name'] = self.name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        if m.get('configurationOverrides') is not None:
            temp_model = StartJobRunRequestConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m['configurationOverrides'])
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class StartJobRunResponseBody(TeaModel):
    def __init__(self, job_run_id=None, request_id=None):
        self.job_run_id = job_run_id  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartJobRunResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartJobRunResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartJobRunResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


